 # coding:utf8
class HtmlOutputer(object):

	def __init__(self):
		self.datas = []
	
	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	def outout_html(self):
		#python 2.x 与python3.x有区别
		fout = open('output.html', 'w', encoding='utf-8')
		fout.write("<html>")
		fout.write("<head>")
		fout.write('<meta charset="utf-8">')
		fout.write("</head>")
		fout.write("<body>")
		fout.write("<table>")
		#ascii
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<<td>%s</td>" % data['url'])
			fout.write("<<td>%s</td>" % data['title'])
			fout.write("<<td>%s</td>" % data['summary'])
		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")