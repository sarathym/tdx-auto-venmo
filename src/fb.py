from pyfacebook import GraphAPI
from pyfacebook import FacebookApi
import requests
import vars
import json

auth = vars.auth

def main():
    #print("Warning: the following program is executing with SAMPLE DATA as I do not have an auth key to be able to access any groups and get any real data.")
    #auth = 'a75512daa63d03a6f1fbd0643d1efabb'
    graph = GraphAPI(access_token=auth)
    api = FacebookApi(access_token=auth)

    #facebook = facepy.get_groups_feed('https://www.facebook.com/groups/163979811044335')
    cont = True

    groupid = '368237921889322'

    #since = input("Date since? Format: (yy-mm-dd) ")
    since = "22-04-04"
    until = "22-04-11"
    posts = api.group.get_feed(object_id=groupid)
    #posts = graph.get_connection(object_id=groupid, connection="posts")
    print(posts)
    """
    link = 'https://graph.facebook.com/v13.0/' + groupid + '/feed?access_token='+auth #+ '&since=' + since
    data = requests.get(link)
    
    #until = input("Date until? Format: (yy-mm-dd) ")
    # Hi, I'm trying to access the feed of a Group with id 368237921889322, but no matter what keep getting this error - "Please reduce the amount of data you're asking for, then retry your request". I have tried with limits from 1 to 100, with the parameters since and before filled, and with all of the parameters one at a time and every combination between. Nothing works, and I always get error code 1 with either no description or the error I mentioned previously. I have the Individual Verification and am verified to use the Groups API. I tried to access the group's feed with both the Graph API Explorer and Facepy on Python on my local machine.
    #data = graph.get(groupid + '/feed',since=since,until=until)

    jsonposts = json.dumps(data.json())
    output = json.loads(jsonposts)
    paging = "&paging_token=" + output['paging']['next'].split("paging_token=",1)[1]
    output = requests.get(link + paging).json()
    print(output['data'])
    paging = "&paging_token=" + output['paging']['next'].split("paging_token=",1)[1]
    print(requests.get(link + paging).json())
    info = output[u'data']
    posts = scrape_data(info)

    # [created time, name, link, likes, comments]
    tmpposts = [["22-06-14", 'Manoj', 'https://www.facebook.com/groups/163979811044335', 0, 3],["22-06-14", 'James', 'https://www.facebook.com/groups/163979811044335', 0, 3],
                ["22-06-14", 'Anders', 'https://www.facebook.com/groups/163979811044335', 0, 3],["22-06-14", 'Boden', 'https://www.facebook.com/groups/163979811044335', 0, 3],
                ["22-06-14", 'Andy', 'https://www.facebook.com/groups/163979811044335', 0, 3],["22-06-14", 'Josh', 'https://www.facebook.com/groups/163979811044335', 0, 3],
                ["22-06-14", 'Anders', 'https://www.facebook.com/groups/163979811044335', 0, 3],["22-06-14", 'Josh', 'https://www.facebook.com/groups/163979811044335', 0, 3],
                ["22-06-14", 'Samuel', 'https://www.facebook.com/groups/163979811044335', 0, 3],["22-06-14", 'Samuel', 'https://www.facebook.com/groups/163979811044335', 0, 3]]
    res = {'Manoj': 0, 'Samuel': 0, 'Andy': 0, 'Anders': 0, 'Marc': 0, 'Chris': 0, 'Josh': 0, 'Boden': 0, 'James': 0}
    keys = []

    print("Scanning data from posts...")
    for post in posts:
        if type(post[4]) == int:
            #res[post[1]] += 1
            keys.append(post[1])

    print(keys)

    for jawn in res:
        if res[jawn] == 0:
            print("Fine " + jawn + " $10.")
        elif res[jawn] == 1:
            print("Fine " + jawn + " $5.")
        else:
            print("No fine for " + jawn + ".")
    # dict of all people in the house and their Facebook usernames to zero. This is the dict that will be used to count how many chores people have done/not done
    chores = {'manojsarathy': 0, 'james': 0, 'anders': 0}
    # dict of all Facebook usernames to venmo usernames
    # usernames = {manojsarathy: sarathym, james: james123, anders: anders123, etc.}
    while cont:
        for post in groupposts:
            if post.date > 7:
                cont = False
                chores[post.username] += 1
                
    for person in chores:
        if chores[person] == 0:
            venmo.request_money(10, usernames[person])
        elif chores[person] == 1:
            venmo.request_money(5, usernames[person])
    """


def scrape_data(a):
    masterlist = []
    for i in a:
        minorlist = []
        # [created time, name, link, likes, comments]
        try:
            minorlist.append(i[u'created_time'])
        except:
            minorlist.append("No Created Time")
        #minorlist.append(i[u'from'][u'name'])
        try:
            minorlist.append(i[u'name'])
        except:
            minorlist.append("No Link")
        try:
            minorlist.append(i[u'link'])
        except:
            minorlist.append("No URL")
        try:
            minorlist.append(len(i[u'likes'][u'data']))
        except KeyError:
            minorlist.append(0)
        try:
            minorlist.append(len(i[u'comments'][u'data']))
        except KeyError:
            minorlist.append("No comments")
        masterlist.append(minorlist)
    print(masterlist)
    return masterlist


if __name__=="__main__":
    main()