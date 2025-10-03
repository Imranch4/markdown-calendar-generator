import calendar
from datetime import datetime
import sys
import argparse

def create_calendar(year, month, with_isoweek=False, start_from_Sun=False, lang="en"):
    firstweekday = 6 if start_from_Sun else 0

    cal = calendar.Calendar(firstweekday=firstweekday)

    mdstr = ""
    dic = get_dict(lang)

    colnames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if start_from_Sun:
        colnames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    if with_isoweek:
        colnames.insert(0, "Week")
    colnames = [dic[col] for col in colnames]

    mdstr += '|' + '|'.join(colnames) + '|' + '\n'
    mdstr += '|' + '|'.join([':-:' for _ in range(len(colnames))]) + '|' + '\n'

    headings = []

    for week in cal.monthdayscalendar(year, month):
        row = '|'
        for day in week:
            if with_isoweek and day != 0:
                isoweek = datetime(year, month, day).isocalendar()[1]
                row += '[{}]({}#{:04d}-{:02d}-{:02d})|'.format(
                    day, '#' + str(isoweek), year, month, day)
                headings.append('## Week {} - {:04d}-{:02d}-{:02d}'.format(
                    isoweek, year, month, day))
            elif day != 0:
                row += '[{}](#{:02d}-{:02d}-{:02d})|'.format(
                    day, day, month, year)
                headings.append('## {:02d}-{:02d}-{:02d}'.format(
                    day, month, year))
            else:
                row += '|'
        mdstr += row + '\n'

    return mdstr + '\n'.join(headings)


def print_calendar(year, month, with_isoweek=False, start_from_Sun=False, lang="en"):
    dic = get_dict(lang)
    month_name = dic['month_names'][month - 1]
    print('# {} {}\n'.format(month_name, year + 2000 if year <= 2000 else year))
    print(create_calendar(year, month, with_isoweek, start_from_Sun, lang))
    print("***")


def get_dict(lang='en'):
    dic = {}
    colnames = ['Week', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    colnames_fr = ['Semaine', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']
    colnames_ar = ['أسبوع', 'إثنين', 'ثلاثاء', 'أربعاء', 'خميس', 'جمعة', 'سبت', 'أحد']
    colnames_es = ['Semana', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']

    month_names_en = ["January", "February", "March", "April", "May", "June", "July",
                      "August", "September", "October", "November", "December"]
    month_names_fr = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
                      "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    month_names_ar = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو",
                      "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
    month_names_es = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                      "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    if lang == 'en':
        for col in colnames:
            dic[col] = col
        dic['month_names'] = month_names_en
    elif lang == 'fr':
        for col, colfr in zip(colnames, colnames_fr):
            dic[col] = colfr
        dic['month_names'] = month_names_fr
    elif lang == 'ar':
        for col, colar in zip(colnames, colnames_ar):
            dic[col] = colar
        dic['month_names'] = month_names_ar
    elif lang == 'es':
        for col, coles in zip(colnames, colnames_es):
            dic[col] = coles
        dic['month_names'] = month_names_es
    else:
        for col in colnames:
            dic[col] = col
        dic['month_names'] = month_names_en


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a Markdown calendar.')
    parser.add_argument('year', nargs='?', type=int, help='Year for the calendar.')
    parser.add_argument('month', nargs='?', type=int, help='Month for the calendar (1-12).')
    parser.add_argument('--with-isoweek', action='store_true',
                        help='Include ISO week numbers.')
    parser.add_argument('--start-from-sun', action='store_true',
                        help='Start week from Sunday instead of Monday.')
    parser.add_argument('--lang', type=str, default='en', choices=['en', 'fr', 'ar', 'es'],
                        help='Language for the calendar (en, fr, ar, es).')

    args = parser.parse_args()

    if args.year is None:
        today = datetime.now()
        print_calendar(today.year, today.month, args.with_isoweek, args.start_from_sun, args.lang)
    elif args.month is None:
        for month in range(1, 13):
            print_calendar(args.year, month, args.with_isoweek, args.start_from_sun, args.lang)
    else:
        if not (1 <= args.month <= 12):
            print("Error: Month must be between 1 and 12.")
            sys.exit(1)
        print_calendar(args.year, args.month, args.with_isoweek, args.start_from_sun, args.lang)