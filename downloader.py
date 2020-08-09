from tkinter import *
from pytube import  YouTube

# Now first creating a GUI

window=Tk()
window.title("YOUTUBE VIDEO DOWNLOADER")
window.geometry('600x600')
window.configure(bg="light sky blue")
window.resizable(0,0)
frameuseless=Frame(window,height=100,bg="light sky blue")
frameuseless.pack()

frame2=Frame(window,height=100,bg="light sky blue")
frame2.pack()

frame_for_res=Frame(window,height=100,bg="light sky blue")
frame_for_res.pack(pady=10)

pasteurltxt=Label(frame2,text="Paste url",font=("Arial Bold",20),bg="light sky blue")
pasteurltxt.pack()

urlentry=Entry(frame2,width=60)
urlentry.pack(pady=5)

downloadbtn=Button(frame2,text="DOWNLOAD",font=("ms serif",16,"bold"),fg="snow",bg="red")
downloadbtn.pack(pady=30)

var=IntVar()

btn720p=Radiobutton(frame_for_res,text="720p",bg="light sky blue",variable=var,value=1)
btn480p=Radiobutton(frame_for_res,text="480p",bg="light sky blue",variable=var,value=2)
btn360p=Radiobutton(frame_for_res,text="360p",bg="light sky blue",variable=var,value=3)
btn240p=Radiobutton(frame_for_res,text="240p",bg="light sky blue",variable=var,value=4)
btn144p=Radiobutton(frame_for_res,text="144p",bg="light sky blue",variable=var,value=5)

btn720p.grid(column=0,row=0,padx=5)
btn480p.grid(column=1,row=0,padx=5)
btn360p.grid(column=2,row=0,padx=5)
btn240p.grid(column=3,row=0,padx=5)
btn144p.grid(column=4,row=0,padx=5)


var.set(5)



window.mainloop()


















'''
yt=YouTube('https://www.youtube.com/watch?v=f4Yc5uMHVGI')
a=list(yt.streams.filter(progressive=True).all())
print(a)
u=yt.streams.filter(progressive=True,res="360p").first()
u.download("D:/")
'''
