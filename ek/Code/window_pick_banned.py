import tkinter
import tkinter.font
import numpy as np

def callback_champion_click(event):
    print(event.widget)
    a = str(event.widget).split(".!")
    print(a[-2], a[-1])

window = tkinter.Tk()

window_width = 1280
window_height = 720

window.title("픽창")
window.geometry("{}x{}+100+100".format(window_width, window_height))
window.resizable(False, False)

font1=tkinter.font.Font(family="맑은 고딕", size=20)
font2=tkinter.font.Font(family="맑은 고딕", size=10)

frame_top_width = window_width
frame_top_height = 80
frame_top = tkinter.Frame(window, width = frame_top_width, height = frame_top_height, relief="solid", bg="black") 
frame_top.place(x=0,y=0)

label_top=tkinter.Label(master=frame_top, text="밴픽", font=font1, bg="black", foreground="white")
label_top=label_top.place(anchor="center", x=window_width/2, y=frame_top_height/2)


frame_blueTeam_width = 350;
frame_blueTeam_height = window_height - frame_top_height
frame_redTeam_width = 350;
frame_redTeam_height = window_height - frame_top_height
frame_center_width = window_width - frame_blueTeam_width - frame_redTeam_width;
frame_center_height = window_height - frame_top_height

frame_blueTeam = tkinter.Frame(window, width = frame_blueTeam_width, height = frame_blueTeam_height, relief="solid", bg="blue")
frame_blueTeam.place(x=0,y=frame_top_height)
label_blueTeam=tkinter.Label(master=frame_blueTeam, text="TEAM NAME", font=font2, bg="black", foreground="white")
label_blueTeam=label_blueTeam.place(anchor="center", x=frame_blueTeam_width/2, y=25)

frame_center = tkinter.Frame(window, width = frame_center_width, height = frame_blueTeam_height, relief="solid", bg="white")
frame_center.place(x=frame_blueTeam_width, y=frame_top_height)
frame_redTeam = tkinter.Frame(window, width = frame_redTeam_width, height = frame_redTeam_height, relief="solid", bg="red")
frame_redTeam.place(x=frame_blueTeam_width + frame_center_width, y=frame_top_height)
label_redTeam=tkinter.Label(master=frame_redTeam, text="TEAM NAME", font=font2, bg="black", foreground="white")
label_redTeam=label_redTeam.place(anchor="center", x=frame_redTeam_width/2, y=25)


frame_member_width = 350;
frame_member_height = (frame_blueTeam_height - 40)/5

frame_blueTeamMember = []

for i in range(5):
    frame_blueTeamMember.append(0)
    frame_blueTeamMember[i] = tkinter.Frame(frame_blueTeam, width = frame_member_width, height = frame_member_height, relief="solid", bg="#7676EE", bd=1)
    frame_blueTeamMember[i].place(x=0, y=50+frame_member_height*i)


frame_redTeamMember = []

for i in range(5):
    frame_redTeamMember.append(0)
    frame_redTeamMember[i] = tkinter.Frame(frame_redTeam, width = frame_member_width, height = frame_member_height, relief="solid", bg="#EE7676", bd=1)
    frame_redTeamMember[i].place(x=0, y=50+frame_member_height*i)

frame_center_search = tkinter.Frame(frame_center, width = frame_center_width-20, height= 30, relief="solid", bg="#111111", bd=1)
frame_center_search.place(anchor="center", x=frame_center_width/2, y=25)

text_search = tkinter.Text(frame_center_search, width=20, height=1, padx=1, pady=1, fg="#000000", bg="#EEEEEE")
text_search = text_search.place(x=0,y=0)

frame_center_champion = tkinter.Frame(frame_center, width = frame_center_width-20, height= frame_center_height-60, relief="solid", bg="#222222", bd=1)
frame_center_champion.place(anchor="n", x=frame_center_width/2, y=50)

#######챔피언 고르는 Frame 설정(scrollbar)
# 스크롤바 생성
scrollbar_champion = tkinter.Scrollbar(frame_center_champion, orient='vertical')
scrollbar_champion.pack(side='right', fill='y')

# 스크롤 가능한 Canvas 위젯 생성
canvas_champions = tkinter.Canvas(frame_center_champion, yscrollcommand=scrollbar_champion.set, width=frame_center_width-40, height=frame_center_height-60, highlightthickness=0)
canvas_champions.pack(side='left', fill='both', expand=True)

# 스크롤바와 Canvas 위젯 연결
scrollbar_champion.config(command=canvas_champions.yview)

# 스크롤 가능한 영역으로 사용할 Frame 생성
scrollable_frame = tkinter.Frame(canvas_champions)

# Frame에 내용 삽입
champion_num = 141

frame_champions = []
frame_champions_line = []
frame_champions_width= (frame_center_width-40-35)/6
frame_champions_height= frame_champions_width

line_num=-1
for i in range(champion_num):
    if i%6==0:
        frame_champions_line.append(0)
        line_num = line_num+1
        frame_champions_line[line_num] = tkinter.Frame(scrollable_frame, width = frame_champions_width*6+5*7, height= frame_champions_height, bg="gray", bd=5)
        frame_champions_line[line_num].pack()
    # print(i)
    frame_champions.append(0)
    frame_champions[i] = tkinter.LabelFrame(frame_champions_line[line_num], width = frame_champions_width, height= frame_champions_height, relief="solid", bg="white", text=str(i))
    frame_champions[i].place(x=(i%6)*frame_champions_width + (i%6)*5, y=0)
    frame_champions[i].bind("<Button-1>", callback_champion_click)

# Canvas 위젯에 Frame 삽입
canvas_champions.create_window((0, 0), window=scrollable_frame, anchor='nw')

# 스크롤바에도 Canvas 위젯 연결
scrollable_frame.bind('<Configure>', lambda e: canvas_champions.configure(scrollregion=canvas_champions.bbox('all')))



window.mainloop()

