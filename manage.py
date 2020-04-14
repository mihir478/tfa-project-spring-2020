import sys
import csv
import sqlite3


def import_squirrel_data(path):
    columns = ['X',
               'Y',
               '"Unique Squirrel ID"',
               'Shift',
               'Date',
               'Age',
               '"Primary Fur Color"',
               'Location',
               '"Specific Location"',
               'Running',
               'Chasing',
               'Climbing',
               'Eating',
               'Foraging',
               '"Other Activities"',
               'Kuks',
               'Quaas',
               'Moans',
               '"Tail flags"',
               '"Tail twitches"',
               'Approaches',
               'Indifferent',
               '"Runs from"']

    column_line = ','.join(columns)

    # remove last by using len - 1,
    wildcards = '?,' * (len(columns) - 1) + '?'

    con = sqlite3.connect(':memory:')
    cur = con.cursor()

    cur.execute(f'CREATE TABLE SquirrelData ({column_line});')

    col_expr = ''
    for col in columns:
        space = col.find(' ') >= 0
        # quote multi token column names
        col_expr += 'i[' + col + '],' if space else 'i["' + col + '"],'
    # remove last ,
    col_expr = col_expr[:-1]

    with open(path, 'rt') as fin:
        dr = csv.DictReader(fin)
        to_db = [(eval(col_expr)) for i in dr]

    cur.executemany(f'INSERT INTO SquirrelData ({column_line}) VALUES ({wildcards});', to_db)
    # print_table(column_line, cur)

    con.commit()
    con.close()


def print_table(column_line, cur):
    cur.execute(f'SELECT {column_line} FROM SquirrelData;')
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    if sys.argv[1] == 'import_squirrel_data':
        path = sys.argv[2]
    import_squirrel_data(path)
