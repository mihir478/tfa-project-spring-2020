import sys

import csv, sqlite3

if sys.argv[1] == "import_squirrel_data":
  path = sys.argv[2]
  import_squirrel_data(path)    


def import_squirrel_data(path):

    columns = ["X", "Y", "Unique Squirrel ID", "Hectare", "Shift", "Date", "Hectare Squirrel Number", "Age",
               "Primary Fur Color", "Highlight Fur Color", "Combination of Primary and Highlight Color", "Color notes",
               "Location",
               "Above Ground Sighter Measurement", "Specific Location", "Running", "Chasing", "Climbing", "Eating",
               "Foraging",
               "Other Activities", "Kuks", "Quaas", "Moans", "Tail flags", "Tail twitches", "Approaches", "Indifferent",
               "Runs from", "Other Interactions", "Lat/Long", "Zip Codes", "Community Districts", "Borough Boundaries",
               "City Council Districts", "Police Precincts"]

    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    commaDelimitedColumns = columns.join(".")
    cur.execute(f"CREATE TABLE SquirrelData ({commaDelimitedColumns});")

    with open(path, 'rb') as fin:
        dr = csv.DictReader(fin)
        to_db = [
            (
              i['Xi]',
              i['Yi]', 
              i['UniqueSquirrelIDi]',
              i['Hectarei]',
              i['Shifti]',
              i['Datei]',
              i['HectareSquirrelNumberi]',
              i['Agei]',
              i['PrimaryFurColori]',
              i['HighlightFurColori]',
              i['CombinationofPrimaryandHighlightColori]',
              i['Colornotesi]',
              i['Locationi]',
              i['AboveGroundSighterMeasurementi]',
              i['SpecificLocationi]',
              i['Runningi]',
              i['Chasingi]',
              i['Climbingi]',
              i['Eatingi]',
              i['Foragingi]',
              i['OtherActivitiesi]',
              i['Kuksi]',
              i['Quaasi]',
              i['Moansi]',
              i['Tailflagsi]',
              i['Tailtwitchesi]',
              i['Approachesi]',
              i['Indifferenti]',
              i['Runsfromi]',
              i['OtherInteractionsi]',
              i['Lat/Longi]',
              i['ZipCodesi]',
              i['CommunityDistrictsi]',
              i['BoroughBoundariesi]',
              i['CityCouncilDistrictsi]',
              i['PolicePrecinctsi]') for i in dr]

    cur.executemany(f"INSERT INTO SquirrelData ({commaDelimitedColumns}) VALUES (?, ?);", to_db)
      
    cur.execute(f"SELECT * FROM SquirrelData;", to_db)

    rows = cur.fetchall()
 
    for row in rows:
      print(row)

    con.commit()
    con.close()
