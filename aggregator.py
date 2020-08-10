import requests
import xml.etree.ElementTree as ET

class Aggregator:

	def __init__(self):
		pass

	def parse_XML(self, content):
		"""
		Given the content of a request response (assuming non-empty),
		this function parses the XML and returns a dictionary urls as keys and titles as values.
		"""

		if not content or not isinstance(content, bytes):
			return {}

		articles = {}
		tree = ET.fromstring(content)
	
		for child in tree[0]:
			if child.tag == 'item':
				title = child.find('title').text
				url = child.find('link').text
				articles[url] = title

		return articles


	def file_input(self, category):
		"""
		This function reads in urls of rss_feeds and returns list of 
		the urls.
		"""
		if category == 'world':
			file = open('feeds/world_feeds.txt', 'r')
		elif category == 'ireland':
			file = open('feeds/irish_feeds.txt', 'r')
		urls = []
		rss_feeds = file.read().splitlines()
		for url in rss_feeds:
			urls.append(url)
		return urls


	def make_requests(self, urls):
		""" Given list of urls of rss_feeds, this function makes GET
		requests to each url and calls parse_XML on the content of the GET """
		content = {}
		for url in urls:
			request = requests.get(url)
			if request.status_code == 200:
				content[url] = self.parse_XML(request.content)
		return content
	

	def get_links(self, category):
		""" This method reads in urls from file input and calls make_requests with the list of urls.
		A dictionary of url, article pairs is returned"""
		urls = self.file_input(category)
		return(self.make_requests(urls))
