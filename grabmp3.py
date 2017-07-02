import youtube_dl

def grab(name, link):
	options = {
		'format':'bestaudio/best',
		'extractaudio':True,
		'audioformat':'mp3',
		'outtmpl': ''+str(name)+'.'+'%(ext)s',   
		'noplaylist':True,
		'nocheckcertificate':True,
		'verbose' : True,
		'postprocessors' :[{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}]
	}

	with youtube_dl.YoutubeDL(options) as ydl: 
		ydl.download([link])
	return