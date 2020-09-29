import os
import glob
import zipfile

from datetime import date
from pathlib import Path
from urllib.request import urlretrieve


class GenerateTemp():
    def __init__(self, token):
        self._token = token
        self._db_file_name = date.today().strftime(
            "%b-%d-%Y_%H-%M-%S") + "_IP2LocationDatabase.zip"
        self._db_file_path = "./temp/{}".format(self._db_file_name)

        self.setup()

    def create_temp(self):
        Path("./temp/").mkdir(parents=True, exist_ok=True)
        return True

    def wipe_temp(self):
        files = glob.glob("./temp/*")
        for f in files:
            os.remove(f)
        return True

    def download_zip(self, db_code="DB3LITEBIN"):
        url = "https://www.ip2location.com/download/?token={}&file={}".format(
            self._token, db_code)
        urlretrieve(url, self._db_file_path)
        return True

    def unzip_bin(self):
        with zipfile.ZipFile(self._db_file_path, 'r') as zip_ref:
            zip_ref.extractall("./temp/")
        return True

    def setup(self):
        print("> Running setup")
        print("> Creating temp directory (if does not exist)")
        self.create_temp()
        print("> Success!")
        print("> Wiping content inside temp (if is any)")
        self.wipe_temp()
        print("> Success!")
        print("> Downloading zip with DATABASE.BIN")
        self.download_zip()
        print("> Success!")
        print("> Unzipping archive with DATABASE.BIN")
        self.unzip_bin()
        print("> Success!")
        print("> Setup completed")
        return True
