# -*- coding:utf-8 -*-
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import string, random


def create_code(count, size):
	count = int(count)
	size = int(size)
	chars = string.letters+string.digits
	result = []
	for i in range(count):
		result.append(''.join([random.choice(chars) for i in range(size)]))
	with open('activation_code.txt', 'wb') as f:
		f.write('\n'.join(result))
	return

if __name__=='__main__':
	count = raw_input('激活码个数：')
	size = raw_input('激活码长度：')
	create_code(count,size)
