from flask import Blueprint, render_template, request

from utils import get_post_by_pk, get_posts_all, get_comments_by_post_id, get_posts_by_user

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")


@main_blueprint.route('/')
def index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:pk>')
def post_page(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/users/<user_name>')
def user_post_page(user_name):
    user_post = get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=user_post, user_name=user_name)
