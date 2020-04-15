import sys
import csv
import sqlite3


def import_squirrel_data(column_line, cur, path):

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
    export_squirrel_data(column_line, cur, 'rows.csv')  # TODO remove


def export_squirrel_data(column_line, cur, path):
    cur.execute(f'SELECT {column_line} FROM SquirrelData;')
    rows = cur.fetchall()
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_line.replace('"', '').split(','))
        writer.writerows(rows)

if __name__ == '__main__':

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

    if sys.argv[1] == 'import_squirrel_data':
        path = sys.argv[2]
        import_squirrel_data(column_line, cur, path)
    if sys.argv[1] == 'export_squirrel_data':
        path = sys.argv[2]
        export_squirrel_data(column_line, cur, path)

    con.commit()
    con.close()
