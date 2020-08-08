from pytube import  YouTube
yt=YouTube('https://www.youtube.com/watch?v=f4Yc5uMHVGI')
a=list(yt.streams.filter(progressive=True).all())
print(a)
u=yt.streams.filter(progressive=True,res="360p").first()
u.download("D:/")
