import sys
import csv
import sqlite3

def import_squirrel_data(path):

    columns = ['X', 'Y', 'Unique Squirrel ID', 'Hectare', 'Shift', 'Date', 'Hectare Squirrel Number', 'Age',
               'Primary Fur Color', 'Highlight Fur Color', 'Combination of Primary and Highlight Color', 'Color notes',
               'Location',
               'Above Ground Sighter Measurement', 'Specific Location', 'Running', 'Chasing', 'Climbing', 'Eating',
               'Foraging',
               'Other Activities', 'Kuks', 'Quaas', 'Moans', 'Tail flags', 'Tail twitches', 'Approaches', 'Indifferent',
               'Runs from', 'Other Interactions', 'Lat/Long', 'Zip Codes', 'Community Districts', 'Borough Boundaries',
               'City Council Districts', 'Police Precincts']

    con = sqlite3.connect(':memory:')
    cur = con.cursor()
    cur.execute(f'CREATE TABLE SquirrelData (X, Y);')

    with open(path, 'rt') as fin:
        dr = csv.DictReader(fin)
        to_db = [
            (
                i['X'],
                i['Y']
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

    cur.executemany(f'INSERT INTO SquirrelData (X, Y) VALUES (?, ?);', to_db)

    cur.execute(f'SELECT X, Y FROM SquirrelData;')

    rows = cur.fetchall()

    for row in rows:
        print(row)

    con.commit()
    con.close()


if __name__ == '__main__':
    if sys.argv[1] == 'import_squirrel_data':
        path = sys.argv[2]
    import_squirrel_data(path)
