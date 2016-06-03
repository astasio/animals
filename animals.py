#!/usr/bin/python
import gtk
from os import popen,walk,path
import atk,cairo,pango,pangocairo,gio
#import winsound

def exit():
	gtk.main_quit()

def play(b):
	popen("play modules/"+mb[b.__hash__()]+"/"+mb[b.__hash__()]+".wav")
#	winsound.PlaySound("modules/"+mb[b.__hash__()]+"/"+mb[b.__hash__()]+".wav", winsound.SND_FILENAME)
	
def list_modules():
	list=[]
	for dirname,dirnames,filenames in walk("modules"):
		for subdirname in dirnames:
						list.append(path.join(subdirname))
	return list

win=gtk.Window()
win.set_title("Versi degli animali")
win.set_resizable(False)
win.set_size_request(720,490)
win.connect("destroy",lambda *w:exit())

scroll=gtk.ScrolledWindow()
win.add(scroll)
vp=gtk.Viewport()
scroll.add(vp)

vb=gtk.VBox()
vb.set_homogeneous(gtk.TRUE)
vp.add(vb)

list=list_modules()
mb={}
count=0
for i in list:
	button=gtk.Button()
	if(count==3 or count==0):
		count=0
		hb=gtk.HBox()
		hb.set_homogeneous(gtk.TRUE)
		vb.add(hb)
		vb.set_child_packing(hb,0,0,0,gtk.PACK_START)
	hb.add(button)
	hb.set_child_packing(button,0,0,0,gtk.PACK_START)
	button.set_size_request(200,200)
	button_image=gtk.Image()
	button_image.set_from_file("modules/"+i+"/"+i+".png")
	button.set_image(button_image)
	button.connect("clicked",play)
	mb[button.__hash__()]=i
	count +=1
win.show_all()

gtk.main()

