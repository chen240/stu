from pymongo import MongoClient

#1.创建数据库连接
conn=MongoClient('localhost',27017)

#２．创建数据库对象
db=conn.stu
#db=conn['stu']

#３．创建集合对象
myset=db.class4

#4.数据操作
# print(dir(myset))

myset.insert({'name':'张铁林','King':"乾隆"})



#５．关闭连接
conn.close()