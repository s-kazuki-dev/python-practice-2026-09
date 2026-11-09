
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
SELECT products.name AS product_name, COUNT(sales_records.sale_id) AS sale_count
FROM products
LEFT JOIN sales_records
ON products.product_id = sales_records.product_id
GROUP BY products.name
ORDER BY products.product_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('------------------')

cursor = conn.execute("""
SELECT 
    products.name AS product_name,
    COUNT(sales_records.sale_id) AS sale_count,
    COALESCE(SUM(sales_records.quantity), 0) AS total_quantity,
    COALESCE(SUM(products.price * sales_records.quantity), 0) AS total_sales
FROM products
LEFT JOIN sales_records
ON products.product_id = sales_records.product_id
GROUP BY products.name
ORDER BY total_sales DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('--------------------')

cursor = conn.execute("""
SELECT
    products.name AS product_name,
    COALESCE(SUM(products.price * sales_records.quantity), 0) AS total_sales,
    CASE
        WHEN COALESCE(SUM(products.price * sales_records.quantity), 0) >= 3000 
            THEN '主力商品'
        ELSE 'その他'
    END AS sales_category
FROM products
LEFT JOIN sales_records
ON products.product_id = sales_records.product_id
GROUP BY products.name
ORDER BY total_sales DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('-------総合演習-------')


cursor = conn.execute("""
SELECT
    products.name AS product_name,
    COUNT(sales_records.sale_id) AS sale_count,
    COALESCE(SUM(sales_records.quantity), 0) AS total_quantity,
    COALESCE(SUM(products.price * sales_records.quantity), 0) AS total_sales,
    CASE
        WHEN COUNT(sales_records.sale_id) = 0
            THEN '未販売'
        WHEN COALESCE(SUM(products.price * sales_records.quantity), 0) >= 3000
            THEN '主力商品'
        ELSE '通常商品'
    END AS sales_category
FROM products
LEFT JOIN sales_records
ON products.product_id = sales_records.product_id
GROUP BY products.name
ORDER BY total_sales DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()

