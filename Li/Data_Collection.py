from lxml import html
import requests
import sys


def text_file(generated_uni_id):
    """
    function will insert generated uni_id to .text file
    :param generated_uni_id
    :return: Uni_ID.txt
    # TODO: insert uni_id to .txt file
    """
    sys.stdout = open("Uni_ID.txt", "w")
    print(generated_uni_id)
    sys.stdout.close()


def scraper(file):
    """
    This function will collect data from the website. Function will loop over each uni_id in Uni_ID.txt file.
    The collected data will insert into the file named FinalData.txt.
    :param file
    :return: FinalData.txt
    # TODO: Reformat uni_id from file, then plug in uni_id to the URL. Write a function that will go to the actual
    thwebsite and function that at will not write empty list(staff with no information) into .txt file.

    """
    sys.stdout = open("FinalData.txt", "w")
    Empty_list = []
    for i in file:
        uni_ID = 'u' + i[0:8].strip()
        website = requests.get("http://www.anu.edu.au/_anu/staffdir/search.php?q=" + uni_ID)
        tree1 = html.fromstring(website.content)
        unsort_role = tree1.xpath('//p[@class="nopadbottom"]/text()')
        name = tree1.xpath('//h3[@class="nopadbottom"]/text()')
        role = unsort_role[2:]
        if name == Empty_list:
            pass
        else:
            print(uni_ID, ',', role)
        sys.stdout.close()

##Generate university id from 0000000 to 10000000
text_file("\n".join(['{0:07}'.format(num) for num in range(0000000, 10000000)]))
with open('Uni_ID.txt') as file:
    scraper(file)

####Reference
#1. http://docs.python-guide.org/en/latest/scenarios/scrape/








