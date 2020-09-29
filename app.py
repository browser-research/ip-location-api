from utils.files import setup
from utils.IP2LocationHelper import IP2LocationHelper

setup()

# create_IP2LocObj()
ip2location = IP2LocationHelper()
print(ip2location.lookup("109.235.70.111"))
print(ip2location.lookup("37.212.62.156"))
