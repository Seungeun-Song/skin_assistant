import pymysql

test_db = pymysql.connect(user='root', passwd='team09', host='35.180.122.212', db='mydb', charset='utf8')
cursor = test_db.cursor()
sql = "SELECT img_url1 FROM user_face"
cursor.execute(sql)
result = cursor.fetchall()


for key, value in result:
    print("key:",key)
    print("value:",value)
#print(result)
