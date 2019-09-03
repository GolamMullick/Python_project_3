from bs4 import BeautifulSoup  #to parse that data
import requests   #provide us with our target's HTML

url='https://twitter.com/KMbappe?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
temp = requests.get(url) # to get the content at `url` by making an HTTP GET request
bs = BeautifulSoup(temp.text,'lxml') #parse the raw HTML by passing it to the BeautifulSoup constructor

try:
    follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'}) #loop
    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of followers: {} ".format(followers.get('data-count')))
except:
    print('URL not found...')
