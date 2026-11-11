
import sqlite3

conn = sqlite3.connect(":memory:")

#商品マスター
conn.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
);
""")

#販売記録
conn.execute("""
CREATE TABLE sales_records (
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER
);
""")

#商品マスターにデータを追加
conn.execute("INSERT INTO products VALUES (1, 'コーヒー', 400);")
conn.execute("INSERT INTO products VALUES (2, '紅茶', 350);")
conn.execute("INSERT INTO products VALUES (3, 'ケーキ', 500);")
conn.execute("INSERT INTO products VALUES (4, '水', 200);")

#販売記録を追加
conn.execute("INSERT INTO sales_records VALUES (1, 1, 4);")
conn.execute("INSERT INTO sales_records VALUES (2, 1, 8);")
conn.execute("INSERT INTO sales_records VALUES (3, 2, 5);")
conn.execute("INSERT INTO sales_records VALUES (4, 3, 3);")

conn.commit()

conn.execute("""
UPDATE products
SET price = 250
WHERE product_id = 4;
""")
conn.commit()
cursor = conn.execute("""
SELECT name, price
FROM products
ORDER BY product_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('---------------------')

conn.execute("""
DELETE FROM sales_records
WHERE sale_id = 4
""")
conn.commit()
cursor = conn.execute("""
SELECT *
FROM sales_records
ORDER BY sale_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('---------------------')

conn.execute("""
UPDATE products
SET price = ?
WHERE product_id = ?;
""", (300, 4))
conn.commit()
cursor = conn.execute("""
SELECT name, price
FROM products
ORDER BY product_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('-----------------------')

conn.execute("""
INSERT INTO sales_records
VALUES (?, ?, ?);
""", (5, 4, 2))
conn.commit()
cursor = conn.execute("""
SELECT *
FROM sales_records
ORDER BY sale_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('最終総合演習')

conn.execute("""
UPDATE products
SET price = ?
WHERE product_id = ?;
""", (999, 1))
cursor = conn.execute("""
SELECT name, price
FROM products
WHERE product_id = 1;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.rollback()

cursor = conn.execute("""
SELECT name, price
FROM products
WHERE product_id = 1;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()

