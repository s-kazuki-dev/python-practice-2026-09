
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

conn.execute("INSERT INTO sales_records VALUES (1, 1, 4, 400, '2026-11-10');")
conn.execute("INSERT INTO sales_records VALUES (2, 1, 3, 400, '2026-11-11');")
conn.execute("INSERT INTO sales_records VALUES (3, 2, 5, 350, '2026-11-12');")
conn.execute("INSERT INTO sales_records VALUES (4, 3, 2, 500, '2026-11-13');")
conn.execute("INSERT INTO sales_records VALUES (5, 1, 2, 500, '2026-11-14');")

conn.commit()

cursor = conn.execute("""
SELECT 
    sales_records.sales_date,
    products.name,
    sales_records.quantity,
    sales_records.unit_price,
    sales_records.unit_price * sales_records.quantity
FROM products
INNER JOIN sales_records
ON products.product_id = sales_records.product_id
WHERE sales_records.sales_date BETWEEN ? AND ?
ORDER BY sales_records.sales_date ASC, sales_records.sale_id ASC;
""", ("2026-11-11", "2026-11-13"))
rows = cursor.fetchall()
for row in rows:
    print(row)

print('------------------------')

conn.execute("INSERT INTO sales_records VALUES (6, 2, 2, 350, '2026-11-12')")

conn.commit()

cursor = conn.execute("""
SELECT 
    sales_date,
    COUNT(*) AS sale_count,
    COALESCE(SUM(quantity), 0) AS total_quantity,
    SUM(unit_price * quantity) AS total_sales
FROM sales_records
GROUP BY sales_date
ORDER BY sales_date ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('--------------------------')

conn.execute("INSERT INTO sales_records VALUES (7, 1, 2, 400, '2026-10-30')")
conn.execute("INSERT INTO sales_records VALUES (8, 3, 3, 500, '2026-12-02')")

conn.commit()

cursor = conn.execute("""
SELECT
    strftime('%Y-%m', sales_date) AS sales_month,
    COUNT(*) AS sale_count,
    SUM(quantity) AS total_quantity,
    SUM(unit_price * quantity) AS total_sales
FROM sales_records
GROUP BY strftime('%Y-%m', sales_date)
ORDER BY sales_month ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('-----総合演習-----')

cursor = conn.execute("""
SELECT 
    products.name AS product_name,
    COUNT(*) AS sale_count,
    SUM(sales_records.quantity) AS total_quantity,
    SUM(sales_records.unit_price * sales_records.quantity) AS total_sales,
    CASE 
        WHEN SUM(sales_records.unit_price * sales_records.quantity) >= 2000
            THEN '主力商品'
        ELSE '通常商品'
    END AS sales_category
FROM products
INNER JOIN sales_records
ON products.product_id = sales_records.product_id
WHERE sales_date BETWEEN ? AND ?
GROUP BY products.name, products.product_id
ORDER BY total_sales DESC;
""", ('2026-11-11', '2026-11-14'))
rows = cursor.fetchall()
for row in rows:
    print(row)

print('---------------------')

cursor = conn.execute("""
SELECT
    sales_date,
    SUM(unit_price * quantity) AS total_sales
FROM sales_records
GROUP BY sales_date
HAVING SUM(unit_price * quantity) >= 2000
ORDER BY total_sales DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)
    

conn.close()
