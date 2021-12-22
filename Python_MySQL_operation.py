import pymysql
#打开数据库连接，参数1：主机或IP；参数2：用户名；参数3：密码；参数4：数据库名称
db=pymysql.connect("localhost","root","JevyMySQL","mrsoft")
cursor=db.cursor()
cursor.execute('select version()')
data=cursor.fetchone()
print(data)
db.close()
