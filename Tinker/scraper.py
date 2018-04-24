# Personal Data Grabber

import requests


class Scraper:

    def __init__(self):
        None

def dir_search(uid):
    """
    function will lookup against the ANU directory for a the input string
    :param uid: this should be a university ID being checked against the ANU directory
    :return: a tuple in the format of University ID, get requests url and content returned.
    # TODO: the clean up returned data.
    """
    directory_url = 'http://www.anu.edu.au/_anu/staffdir/search.php'
    payload = {'q': uid, 'submit': 'search'}
    r = requests.get(directory_url, params=payload)
    return uid, r.url, r.content

def uid_generator():
    """

    :return: University ID in the formate Unnnnnnn
    """
    for i in range(10000000):
        uid = "u{0:07d}".format(i)
        print(dir_search(uid))


# uid_generator()
print(dir_search('u5318579'))



