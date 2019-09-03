from bs4 import BeautifulSoup
import requests

url='https://twitter.com/KMbappe?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor' 
temp = requests.get(url)
bs = BeautifulSoup(temp.text,'lxml')

try:
    follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of followers: {} ".format(followers.get('data-count')))
except:
    print('URL not found...')
