
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_thiru():
	return 'Hello Thirumalai'

if __name__ == '__main__':

	app.run()
