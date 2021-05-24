import pymssql


class linkDB():
    def linkdb():
        # 数据库远程连接
        conn = pymssql.connect(host="test.weiningbo.net:21433", user="sa", password="Weiningbo2020", database="MatchData_CS", charset="GBK")
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        # 查询语句
        sql = "select * from FenbuItem"
        try:
            cursor.execute(sql)  # 游标
            result = cursor.fetchall()  # 查询
            print(result)
        except:
            print("连接数据库报错了！")
        # 关闭数据库连接
        conn.close()


if __name__ == '__main__':
    linkDB.linkdb()