
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

#JOIN
cursor = conn.execute("""
SELECT products.name, sales_records.quantity
FROM products
INNER JOIN sales_records
ON products.product_id = sales_records.product_id
ORDER BY sales_records.sale_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor = conn.execute("""
SELECT products.name, SUM(sales_records.quantity), SUM(products.price * sales_records.quantity)
FROM products
INNER JOIN sales_records
ON products.product_id = sales_records.product_id
GROUP BY products.name
ORDER BY SUM(products.price * sales_records.quantity) DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = conn.execute("""
SELECT products.name, sales_records.quantity
FROM products
LEFT JOIN sales_records
ON products.product_id = sales_records.product_id
ORDER BY products.product_id ASC, sales_records.sale_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('最終総合演習')
cursor = conn.execute("""
SELECT products.name, SUM(sales_records.quantity), SUM(products.price * sales_records.quantity)
FROM products
LEFT JOIN sales_records
ON products.product_id = sales_records.product_id
GROUP BY products.name
ORDER BY products.product_id;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)



conn.close()
