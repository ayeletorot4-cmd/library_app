
from db import run_query_select, run_update_query
##2)Run the two CREATE TABLE statements using run_update_query().
run_update_query("""DROP TABLE IF EXISTS authors;""")
run_update_query("""DROP TABLE IF EXISTS books;""")
run_update_query("""CREATE TABLE authors (
  id      INTEGER PRIMARY KEY,
  name    TEXT    NOT NULL,
  country TEXT)""")
run_update_query("""CREATE TABLE books (
  id        INTEGER PRIMARY KEY,
  title     TEXT    NOT NULL,
  author_id INTEGER,
  year      INTEGER NOT NULL,
  FOREIGN KEY (author_id) REFERENCES authors(id)
)""")

##3)Use these INSERT statements as the SQL inside run_update_query(sql, params)
run_update_query("INSERT INTO authors (id,name,country )VALUES (?,?,?)",(1, 'George Orwell','UK'))
run_update_query("INSERT INTO authors (id,name,country )VALUES (?,?,?)",(2, 'Gabriel García Márquez', 'Colombia'))
run_update_query("INSERT INTO authors (id,name,country )VALUES (?,?,?)",(3, 'Haruki Murakami','Japan'))

run_update_query("INSERT INTO books (id,title,author_id,year )VALUES (?,?,?,?)",(1, '1984',1, 1949))
run_update_query("INSERT INTO books (id,title,author_id,year )VALUES (?,?,?,?)",(2, 'Animal Farm',1, 1945))
run_update_query("INSERT INTO books (id,title,author_id,year )VALUES (?,?,?,?)",(3, 'One Hundred Years of Solitude', 2, 1967))
run_update_query("INSERT INTO books (id,title,author_id,year )VALUES (?,?,?,?)",(4, 'Norwegian Wood',3, 1987))

##4)Run SELECT * FROM books and print each book's title using row["title"].

books=run_query_select("SELECT * FROM books")
for book in books:
    print(book["title"])

##5)Add a WHERE clause to show only books published after 1960.
books=run_query_select("SELECT * FROM books WHERE year>1960")
for book in books:
    print(book)

##6)Write an INNER JOIN to print: title — author name (e.g. 1984 — George Orwell).
title_author=run_query_select("""SELECT b.title, a.name
FROM   books b
INNER JOIN authors a ON b.author_id = a.id;""")
for title_author in title_author:
    print(title_author["title"],"-", title_author["name"])
##7)Add input() to let the user add a new book. Wrap the INSERT in try/except.

title=input("please insert the title of your book:")
author_id=input("please insert the author of your book:")
year=input("please insert the year of your book:")

try:
   run_update_query("INSERT INTO books (title, author_id, year) VALUES (?,?,?)",(title,int(author_id),int(year)))
   print(run_query_select("SELECT * FROM books ORDER BY id DESC LIMIT 1"))
except Exception as e:
    print("insert failed")
    print(e)
