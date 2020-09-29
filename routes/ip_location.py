import json

from flask import request, json, Blueprint, jsonify, current_app
from flask_cors import CORS, cross_origin

ip_location_blueprint = Blueprint("ip_location", __name__,)
CORS(ip_location_blueprint, supports_credentials=True)


@ip_location_blueprint.route("/ip-location", methods=["POST", "OPTIONS"])
@cross_origin()
def ip_location():
    if request.method == "POST":
        data = json.loads(request.get_data())

        if data["secret"] is not None and data["ip"] is not None:
            if data["secret"] == current_app.config["SECRET_KEY"]:
                response = current_app.ip2location.lookup(data["ip"])
                return jsonify({
                    "ip": response.ip,
                    "country_long": response.country_long
                })
            else:
                return ("Invalid incoming JSON"), 400

        else:
            return ("Invalid incoming JSON"), 400

    return ("Unable to process your request"), 405
