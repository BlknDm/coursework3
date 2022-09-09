from flask import Flask

from api.api import api_blueprint
from search.views import search_blueprint
from bookmarks.views import boookmarks_blueprint
from main.views import main_blueprint

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(boookmarks_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == '__main__':
    app.run()
