from lxml import etree 
import grabmp3
import create_xml
import processed
import sys

if (len(sys.argv) ==3 ): 
    print(sys.argv[1]+" and "+sys.argv[2]);
    create_xml.addSong(sys.argv[1],sys.argv[2]);
elif (len(sys.argv) ==2 ) : 
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
    create_xml.runPrompt();
            
