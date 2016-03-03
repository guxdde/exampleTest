# -*- coding:utf-8 -*-

import MySQLdb


def save_to_mysql():
    conn = MySQLdb.connect(
        host="localhost", user="guxdde", passwd="123456", db="list", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("show tables;")
    tables = cursor.fetchall()
    flag = False
    for table in tables:
        if 'code' in table:
            flag = True
    if flag:
        cursor.execute('''CREATE TABLE code (
            id INT NOT NULL AUTO_INCREMENT,
            code VARCHAR(10) NOT NULL,
            PRIMARY KEY(id)
            )''')
    code_list = []
    with open('activation_code.txt', 'rb') as f:
        for line in f.readlines():
            code_list.append(line.strip())
    for code in code_list:
        cursor.execute("insert into code (code) values(%s);",[code])
    conn.commit()
    #cursor.close()
    conn.close()
