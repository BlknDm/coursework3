from flask import Blueprint, request, jsonify, render_template
from utils import get_posts_all, get_post_by_pk, search_for_posts, get_comments_by_post_id, get_posts_by_user
from bookmarks_utils import get_all_bookmarks
import logging

api_blueprint = Blueprint('api_blueprint', __name__, template_folder="templates")

api_logger = logging.getLogger('api_logger')
api_logger.setLevel(level=logging.INFO)

file_handler = logging.FileHandler("logs/api.log", encoding='utf-8')
api_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

api_logger.addHandler(file_handler)


@api_blueprint.route("/")
def main_page():
    posts = get_posts_all()
    all_bookmarks = get_all_bookmarks()
    return render_template('index.html', posts=posts, len_bookmarks=len(all_bookmarks))


@api_blueprint.route("/posts/<int:post_id>")
def post_page(pk, post_id):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, len_comments=len(comments), comments=comments)


@api_blueprint.route("/users/<user_name>")
def user_page(user_name):
    posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts, user_name=user_name)


@api_blueprint.route("/search")
def search_page():
    query = request.args.get('s')
    posts = search_for_posts(query)
    return render_template('search.html', posts=posts, len_posts=len(posts))


@api_blueprint.route("/api/posts/")
def api_posts_page():
    api_logger.info('Запрос /api/posts')
    posts = get_posts_all()
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:post_id>/")
def api_post_page(post_id):
    api_logger.info(f'Запрос /api/posts/{post_id}')
    post = get_post_by_pk(post_id)
    return jsonify(post)
