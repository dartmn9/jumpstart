import requests


def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (90210)? ')

    # get html from web
    get_html_from_web(code)

    # parse the html

    # display for the forecast


def print_the_header():
    print('----------------------------------')
    print('            WEATHER APP')
    print('----------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    # print(url)
    requests


if __name__ == '__main__':
    main()
