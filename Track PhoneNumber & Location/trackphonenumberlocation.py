import phonenumbers
import sys
from testnumbers import number

# this is to fetch country name based on country code
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number,"en"))

 #this is to fetch phone number service provider(like airtel,aircel,geo)
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

import phonenumbers
x = phonenumbers.parse("+442083661177", None)
print(x)