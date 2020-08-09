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


def downloadvid(event):
    val=var.get()
    url=urlentry.get()
    print(url)
    yt=YouTube(url)

    try:
        if(val==1):
            vid=yt.streams.filter(res="720p").first()
            try:
                vid.download("D:/")
            except:
                print("some error occured while downloading")
        elif(val==2):
            vid = yt.streams.filter(res="480p").first()
            try:
                vid.download("D:/")
            except:
                print("some error occured while downloading")
        elif(val==3):
            vid = yt.streams.filter(res="360p").first()
            try:
                vid.download("D:/")
            except:
                print("some error occured while downloading")
        elif(val==4):
            vid = yt.streams.filter(res="240p").first()
            try:
                vid.download("D:/")
            except:
                print("some error occured while downloading")
        elif(val==5):
            vid = yt.streams.filter(res="144p").first()
            try:
                vid.download("D:/")
            except:
                print("some error occured while downloading")


    except:
        print("some error occured")


    print("downlaod vid is called")



pasteurltxt=Label(frame2,text="Paste url",font=("Arial Bold",20),bg="light sky blue")
pasteurltxt.pack()
pasteurltxt.bind("<Return>",downloadvid)

urlentry=Entry(frame2,width=60)
urlentry.pack(pady=5)

downloadbtn=Button(frame2,text="DOWNLOAD",font=("ms serif",16,"bold"),fg="snow",bg="red")
downloadbtn.pack(pady=30)
downloadbtn.bind("<Button-1>",downloadvid)

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
