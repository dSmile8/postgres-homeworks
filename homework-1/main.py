"""Скрипт для заполнения данными таблиц в БД Postgres."""
if __name__ == '__main__':

    import psycopg2
    import csv
    from pathlib import Path

    DATA_COSTUMERS = Path(__file__).parent.joinpath('north_data', 'customers_data.csv')
    DATA_EMPLOYEES = Path(__file__).parent.joinpath('north_data', 'employees_data.csv')
    DATA_ORDERS = Path(__file__).parent.joinpath('north_data', 'orders_data.csv')

    connect = psycopg2.connect(host='localhost', database='north', user='postgres', password='asg6515ZX')
    try:
        with connect:
            with open(DATA_COSTUMERS, 'r', encoding='UTF-8') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                with connect.cursor() as cursor:
                    for r in reader:
                        cursor.execute(f'INSERT INTO "customers" VALUES (%s, %s, %s)', (r[0], r[1], r[2]))

            with open(DATA_EMPLOYEES, 'r', encoding='UTF-8') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                with connect.cursor() as cursor:
                    for r in reader:
                        cursor.execute(f'INSERT INTO "employees" VALUES (%s, %s, %s, %s, %s, %s)', (r[0], r[1], r[2], r[3],
                                                                                                    r[4], r[5]))

            with open(DATA_ORDERS, 'r', encoding='UTF-8') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                with connect.cursor() as cursor:
                    for r in reader:
                        cursor.execute(f'INSERT INTO "orders" VALUES (%s, %s, %s, %s, %s)', (r[0], r[1], r[2], r[3], r[4]))
    finally:
        connect.close()

    # def load_from_csv_to_table(csv_f):
    #     connect_ = psycopg2.connect(host='localhost', database='north', user='postgres', password='asg6515ZX')
    #     try:
    #         with connect:
    #             with connect.cursor() as cursor_:
    #                 cursor.copy_from(csv_f, "customers")
    #                 cursor.copy_from(csv_f, "employers")
    #                 cursor.copy_from(csv_f, "orders")
    #     finally:
    #         connect_.close()
    #
    # load_from_csv_to_table(DATA_COSTUMERS)
    # load_from_csv_to_table(DATA_EMPLOYEES)
    # load_from_csv_to_table(DATA_ORDERS)
