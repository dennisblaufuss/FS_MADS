import mysql.connector as sql

mydb = sql.connect(host="localhost", user="root", passwd="", charset="utf8")

mycursor = mydb.cursor()
mycursor.execute("Use ShopDB")


# Excercise 1
print("Excercise 1")
query = "select * from product"
mycursor.execute(query)
for x in mycursor:
    print(x)


# Excercise 2
print()
print("Excercise 2")
query = "select * from product"
where = input("input your filter here (without the where):")
if where != "":
    where = "where " + where
mycursor.execute(query + " " + where)
for x in mycursor:
    print(x)

mydb.close()


# Exercise 3
def GenerateProductList():
    mydb = sql.connect(host="localhost", user="root", passwd="", charset="utf8")
    mycursor = mydb.cursor()
    mycursor.execute("Use ShopDB")

    p_list = []
    query = "select Product_ID from product"
    mycursor.execute(query)
    for x in mycursor:
        p_list.append(x[0])
    mydb.close()
    print(p_list)
    return


GenerateProductList()

# Exercise 4
def SearchProductID(ID):
    mydb = sql.connect(host="localhost", user="root", passwd="", charset="utf8")
    mycursor = mydb.cursor()
    mycursor.execute("Use ShopDB")

    query = "select * from product where product_id = %s"
    mycursor.execute(query, (ID,))
    record = mycursor.fetchone()
    if record is None:
        return "ID not found"
    if mycursor.fetchone() is not None:
        return "ID is given twice"
    mydb.close()
    return record


SearchProductID(3)


# Exercise 5
def PrintProducts():
    mydb = sql.connect(host="localhost", user="root", passwd="", charset="utf8")
    mycursor = mydb.cursor()
    mycursor.execute("Use ShopDB")

    query = "select * from product"
    mycursor.execute(query)
    record = mycursor.fetchone()
    while record is not None:
        print(record)
        record = mycursor.fetchone()
    mydb.close()
    return


PrintProducts()
