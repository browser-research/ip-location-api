import os
import glob
import zipfile
import IP2Location

from pathlib import Path
from urllib.request import urlretrieve

# TODO: To .env vars
token = "pSWDCyKfq5LdQghZrxe9ibxXvmD4MCKcvGP7eAmFF8Swo9vQHKZZVwXrTAvFdfRI"
temp_dir = "./temp/"
db_file_name = "database.zip"

location = temp_dir + db_file_name


def make_temp(folder_name="temp"):
    Path("./" + folder_name).mkdir(parents=True, exist_ok=True)
    return True


def wipe_temp():
    files = glob.glob(temp_dir + "*")
    for f in files:
        os.remove(f)
    return True


def download_zip(db_code="DB3LITEBIN"):
    url = "https://www.ip2location.com/download/?token={}&file={}".format(
        token, db_code)
    urlretrieve(url, location)
    return True


def unzip_bin():
    with zipfile.ZipFile(location, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    return True


def setup():
    make_temp()
    print("> Temp directory created (if not existed)")
    wipe_temp()
    print("> Temp content wiped (if existed)")
    download_zip()
    print("> Zip archive with DATABASE.BIN successfully downloaded")
    unzip_bin()
    print("> The content of Zip archive was unzipped")
