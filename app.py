import json

# We import Flask
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

    
# We create a Flask app
app = Flask(__name__)



# We establish a Flask route so that we can serve HTTP traffic on that route 
@app.route('/<name>')
def main(name=None):
  gotyourname = name
  return render_template('index.html', name=gotyourname)
@app.route('/api/weather/<date>')
def weather(date):
        # Additionally, we're now loading the JSON file's data into file_data 
    # every time a request is made to this endpoint# We hardcode some information to be returned
    with open('./seattle-data.json', 'r') as jsonfile:
      file_data = json.loads(jsonfile.read())
          # We can then find the data for the requested date and send it back as json
    return json.dumps(file_data[date])

# Get setup so that if we call the app directly (and it isn't being imported elsewhere)
# it will then run the app with the debug mode as True
# More info - https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    app.run(debug=True)