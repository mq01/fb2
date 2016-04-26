import sublime, sublime_plugin, re

class FixCommand(sublime_plugin.TextCommand):
	
	def run(self, edit):
		src = self.view
		
		# список строк из тэгов
		tag = "p"
		listStr = []
		listTagText = src.find_all(r'<' + tag + r'>.*</' + tag + r'>')
		for item in listTagText:
			listStr.append(src.substr(item))

		# замена тире
		listStrReplaced = []
		for i in range(0, len(listStr)):
			listStrReplaced.append(re.sub(r'- ', '— ', listStr[i]))

		# замена в тексте
		for i in range(0, len(listStr)):
			src.replace(edit, listTagText[i], listStrReplaced[i])



	# def getStrListFromTags(tag):
	# 	listStr = []
	# 	#count = 0
	# 	listTagText = src.find_all(r'<' + tag + r'>.*</' + tag + r'>')
	# 	for item in listTagText:
	# 		listStr.append(src.substr(item))
	# 		#count += 1
	# 	return listStr
	
	# def replaceDashes(listStr):
	# 	listStrReplaced = []
	# 	for i in range(0, listStr.count + 1):
	# 		listStrReplaced[i] = re.sub(r'- ', '— ', listStr[i])
	# 	return listStrReplaced

	# def replaceInText(listStr, listStrReplaced):
	# 	for i in range(0, listStr.count + 1):
	# 		src.replace(edit, listStr[i], listStrReplaced[i])

	# def replaceTestTag():
	# 	test_tag_content = src.substr(src.find_all(r'<test>.*</test>')[0])
	# 	test_tag_content = re.findall(r'>(.*)<', test_tag_content)[0]
	# 	src.replace(edit, src.find(r'<title>.*</title>', 0),
	# 	 "<title>" + test_tag_content + "</title>")
	# 	src.insert(edit, 1, "test");



	
		
