from lxml import etree 
import grabmp3
import processed

mode = int(input("1.add songs \n2.download songs"))
if (mode == 2 ):
	parser =etree.XMLParser(remove_blank_text=True)
	tree = etree.parse("data.xml",parser);

	videos = tree.getiterator('video')

	for video in videos:
		name =''
		link =''
		artist = ''
		for element in video.getiterator('name'):
			name = element.text;
		for element in video.getiterator('link'): 
			link = element.text;
		for element in video.getiterator('artist'):
			artist = element.text;
		grabmp3.grab(name,link)
		processed.backup(artist, name)
		processed.delete(name)
else : 
	import create_xml
	
