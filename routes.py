import aggregator
from flask import Flask, render_template, render_template_string
app = Flask(__name__)


# render HTML page with button
@app.route('/')
def json():
    return render_template('json.html')


@app.route('/world')
def background_aggregator():
	agg = aggregator.Aggregator()
	content = agg.get_links("world")
	return render_template('rss_feed.html', content = content)


@app.route('/ireland')
def ireland_headlines():
	agg = aggregator.Aggregator()
	content = agg.get_links("ireland")
	return render_template('rss_feed.html', content = content)


if __name__ == '__main__':
	app.run()