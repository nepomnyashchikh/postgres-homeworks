"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="25802580"
)

try:
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/employees_data.csv', 'r', encoding='UTF-8') as file:
                data = csv.DictReader(file)
                for row in data:
                    cursor.execute(
                        'INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)',
                        (row['employee_id'], row['first_name'], row['last_name'],
                         row['title'], row['birth_date'], row['notes'])
                    )

            with open('north_data/customers_data.csv', 'r', encoding='UTF-8') as file:
                data = csv.DictReader(file)
                for row in data:
                    cursor.execute(
                        'INSERT INTO customers VALUES(%s, %s, %s)',
                        (row['customer_id'], row['company_name'], row['contact_name'])
                    )

            with open('north_data/orders_data.csv', 'r', encoding='UTF-8') as file:
                data = csv.DictReader(file)
                for row in data:
                    cursor.execute(
                        'INSERT INTO orders VALUES(%s, %s, %s, %s, %s)',
                        (row['order_id'], row['customer_id'], row['employee_id'],
                         row['order_date'], row['ship_city'])
                    )
finally:
    conn.close()