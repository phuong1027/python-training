import sqlite3


#sql_create_table = """
#CREATE TABLE IF NOT EXISTS books (
 #   title TEXT NOT NULL,
  #  author TEXT NOT NULL,
   # year INTEGER NOT NULL
#)
#"""

#sql_insert_table = """
#INSERT INTO books VALUES ('Python', 'John', '2019')
#"""

#sql_insert_table = """
#INSERT INTO books VALUES (?, ?, ?);
#"""

#data = [
    #('Gone', 'Mai', 2020),
    #('Pie', 'Jean', 2019)
#]

sql_update_template = """
update books
set author='Jack'
where title='Python';
"""

conn = sqlite3.connect("books.db")
cur = conn.cursor()
cur.execute(sql_update_template)

conn.commit()
conn.close()