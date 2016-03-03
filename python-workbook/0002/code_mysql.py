# -*- coding:utf-8 -*-

import MySQLdb


def read_file(file_name):
    code_list = []
    with open(file_name, 'rb') as f:
        for line in f.readlines():
            code_list.append(line.strip())
    return code_list


def save_to_mysql():
    code_list = read_file('activation_code.txt')
    conn = MySQLdb.connect(
        host="localhost", user="guxdde", passwd="123456", db="list", charset="utf8")
    cursor = conn.cursor()
    try:
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
        for code in code_list:
            cursor.execute("insert into code (code) values(%s);", [code])
        conn.commit()
    except Exception, e:
        raise e
    finally:
        conn.close()
    # cursor.execute("show tables;")
    # tables = cursor.fetchall()
    # flag = False
    # for table in tables:
    #     if 'code' in table:
    #         flag = True
    # if flag:
    #     cursor.execute('''CREATE TABLE code (
    #         id INT NOT NULL AUTO_INCREMENT,
    #         code VARCHAR(10) NOT NULL,
    #         PRIMARY KEY(id)
    #         )''')
    # for code in code_list:
    #     cursor.execute("insert into code (code) values(%s);", [code])
    # conn.commit()
    # cursor.close()
