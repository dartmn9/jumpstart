import datetime

def print_header():
    print('-------------------------')
    print('     BIRTHDAY APP')
    print('-------------------------')
    print()

def get_birthday_from_user():
    print('When is your birthday?')
    year = int(input('Enter year [YYYY]: '))
    month = int(input('Enter month [MM]: '))
    day = int(input('Enter day [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates():
    pass


def print_birthday_information():
    pass

def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    now = None
    # number_of_days = compute_days_between_dates(bday, now)
    # print_birthday_information()


main()