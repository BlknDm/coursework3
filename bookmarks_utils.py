import json

from utils import get_posts_all

BOOKMARKS_PATH = "data/bookmarks.json"


def get_all_bookmarks():
    """Получает все сохраненные закладки"""

    with open(BOOKMARKS_PATH, 'r', encoding='utf-8') as file:
        return json.loads(file.read())


def save_to_bookmark(bookmarks):
    """Сохраняет обновленный список закладок"""

    with open(BOOKMARKS_PATH, 'w', encoding='utf-8') as file:
        return json.dump(bookmarks, file, ensure_ascii=False)


def add_to_bookmarks(post_id):
    """Добавляет пост в закладки"""
    posts = get_posts_all()
    bookmarks = get_all_bookmarks()
    for post in posts:
        if post_id == post['pk']:
            bookmarks.append(post)
    return save_to_bookmark(bookmarks)


def remove_from_bookmarks(post_id):
    """Удаляет пост из закладок"""

    bookmarks = get_all_bookmarks()
    for bookmark in bookmarks:
        if post_id == bookmark['pk']:
            bookmarks.remove(bookmark)
    return save_to_bookmark(bookmarks)
