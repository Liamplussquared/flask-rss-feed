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
	output = ""
	agg = aggregator.Aggregator()
	content = agg.get_links()

	for url in content:
		output += "All articles from " + str(url)
		output += "\n******************************************\n"
		output += str(content[url]) 
		output += "\n******************************************\n\n"

	return render_template('rss_feed.html', text = output)


if __name__ == '__main__':
	app.run()