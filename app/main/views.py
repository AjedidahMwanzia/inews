from flask import render_template
from . import main
from ..request import get_news



@main.route('/')
def index():
    
    news= get_news()
    title = "INEWS"
    return render_template('index.html',title=title,articles = news)

# @app.route('/sources')
# def sources():

#     news = get_sources()
#     return render_template('news.html',source = news)