#!/usr/bin/env python


import csv
import sys

from datetime import date, time

from games.models import Game

def import_games(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            g = Game()
            g.location = row["location"]
            g.name = row["name"]
            hour = row["time"].split(":")[0]
            minute = row["time"].split(":")[1]
            year = row["date"].split("-")[0]
            month = row["date"].split("-")[1]
            day = row["date"].split("-")[2]        
            g.date = date(int(year), int(month), int(day))
            g.time = time(int(hour), int(minute))
            g.save()


def main():
    for file_name in sys.argv[1:]:
        import_games(file_name)


if __name__ == "__main__":
    main() 
