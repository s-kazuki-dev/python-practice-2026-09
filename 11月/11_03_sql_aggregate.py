
import sqlite3

conn = sqlite3.connect("sales.db")

cursor = conn.execute("SELECT COUNT(*) FROM sales;")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = conn.execute("SELECT SUM(quantity) FROM sales")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = conn.execute("SELECT AVG(price) FROM sales")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = conn.execute("SELECT SUM(price * quantity) FROM sales")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = conn.execute("SELECT name, SUM(quantity) FROM sales GROUP BY name;")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = conn.execute("""
SELECT name, SUM(price * quantity)
FROM sales
GROUP BY name
ORDER BY SUM(price * quantity) DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = conn.execute("""
SELECT name, SUM(price * quantity)
FROM sales
WHERE quantity >= 8
GROUP BY name
ORDER BY SUM(price * quantity) DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = conn.execute("""
SELECT name, SUM(quantity), SUM(price * quantity)
FROM sales
WHERE price >= 400
GROUP BY name
ORDER BY SUM(price * quantity) DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()

