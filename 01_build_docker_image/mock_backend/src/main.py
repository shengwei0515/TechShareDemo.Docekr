from flask import Flask
from flask_cors import CORS
from flask import jsonify

from app.routes.get_json_from_file import get_json_from_file

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def hello():
    return "Hello World!"

app.register_blueprint(get_json_from_file)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)