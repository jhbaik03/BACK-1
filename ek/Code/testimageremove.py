import tkinter
import tkinter.font
import numpy as np
from tkinter import ttk
from PIL import Image, ImageTk

def champion_click(event):
    widget_selected_champion = event.widget
    print(widget_selected_champion.cget('text'))
    widget_selected_champion.config(image='')
    # widget_selected_champion.image.blank()
    # widget_selected_champion.image = None
    
    # global name_selected_champion
    # global image_selected_champion

    # # 선택된 챔피언 라벨의 이미지 정보 가져오기
    # widget_selected_champion = event.widget
    # print(widget_selected_champion)
    # name_selected_champion = widget_selected_champion.cget('text')
    # image_selected_champion = widget_selected_champion.cget('image')
    # if image_selected_champion is not None and name_selected_champion is not None:
    #     print("copy")

#전체 화면 설계 (590*650)
window = tkinter.Tk()
window_width = 590
window_height = 650

window.title("픽창")
window.geometry("{}x{}+100+100".format(window_width, window_height))
window.resizable(False, False)

image = Image.open("lck analyzing tool/champ/Aatrox.png")
width_image = 50
height_image = 50

image_resize = image.resize((width_image, height_image), Image.LANCZOS)
img = ImageTk.PhotoImage(image_resize)

frame_champion = tkinter.LabelFrame(window, width=100, height=100+15, 
         relief="solid", bg="white", highlightthickness=0, text="Aatrox",
         labelanchor="s", padx=0, pady=0, border=0)
frame_champion.place(x=0, y=0)
frame_champion.bind("<Button-1>", champion_click)

inframe = tkinter.Label(frame_champion, image=img, text="Aatrox", 
             border=0, padx=0, pady=0)
inframe.place(x=0, y=0)

image = Image.open("lck analyzing tool/champ/Aatrox.png")
width_image = 50
height_image = 50

image_resize = image.resize((width_image, height_image), Image.LANCZOS)
img = ImageTk.PhotoImage(image_resize)

frame_champion = tkinter.LabelFrame(window, width=100, height=100+15, 
         relief="solid", bg="white", highlightthickness=0, text="Aatrox",
         labelanchor="s", padx=0, pady=0, border=0)
frame_champion.place(x=0, y=0)
frame_champion.bind("<Button-1>", champion_click)

inframe = tkinter.Label(frame_champion, image=img, text="Aatrox", 
             border=0, padx=0, pady=0)
inframe.bind("<Button-1>", champion_click)
inframe.place(x=0, y=0)
window.mainloop()
