import bcrypt
import csv
import datetime, time

from random import randint

HOUSE_QUANTITY     = 100
HOUSEHOLD_QUANTITY = 25

HOUSE_TEST                = "0501"
HOUSE_PASSWORD_TEST       = "1234"
HOUSE_ADMIN_TEST          = "0000"
HOUSE_ADMIN_PASSWORD_TEST = "5678"
DOOR_USE_LOG_TEST         = 300

ADMIN_TEST    = 'admin'
USER_PASSWORD = 'password123'

household_list = []

# house.csv
csv_filename = "csv/house.csv"
csv_open = open(csv_filename, "w+", encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(["id", "number", "password"])

for i in range(HOUSE_QUANTITY):
    password        = f'{randint(1, 9999):>04d}'
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    household = f"{i//HOUSEHOLD_QUANTITY+1:>02d}{i%HOUSEHOLD_QUANTITY+1:>02d}"
    household_list.append(household)
    csv_writer.writerow([i+1, household, hashed_password])

# # test public
# password = HOUSE_PASSWORD_TEST
# hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
# csv_writer.writerow([101, HOUSE_TEST, hashed_password])
# household_list.append(HOUSE_TEST)

# # test admin
# password = HOUSE_ADMIN_PASSWORD_TEST
# hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
# csv_writer.writerow([102, HOUSE_ADMIN_TEST, hashed_password])

#door_use_log.csv
csv_filename = "csv/door_use_log.csv"
csv_open = open(csv_filename, "w+", encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(["id", "created_at", "house_number"])

for i in range(DOOR_USE_LOG_TEST):
    csv_writer.writerow([i+1, datetime.datetime.now(), household_list[randint(0, HOUSE_QUANTITY-1)]])

#user.csv
csv_filename = "csv/user.csv"
csv_open = open(csv_filename, "w+", encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(["id", "email", "name", "password"])

for i in range(HOUSE_QUANTITY):
    password        = USER_PASSWORD
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    csv_writer.writerow([i+1, f'user{i+1}@gmail.com', f'user{i+1}', hashed_password])

password        = USER_PASSWORD
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

csv_writer.writerow([HOUSE_QUANTITY+1, f'{ADMIN_TEST}@gmail.com', ADMIN_TEST, hashed_password])