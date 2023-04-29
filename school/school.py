import mysql.connector

""" MySQL Connection """
mainDB = mysql.connector.connect(
    host="b9syngpkzy7gldxwdbjk-mysql.services.clever-cloud.com",
    user="uov5wkc5efcarh2f",
    password="tVaFBwD3ZiYPhAs4xWXF",
    database="b9syngpkzy7gldxwdbjk"
)

""" MySQL Cursor """
mainCursor = mainDB.cursor()