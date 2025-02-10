import mysql.connector

mydb = mysql.connector.connect(
  host="abcd.com",
  user="eshwar",
  passwd="abcdzyx",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name , DOB, phone , email, address) VALUES (%s, %s, %s, %s, %s)"
val = [("Yash", "01/01/2013", "9738432543", "yash@gmail.in", "no.53, bangalore"),
        ("raju", "02/01/2013", "123456654", "raju@gmail.in", "no.51, bangalore"),
        ("mahesh", "03/01/2015", "1234556677", "mahesh@gmail.in", "no.52, bangalore"),
        ("manju", "05/06/1995", "9876567812", "manju@gmail.in", "no.56, bangalore"),
        ("latesh", "15/01/2001", "1234545656", "latesh@gmail.in", "no.58, bangalore"),
        ("sanju", "12/05/2003", "6566446745", "sanju@gmail.in", "no.60, bangalore"),
        ("Ramu", "22/07/2017", "97384445566", "ramu@gmail.in", "no.62, bangalore")
       ]
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record insertion completed.")
