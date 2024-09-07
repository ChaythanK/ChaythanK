PHONE_NUMBER = "phone_number_here"
from twilio.phone_numbers import PhoneNumber
from twilio.rest import Client
import geocoder
import opencage
import folium
from voluptuous import Schema, Required, Coerce
with open("test.py") as f:
    exec(f.read())

client = Client("account_sid_here", "auth_token_here")
phone_number = PhoneNumber(PHONE_NUMBER)
carrier = client.lookups.carrier(phone_number).carrier
print(f"Phone number carrier: {carrier.name}")
g = geocoder.ip('me')
location = g.latlng
print(f"Phone number location: {location}")
number = phonenumbers.parse(PHONE_NUMBER)
country_code = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
print(f"Phone number country code: {country_code}")
geocoder = OpenCageGeocode("opencage_api_key_here")
query = str(country_code) + " " + str(carrier.name)
results = geocoder.geocode(query)
print(f"Phone number location (opencage): {results[0]['geometry']['lat'], results[0]['geometry']['lng']}")
map = folium.Map(location=location, zoom_start=9)
folium.Marker(location=results[0]['geometry']['lat'], popup=str(carrier.name), icon=folium.Icon(color='green')).add_to(map)
map.save("phone_number_location.html")
