
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("PRAGMA foreign_keys = ON;")

conn.execute("""
CREATE TABLE products(
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    price INTEGER NOT NULL
);
""")
conn.execute("""
CREATE TABLE sales_records(
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price INTEGER NOT NULL,
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);
""")

conn.execute("INSERT INTO products VALUES (1, 'コーヒー', 400);")
conn.execute("INSERT INTO products VALUES (2, '紅茶', 350);")
conn.execute("INSERT INTO products VALUES (3, 'ケーキ', 500);")

conn.execute("INSERT INTO sales_records VALUES (1, 1, 10, 400);")
conn.execute("INSERT INTO sales_records VALUES (2, 2, 5, 350);")
conn.execute("INSERT INTO sales_records VALUES (3, 3, 3, 500);")

conn.commit()

conn.execute("""
UPDATE products
SET price = ?
WHERE product_id = ?;
""", (500, 1))

conn.execute("INSERT INTO sales_records VALUES(4, 1, 2, 500)")

conn.commit()

cursor = conn.execute("""
SELECT
    products.name,
    sales_records.quantity,
    sales_records.unit_price,
    sales_records.quantity * sales_records.unit_price AS sales_amount
FROM products
INNER JOIN sales_records
ON products.product_id = sales_records.product_id
ORDER BY sales_records.sale_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('---------------------------')

conn.execute("INSERT INTO products VALUES (?, ?, ?);", (4, '水', 200))

conn.commit()

cursor = conn.execute("""
SELECT
    products.name AS product_name,
    COUNT(sales_records.sale_id) AS sale_count,
    COALESCE(SUM(sales_records.quantity), 0) AS total_quantity,
    COALESCE(SUM(sales_records.unit_price * sales_records.quantity), 0) AS total_sales
FROM products
LEFT JOIN sales_records
ON products.product_id = sales_records.product_id
GROUP BY products.name, products.product_id
ORDER BY total_sales DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('最終総合演習')

cursor = conn.execute("""
SELECT 
    products.name AS product_name,
    products.price AS current_price,
    COALESCE(SUM(sales_records.unit_price * sales_records.quantity), 0) AS actual_sales,
    COALESCE(SUM(products.price * sales_records.quantity), 0) AS incorrect_sales,
    COALESCE(SUM(products.price * sales_records.quantity), 0)
    -
    COALESCE(SUM(sales_records.unit_price * sales_records.quantity), 0) AS difference
FROM products
LEFT JOIN sales_records
ON products.product_id = sales_records.product_id
GROUP BY products.name, products.product_id
ORDER BY difference DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('------------------------------')

cursor = conn.execute("""
SELECT 
    products.name AS product_name,
    COALESCE(SUM(sales_records.unit_price * sales_records.quantity), 0) AS total_sales,
    CASE
        WHEN COALESCE(SUM(sales_records.unit_price * sales_records.quantity), 0) = 0
            THEN '未販売'
        WHEN COALESCE(SUM(sales_records.unit_price * sales_records.quantity), 0) >= 3000
            THEN '主力商品'
        ELSE '通常商品'
    END AS sales_category
FROM products
LEFT JOIN sales_records
ON products.product_id = sales_records.product_id
GROUP BY products.name, products.product_id
ORDER BY total_sales DESC, products.product_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()
