import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="",
                               charset="utf8")

mycursor = mydb.cursor()

mycursor.execute("SHOW databases")
for x in mycursor:
    print(x)

mycursor.execute("USE securitiesaccountmanagement")

mycursor.execute("SHOW Tables")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM customer")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM customer")
myresult = mycursor.fetchall()
for record in myresult:
    print(record)

mycursor.execute("SELECT * FROM customer")
myresult = mycursor.fetchall()
for record in myresult:
    print("ID:", record[0], "Name:", record[1])

mycursor.execute("SELECT * FROM customer")
myresult = mycursor.fetchall()
for i in range(0,len(myresult)):
    print(myresult[i])
print(myresult[3])
print(myresult[1])
print(myresult[0][2])

mycursor.execute("SELECT * FROM customer")
record = mycursor.fetchone()
while record is not None:
    print(record)
    record = mycursor.fetchone()

name = "Meier, Thomas"
query = "SELECT * FROM customer WHERE Name='" + name + "'"
mycursor.execute(query)
myresult = mycursor.fetchall()
for record in myresult:
    print(record)

id = 3
query = "SELECT * FROM customer WHERE Customer_id=" + str(id)
mycursor.execute(query)
myresult = mycursor.fetchall()
for record in myresult:
    print(record)

id = 3
name = "Meier, Thomas"
query = "SELECT * FROM customer WHERE Customer_id=%s and Name=%s"
mycursor.execute(query, (id, name))
myresult = mycursor.fetchall()
for record in myresult:
    print(record)

id = 6
name = "Rossbach, Peter"
address = "Adickesallee 32-34, 60322 Frankfurt"
query = "INSERT INTO customer (Customer_id, Name, Address) VALUES (%s,%s,%s)"
mycursor.execute(query, (id, name, address))

id = 6
name = "Stieglitz, Nils"
query = "UPDATE customer SET Name=%s WHERE Customer_id=%s"
mycursor.execute(query, (name, id))

id = 6
query = "DELETE FROM customer WHERE Customer_id=%s"
mycursor.execute(query, (id,))

mydb.close()
