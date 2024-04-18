from flask import Flask, render_template, request
import json
from Gertrudis.static.Claude import Claude

gertrudis = Claude()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/api/pseudo", methods=['GET', 'POST'])
    def pseudo():
          r = request.json
          print(r)
          r = gertrudis.pseudo(r['data'])
          message = r.content[0].text
          return json.dumps(message)
    
    @app.route("/api/clinCode", methods=['GET', 'POST'])
    def clinCode():
          r = request.json
          print(r)
          r = gertrudis.clinCode(r['data'], r['language'])
          message = r.content[0].text
          return json.dumps(message)
    
    @app.route("/", methods=['GET', 'POST'])
    def home():
            return render_template("index.html")

    return app