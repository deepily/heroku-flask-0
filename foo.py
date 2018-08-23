import flask
print( flask.__version__ )

import requests
print( requests.__version__ )

doggie_url = "https://dog.ceo/api/breeds/image/random"

# defining a params dict for the parameters to be sent to the API
#PARAMS = { "foo":"bar" }

# sending get request and saving the response as response object
response = requests.get( url=doggie_url )#, params=PARAMS )

# extracting data in json format
data = response.json()
print( data )
print( data[ "message" ] )
