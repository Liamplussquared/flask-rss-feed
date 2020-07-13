import unittest, aggregator, requests

class TestAgg(unittest.TestCase):
	def setUp(self):
		self.agg = aggregator.Aggregator()

	def test_parsing_empty(self):
		""" Test that parse_XML can handle empty input"""
		self.assertFalse(self.agg.parse_XML(""), "Must be able to handle empty input")

	def test_parsing_correct(self):
		""" Test that parse_XML handles right format input correctly"""
		r = requests.get("https://www.theguardian.com/world/rss")
		self.assertIsNotNone(self.agg.parse_XML(r.content), "Should return articles from valid URL")

	def test_parsing_incorrect(self):
		""" Test that parse_XML handles incorrectly formatted input correctly"""
		self.assertFalse(self.agg.parse_XML(123456), "Should only accept dictionaries as input")
		

if __name__ == '__main__':
	unittest.main()