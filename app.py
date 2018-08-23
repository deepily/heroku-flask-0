from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time} GMT.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':

    # From: https://stackoverflow.com/questions/4906977/how-do-i-access-environment-variables-from-python
    env_port = int( os.getenv( key='PORT', default=8888 ) )
    print( env_port )
    app.run( host='0.0.0.0', port=env_port )


