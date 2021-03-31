import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe_api.settings")
django.setup()

from api.models import House, DoorUseLog
from accounts.models import User, UserManager

CSV_PATH_HOUSE = './csv/house.csv'
def insert_house():
    with open(CSV_PATH_HOUSE) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        House.objects.all().delete()
        for row in data_reader:
            House.objects.create(
                user_id = row[0],
                number = row[1],
                password = row[2]
            )

CSV_PATH_DOOR_USE_LOG = './csv/door_use_log.csv'
def insert_door_use_log():
    with open(CSV_PATH_DOOR_USE_LOG) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        DoorUseLog.objects.all().delete()
        for row in data_reader:
            DoorUseLog.objects.create(
                created_at   = row[1],
                house_number = House.objects.get(number=row[2]),
            )

ADMIN_TEST    = 'admin'
CSV_PATH_USER = './csv/user.csv'
def insert_user():
    with open(CSV_PATH_USER) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        User.objects.all().delete()
        for row in data_reader:
            if row[2] == ADMIN_TEST:
                User.objects.create_super_user(
                    email    = row[1],
                    password = row[3]
                )
            else:
                User.objects.create_user(
                    email    = row[1],
                    name     = row[2],
                    password = row[3]
                )

insert_house()
insert_door_use_log()
insert_user()