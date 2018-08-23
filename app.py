from flask import Flask
from datetime import datetime
import os
import requests

app = Flask(__name__)

@app.route( "/" )
def home():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
        <h1>Like Cats 'n' Dogs!</h1>
        <p>It is currently {time} GMT.</p>
        <p>¿Quieres <a href="/doggies">perros</a> o <a href="/kitties">gatos</a>?</p>
        """.format( time=the_time )

@app.route( '/kitties' )
def kitties():

    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Gatos?</h1>
    <p>It is currently {time} GMT.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format( time=the_time )

@app.route( '/doggies' )
def get_doggies():

    # From: https://dog.ceo/dog-api/
    doggie_url = "https://dog.ceo/api/breeds/image/random"

    # sending get request and saving the response as response object
    response = requests.get( url=doggie_url )

    # extracting data in json format
    data = response.json()
    print( data )
    print( data[ "message" ] )

    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
        <h1>Doggies!</h1>
        <p>It is currently {time} GMT...</p>

        <img src="{doggie_url}" />
        """.format( time=the_time, doggie_url=data[ "message" ] )

if __name__ == '__main__':

    # From: https://stackoverflow.com/questions/4906977/how-do-i-access-environment-variables-from-python
    env_port = int( os.getenv( key='PORT', default=8888 ) )
    print( env_port )
    app.run( host='0.0.0.0', port=env_port )


