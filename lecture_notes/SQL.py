# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:51:08 2024

@author: HUAWEI
"""

# python
import sqlite3

# create some data
stocks = [
        ('NVDA',219,-3.42),
        ('AAPL',146,-2.73),
        ('GOOG',2829.27,-58.20)]


# connect to db

# update with your path to the database
path_to_db = "/Users/HUAWEI/sqlite/stocks.db"    

# create db connection
conn = sqlite3.connect(path_to_db)

# create cursor
cur = conn.cursor()#to point out the record you want to get

# create a table in the db called "holdings" and pass a schema
# end the transaction with a commit
cur.execute('create table holdings (ticker text, price real, chg real)')
conn.commit()

# insert multiple records of data with executemany()
cur.executemany('insert into holdings values (?,?,?)', stocks)
conn.commit()

# query the table
# print all the rows
for row in conn.execute('select * from holdings'):
    print(row)

# print all the rows where price > 200
for row in conn.execute('select * from holdings where price > 200'):
    print(row)

# print all the rows where price > 200. show only ticker, price
for row in conn.execute('select ticker, price from holdings where price > 200'):
    print(row)

# save the resultant dataset in a list
data = []
for row in conn.execute('select ticker, price from holdings where price > 200'):
    data.append(row)

# TRY FOR YOURSELF 
# Create a dataframe with columns: ticker, price.
# Load all of the data into the dataframe


------------------------------------------------------------------
Lastly, we revisit SQLite

List the tables
sqlite> .tables
holdings

Select all data from holdings. Notice queries end with ;
sqlite> select * from holdings;#在CMD中运行
NVDA|219.0|-3.42
AAPL|146.0|-2.73
GOOG|2829.27|-58.2


TRY FOR YOURSELF 
Write a query that returns all rows where chg > -3.

Exit SQLite
sqlite> .q

#将SQL格式转换成panda的形式，然后就可以去panda里面分析了
#import pandas as pd

#df = pd.DataFrame(columns = ['ticker','price'], data = data)

#df
------------------------------------------------------------------