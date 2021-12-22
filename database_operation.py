import sqlite3
'''
#创建user数据表
conn=sqlite3.connect("mrsoft.db")
cursor=conn.cursor()
cursor.execute('create table user (id int(10) primary key, name varchar(20))')
cursor.close()
conn.close()
'''

'''
#新增用户数据信息
conn=sqlite3.connect('mrsoft.db')
cursor=conn.cursor()
cursor.execute('insert into user (id,name) values ("1","MRSOFT")')
cursor.execute('insert into user (id,name) values ("2","Andy")')
cursor.execute('insert into user (id,name) values ("3","Tom")')
cursor.close()
conn.commit()
conn.close()
'''

'''
#查询用户信息
conn=sqlite3.connect('mrsoft.db')
cursor=conn.cursor()
cursor.execute('select * from user')
#获取查询结果
result1=cursor.fetchone()
print(result1)
cursor.close()
conn.close()
'''

'''
#修改用户信息
conn=sqlite3.connect('mrsoft.db')
cursor=conn.cursor()
cursor.execute('update user set name=? where id=?',('MR',1))
cursor.execute('select * from user')
result=cursor.fetchall()
print(result)
cursor.close()
conn.commit()
conn.close()
'''

'''
#删除用户信息
conn=sqlite3.connect('mrsoft.db')
cursor=conn.cursor()
cursor.execute('delete from user where id = ?',(1,))
cursor.execute('select * from user')
result=cursor.fetchall()
print(result)
cursor.close()
conn.commit()
conn.close()
'''