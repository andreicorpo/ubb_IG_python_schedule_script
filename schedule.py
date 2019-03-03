import pandas as pd
import urllib
import sys


def get_schedules(url_link):

    schedules = []

    for i in range(len(pd.read_html(url_link, flavor="lxml"))):
        try:
            df = pd.read_html(url_link, flavor="lxml")[i]
            new_header = df.iloc[0]
            df = df[1:]
            df.columns = new_header
            schedules.append(df.to_dict('records'))
        except urllib.error.URLError:
            print('\nGiven values are not correct. Rerun the script.\n')
            sys.exit(2)

    return schedules


def get_rooms(room):
    df = pd.read_html(
        'http://www.cs.ubbcluj.ro/files/orar/2018-2/sali/legenda.html', flavor="lxml")[0]
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    rooms = df.to_dict('records')
    for r in rooms:
        if r['Sala'] == room:
            return f'{r["Sala"]} - {(r["Localizarea"])}'
