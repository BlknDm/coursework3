from flask import Blueprint, request, render_template

from utils import search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__, template_folder="templates")


@search_blueprint.route('/')
def search_page():
    s = request.args.get('s')
    suitable_posts = search_for_posts(s)
    return render_template('search.html', posts=suitable_posts)
