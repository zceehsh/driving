# 让使用者输入年龄，国家；从而判断可否开车。
country = input('你是哪国人： ')
age = input('请输入您的年龄： ')
age = int(age)
if country == '台湾':
	if age >= 18:
		print('你可以考驾照。')
	else:
		print('你不可以考驾照。')
