from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
import requests
from io import BytesIO

window=Tk()

window.title("BACK-LCK Analyzer")
window.geometry("750x480")
window.resizable(0,0)

imgURL = 'https://ticketimage.interpark.com/TicketImage/sports/mobile/bg/PE015.jpg'
response = requests.get(imgURL)
img_data = response.content
bg = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
labelbg=Label(window,image=bg)

label1=Label(window, text="BACK-LCK Analyzer", width=20,height=5,fg="black", relief="solid")
label2=Button(window, text="BANPICK TOOL", width=20,height=5,fg="black", relief="solid")
label3=Button(window, text="ANALYZING TOOL", width=20,height=5,fg="black", relief="solid")

labelbg.place(x=0,y=0)
label1.place(x=300,rely=0.1)
label2.place(x=300,rely=0.4)
label3.place(x=300,rely=0.7)

window.mainloop()