import requests
import calendar

s = requests.Session()


def get_temps():
    # Using manual array since we need leading 0 in months for url
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    # Ask for start and end year, if same year is entered it will get 1 year of temps
    start_year = int(input("Enter Start year > "))
    end_year = int(input("Enter End year > "))

    # Make the range inclusive
    end_year += 1

    # Iterate over years and months
    for year in range(start_year, end_year):
        for month in months:

            # Get the last day of the month for url using calendar
            last_day = calendar.monthrange(year, int(month))[1]

            # Date link inside url example: 2019010120190131 (start and end date)
            date_link = '{0}{1}01{0}{1}{2}'.format(year, month, last_day)
            final_url = 'https://api-ak.wunderground.com/api/75e91f5c866f39a2/history_' \
                        + date_link + \
                        '/lang:EN/units:english/bestfct:1/v:2.0/q/KHOU.json?showObs=0&ttl=120'
            get_data(final_url)


def get_data(url):
    r = s.get(url)          # Open final url created
    r.raise_for_status()    # Check for errors
    resp = r.json()         # Get JSON response

    try:
        # Get Average Maximum Temperature for the month
        print(resp['history']['summary']['max_temperature_avg'])
    except KeyError:        # If data is unavailable print NA
        print("N/A")


get_temps()
