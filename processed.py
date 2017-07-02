from lxml import etree

def backup(name,song): 

	f=open("downloaded.xml","a")
	f.write(song + " - "+name +'\n')
	f.close()



def delete(link):
    f=open("data.xml",'r')
    text = f.read();
    tree = etree.fromstring(text)
    f.close()

    videos = tree.xpath("//*[child::*[contains(text(),'"+link+"')]]")

    for video in videos : 
        video.getparent().remove(video)

    f = open("data.xml",'w')
    f.write(etree.tostring(tree,pretty_print = True, xml_declaration = True))
    f.close()
