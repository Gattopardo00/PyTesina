from pytube import YouTube
import re

def scelta():
	global yt
        link=raw_input("inserire il link del video-->")
        yt=YouTube(link)
        print "il link mi riporta la canzone: "+yt.title

def visualizzazione():
	global yt
	print yt.streams.all()

def selezione():
	global filtro,yt,qualita,videoaudio
	videoaudio=raw_input("desidera la canzone o il video?")
	if videoaudio == "canzone":
		filtro="only_audio"
	elif videoaudio == "video":
		filtro="only_video"
		provaa = str(yt.streams.filter(only_video=True,subtype='mp4',fps=30).all())
		#print provaa
		prova=re.findall('res\=\"([0-9]+)', provaa)
		for i in range(len(prova)):
			print prova[i] + "p \n"
		qualita=raw_input("seleziona la qualita del video -->")
def download():
	global filtro,yt,qualita,videoaudio
	if videoaudio == "canzone":	
		yt.streams.filter(only_audio=True).first().download()
	elif videoaudio == "video":
		prova=str(qualita)
		yt.streams.filter(res=prova).first().download()	

#exec "yt.streams.filter("+ filtro +"=True).download()"
#yt.streams.filter(only_audio=True).first().download()
while True:
	print '''Menu:
	1)Inserire il video
	2)Visualizzare cosa posso scaricare
	3)Selezione cosa voglio scaricare
	4)Download
	5)Quit'''
	a=raw_input()
	if a == "1":
		scelta()
	elif a == "2":
		visualizzazione()
	elif a == "3":
		selezione()
	elif a == "4":
		download()
	elif a == "5":
		break
