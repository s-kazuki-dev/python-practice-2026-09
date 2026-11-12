
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
    product_id INTEGER, 
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);
""")

conn.execute("INSERT INTO products VALUES (1, 'コーヒー', 400);")
conn.execute("INSERT INTO products VALUES (2, '紅茶', 350);")
conn.execute("INSERT INTO products VALUES (3, 'ケーキ', 500);")
conn.execute("INSERT INTO products VALUES (4, '水', 200);")

conn.execute("INSERT INTO sales_records VALUES (1, 1, 4);")
conn.execute("INSERT INTO sales_records VALUES (2, 1, 8);")
conn.execute("INSERT INTO sales_records VALUES (3, 2, 5);")
conn.execute("INSERT INTO sales_records VALUES (4, 3, 3);")

conn.commit()

try:
    conn.execute("""
    INSERT INTO sales_records
    VALUES (?, ?, ?);
    """, (5, 999, 3))
    conn.commit()
    print('販売記録の登録に成功しました')
except sqlite3.IntegrityError as error:
    print('データの登録に失敗しました')
    print(error)
    conn.rollback()

try:
    conn.execute("""
    INSERT INTO products
    VALUES (?, ?, ?);
    """, (5, None, 300))
    conn.commit()
    print('商品の登録に成功しました')
except sqlite3.IntegrityError as error:
    print('商品の登録に失敗しました')
    print(error)
    conn.rollback()

try:
    conn.execute("""
    INSERT INTO products
    VALUES (?, ?, ?);
    """, (6, 'コーヒー', 450))
    conn.commit()
    print('商品の登録に成功しました')
except sqlite3.IntegrityError as error:
    print('商品の登録に失敗しました')
    print(error)
    conn.rollback()

print('最終総合演習')

try:
    conn.execute("""
    INSERT INTO products
    VALUES (?, ?, ?);
    """, (5, 'サンドイッチ', 650))
    conn.execute("""
    INSERT INTO sales_records
    VALUES (?, ?, ?);
    """, (5, 5, 2))
    conn.commit()
except sqlite3.IntegrityError as error:
    print(error)
    conn.rollback()

try:
    conn.execute("""
    UPDATE products
    SET price = ?
    WHERE product_id = ?;
    """, (999, 1))
    conn.execute("""
    INSERT INTO sales_records
    VALUES (?, ?, ?);
    """, (6, 999, 2))
    conn.commit()
except sqlite3.IntegrityError as error:
    print(error)
    conn.rollback()
    
cursor = conn.execute("""
SELECT *
FROM products
ORDER BY product_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = conn.execute("""
SELECT *
FROM sales_records
ORDER BY sale_id ASC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)




conn.close()
