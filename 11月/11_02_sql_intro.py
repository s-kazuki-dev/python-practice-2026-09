import sqlite3


conn = sqlite3.connect("sales.db")

sql = """
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    quantity INTEGER
)
"""
conn.execute(sql)


# sql_insert = """
# INSERT INTO sales (name, price, quantity)
# VALUES ('コーヒー', 400, 12);
# """
# conn.execute(sql_insert)

# sql_insert = """
# INSERT INTO sales (name, price, quantity)
# VALUES ('紅茶', 350, 8);
# """
# conn.execute(sql_insert)

# sql_insert = """
# INSERT INTO sales (name, price, quantity)
# VALUES ('ケーキ', 500, 5);
# """
# conn.execute(sql_insert)

# conn.commit()


cursor = conn.execute("SELECT * FROM sales;")
rows = cursor.fetchall()

for row in rows:
    print(row)

# cursor = conn.execute("SELECT * FROM sales WHERE price >= 400;")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# cursor = conn.execute("SELECT * FROM sales WHERE quantity < 10;")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# cursor = conn.execute("SELECT * FROM sales WHERE name = '紅茶';")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# conn.commit()


# cursor = conn.execute("SELECT * FROM sales ORDER BY price ASC;")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# cursor = conn.execute("SELECT * FROM sales ORDER BY quantity DESC;")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# cursor = conn.execute("SELECT * FROM sales WHERE price >= 400 ORDER BY price DESC;")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

cursor = conn.execute("SELECT name, price, quantity FROM sales WHERE quantity >= 8 ORDER BY price DESC;")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()

