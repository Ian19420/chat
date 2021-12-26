def main():
	import os
	filename = "input.txt" 
	if os.path.isfile(filename):
		print("找到檔案")
		run_file(filename)
	else:
		print("找不到檔案")

def run_file(filename):
	lines = []
	with open(filename, encoding = "utf-8-sig") as f: #utf-8-sig 去除編碼問題
		for line in f:
			lines.append(line.strip())
	convert(lines)
	"""這部分你還能這樣寫
	with open(filename, encoding = "utf8") as f:
		file_str = f.read()
	print(file_str) file_str是個字串"""
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == "Allen":
			person = "Allen"
			continue
		elif line == "Tom":
			person = "Tom"
			continue
		if person:
			new.append(person + ":" + line)
	write_file(new)

def write_file(new):
	with open("output.txt", 'w') as f:
		for line in new:
			f.write(line + '\n')


main()
