# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:38:28 2021

@author: Saurabh
"""

import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mydb@2010",
  database="ecommerce"
)

# Define a Cursor
cursor = database.cursor()

# Drop a table
sql = "DROP TABLE IF EXISTS transactions"
cursor.execute(sql)

# Create table sql
sql = """CREATE TABLE transactions (
      payment_id       VARCHAR(255) NOT NULL,
      type             VARCHAR(255),
	  amount           DECIMAL (6,2) NOT NULL,
	  currency         VARCHAR(10),
	  status           VARCHAR(255),
	  method           VARCHAR(255),
	  order_id         VARCHAR(255),
	  description      VARCHAR(255),
	  refund_status    VARCHAR(255),
	  amount_refunded  DECIMAL(6,2) NOT NULL,
	  email            VARCHAR(255),
	  contact          VARCHAR(255),
	  error_code       VARCHAR(255),
	  date_created     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (payment_id) 
      )"""

cursor.execute(sql)

cursor.close()
database.close()





