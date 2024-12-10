# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:05:48 2024

@author: HUAWEI
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:50:35 2023

@author: youmisuk
"""

Warm-up: Table joins

PURPOSE
In this small exercise, you will create two tables and join them,
using Python.

You might want to use the sqlite lecture notes as a reference
------------------------------------------------------------------
# python
import sqlite3

# create some data
company_hq = [
        ('NVDA','Santa Clara'),
        ('AAPL','Cupertino'),
        ('GOOG','Mountain View')]

company_ceos = [
        ('NVDA','Jensen Huang'),
        ('AAPL','Tim Cook')]


# connect to db

# update with your path to the database
path_to_db = "/Users/HUAWEI/sqlite/wmup.db"    

# create db connection
conn = sqlite3.connect(path_to_db)

# create cursor
cur = conn.cursor()

# create a table in the db called "hq" and pass schema (ticker text, location text)
# end the transaction with a commit
cur.execute('create table hq (ticker text, location text)')
conn.commit()

# create a table in the db called "ceo" and pass schema (ticker text, ceo text)
cur.execute('create table ceo (ticker text, ceo text)')
conn.commit()

# insert records into hq table
cur.executemany('insert into hq values (?,?)', company_hq)
conn.commit()

# insert records into ceo table
cur.executemany('insert into ceo values (?,?)', company_ceos)
conn.commit()

# query each table to make sure all the data has been loaded
for row in cur.execute('select * from hq'):
    print(row)

# repeat for ceo table
for row in cur.execute('select * from ceo'):
    print(row)

# join the two tables together, printing records with columns: ticker, location, ceo
# Run the code below, notice the result, and we will discuss it.
    
for row in conn.execute('select hq.ticker, hq.location, ceo.ceo \
                        from hq inner join ceo \
                        on hq.ticker = ceo.ticker'):
    print(row)
    
# Next, change inner join to left join, run the query, and notice the result
for row in conn.execute('select hq.ticker, hq.location, ceo.ceo \
                        from hq left join ceo \
                        on hq.ticker = ceo.ticker'):
    print(row)#left join是取并集

# For discussion:
# 1) notation: table.field; for example hq.ticker
# 2) inner join vs left join
# 3) joining "on" fields