import pzgram
import re
from pytube import YouTube

bot=pzgram.Bot("590932411:AAGS3ri3itZXYlgylWIZBBX1LJ7TivzHrH4")

yt={}
filtro={}
filename=1

def scelta(chat):
	chat.send("inserisci il link")
	bot.set_next(chat,recivelink)
	
def recivelink(chat,message):
	global yt	
	yt[chat.id]=YouTube(message.text)
	b1=pzgram.create_button("audio","downloadcanzone")
	b2=pzgram.create_button("video","downloadvideo")
	k=pzgram.create_inline([[b1,b2]])	
	chat.send("il link mi riporta la canzone: "+yt[chat.id].title+"\n Solo audio o video?",reply_markup=k)

def qualita(query,message,data):
	global filtro,yt
	if data=="downloadcanzone":
		filtro[message.chat.id]="only_audio"
		download("download_audio",message)
	elif data=="downloadvideo":
		filtro[message.chat.id]="only_video"
		provaa = str(yt[message.chat.id].streams.filter(only_video=True,subtype='mp4',fps=30).all())
		prova = re.findall('res\=\"([0-9]+)', provaa)
		k=[]		
		for i in range(len(prova)):
			k.append([pzgram.create_button(prova[i],"download_"+prova[i])])
		keyboard=pzgram.create_inline(k)
		message.edit("seleziona la qualita",reply_markup=keyboard)
		
def download(data,message):
	global filtro,yt,filename
	print ("ciao")	
	if data.startswith("download_"):
		s=data.split("_")[1]
		if s == "audio":
			filename+=1
			message.chat.send("la canzone si sta scaricando attendere prego")
			yt[message.chat.id].streams.filter(only_audio=True).first().download("/home/pardo/Scrivania/PyTesina/download/",str(filename))
			message.chat.send_document("/home/pardo/Scrivania/PyTesina/download/"+str(filename)+".mp4")
			return
		s=s+"p"
		print("prova")		
		message.chat.send("il tuo video si sta scaricando attendere prego")
		filename+=1		
		yt[message.chat.id].streams.filter(res=s).first().download("/home/pardo/Scrivania/PyTesina/download/",str(filename))
		message.chat.send_document("/home/pardo/Scrivania/PyTesina/download/"+str(filename)+".mp4")

		

def start(chat, message):
	chat.send("Benvenuto nel bot")
bot.set_commands({"start":start,"scelta_url":scelta})
bot.set_query({"downloadcanzone":qualita,"downloadvideo":qualita})
bot.callBackFunc=download

bot.run()


