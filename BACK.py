import tkinter
import tkinter.font
import numpy as np
from tkinter import ttk
from PIL import Image, ImageTk

# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='192.168.219.101', user='back', password='0000',
                       db='back', charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()
 
# STEP 4: SQL문 실행 및 Fetch
sql = "SELECT * FROM champion"
cur.execute(sql)
 
# 데이타 Fetch
champs = cur.fetchall()
champs = sorted(champs, key=lambda x:x[1])

# STEP 5: DB 연결 종료
con.close()

T1=["Zeus","Oner","Faker", "Gumayusi","Keria"]
Gen=["Doran","Peanut","Chovy","Peyz","Delight"]

window_width = 1280
window_height = 720

class BackBanpickAnalyzer(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.show_window1()


    def show_window1(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.title("BACK BANPICK ANALYZER")
        self.geometry('400x400+100+50')

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
        right_button = tkinter.Button(right_frame, text='ANALYZING TOOL', font=('Arial', 14), bg='#322756',command=self.show_window3)
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

        image_to_paste = None

        def callback_champion_click(event):
            global image_to_paste
            print(event.widget)
            a = str(event.widget['text']).split(".!")
            print(a)
                    # 선택된 챔피언 라벨에서 이름과 이미지 정보 가져오기
            selected_champion = event.widget
            champion_image = selected_champion.cget('image')

    # 챔피언 이미지를 image_to_paste 배열에 추가
            image_to_paste = champion_image
            if image_to_paste is not None:
                print("copy")

        def paste_image(event):
        # 클릭한 프레임에 이미지 붙여넣기
            global image_to_paste
            if image_to_paste is not None:
                event.widget.configure(image=image_to_paste)
            elif image_to_paste is None:
                print("NONE")

        self.title("픽창")
        self.geometry("{}x{}+100+50".format(window_width, window_height))
        self.resizable(False, False)

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)

        frame_top_width = window_width/3
        frame_top_height = 80

        frame_top1 = []
        label_top1 = []
        label_top3 = []

        for i in range(5):
            frame_top1.append(0)
            frame_top1[i] = tkinter.Frame(self, width = int(frame_top_width/5), height = int(frame_top_height), relief="solid", bg="blue",bd='1')
            frame_top1[i].place(x=frame_top_width/5*i,y=0)
            label_top1.append(0)
            label_top1[i] = tkinter.Label(frame_top1[i],bg="blue",anchor="center",width = int(frame_top_width/5),height=int(frame_top_height))
            label_top1[i].pack()
            label_top1[i].bind('<Button-1>',paste_image)


        frame_top2 = tkinter.Frame(self, width = frame_top_width, height = frame_top_height, relief="solid", bg="black") 
        frame_top2.place(x=frame_top_width,y=0)


        
        frame_top3 = []
        for i in range(5):
            frame_top3.append(0)
            frame_top3[i] = tkinter.Frame(self, width = frame_top_width/5, height = frame_top_height, relief="solid", bg="red",bd='1') 
            frame_top3[i].place(x=frame_top_width*2+frame_top_width/5*i,y=0)
            label_top3.append(0)
            label_top3[i] = tkinter.Label(frame_top3[i],bg="red",anchor="center",width = int(frame_top_width/5), height = frame_top_height)
            label_top3[i].pack()
            label_top3[i].bind('<Button-1>',paste_image)

        label_top=tkinter.Button(frame_top2, text="HOME", font=font1, bg="black", foreground="white",anchor='center',command=self.show_window1)
        label_top.place(relx='0.41',rely='0.12')


        frame_blueTeam_width = 350;
        frame_blueTeam_height = window_height - frame_top_height
        frame_redTeam_width = 350;
        frame_redTeam_height = window_height - frame_top_height
        frame_center_width = window_width - frame_blueTeam_width - frame_redTeam_width;
        frame_center_height = window_height - frame_top_height

        frame_blueTeam = tkinter.Frame(self, width = frame_blueTeam_width, height = frame_blueTeam_height, relief="solid", bg="blue")
        frame_blueTeam.place(x=0,y=frame_top_height)
        button_blueteam = tkinter.Button(frame_blueTeam,width=frame_blueTeam_width,height=frame_blueTeam_height,text='승리',bg='blue')
        button_blueteam.pack(side="right")
        blue_combobox=ttk.Combobox(frame_blueTeam, height=10, values=("T1","Gen"), font="6",state='readonly')
        blue_combobox.pack()
        blue_combobox.set("Select Team")
        blue_combobox.place(x=10, y=10)



        frame_center = tkinter.Frame(self, width = frame_center_width, height = frame_blueTeam_height, relief="solid", bg="white")
        frame_center.place(x=frame_blueTeam_width, y=frame_top_height)

        frame_redTeam = tkinter.Frame(self, width = frame_redTeam_width, height = frame_redTeam_height, relief="solid", bg="red")
        frame_redTeam.place(x=frame_blueTeam_width + frame_center_width, y=frame_top_height)
        button_redteam = tkinter.Button(frame_redTeam,width=frame_redTeam_width,height=frame_redTeam_height,bg='red')
        button_redteam.pack(side='right')
        red_combobox=ttk.Combobox(frame_redTeam, height=10, values=("T1","Gen"), font="6",state='readonly')
        red_combobox.pack()
        red_combobox.set("Select Team")
        red_combobox.place(x=10, y=10)


        frame_member_width = 350;
        frame_member_height = (frame_blueTeam_height - 40)/5

        frame_blueTeamMember = []
        label_blueTeamMember = []
        label_redTeamMember = []

        for i in range(5):
            frame_blueTeamMember.append(0)
            frame_blueTeamMember[i] = tkinter.LabelFrame(frame_blueTeam, width = frame_member_width, height = frame_member_height, relief="solid", bg="#7676EE", bd=1)
            frame_blueTeamMember[i].place(x=0, y=50+frame_member_height*i)
            label_blueTeamMember.append(0)
            label_blueTeamMember[i] = tkinter.Label(frame_blueTeamMember[i], width = frame_member_width,height=int(frame_member_height), relief="solid", bg="#7676EE", bd=0)
            label_blueTeamMember[i].pack()
            label_blueTeamMember[i].bind('<Button-1>',paste_image)


        frame_redTeamMember = []

        for i in range(5):
            frame_redTeamMember.append(0)
            frame_redTeamMember[i] = tkinter.LabelFrame(frame_redTeam, width = frame_member_width, height = frame_member_height, relief="solid", bg="#EE7676", bd=1)
            frame_redTeamMember[i].place(x=0, y=50+frame_member_height*i)
            label_redTeamMember.append(0)
            label_redTeamMember[i] = tkinter.Label(frame_redTeamMember[i], width = frame_member_width,height=int(frame_member_height), relief="solid", bg="#EE7676", bd=0)
            label_redTeamMember[i].pack()
            label_redTeamMember[i].bind('<Button-1>',paste_image)

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
        frame_champions = []
        frame_champions_line = []
        frame_champions_width= (frame_center_width-40-35)/6
        frame_champions_height= frame_champions_width
    

        class Champion:
            def __init__(self, parent, champion_name, image_path):
                self.image = Image.open(image_path)
                self.image_width = int(frame_champions_width)
                self.image_height = self.image_width

                self.image_resize = self.image.resize((self.image_width, self.image_height), Image.LANCZOS)
                self.img = ImageTk.PhotoImage(self.image_resize)

                self.frame_champion = tkinter.LabelFrame(parent, width=frame_champions_width, height=frame_champions_height+15, 
                                                         relief="solid", bg="white", highlightthickness=0, text=champion_name,
                                                         labelanchor="s", padx=0, pady=0, border=0)
                
                self.frame_champion.bind("<Button-1>", callback_champion_click)
                
                self.inframe = tkinter.Label(self.frame_champion, image=self.img, text=champion_name, 
                                             border=0, padx=0, pady=0)
                self.inframe.bind("<Button-1>", callback_champion_click)
                self.inframe.place(x=0, y=0)

            def name(self):
                return self.inframe['text']
            
            def __del__(self):
                try:
                    self.inframe.destroy()
                    self.frame_champion.destroy()
                except:
                    pass

        line_num = -1
        for i in range(len(champs)):
            if i % 6 == 0:
                frame_champions_line.append(0)
                line_num = line_num + 1
                frame_champions_line[line_num] = tkinter.Frame(scrollable_frame, width=frame_champions_width*6+5*7, height=frame_champions_height+15, bg="gray", bd=5)
                frame_champions_line[line_num].pack()

            champion = Champion(frame_champions_line[line_num], champs[i][1], "lck analyzing tool/champ/"+ champs[i][3] +".png")
            champion.frame_champion.place(x=(i % 6)*frame_champions_width + (i % 6)*5, y=0)
            frame_champions.append(champion)
        



# Canvas 위젯에 Frame 삽입
        canvas_champions.create_window((0, 0), window=scrollable_frame, anchor='nw')

# 스크롤바에도 Canvas 위젯 연결
        scrollable_frame.bind('<Configure>', lambda e: canvas_champions.configure(scrollregion=canvas_champions.bbox('all')))

        def search():
    # Text 위젯에서 입력된 값 가져오기
            text = text_search.get("1.0", "end-1c")
            text_search.delete("1.0", "end")
    # 입력값을 포함하는 Frame만 저장하기
            filtered_champs = []

            for i in champs:
                if text in i[1]:
                    filtered_champs.append(i)

            print(filtered_champs)  

    # 모든 Frame을 숨기기
            for champion in frame_champions:
                del champion
            for frame in frame_champions_line:
                frame.destroy()
            
            frame_champions_line.clear()


            line_num=-1
    # 새로운 순서로 Frame을 보여주기
            for i in range(len(filtered_champs)):
                if i%6==0:
                    frame_champions_line.append(0)
                    line_num = line_num+1
                    frame_champions_line[line_num] = tkinter.Frame(scrollable_frame, width = frame_champions_width*6+5*7, height= frame_champions_height+15, bg="gray", bd=5)
                    frame_champions_line[line_num].pack()

                champion = Champion(frame_champions_line[line_num], filtered_champs[i][1], "lck analyzing tool/champ/"+ filtered_champs[i][3] +".png")
                champion.frame_champion.place(x=(i % 6)*frame_champions_width + (i % 6)*5, y=0)
                frame_champions.append(champion)




# 검색 버튼 바인딩
        text_search.bind("<Return>", lambda event: search())

    def show_window3(self):
        # Clear window 1 widgets
        for widget in self.winfo_children():
            widget.destroy()

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)
        
        self.title("ANALYZING TOOL")
        self.geometry("{}x{}+100+50".format(400, 400))
        self.resizable(False, False)

 # 상단 프레임 생성
        analyize_top = tkinter.Frame(self, bg="#322756", width=400, height=50)
        analyize_top.pack(side="top", fill='both')

        # 좌 프레임 생성
        analyize_left = tkinter.Frame(self, bg='#322756', width=200, height=400, bd=3)
        analyize_left.pack(side='left')

        # 좌 프레임에 버튼 배치
        analyize_leftb = tkinter.Button(analyize_left, text='Champion', font=('Arial', 14), bg='#322756',command=self.show_window4)
        analyize_leftb.place(relx=0.5, rely=0.5, anchor='center')

        # 우 프레임 생성
        analyize_right = tkinter.Frame(self, bg='#322756', width=200, height=400)

        # 우 프레임에 버튼 배치
        analyize_rightb = tkinter.Button(analyize_right, text='Player', font=('Arial', 14), bg='#322756',command=self.show_window5)
        analyize_rightb.place(relx=0.5, rely=0.5, anchor='center')

        # 우 프레임을 윈도우 오른쪽에 위치시킴
        analyize_right.pack(side='right')

        label_top=tkinter.Button(analyize_top, text="HOME", font=font1, bg="black", foreground="white",anchor='center',command=self.show_window1)
        label_top.pack(side='top',fill='x')

    def show_window4(self):
        # Clear window 1 widgets
        for widget in self.winfo_children():
            widget.destroy()

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)
        
        self.title("ANALYZING TOOL")
        self.geometry("{}x{}+100+50".format(window_width, window_height))
        self.resizable(False, False)

        champ_top = tkinter.Frame(self, width= window_width, height = 100,bg='blue')
        champ_top.pack(side="top")

        champ_main = tkinter.Frame(self, width=window_width, height=620, bg='red')
        champ_main.pack(side="bottom")
        
        label_champ=tkinter.Button(champ_top, text="HOME", font=font1, bg="black", foreground="white",anchor='center',command=self.show_window3)
        label_champ.place(relx=0.8, rely=0.23)

        champ_treeview = ttk.Treeview(champ_main, columns=["champ",'W.R','B.R','P.R','K/D/A','SIDE Preference'],displaycolumns=["champ",'W.R','B.R','P.R','K/D/A','SIDE Preference'])
        champ_treeview.pack(ipadx=40)

        champ_treeview.column('#0',width=200)
        champ_treeview.heading("#0",text="champ")

        champ_treeview.column('#1',width=200)
        champ_treeview.heading("#1",text="W.R")

        champ_treeview.column('#2',width=200)
        champ_treeview.heading("#2",text="B.R")

        champ_treeview.column('#3',width=200)
        champ_treeview.heading("#3",text="P.R")

        champ_treeview.column('#4',width=200)
        champ_treeview.heading("#4",text="K/D/A")

        champ_treeview.column('#5',width=280)
        champ_treeview.heading("#5",text="SIDE Preference")

    def show_window5(self):
        # Clear window 1 widgets
        for widget in self.winfo_children():
            widget.destroy()

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)
        
        self.title("ANALYZING TOOL")
        self.geometry("{}x{}+100+50".format(window_width, window_height))
        self.resizable(False, False)

        player_top = tkinter.Frame(self, width= window_width, height = 100,bg='blue')
        player_top.pack(side="top")

        player_main = tkinter.Frame(self, width=window_width, height=620, bg='red')
        player_main.pack(side="bottom")
        
        label_player=tkinter.Button(player_top, text="HOME", font=font1, bg="black", foreground="white",anchor='center',command=self.show_window3)
        label_player.place(relx=0.8, rely=0.23)

        player_treeview = ttk.Treeview(player_main, columns=["TEAM","TOP",'JGL','MID','ADC','SPT'],displaycolumns=["TEAM","TOP",'JGL','MID','ADC','SPT'])
        player_treeview.pack()

        player_treeview.column('#0',width=80)
        player_treeview.heading("#0",text="TEAM")

        player_treeview.column('#1',width=240)
        player_treeview.heading("#1",text="TOP")

        player_treeview.column('#2',width=240)
        player_treeview.heading("#2",text="JGL")

        player_treeview.column('#3',width=240)
        player_treeview.heading("#3",text="MID")

        player_treeview.column('#4',width=240)
        player_treeview.heading("#4",text="ADC")

        player_treeview.column('#5',width=240)
        player_treeview.heading("#5",text="SPT")

    def show_window6(self):
        # Clear window 1 widgets
        for widget in self.winfo_children():
            widget.destroy()

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)
        
        self.title("ANALYZING TOOL")
        self.geometry("{}x{}+100+50".format(window_width, window_height))
        self.resizable(False, False)

if __name__ == '__main__':
    app = BackBanpickAnalyzer()
    app.mainloop()


