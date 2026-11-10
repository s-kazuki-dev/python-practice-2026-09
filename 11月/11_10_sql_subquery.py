
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

cursor = conn.execute("""
SELECT name, price
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
    )
ORDER BY product_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('--------------------')

cursor = conn.execute("""
SELECT name, price
FROM products
WHERE product_id IN (
    SELECT product_id
    FROM sales_records
    WHERE quantity >= 5
    )
ORDER BY product_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('---------------------')

cursor = conn.execute("""
SELECT
    products.name AS product_name,
    products.price AS unit_price,
    COALESCE(SUM(products.price * sales_records.quantity), 0) AS total_sales,
    CASE
        WHEN products.price > (
            SELECT AVG(price)
            FROM products
            )
        THEN '平均超え'
        ELSE '平均以下'
    END AS price_category
FROM products
LEFT JOIN sales_records
ON products.product_id = sales_records.product_id
GROUP BY products.product_id, products.name, products.price
ORDER BY total_sales DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()
