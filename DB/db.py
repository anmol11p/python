import mysql.connector


try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anmol0031@",
        database="anp_d1388"
    )
    if conn.is_connected():
        print("db connection built successfully!!")
        cursor=conn.cursor()

        #? query
        # cursor.execute("show tables")
        # tables=cursor.fetchall()
        
        # crud
        #* create 
        # query="insert into users(name,email,age) values(%s,%s,%s)"
        # values=("anmol pandey","pandayji@gmail.com",22)
        # cursor.execute(query,values)
        # conn.commit()
        # print("record insert successfully")

        #* read
        # query="select * from users"
        # cursor.execute(query) 
        # rows=cursor.fetchall()
        # for i in rows:
        #     print(i)

        #* update
        # query="update users set name=%s where id=%s"
        # values=("anubhav","6")
        # cursor.execute(query,values)
        # conn.commit()
        # print("updating success!")

        #*  delete
        # query="delete from users where id=%s"
        # value=(1,)
        # cursor.execute(query,value)
        # conn.commit()
        # print("data deletion successfully!")
except Exception as e:
    print(e)
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print('connection close')
