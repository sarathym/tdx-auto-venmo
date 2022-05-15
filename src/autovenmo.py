from venmo_api import Client
import os.path
import csv
from facepy import GraphAPI
import json
import requests
from bs4 import BeautifulSoup
import vars

group_url = 'https://www.facebook.com/groups/163979811044335'
JSTOKEN = vars.JSTOKEN
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
#access_token = ***
#venmo = Client(access_token=access_token)
SHEET_ID = "1zzP_-JUzKRuqBy-igGIRYaoFCb_WE-5K88nSjdk1frA"
RANGE = "jawn!A:C"
#api = facebook.GraphAPI(app_id="id", app_secret="secret", oauth_flow=True)


class FBGroupScraper:

    def __init__(self, group_id):
        self.group_id = group_id
        self.page_url = "https://mobile.facebook.com/groups/" + self.group_id
        self.page_content = ""

    def get_page_content(self):
        self.page_content = requests.get(self.page_url).text

    def parse(self):
        soup = BeautifulSoup(self.page_content, "html.parser")
        feed_container = soup.find(id="m_group_stories_container").find_all("p")
        for i in feed_container:
            print(i.text)


def main():
    jawn = []
    payload = {"m_login_email": "stealthisaur@gmail.com", "m_login_password": "brownTable007"}
    group_id = "163979811044335"
    page_url = "https://mobile.facebook.com/groups/" + group_id


    with requests.Session() as s:
        p = s.post("https://mobile.facebook.com/login", data=payload)
        print(p.text)
        page_content = s.get(page_url).text
        soup = BeautifulSoup(page_content, "html.parser")
        feed_container = soup.find(id="m_group_stories_container").find_all("p")
        for i in feed_container:
            print(i.text)

    """:
    with open('The Master Sheet - jawn.csv','r') as f:
        csvfile = csv.reader(f)
        for line in csvfile:
            jawn.append(line)

    for jawny in jawn:
        id = ""
        jawnathan = True
        tmp1 = 0

        while jawnathan:
            tmp = venmo.user.search_for_users(query=jawny[0],offset=tmp1, limit=50)
            for yerba in tmp:
                if yerba.username == jawny[0]:
                    id = yerba.id
                    jawnathan = False
            tmp1+=50

        venmo.payment.request_money(int(jawny[1]), jawny[2], id)

    venmo.log_out(access_token)
    """


if __name__=="__main__":
    main()
