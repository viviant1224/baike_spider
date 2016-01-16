# coding:utf8
import urllib.request
"""
Html content download
"""

class HtmlDownloader(object):

	def download(self, url):
		if url is None:
			return None
		response = urllib.request.urlopen(url)

		if response.getcode() != 200:
			return None
		return response.read()