import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE books
                  (name TEXT, pages INTEGER, price REAL, barcode TEXT)''')
cursor.execute("INSERT INTO books VALUES ('Book 1', 200, 150.0, '')")

book_data = [
    ('Book 2', 300, 120.0, ''),
    ('Book 3', 150, 90.0, ''),
    ('Book 4', 250, 200.0, ''),
]
cursor.executemany("INSERT INTO books VALUES (?, ?, ?, '')", book_data)

cursor.execute("SELECT * FROM books WHERE price > 100.0")
expensive_books = cursor.fetchall()
print("Expensive books:")
for book in expensive_books:
    print(book)

cursor.execute("SELECT * FROM books ORDER BY price ASC LIMIT 3")
cheap_books = cursor.fetchall()
print("Cheap books:")
for book in cheap_books:
    print(book)
    cursor.execute("SELECT * FROM books WHERE name LIKE '%історія%' LIMIT 2")
    history_books = cursor.fetchall()
    print("History books:")
    for book in history_books:
        print(book)

    cursor.execute("ALTER TABLE books ADD COLUMN barcode TEXT")

    cursor.execute("UPDATE books SET barcode = '0-00045' WHERE pages > 200")

    cursor.execute("DELETE FROM books WHERE price = 100.0")

    conn.commit()
    conn.close()
