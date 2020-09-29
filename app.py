from dotenv import load_dotenv
from flask import Flask

from utils.GenerateTemp import GenerateTemp
from utils.IP2LocationHelper import IP2LocationHelper

from routes.ping import ping_blueprint
from routes.ip_location import ip_location_blueprint

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Register blueprints
app.register_blueprint(ping_blueprint)
app.register_blueprint(ip_location_blueprint)

# Run setup scripts
generate_temp = GenerateTemp(app.config["IP2LOCATION_TOKEN"])

# Register Helper
app.ip2location = IP2LocationHelper()

if __name__ == "__main__":
    app.run()
