import tkinter
import tkinter.font
import numpy as np
from tkinter import ttk
from PIL import Image, ImageTk

T1=["Zeus","Oner","Faker", "Gumayusi","Keria"]
Gen=["Doran","Peanut","Chovy","Peyz","Delight"]

window_width = 1280
window_height = 720


class BackBanpickAnalyzer(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("BACK BANPICK ANALYZER")

        # 상단 프레임 생성
        top_frame = tkinter.Frame(self, bg="#322756", width=400, height=50)
        top_frame.pack(side="top", fill='both')

        # 좌 프레임 생성
        left_frame = tkinter.Frame(self, bg='#322756', width=200, height=400, bd=3)
        left_frame.pack(side='left')

        # 좌 프레임에 버튼 배치
        left_button = tkinter.Button(left_frame, text='BANPICK TOOL', font=('Arial', 14), bg='#322756',command=self.show_window2)
        left_button.place(relx=0.5, rely=0.5, anchor='center')

        # 우 프레임 생성
        right_frame = tkinter.Frame(self, bg='#322756', width=200, height=400)

        # 우 프레임에 버튼 배치
        right_button = tkinter.Button(right_frame, text='ANALYZING TOOL', font=('Arial', 14), bg='#322756')
        right_button.place(relx=0.5, rely=0.5, anchor='center')

        # 우 프레임을 윈도우 오른쪽에 위치시킴
        right_frame.pack(side='right')

        # 상단 라벨 생성
        top_label = tkinter.Label(top_frame, text='BACK LCK ANALYZER', font=('Arial', 16, 'bold'), bg='#322756', fg='white')
        top_label.pack(side='top', fill='x')



    def show_window2(self):
        # Clear window 1 widgets
        for widget in self.winfo_children():
             widget.destroy()

        self.title("픽창")
        self.geometry("{}x{}+100+50".format(window_width, window_height))
        self.resizable(False, False)

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)

        frame_top_width = window_width/3
        frame_top_height = 80

        frame_top1 = []
        for i in range(5):
            frame_top1.append(0)
            frame_top1[i] = tkinter.Frame(self, width = frame_top_width/5, height = frame_top_height, relief="solid", bg="blue",bd='1') 
            frame_top1[i].place(x=frame_top_width/5*i,y=0)



        frame_top2 = tkinter.Frame(self, width = frame_top_width, height = frame_top_height, relief="solid", bg="black") 
        frame_top2.place(x=frame_top_width,y=0)


        frame_top3 = tkinter.Frame(self, width = frame_top_width, height = frame_top_height, relief="solid", bg="red", bd='1') 
        frame_top3.place(x=frame_top_width*2,y=0)

        frame_top3 = []
        for i in range(5):
            frame_top3.append(0)
            frame_top3[i] = tkinter.Frame(self, width = frame_top_width/5, height = frame_top_height, relief="solid", bg="red",bd='1') 
            frame_top3[i].place(x=frame_top_width*2+frame_top_width/5*i,y=0)

        label_top=tkinter.Label(frame_top2, text="밴픽", font=font1, bg="black", foreground="white",anchor='center')
        label_top.place(relx='0.42',rely='0.25')



        frame_blueTeam_width = 350;
        frame_blueTeam_height = window_height - frame_top_height
        frame_redTeam_width = 350;
        frame_redTeam_height = window_height - frame_top_height
        frame_center_width = window_width - frame_blueTeam_width - frame_redTeam_width;
        frame_center_height = window_height - frame_top_height

        frame_blueTeam = tkinter.Frame(self, width = frame_blueTeam_width, height = frame_blueTeam_height, relief="solid", bg="blue")
        frame_blueTeam.place(x=0,y=frame_top_height)
        blue_combobox=ttk.Combobox(frame_blueTeam, height=10, values=("T1","Gen"), font="6",state='readonly')
        blue_combobox.pack()
        blue_combobox.set("Select Team")
        blue_combobox.place(x=10, y=10)



        frame_center = tkinter.Frame(self, width = frame_center_width, height = frame_blueTeam_height, relief="solid", bg="white")
        frame_center.place(x=frame_blueTeam_width, y=frame_top_height)

        frame_redTeam = tkinter.Frame(self, width = frame_redTeam_width, height = frame_redTeam_height, relief="solid", bg="red")
        frame_redTeam.place(x=frame_blueTeam_width + frame_center_width, y=frame_top_height)
        red_combobox=ttk.Combobox(frame_redTeam, height=10, values=("T1","Gen"), font="6",state='readonly')
        red_combobox.pack()
        red_combobox.set("Select Team")
        red_combobox.place(x=10, y=10)


        frame_member_width = 350;
        frame_member_height = (frame_blueTeam_height - 40)/5

        frame_blueTeamMember = []
 

        for i in range(5):
            frame_blueTeamMember.append(0)
            frame_blueTeamMember[i] = tkinter.LabelFrame(frame_blueTeam, width = frame_member_width, height = frame_member_height, relief="solid", bg="#7676EE", bd=1)
            frame_blueTeamMember[i].place(x=0, y=50+frame_member_height*i)

        frame_redTeamMember = []

        for i in range(5):
            frame_redTeamMember.append(0)
            frame_redTeamMember[i] = tkinter.LabelFrame(frame_redTeam, width = frame_member_width, height = frame_member_height, relief="solid", bg="#EE7676", bd=1)
            frame_redTeamMember[i].place(x=0, y=50+frame_member_height*i)

        def blue_combo_select(event):
            selected = blue_combobox.get()  # 콤보박스에서 선택한 값 가져오기
            if selected == "T1":  # T1 선택 시
                for i in range(5):
                    # T1 팀의 멤버 이름으로 변경
                    frame_blueTeamMember[i].config(text=T1[i])
            elif selected == "Gen":  # Gen 선택 시
                for i in range(5):
                # Gen 팀의 멤버 이름으로 변경
                    frame_blueTeamMember[i].config(text=Gen[i])

        blue_combobox.bind("<<ComboboxSelected>>", blue_combo_select)

        def red_combo_select(event):
            selected = red_combobox.get()  # 콤보박스에서 선택한 값 가져오기
            if selected == "T1":  # T1 선택 시
                for i in range(5):
                # T1 팀의 멤버 이름으로 변경
                    frame_redTeamMember[i].config(text=T1[i])
            elif selected == "Gen":  # Gen 선택 시
                for i in range(5):
                # Gen 팀의 멤버 이름으로 변경
                    frame_redTeamMember[i].config(text=Gen[i])

        red_combobox.bind("<<ComboboxSelected>>", red_combo_select)


        frame_center_search = tkinter.Frame(frame_center, width = frame_center_width-20, height= 30, relief="solid", bg="#111111", bd=1)
        frame_center_search.place(anchor="center", x=frame_center_width/2, y=25)

        text_search = tkinter.Text(frame_center_search, width=20, height=1, padx=1, pady=1, fg="#000000", bg="#EEEEEE", font="3")
        text_search.place(x=0,y=0)

        frame_center_champion = tkinter.Frame(frame_center, width = frame_center_width-20, height= frame_center_height-60, relief="solid", bg="#222222", bd=1)
        frame_center_champion.place(anchor="n", x=frame_center_width/2, y=50)

        def callback_champion_click(event):
                print(event.widget)
                a = str(event.widget['text']).split(".!")
                print(a)


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

        class Champion:
            def __init__(self, parent, image_path):
                self.image = Image.open(image_path)
                self.image_width = int(frame_champions_width)
                self.image_height = self.image_width

                self.image_resize = self.image.resize((self.image_width, self.image_height), Image.LANCZOS)
                self.img = ImageTk.PhotoImage(self.image_resize)

                self.frame_champion = tkinter.LabelFrame(parent, width=frame_champions_width, height=frame_champions_height, relief="solid", bg="white", highlightthickness=0, text='Aatrox')
                
                self.inframe = tkinter.Label(self.frame_champion, image=self.img, text="Aatrox", border=0)
                self.inframe.bind("<Button-1>", callback_champion_click)
                self.inframe.place(x=0, y=0)

            def name(self):
                return self.inframe['text']
            
            def __del__(self):
                self.inframe.destroy()
                self.frame_champion.destroy()

        line_num = -1
        for i in range(champion_num):
            if i % 6 == 0:
                frame_champions_line.append(0)
                line_num = line_num + 1
                frame_champions_line[line_num] = tkinter.Frame(scrollable_frame, width=frame_champions_width*6+5*7, height=frame_champions_height, bg="gray", bd=5)
                frame_champions_line[line_num].pack()

            champion = Champion(frame_champions_line[line_num], "Aatrox.png")
            champion.frame_champion.place(x=(i % 6)*frame_champions_width + (i % 6)*5, y=0)
            frame_champions.append(champion)



# Canvas 위젯에 Frame 삽입
        canvas_champions.create_window((0, 0), window=scrollable_frame, anchor='nw')

# 스크롤바에도 Canvas 위젯 연결
        scrollable_frame.bind('<Configure>', lambda e: canvas_champions.configure(scrollregion=canvas_champions.bbox('all')))

        def search():
    # Text 위젯에서 입력된 값 가져오기
            text = text_search.get("1.0", "end-1c")

    # 입력값을 포함하는 Frame만 저장하기
            filtered_text = []
            for champion in frame_champions:
                if text.lower() in champion.name().lower():
                    filtered_text.append(champion.name())

            print(filtered_text)  

    # 모든 Frame을 숨기기
            for champion in frame_champions:
                del champion
            for frame in frame_champions_line:
                frame.destroy()

            line_num=-1
    # 새로운 순서로 Frame을 보여주기
            for i in range(len(filtered_text)):
                if i%6==0:
                    frame_champions_line.append(0)
                    line_num = line_num+1
                    frame_champions_line[line_num] = tkinter.Frame(scrollable_frame, width = frame_champions_width*6+5*7, height= frame_champions_height, bg="gray", bd=5)
                    frame_champions_line[line_num].pack()
    # print(i)
                champion = Champion(frame_champions_line[line_num], "Aatrox.png")
                champion.frame_champion.place(x=(i % 6)*frame_champions_width + (i % 6)*5, y=0)
                frame_champions.append(champion)



# 검색 버튼 바인딩
        text_search.bind("<Return>", lambda event: search())

if __name__ == '__main__':
    app = BackBanpickAnalyzer()
    app.mainloop()


