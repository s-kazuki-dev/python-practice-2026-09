
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
    sales_date TEXT NOT NULL,
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);
""")

conn.execute("INSERT INTO products VALUES (1, 'コーヒー', 500);")
conn.execute("INSERT INTO products VALUES (2, '紅茶', 350);")
conn.execute("INSERT INTO products VALUES (3, 'ケーキ', 500);")
conn.execute("INSERT INTO products VALUES (4, '水', 200);")

conn.execute("INSERT INTO sales_records VALUES (1, 1, 3, 400, '2026-11-14');")
conn.execute("INSERT INTO sales_records VALUES (2, 3, 2, 500, '2026-11-14');")
conn.execute("INSERT INTO sales_records VALUES (3, 2, 4, 350, '2026-11-15');")
conn.execute("INSERT INTO sales_records VALUES (4, 1, 5, 450, '2026-11-16');")
conn.execute("INSERT INTO sales_records VALUES (5, 2, 2, 350, '2026-11-16');")
conn.execute("INSERT INTO sales_records VALUES (6, 4, 2, 200, '2026-11-17');")

conn.commit()

cursor = conn.execute("""
WITH daily_sales AS(
    SELECT 
        sales_date,
        SUM(unit_price * quantity) AS total_sales
    FROM sales_records
    GROUP BY sales_date
)
SELECT 
    sales_date,
    total_sales
FROM daily_sales
WHERE total_sales >= 2000
ORDER BY total_sales DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('----------------------------------------')

conn.execute("INSERT INTO products VALUES (5, 'サンドイッチ', 650);")
conn.commit()

cursor = conn.execute("""
WITH product_sales AS(
    SELECT
        products.name AS product_name,
        COUNT(sales_records.sale_id) AS sale_count,
        COALESCE(SUM(sales_records.quantity), 0) AS total_quantity,
        COALESCE(SUM(sales_records.unit_price * sales_records.quantity), 0) AS total_sales
    FROM products
    LEFT JOIN sales_records
    ON products.product_id = sales_records.product_id
    GROUP BY products.product_id, products.name
)
SELECT 
    product_name,
    sale_count,
    total_quantity,
    total_sales,
    CASE
        WHEN total_sales = 0
            THEN '未販売'
        WHEN total_sales >= 2000
            THEN '主力商品'
        ELSE '通常商品'
    END AS sales_category
FROM product_sales
ORDER BY total_sales DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('--------------------------------------')

cursor = conn.execute("""
WITH product_sales AS (
    SELECT
        products.name AS product_name,
        COALESCE(SUM(sales_records.unit_price * sales_records.quantity), 0) AS total_sales
    FROM products
    LEFT JOIN sales_records
    ON products.product_id = sales_records.product_id
    GROUP BY products.product_id, products.name
)
SELECT 
    product_name,
    total_sales,
    ROUND(
        total_sales * 100.0 /
        (
            SELECT SUM(sales_records.unit_price * sales_records.quantity)
            FROM sales_records
        ),
        2
    ) AS sales_ratio
FROM product_sales
ORDER BY total_sales DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('----------------------------------------')

cursor = conn.execute("""
WITH daily_sales AS (
    SELECT
        sales_date,
        SUM(unit_price * quantity) AS total_sales
    FROM sales_records
    WHERE sales_date BETWEEN ? AND ?
    GROUP BY sales_date
)
SELECT 
    sales_date,
    total_sales,
    ROUND(
        total_sales * 100.0 /
        (
            SELECT SUM(unit_price * quantity)
            FROM sales_records
            WHERE sales_date BETWEEN ? AND ?
        ),
        2
    ) AS sales_ratio
FROM daily_sales
WHERE total_sales >= 2000
ORDER BY total_sales DESC;
""", ('2026-11-14', '2026-11-16', '2026-11-14', '2026-11-16'))
rows = cursor.fetchall()
for row in rows:
    print(row)



conn.close()

