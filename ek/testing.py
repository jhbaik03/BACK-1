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
champion_data = cur.fetchall() #(id, kor_name, eng_name, img_name)
champion_data = sorted(champion_data, key=lambda x:x[1])
# STEP 5: DB 연결 종료
con.close()


con = pymysql.connect(host='192.168.219.101', user='back', password='0000',
                       db='back', charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()

sql = "SELECT table_team.Team_Initial, player.Player_ID, player.Player_Name, player.Position\
    FROM table_team \
    INNER JOIN 2023_lck_team_player ON 2023_lck_team_player.Team_ID=table_team.Team_ID\
    INNER JOIN player ON 2023_lck_team_player.Player_ID=player.Player_ID AND player.Main=0"
cur.execute(sql)

team_member = cur.fetchall()
team_member = sorted(team_member, key=lambda x:x[1])

team_dic = {}
for item in team_member:
    team = item[0]
    player = item[2]
    team_dic.setdefault(team, []).append(player)

#(team:(member_list))
team_dic = {team: tuple(players) for team, players in team_dic.items()}

con.close()

# 픽밴툴, 분석툴 가로세로 크기
width_window = 1280
height_window = 720

#전체 class
class BackBanpickAnalyzer(tkinter.Tk):
    #BackBanpickAnalyzer 생성자, 시작화면 출력(show_window_main)
    def __init__(self):
        super().__init__()
        self.show_window_main()

    #메인화면 출력
    def show_window_main(self):
        for widget in self.winfo_children():
            widget.destroy()

        #메인화면 크기 지정
        width_mainWindow= 400
        height_mainWindow = 400
        
        #제목 폰트 지정
        font_title=('Arial', 16, 'bold')

        self.title("BACK BANPICK ANALYZER")
        self.geometry("{}x{}+100+50".format(width_mainWindow, height_mainWindow))

        # 상단 프레임 생성
        frame_top = tkinter.Frame(self, bg="#322756", width=400, height=50)
        frame_top.pack(side="top", fill='both')

        # 제목(BACK LCK ANALYZER) 라벨 생성, 상단에 출력
        label_title = tkinter.Label(frame_top, text='BACK LCK ANALYZER', font=font_title, bg='#322756', fg='white')
        label_title.pack(side='top', fill='x')

        # 좌 프레임 생성
        frame_left = tkinter.Frame(self, bg='#322756', width=200, height=400, bd=3)
        frame_left.pack(side='left')

        # 좌 프레임에 버튼 배치, 버튼 누르면 밴픽화면 출력
        button_toBanPickWindow = tkinter.Button(frame_left, text='BANPICK TOOL', font=('Arial', 14), bg='#322756',command=self.show_window_banPick)
        button_toBanPickWindow.place(relx=0.5, rely=0.5, anchor='center')

        # 우 프레임 생성
        frame_right = tkinter.Frame(self, bg='#322756', width=200, height=400)
        frame_right.pack(side='right')

        # 우 프레임에 버튼 배치, 버튼 누르면 분석화면 출력
        button_toAnalyzeWindow = tkinter.Button(frame_right, text='ANALYZING TOOL', font=('Arial', 14), bg='#322756',command=self.show_window_analyze)
        button_toAnalyzeWindow.place(relx=0.5, rely=0.5, anchor='center')

    #픽밴화면 출력
    def show_window_banPick(self):
        image_selected_champion = None
        #챔피언 리스트에서 클릭시 해당 챔피언 정보 저장하기
        def champion_click(event):
            global image_selected_champion

            # 선택된 챔피언 라벨의 이미지 정보 가져오기
            widget_selected_champion = event.widget
            image_selected_champion = widget_selected_champion.cget('image')
            if image_selected_champion is not None:
                print("copy")

        # 클릭한 프레임에 이미지 붙여넣기
        def paste_image(event):
            global image_selected_champion

            # 선택한 선수의 픽을 선택한 이미지로 설정하기
            if image_selected_champion is not None:
                event.widget.configure(image=image_selected_champion)
            elif image_selected_champion is None:
                print("NONE")

        #다른 화면 전부 삭제
        for widget in self.winfo_children():
             widget.destroy()

        #내용 폰트 설정
        font_contents=tkinter.font.Font(family="맑은 고딕", size=20)
        #밴픽화면 크기
        width_window_banPick = 1280
        height_window_banPick = 720

        #밴픽화면 설정
        self.title("BANPICK")
        self.geometry("{}x{}+100+50".format(width_window_banPick, height_window_banPick))
        self.resizable(False, False)

        width_frame_top = int(width_window_banPick/3)
        height_frame_top = 80

        #블루팀 밴 frame 생성
        frame_blueBan = []
        label_blueBan = []
        for i in range(5):
            frame_blueBan.append(0)
            frame_blueBan[i] = tkinter.Frame(self, width = int(width_frame_top/5), height = height_frame_top, relief="solid", bg="blue", bd='1')
            frame_blueBan[i].place(x=int(width_frame_top/5)*i,y=0)

            label_blueBan.append(0)
            label_blueBan[i] = tkinter.Label(frame_blueBan[i], bg="blue", anchor="center", width = int(width_frame_top/5), height = height_frame_top)
            label_blueBan[i].pack()
            label_blueBan[i].bind('<Button-1>',paste_image)

        #레드팀 밴 frame 생성
        frame_redBan = []
        label_redBan = []
        for i in range(5):
            frame_redBan.append(0)
            frame_redBan[i] = tkinter.Frame(self, width = width_frame_top/5, height = height_frame_top, relief="solid", bg="red", bd='1') 
            frame_redBan[i].place(x = width_frame_top*2 + int(width_frame_top/5)*i,y=0)

            label_redBan.append(0)
            label_redBan[i] = tkinter.Label(frame_redBan[i], bg="red", anchor="center",width = int(width_frame_top/5), height = height_frame_top)
            label_redBan[i].pack()
            label_redBan[i].bind('<Button-1>',paste_image)

        #상단 프레임 설정
        frame_top_center = tkinter.Frame(self, width = width_frame_top, height = height_frame_top, relief="solid", bg="black") 
        frame_top_center.place(x=width_frame_top,y=0)

        #메인화면으로 돌아가는 버튼 생성
        button_toMain=tkinter.Button(frame_top_center, text="HOME", font=font_contents, bg="black", foreground="white",anchor='center',command=self.show_window_main)
        button_toMain.place(relx='0.41',rely='0.12')

        #blueTeam Pick Frame
        width_frame_blueTeam = 350;
        height_frame_blueTeam = height_window_banPick - height_frame_top

        frame_blueTeam = tkinter.Frame(self, width = width_frame_blueTeam, height = height_frame_blueTeam, relief="solid", bg="blue")
        frame_blueTeam.place(x=0,y=height_frame_top)

        button_blueteam = tkinter.Button(frame_blueTeam, width=width_frame_blueTeam, height=height_frame_blueTeam, text='승리', bg='blue')
        button_blueteam.pack(side="left")

        combobox_blueteam=ttk.Combobox(frame_blueTeam, height=10, values=(list(team_dic.keys())), font="6",state='readonly')
        combobox_blueteam.pack()
        combobox_blueteam.set("Select Team")
        combobox_blueteam.place(x=10, y=10)

        def blue_combo_select(event):
            selected = combobox_blueteam.get()  # 콤보박스에서 선택한 값 가져오기
            for i in range(5):
                frame_blueTeamMember[i].config(text=team_dic[selected][i])
        
        combobox_blueteam.bind("<<ComboboxSelected>>", blue_combo_select)

        #Center Frame(champion list Frame)
        frame_center_width = width_window_banPick - width_frame_blueTeam*2;
        frame_center_height = height_window_banPick - height_frame_top

        frame_center = tkinter.Frame(self, width = frame_center_width, height = height_frame_blueTeam, relief="solid", bg="white")
        frame_center.place(x=width_frame_blueTeam, y=height_frame_top)

        frame_center_search = tkinter.Frame(frame_center, width = frame_center_width-20, height= 30, relief="solid", bg="#111111", bd=1)
        frame_center_search.place(anchor="center", x=frame_center_width/2, y=25)

        text_search = tkinter.Text(frame_center_search, width=20, height=1, padx=1, pady=1, fg="#000000", bg="#EEEEEE", font="3")
        text_search.place(x=0,y=0)

        frame_center_champion = tkinter.Frame(frame_center, width = frame_center_width-20, height= frame_center_height-60, relief="solid", bg="#222222", bd=1)
        frame_center_champion.place(anchor="n", x=frame_center_width/2, y=50)

        #redTeam Pick Frame
        width_frame_redTeam = 350;
        height_frame_redTeam = height_window_banPick - height_frame_top

        frame_redTeam = tkinter.Frame(self, width = width_frame_redTeam, height = height_frame_redTeam, relief="solid", bg="red")
        frame_redTeam.place(x=width_frame_blueTeam + frame_center_width, y=height_frame_top)

        button_redteam = tkinter.Button(frame_redTeam,width=width_frame_redTeam,height=height_frame_redTeam,bg='red')
        button_redteam.pack(side='right')

        combobox_redteam=ttk.Combobox(frame_redTeam, height=10, values=(list(team_dic.keys())), font="6",state='readonly')
        combobox_redteam.pack()
        combobox_redteam.set("Select Team")
        combobox_redteam.place(x=10, y=10)
        
        def red_combo_select(event):
            selected = combobox_redteam.get()  # 콤보박스에서 선택한 값 가져오기
            for i in range(5):
                frame_redTeamMember[i].config(text=team_dic[selected][i])
        combobox_redteam.bind("<<ComboboxSelected>>", red_combo_select)


        frame_member_width = 350;
        frame_member_height = (height_frame_blueTeam - 40)/5

        frame_blueTeamMember = []
        label_blueTeamMember = []
        for i in range(5):
            frame_blueTeamMember.append(0)
            frame_blueTeamMember[i] = tkinter.LabelFrame(frame_blueTeam, width = frame_member_width, height = frame_member_height, relief="solid", bg="#7676EE", bd=1)
            frame_blueTeamMember[i].place(x=0, y=50+frame_member_height*i)

            label_blueTeamMember.append(0)
            label_blueTeamMember[i] = tkinter.Label(frame_blueTeamMember[i], width = frame_member_width,height=int(frame_member_height), relief="solid", bg="#7676EE", bd=0)
            label_blueTeamMember[i].pack()
            label_blueTeamMember[i].bind('<Button-1>',paste_image)

        label_redTeamMember = []
        frame_redTeamMember = []
        for i in range(5):
            frame_redTeamMember.append(0)
            frame_redTeamMember[i] = tkinter.LabelFrame(frame_redTeam, width = frame_member_width, height = frame_member_height, relief="solid", bg="#EE7676", bd=1)
            frame_redTeamMember[i].place(x=0, y=50+frame_member_height*i)

            label_redTeamMember.append(0)
            label_redTeamMember[i] = tkinter.Label(frame_redTeamMember[i], width = frame_member_width,height=int(frame_member_height), relief="solid", bg="#EE7676", bd=0)
            label_redTeamMember[i].pack()
            label_redTeamMember[i].bind('<Button-1>',paste_image)


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
                
                self.frame_champion.bind("<Button-1>", champion_click)
                
                self.inframe = tkinter.Label(self.frame_champion, image=self.img, text=champion_name, 
                                             border=0, padx=0, pady=0)
                self.inframe.bind("<Button-1>", champion_click)
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
        for i in range(len(champion_data)):
            if i % 6 == 0:
                frame_champions_line.append(0)
                line_num = line_num + 1
                frame_champions_line[line_num] = tkinter.Frame(scrollable_frame, width=frame_champions_width*6+5*7, height=frame_champions_height+15, bg="gray", bd=5)
                frame_champions_line[line_num].pack()

            champion = Champion(frame_champions_line[line_num], champion_data[i][1], "lck analyzing tool/champ/"+ champion_data[i][3] +".png")
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

            for i in champion_data:
                if text in i[1]:
                    filtered_champs.append(i)

            print(filtered_champs)  

            # 모든 Frame을 숨기기
            for champion in frame_champions:
                del champion
            for frame in frame_champions_line:
                frame.destroy()
            
            frame_champions_line.clear()

            # 새로운 순서로 Frame을 보여주기
            line_num=-1
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

    def show_window_analyze(self):
        # Clear window 1 widgets
        for widget in self.winfo_children():
            widget.destroy()

        #내용 폰트 설정
        font_contents=tkinter.font.Font(family="맑은 고딕", size=20)
        #밴픽화면 크기
        width_window_analyze = 1280
        height_window_analyze = 720

        self.title("픽창")
        self.geometry("{}x{}+100+50".format(width_window_analyze, height_window_analyze))
        self.resizable(False, False)

        label_top=tkinter.Button(self, text="HOME", font=font_contents, bg="black", foreground="white",anchor='center',command=self.show_window_main)
        label_top.place(relx='0.41',rely='0.12')


if __name__ == '__main__':
    app = BackBanpickAnalyzer()
    app.mainloop()


