#!/usr/bin/python3.5
from lxml import etree
from grablink import call_link
          
id =0; 
def addsongs(songName, artistName):
	video = etree.Element('video'); 
	artist = etree.Element('artist');
	name = etree.Element('name'); 
	id = etree.Element('id');
	status = etree.Element('none');
	link = etree.Element('link');
	#set up tree
	video.append(artist); 
	video.append(name);
	video.append(id);
	video.append(status);
	video.append(link)
	# input 
	# songName = str(raw_input("input name: "));
	# artistName = str(raw_input("input artist name: "));

	name.text = str(songName); 
	artist.text = str(artistName); 
	status.text = "False";
	link.text = call_link(songName,artistName)

	#set data variable
	# data = etree.tostring(video, pretty_print = True);

	#file appen 
	parser =etree.XMLParser(remove_blank_text=True)
	tree = etree.parse("data.xml",parser);
	root = tree.getroot()
	root.append(video)

	f = open('data.xml','w')
	# f.write(data+'\n')
	f.write(etree.tostring(root,pretty_print=True))
	f.close();

def delsongs(songName):
	print("removing stuffs in data.xml")
	f=open("data.xml",'r')
	text = f.read();
	tree = etree.fromstring(text)
	f.close()

	songname = str(songName)
	videos = tree.xpath("//*[child::*[contains(text(),'"+songname+"')]]")
	print(videos)
	for video in videos : 
		video.getparent().remove(video)

	f = open("data.xml",'w')
	f.write(etree.tostring(tree,pretty_print = True, xml_declaration = True))
	f.close()