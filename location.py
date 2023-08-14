import requests
import json
import re
from pyfiglet import Figlet
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

def print_header(text):
    f = Figlet(font='slant')
    header = f.renderText(text)
    print(header)

def get_ip():
    return requests.get('https://api64.ipify.org?format=json').json()["ip"]

def is_valid_ip(ip_str):
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$|(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})$'
    return re.match(ip_pattern, ip_str)

def get_location(ip_address, detailed=True):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    
    if detailed:
        location_data = {
            "ip": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country"),
            "country_name": response.get("country_name"),
            "country_capital": response.get("country_capital"),
            "country_tld": response.get("country_tld"),
            "continent_code": response.get("continent_code"),
            "postal": response.get("postal"),
            "latitude": response.get("latitude"),
            "longitude": response.get("longitude"),
            "timezone": response.get("timezone"),
            "country_calling_code": response.get("country_calling_code"),
            "currency": response.get("currency"),
            "currency_name": response.get("currency_name"),
            "languages": response.get("languages"),
            "country_population": response.get("country_population")
        }
    else:
        location_data = {
            "ip": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name")
        }
    
    return location_data

def print_colored_json(json_data):
    json_str = json.dumps(json_data, indent=4)
    colored_json = highlight(json_str, JsonLexer(), TerminalFormatter())
    print(colored_json)

def main():
    print_header("Geo Location With Python3 By EWRC01")

    print("1. Test on My IP")
    print("2. Test on My IP with detailed information")
    print("3. I want to enter an IP")
    print("4. I want to enter an IP and detailed information")

    option = input("Choose an option: ")

    if option == "1":
        ip_address = get_ip()
        location = get_location(ip_address, detailed=False)  # Choose detailed=False for option 1
        print_colored_json(location)
    elif option == "2":
        ip_address = get_ip()
        location = get_location(ip_address, detailed=True)  # Choose detailed=True for option 2
        print_colored_json(location)
    elif option == "3" or option == "4":
        while True:
            ip_address = input("Enter IP Address: ")
            if is_valid_ip(ip_address):
                detailed_option = option == "4"
                location = get_location(ip_address, detailed=detailed_option)
                print_colored_json(location)
                break
            else:
                print("Invalid IP address format. Please try again.")

if __name__ == "__main__":
    main()
