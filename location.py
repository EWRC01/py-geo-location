import requests
import json
from pyfiglet import Figlet
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter


f = Figlet(font='slant')
text = f.renderText("Geo Location With Python3 By EWRC01")

print(text)

print("1. Test on My IP")
print("2. Test on My IP with detailed information")
print("3. I want to enter a IP")
print("4. I want to enter a IP and detailed information")

option = input("Choose an option: ")

match option:
    case  "1":
            def get_ip():
                response = requests.get('https://api64.ipify.org?format=json').json()
                return response["ip"]

            def get_location():
                ip_address = get_ip()
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
                location_data = {
                    "ip": ip_address,
                    "city": response.get("city"),
                    "region": response.get("region"),
                    "country": response.get("country_name")
                }
                return location_data

            location = get_location()

            json_str = json.dumps(location, indent = 4)
            colored_json = highlight(json_str, JsonLexer(), TerminalFormatter())

            print(colored_json)

    case "2":
            def get_ip():
                response = requests.get('https://api64.ipify.org?format=json').json()
                return response["ip"]

            def get_location():
                ip_address = get_ip()
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
                location_data = {
                    "ip": ip_address,
                    "city": response.get("city"),
                    "region": response.get("region"),
                    "country": response.get("country"),
                    "country_name" : response.get("country_name"),
                    "country_capital" : response.get("country_capital"),
                    "country_tld" : response.get("country_tld"),
                    "continent_code" : response.get("continent_code"),
                    "postal" : response.get("postal"),
                    "latitude" : response.get("latitude"),
                    "longitude" : response.get("longitude"),
                    "timezone" : response.get("timezone"),
                    "country_calling_code" : response.get("country_calling_code"),
                    "currency" : response.get("currency"),
                    "currency_name" : response.get("currency_name"),
                    "languages": response.get("languages"),
                    "country_population" : response.get("country_population")
                }
                return location_data

            location = get_location()

            json_str = json.dumps(location, indent = 4)
            colored_json = highlight(json_str, JsonLexer(), TerminalFormatter())

            print(colored_json)

    case  "3":
            def get_ip():
               ip_address = input("Enter IP Address: ")
               return ip_address


            def get_location():
                ip_address = get_ip()
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
                location_data = {
                    "ip": ip_address,
                    "city": response.get("city"),
                    "region": response.get("region"),
                    "country": response.get("country_name")
                }
                return location_data

            location = get_location()

            json_str = json.dumps(location, indent = 4)
            colored_json = highlight(json_str, JsonLexer(), TerminalFormatter())

            print(colored_json)
                
    
    case "4":
         
         print("You select option 4")
         


