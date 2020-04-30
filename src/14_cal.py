import sys
import calendar
from datetime import datetime
now = datetime.now()
# todo test this file


# else print usage statement for format that it expects
# def check_input():
if(len(sys.argv) > 2):
    # check if number, and month is valid
    if(not sys.argv[1].isdigit() or int(sys.argv[1]) > 12 or not sys.argv[2].isdigit()):
        print("Run program in format: 14_cal.py [MM] [YYYY]")
        sys.exit()
if(len(sys.argv) == 2):
    if(not sys.argv[1].isdigit() or int(sys.argv[1]) > 12):
        print("Run program in format: 14_cal.py [MM] [[YYYY]]")
        sys.exit()
# check_input()


# two args (month, year) print month of year
if(len(sys.argv) == 3):
    print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
# single arg(month) print month for current year
elif(len(sys.argv) == 2):
    print(calendar.month(now.year, int(sys.argv[1])))
# no args print current month
elif(len(sys.argv) == 1):
    print(calendar.month(now.year, now.month))
# exit the program

sys.exit()
