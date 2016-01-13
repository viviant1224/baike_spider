# coding:utf8
class SpiderMain(object):

	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloadder = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print('craw %d :%s' % (count, new_url))
				html_cont = self.downloadder.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(news_urls)
				self.outputer.collect_data(new_data)

				if count == 1000:
					break

				count = count + 1
		except:
			print('craw failed')
		self.outputer.outout_html() 

if __name__ == "__main__":
	root_url = ""
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)

