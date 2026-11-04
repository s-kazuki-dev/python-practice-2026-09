
import sqlite3

conn = sqlite3.connect("sales.db")

cursor = conn.execute("""
SELECT name, SUM(price * quantity)
FROM sales
GROUP BY name
HAVING SUM(price * quantity) >= 3000;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = conn.execute("""
SELECT name, SUM(quantity), SUM(price * quantity)
FROM sales
WHERE price >= 400
GROUP BY name
HAVING SUM(quantity) >= 6;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()


#ここから複数レコードの練習
practice_conn = sqlite3.connect(":memory:")

practice_conn.execute("""
CREATE TABLE practice_sales (
    name TEXT,
    price INTEGER,
    quantity INTEGER
    );
""")

practice_conn.execute("INSERT INTO practice_sales VALUES ('コーヒー', 400, 4);")
practice_conn.execute("INSERT INTO practice_sales VALUES ('コーヒー', 400, 8);")
practice_conn.execute("INSERT INTO practice_sales VALUES ('紅茶', 350, 5);")
practice_conn.execute("INSERT INTO practice_sales VALUES ('紅茶', 350, 5);")
practice_conn.execute("INSERT INTO practice_sales VALUES ('ケーキ', 500, 3);")
practice_conn.execute("INSERT INTO practice_sales VALUES ('ケーキ', 500, 3);")

practice_conn.commit()

cursor = practice_conn.execute("""
SELECT name, SUM(quantity)
FROM practice_sales
WHERE quantity >= 5
GROUP BY name
HAVING SUM(quantity) >= 9;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor = practice_conn.execute("""
SELECT name, SUM(quantity), SUM(price * quantity)
FROM practice_sales
WHERE quantity >= 4
GROUP BY name
HAVING SUM(price * quantity) >= 3500
ORDER BY SUM(price * quantity) DESC;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)


practice_conn.close()


