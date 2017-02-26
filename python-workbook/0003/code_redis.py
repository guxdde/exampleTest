# -*-coding:utf-8-*-

import redis

def read_file(file_name):
    code_list = []
    with open(file_name, 'rb') as f:
        for line in f.readlines():
            code_list.append(line.strip())
    return code_list

def save_to_redis(file_name):
	code_list = read_file(file_name)
	r = redis.Redis(host='localhost', port=6379, db=0)
	for code in code_list:
		r.lpush('code',code.strip())
	

if __name__=='__main__':
	save_to_redis('activation_code.txt')
	
	


