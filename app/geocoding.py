from geopy.geocoders import ( Nominatim )
nom = Nominatim()

def address_to_latlong(address):
	result = nom.geocode(address)
	lat = result.latitude
	long = result.longitude
	return [lat, long]

def latlong_to_address(lat,long):
	address = nom.reverse(str(lat) + ',' + str(long))
	return address