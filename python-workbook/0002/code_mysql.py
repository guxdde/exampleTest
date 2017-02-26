# -*- coding:utf-8 -*-

import MySQLdb


def read_file(file_name):
    code_list = []
    with open(file_name, 'rb') as f:
        for line in f.readlines():
            code_list.append(line.strip())
    return code_list


def save_to_mysql(file_name):
    code_list = read_file(file_name)
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
        if not flag:
            cursor.execute('''CREATE TABLE code (
                id INT NOT NULL AUTO_INCREMENT,
                code VARCHAR(10) NOT NULL,
                PRIMARY KEY(id)
                )''')
        for code in code_list:
            if len(code) > 0:
                cursor.execute(
                    "insert into code (code) values(%s);", [code])
        conn.commit()
    except Exception, e:
        conn.rollback()
        print e
    finally:
        conn.close()


if __name__ == '__main__':
    save_to_mysql('activation_code.txt')
