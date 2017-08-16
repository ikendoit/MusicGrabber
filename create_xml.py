#!/usr/bin/python
from lxml import etree
from io import StringIO
from grablink import call_link
from xml.dom import minidom
from xml.dom.minidom import parseString
          
def addSong(songName,artistName):
    #get info and setup
    print("getting the link: ")
    video = etree.Element('video'); 
    artist = etree.Element('artist');
    name = etree.Element('name'); 
    ids = etree.Element('id');
    status = etree.Element('none');
    link = etree.Element('link');
    #set up tree
    video.append(artist); 
    video.append(name);
    video.append(ids);
    video.append(status);
    video.append(link)

    name.text = songName; 
    artist.text = artistName; 
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

def runPrompt():
    print("1: add song info \n2: delete song \n3:nothing, get me out.")
    option = int(input("input the option ")); 
    while (option != 3):

        if (option == 1 ) : 

            # input 
            songName = str(raw_input("input name: "));
            artistName = str(raw_input("input artist name: "));

            addSong(songName,artistName);
            print("1: add song info \n2: delete song \n3:nothing, get me out.")
            option = int(input("input the option ")); 

        if (option == 2) : 
            print("removing stuffs in data.xml")
            f=open("data.xml",'r')
            text = f.read();
            tree = etree.fromstring(text)
            f.close()

            songName = str(raw_input("input name: "));
            songName.strip();
            videos = tree.xpath("//*[child::*[contains(text(),'"+songName+"')]]")
            print(videos)
            for video in videos : 
                    video.getparent().remove(video)

            f = open("data.xml",'w')
            f.write(etree.tostring(tree,pretty_print = True, xml_declaration = True))
            f.close()
            option = int(input("input option"))
