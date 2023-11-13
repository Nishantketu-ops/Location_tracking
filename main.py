import phonenumbers
import opencage
import folium

from phonenumbers import geocoder
number = input("Enter the Phone no. U wanna check alogwith country code (eg:+9179xxxxxxx) : \n")

if len(number)<13:
    print("Please enter a valid no along with country code")

elif len(number)>14:
    print("The value entered  is too long to be a phone number.")

else:
    print("Your entered no to check is :"+number)


pepnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepnumber,"en")

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
carrier_name = carrier.name_for_number(service_pro,"en")
print(f"Carrier name for the No. provided is : {carrier_name} , Location is :{location}")

from opencage.geocoder import OpenCageGeocode

key = input("Please enter Your opencage api key to get precise location : \n")

geocoder = OpenCageGeocode(key)
# print(location)
query = str(location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']


print(f"Latitude : {lat} , Longitude : {lng}")

myMap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("Location.html")
print("Please check Location.html file to view In Map.")
