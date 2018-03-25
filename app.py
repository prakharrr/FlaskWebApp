import feedparser

from flask import Flask
from flask import render_template
from flask import request
import json
import urllib
import urllib.request

RSS_FEEDS = {'Best of abc.net.au': 'http://abc.net.au/bestof/bestofabc.xml',
             'Radio Australia: Asia Pacific': 'http://abc.net.au/ra/rss/asiapacific.rss',
             'ABC iView Programs': 'http://tvmp.abc.net.au/iview/rss/category/abc1.xml',
             'ABC Hobart': 'http://www.abc.net.au/local/rss/hobart/news.xml',
             'First Dog on the Moon': 'http://www.abc.net.au/radionational/feed/5086350/rss.xml'}

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# @app.route('/weather')
# def get_weather(query):
#     api_url = "api.openweathermap.org/data/2.5/weather?zip=14623,us"
#     query = urllib.parse.quote(query)
#     url = api_url.format(query)
#     data = urllib.request.urlopen(url).read()
#     parsed = json.loads(data.decode("utf-8"))
#     weather = None
#     if parsed.get("weather"):
#         weather = {"description": parsed["weather"][0]["description"],
#                    "temperature": parsed["main"]["temp"],
#                    "city": parsed["name"]
#                    }
#     return render_template('weather.html')


@app.route('/filter')
def test():
    return render_template('filter.html')


if __name__ == '__main__':
    app.run(debug=True)
