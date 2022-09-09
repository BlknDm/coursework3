import json

from flask import jsonify

POSTS_PATH = "data/posts.json"
COMMENT_PATH = "data/comments.json"


def get_posts_all():
    """возвращает посты"""
    with open(POSTS_PATH, "r", encoding='utf-8') as file:
        return json.load(file)


def get_comments_all():
    """Возвращает все комменты"""
    with open(COMMENT_PATH, "r", encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
    """
    возвращает посты определенного пользователя.
    Функция должна вызывать ошибку `ValueError` если такого пользователя нет и пустой список,
    если у пользователя нет постов.
    """
    list = []
    for post in get_posts_all():
        if user_name == post["poster_name"].lower():
            list.append(post)
    return list


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста.
    Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список,
    если у поста нет комментов.
    """
    comment_list = []
    for comment in get_comments_all():
        if post_id == comment["post_id"]:
            comment_list.append(comment)
    return comment_list


def search_for_posts(query):
    """возвращает список постов по ключевому слову"""
    suitable_posts = []

    for post in get_posts_all():
        if query.lower().strip() in post['content'].lower():
            suitable_posts.append(post)
    return suitable_posts


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору."""
    one_post = []
    for post in get_posts_all():
        if pk == post["pk"]:
            one_post.append(post)
    return one_post
