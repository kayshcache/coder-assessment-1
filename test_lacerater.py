import requests
import os
from lacerater import download_url, make_file

URL_OBJ = download_url('http://www.coder-academy-ctf.site/')
def test_download_url():
    assert isinstance(URL_OBJ, requests.models.Response) == True # Expect to create a requests class object from URL

def test_make_file():
    filename = make_file(URL_OBJ)
    assert os.path.exists(filename) == True # Expect to create the file
    os.remove(filename)