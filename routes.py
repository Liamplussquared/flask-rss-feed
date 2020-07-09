import aggregator
from flask import Flask, render_template, render_template_string
app = Flask(__name__)


# render HTML page with button
@app.route('/')
def json():
    return render_template('json.html')


# aggreggator happening in the background
@app.route('/background_aggregator')
def background_aggregator():
	agg = aggregator.Aggregator()
	content = agg.get_links()
	return render_template('rss_feed.html', content = content)


if __name__ == '__main__':
	app.run()