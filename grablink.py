from bs4 import BeautifulSoup
import requests

def call_link(name,artist):
	name = str(name)
	artist = str(artist);
	query = (name+' '+artist+' lyrics').replace(' ','+')
	
	url = "https://www.youtube.com/results?search_query="+query
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,'lxml')


	for link in soup.find_all('a'):
		if "/watch?" in link.get('href'): 
			s=link.get('href')
			break
	return "https://youtube.com"+s
