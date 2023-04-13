import tkinter
import tkinter.font
import numpy as np

#전체 화면 설계 (590*650)
window = tkinter.Tk()
window_width = 590
window_height = 650

window.title("픽창")
window.geometry("{}x{}+100+100".format(window_width, window_height))
window.resizable(False, False)

# 스크롤바 생성
scrollbar_champion = tkinter.Scrollbar(window, orient='vertical')
scrollbar_champion.pack(side='right', fill='y')

# 스크롤 가능한 Canvas 위젯 생성
canvas_champions = tkinter.Canvas(window, yscrollcommand=scrollbar_champion.set)
canvas_champions.pack(side='left', fill='both', expand=True)

# 스크롤바와 Canvas 위젯 연결
scrollbar_champion.config(command=canvas_champions.yview)

# 스크롤 가능한 영역으로 사용할 Frame 생성
scrollable_frame = tkinter.Frame(canvas_champions, bg='blue')

# Frame에 내용 삽입
champion_num = 141

frame_champions = []
frame_champions_line = []
frame_champions_width= 15
frame_champions_height= 50

line_num=-1
for i in range(champion_num):
    if i%6==0:
        frame_champions_line.append(0)
        line_num = line_num+1
        frame_champions_line[line_num] = tkinter.Frame(scrollable_frame, width = frame_champions_width*6+5*7, height= frame_champions_height, bg="red", bd=5)
        frame_champions_line[line_num].pack()
    print(i)
    frame_champions.append(0)
    frame_champions[i] = tkinter.Frame(frame_champions_line[line_num], width = frame_champions_width, height= frame_champions_height, relief="solid", bg="#FF00FF")
    frame_champions[i].place(x=(i%6)*frame_champions_width + (i%6)*5, y=0)


# Canvas 위젯에 Frame 삽입
canvas_champions.create_window((0, 0), window=scrollable_frame, anchor='nw')

# 스크롤바에도 Canvas 위젯 연결
scrollable_frame.bind('<Configure>', lambda e: canvas_champions.configure(scrollregion=canvas_champions.bbox('all')))



window.mainloop()
