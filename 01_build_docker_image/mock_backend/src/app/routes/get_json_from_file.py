from flask import Blueprint
from flask import jsonify
import app.services.file_reader as file_reader

get_json_from_file = Blueprint("get_json_from_file",  __name__)

@get_json_from_file.route("/api/get/<json_file_name>", methods=["GET"])
def get_json_file(json_file_name):
    json_data = file_reader.get_json_from_file(f"./app/static/{json_file_name}.json")
    return jsonify(json_data)