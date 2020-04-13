import sys
import csv
import sqlite3



def import_squirrel_data(path):

    columns = ['X',
               'Y',
               'Unique Squirrel ID',
               'Shift',
               'Date',
                'Age',
                'Primary Fur Color',
                'Location',
                'Specific Location',
                'Running',
                'Chasing',
                'Climbing',
                'Eating',
                'Foraging',
                'Other Activities',
                'Kuks',
                'Quaas',
                'Moans',
                'Tail flags',
                'Tail twitches',
                'Approaches',
                'Indifferent',
                'Runs from']

    column_line = ','.join(columns)

    wildcards = '?,' * (len(columns)-1) + '?'

    con = sqlite3.connect(':memory:')
    cur = con.cursor()

    print(cur.execute(f'CREATE TABLE SquirrelData ({column_line});'))
    cur.execute(f'CREATE TABLE SquirrelData ({column_line});')

    col_expr = ''
    for col in columns:
        col_expr += "i['" + col + "'],"
    col_expr = col_expr[:-1]

    with open(path, 'rt') as fin:
        dr = csv.DictReader(fin)
        to_db = [
            (eval(col_expr)
                #i['X'],
                #i['Y']
                # i['UniqueSquirrelID'],
                # i['Hectare'],
                # i['Shift'],
                # i['Date'],
                # i['HectareSquirrelNumber'],
                # i['Age'],
                # i['PrimaryFurColor'],
                # i['HighlightFurColor'],
                # i['CombinationofPrimaryandHighlightColor'],
                # i['Colornotes'],
                # i['Location'],
                # i['AboveGroundSighterMeasurement'],
                # i['SpecificLocation'],
                # i['Running'],
                # i['Chasing'],
                # i['Climbing'],
                # i['Eating'],
                # i['Foraging'],
                # i['OtherActivities'],
                # i['Kuks'],
                # i['Quaas'],
                # i['Moans'],
                # i['Tailflags'],
                # i['Tailtwitches'],
                # i['Approaches'],
                # i['Indifferent'],
                # i['Runsfrom'],
                # i['OtherInteractions'],
                # i['Lat/Long'],
                # i['ZipCodes'],
                # i['CommunityDistricts'],
                # i['BoroughBoundaries'],
                # i['CityCouncilDistricts'],
                # i['PolicePrecincts']
            ) for i in dr]

    print(f'INSERT INTO SquirrelData ({column_line}) VALUES ({wildcards});')
    cur.executemany(f'INSERT INTO SquirrelData ({column_line}) VALUES ({wildcards});', to_db)


    cur.execute(f'SELECT {column_line} FROM SquirrelData;')

    rows = cur.fetchall()

    for row in rows:
        print(row)

    con.commit()
    con.close()


if __name__ == '__main__':
    if sys.argv[1] == 'import_squirrel_data':
        path = sys.argv[2]
    import_squirrel_data(path)
