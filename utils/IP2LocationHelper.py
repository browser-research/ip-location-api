from IP2Location import IP2Location
from glob import glob


class IP2LocationHelper():

    def __init__(self):
        # TODO: Get from .env
        self._temp_dir = "./temp/"

        self._bin_db_path = glob(self._temp_dir + '*.BIN')[0]
        self._IP2LocObj = IP2Location()
        self._IP2LocObj.open(self._bin_db_path)

    def lookup(self, ip="127.0.0.1"):
        try:
            return self._IP2LocObj.get_all(ip)
        except:
            print("Unable to get information about IP address")
            return False
