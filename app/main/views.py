from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_sources,get_articles
from ..models import sources 

#views
@main.route('/')
def index():
    sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    title = "News Highlighter"

    return render_template('index.html',title = title, sources = sources, sports_sources = sport_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@main.route('/sources/<id>')
def articles(id):
    articles = get_articles(id)
    title = f'NH | {id}'
    
    return render_templates('articles.html',title= title,articles = articles)