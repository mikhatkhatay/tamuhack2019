import smartcar
from flask import Flask, request, jsonify

# 1. Create an instance of Smartcar client
client = smartcar.AuthClient(
    client_id='85e3a0e5-646d-48da-a145-295eeef00f42',
    client_secret='eb4b756d-8cb5-4dcc-8973-6fc4d2398763',
    redirect_uri='http://localhost:8000/callback',
    scope=[
    	'read_vehicle_info',
    	'read_location',
    	'read_odometer',
    	'control_security'
    ],
    test_mode=True,
)
#2. Create a new webserver with the FLask framework
app = Flask(__name__)

#3. Create a page with  'Connet Car' button
@app.route('/', methods=['GET'])
def index():
	auth_url = client.get_auth_url()
	return '''
		<h1>Hello, TamuHack!!</h1>
		<a href=%s>
			<button>Connect Car</button>
		</a>
	''' % auth_url

#4. HTTP GET to our callback will exchange our OAuth Auth for an access token and
#   log it out; should route to the redirect_uri
#   Is called after developer is given permission, gets the token needed
#   to create the desired app
@app.route('/callback', methods = ['GET'])
def callback():
	code = request.args.get('code')

	access = client.exchange_code(code)

	# log the access token response
	print(access)

	# respond with a success status to browser
	return jsonify(access)

if __name__ == '__main__':
    app.run(port=8000)
