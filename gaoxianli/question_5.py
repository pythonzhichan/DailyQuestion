import re
class url:
	def __init__(self, url_str):
		self.url_str=url_str

	def url_parse(self):
		# 协议
		m = re.search(r"([a-zA-Z]+(?=://))?", self.url_str)
		scheme=m.group()

		# 主机名
		m = re.search(r"(?<=//)?([a-zA-Z0-9]+-?[a-zA-Z0-9]+\.?)+\.[a-zA-Z]+(?=\/)?", self.url_str)
		netloc=m.group()

		# 路径
		m = re.search(r"(?<=[a-zA-Z])(\.?\/[\w\-\.\#\%\(\)\']*)+", self.url_str)
		path=m.group()

		# 查询参数
		query_params_key = re.findall(r"(?<=\?|\&)[\w\-]+(?=\=)", self.url_str)
		query_params_value = re.findall(r"(?<=\=)[\w\-\=\%]+(?=\&)?", self.url_str)
		query_params = {}
		for index in range(len(query_params_key)):
			query_params.update({query_params_key[index] : query_params_value[index]})

		# 分段（指定id所在的位置）
		m = re.search(r"((?<=\#)([\w\-\/\.]*))?$", self.url_str)
		fragment=m.group()

		print("scheme:", scheme)
		print("netloc:", netloc)
		print("path:", path)
		print("query_params:", query_params)
		print("fragment:", fragment, "\n")


if __name__ == "__main__":
	try:
		while True:
			url_str = input("解析URL：")
			urlapp = url(url_str)
			urlapp.url_parse()
	except KeyboardInterrupt:
		print("结束\n")
