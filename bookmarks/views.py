from flask import Blueprint, render_template, redirect

from bookmarks_utils import get_all_bookmarks, add_to_bookmarks, remove_from_bookmarks

boookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


@boookmarks_blueprint.route("/bookmarks/")
def bookmarks_page():
    bookmarks = get_all_bookmarks()
    return render_template('bookmarks.html', bookmarks=bookmarks)


@boookmarks_blueprint.route("/bookmarks/add/<int:post_id>")
def add_to_bookmarks_page(post_id):
    add_to_bookmarks(post_id)
    return redirect("/", code=302)


@boookmarks_blueprint.route("/bookmarks/remove/<int:post_id>")
def remove_from_bookmarks_page(post_id):
    remove_from_bookmarks(post_id)
    return redirect("/", code=302)
