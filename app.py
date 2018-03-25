import feedparser

from flask import Flask
from flask import render_template
from flask import request
import json
import urllib
import urllib.request

RSS_FEEDS = {'Best of abc.net.au': 'http://abc.net.au/bestof/bestofabc.xml', 'Radio Australia: Asia Pacific': 'http://abc.net.au/ra/rss/asiapacific.rss',
             'ABC iView Programs': 'http://tvmp.abc.net.au/iview/rss/category/abc1.xml', 'ABC Hobart': 'http://www.abc.net.au/local/rss/hobart/news.xml',
             'First Dog on the Moon': 'http://www.abc.net.au/radionational/feed/5086350/rss.xml'}

app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sources')
def recent_feed():
    feed = AtomFeed('Recent Articles',
        feed_url=request.url, url=request.url_root)
    articles = Article.query.order_by(Article.pub_date.desc()) \
        .limit(15).all()
    for article in articles:
        feed.add(article.title, unicode(article.rendered_text),
                 content_type='html',
                 author=article.author.name,
                 url=make_external(article.url),
                 updated=article.last_update,
                 published=article.published)
    return feed.get_response()


if __name__ == '__main__':
    app.run(debug=True)
