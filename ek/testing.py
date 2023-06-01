import tkinter
import tkinter.font
import numpy as np
from tkinter import ttk
from PIL import Image, ImageTk

# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='192.168.219.102', user='back', password='0000',
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


con = pymysql.connect(host='192.168.219.102', user='back', password='0000',
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
        #경기 정보 저장, 중복 불가능하도록 설정
        class Match_info:
            def __init__(self):
                self.blueteam_Name = None
                #탑, 정글, 미드, 원딜, 서폿순
                self.blueteam_Pick = [None] * 5
                self.blueteam_Ban = [None] * 5
            
                self.redteam_Name = None
                #탑, 정글, 미드, 원딜, 서폿순
                self.redteam_Pick = [None] * 5
                self.redteam_Ban = [None] * 5

                self.winnerTeam = None
                    
            #팀 이름 정보 설정
            def set_blueteam_Name(self, team_Name):
                self.blueteam_Name = team_Name
                self.printInfo()
            def set_redteam_Name(self, team_Name):
                self.redteam_Name = team_Name
                self.printInfo()
        
            #승리 팀 정보 설정
            def set_winnerTeam_Name(self, team_Name):
                self.winnerTeam = team_Name
                self.printInfo()

            #각 포지션 별 챔피언 정보 설정
            def set_blueteam_Pick(self, champion_Name, position):
                (type, location) = self.check_exist(champion_Name)
                if type!=False:
                    self.remove(type, location)

                self.blueteam_Pick[position] = champion_Name
                self.printInfo()
                
            def set_blueteam_Ban(self, champion_Name, position):
                (type, location) = self.check_exist(champion_Name)
                if type!=False:
                    self.remove(type, location)

                self.blueteam_Ban[position] = champion_Name
                self.printInfo()

            def set_redteam_Pick(self, champion_Name, position):
                (type, location) = self.check_exist(champion_Name)
                if type!=False:
                    self.remove(type, location)

                self.redteam_Pick[position] = champion_Name
                self.printInfo()

            def set_redteam_Ban(self, champion_Name, position):
                (type, location) = self.check_exist(champion_Name)
                if type!=False:
                    self.remove(type, location)

                self.redteam_Ban[position] = champion_Name
                self.printInfo()

            #이미 존재하는 챔피언을 삭제하는 함수
            def remove(self, type, location):
                if type=="blueTeam_ban":
                    self.blueteam_Ban[location] = None
                    label = label_blueBan[location]
                    label.image=''
                    label.config(image='')
                    
                elif type=="blueTeam_pick":
                    self.blueteam_Pick[location] = None
                    label = label_blueTeamMember[location]
                    label.image=''
                    label.config(image='')

                elif type=="redTeam_ban":
                    self.redteam_Ban[location] = None
                    label = label_redBan[location]
                    label.image=''
                    label.config(image='')
                    
                elif type=="redTeam_pick":
                    self.redteam_Pick[location] = None
                    label = label_redTeamMember[location]
                    label.image=''
                    label.config(image='')


            #챔피언이 이미 존재하는지 확인해주는 함수
            def check_exist(self, champion_name):
                if champion_name in self.blueteam_Ban:
                    return ("blueTeam_ban", self.blueteam_Ban.index(champion_name))
                elif champion_name in self.blueteam_Pick:
                    return ("blueTeam_pick", self.blueteam_Pick.index(champion_name))
                elif champion_name in self.redteam_Ban:
                    return ("redTeam_ban", self.redteam_Ban.index(champion_name))
                elif champion_name in self.redteam_Pick:
                    return ("redTeam_pick", self.redteam_Pick.index(champion_name))

                return(False, False)

            def checkAllSelected(self):
                if None in self.blueteam_Pick:
                    return False
                elif None in self.blueteam_Ban:
                    return False
                elif None in self.redteam_Pick:
                    return False
                elif None in self.redteam_Ban:
                    return False
                elif self.blueteam_Name is None:
                    return False
                elif self.redteam_Name is None:
                    return False
                elif self.winnerTeam is None:
                    return False

                return True 

            def printInfo(self):
                print("blue : ", self.blueteam_Name)
                for i in range(5):
                    print(str(i), " : ", self.blueteam_Pick[i], end="  ")
                print()
                
                print("blueTeam Ban : ", end=" ")
                for i in range(5):
                    print(self.blueteam_Ban[i], end="   ")
        
                print()
                print()
                print("red : ", self.redteam_Name)
                for i in range(5):
                    print(str(i), " : ", self.redteam_Pick[i], end="   ")
                print()

                print("redTeam Ban : ", end=" ")
                for i in range(5):
                    print(self.redteam_Ban[i], end="   ")
                print()

        #현재 경기 정보 저장 객체 생성
        now_match = Match_info()

        global name_selected_champion
        name_selected_champion = None
        global image_selected_champion
        image_selected_champion = None
        #챔피언 리스트에서 클릭시 해당 챔피언 정보 저장하기
        def champion_click(event):
            global name_selected_champion
            global image_selected_champion

            # 선택된 챔피언 라벨의 이미지 정보 가져오기
            widget_selected_champion = event.widget
            # print(widget_selected_champion)
            name_selected_champion = widget_selected_champion.cget('text')
            image_selected_champion = widget_selected_champion.cget('image')
            if image_selected_champion is not None and name_selected_champion is not None:
                # print("copy")
                print()

        # 클릭한 프레임에 이미지 붙여넣기
        def paste_image(event, type, location):
            global name_selected_champion
            global image_selected_champion
            # 선택한 선수의 픽을 선택한 이미지로 설정하기
            if image_selected_champion is not None:
                #선택한 라벨에따라 현재 경기 정보 설정
                if type == "blueTeam_ban":
                    now_match.set_blueteam_Ban(name_selected_champion, location)
                elif type == "blueTeam_pick":
                    now_match.set_blueteam_Pick(name_selected_champion, location)
                elif type == "redTeam_ban":
                    now_match.set_redteam_Ban(name_selected_champion, location)
                elif type == "redTeam_pick":
                    now_match.set_redteam_Pick(name_selected_champion, location)
                    
                event.widget.configure(image=image_selected_champion)
                image_selected_champion = None

            elif image_selected_champion is None:
                event.widget.image=''
                event.widget.config(image='')
                now_match.remove(type, location)
            


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
            label_blueBan[i].bind('<Button-1>', lambda event, idx=i: paste_image(event, "blueTeam_ban", idx))

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
            label_redBan[i].bind('<Button-1>', lambda event, idx=i: paste_image(event, "redTeam_ban", idx))

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
        frame_blueTeam.place(x=0, y=height_frame_top)

        #승리팀을 정하는 버튼 - 버튼을 누르면 해당 팀이 승리팀이 되고, 해당 게임의 정보가 데이터베이스에 저장된다.
        button_blueteam = tkinter.Button(frame_blueTeam, width=width_frame_blueTeam, height=height_frame_blueTeam, text='승리', bg='blue')
        button_blueteam.pack(side="left")

        combobox_blueteam=ttk.Combobox(frame_blueTeam, height=10, values=(list(team_dic.keys())), font="6",state='readonly')
        combobox_blueteam.pack()
        combobox_blueteam.set("Select Team")
        combobox_blueteam.place(x=10, y=10)

        #블루팀 콤보박스에서 임의의 팀을 선택시 해당 팀의 팀원 이름을 labelframe에 출력시키는 함수
        def blueteam_combobox_select(event):
            selected_team = combobox_blueteam.get()  # 콤보박스에서 선택한 값 가져오기
            
            #선택한 팀에 따라 팀원 labelframe에 이름 출력
            for i in range(5):
                frame_blueTeamMember[i].config(text=team_dic[selected_team][i])
            
            now_match.set_blueteam_Name(selected_team)

        combobox_blueteam.bind("<<ComboboxSelected>>", blueteam_combobox_select)

        width_frame_member = 350;
        height_frame_member = (height_frame_blueTeam - 40)/5

        #팀 멤버 5명을 위한 frame, label
        frame_blueTeamMember = []
        label_blueTeamMember = []

        #5개의 label, frame 위치 설정
        for i in range(5):
            frame_blueTeamMember.append(0)
            frame_blueTeamMember[i] = tkinter.LabelFrame(frame_blueTeam, width = width_frame_member, height = height_frame_member, relief="solid", bg="#7676EE", bd=1)
            frame_blueTeamMember[i].place(x=0, y=50+height_frame_member*i)

            label_blueTeamMember.append(0)
            label_blueTeamMember[i] = tkinter.Label(frame_blueTeamMember[i], width = width_frame_member,height=int(height_frame_member), relief="solid", bg="#7676EE", bd=0)
            label_blueTeamMember[i].pack()
            label_blueTeamMember[i].bind('<Button-1>', lambda event, idx=i: paste_image(event, "blueTeam_pick", idx))

        #redTeam Pick Frame
        width_frame_redTeam = 350;
        height_frame_redTeam = height_window_banPick - height_frame_top

        frame_redTeam = tkinter.Frame(self, width = width_frame_redTeam, height = height_frame_redTeam, relief="solid", bg="red")
        frame_redTeam.place(x=width_window - width_frame_redTeam, y=height_frame_top)

        button_redteam = tkinter.Button(frame_redTeam,width=width_frame_redTeam,height=height_frame_redTeam,bg='red')
        button_redteam.pack(side='right')

        combobox_redteam=ttk.Combobox(frame_redTeam, height=10, values=(list(team_dic.keys())), font="6",state='readonly')
        combobox_redteam.pack()
        combobox_redteam.set("Select Team")
        combobox_redteam.place(x=10, y=10)
        
        #레드팀 콤보박스에서 임의의 팀을 선택시 해당 팀의 팀원 이름을 labelframe에 출력시키는 함수
        def redteam_combobox_select(event):
            selected_team = combobox_redteam.get()  # 콤보박스에서 선택한 값 가져오기
            
            #선택한 팀에 따라 팀원 labelframe에 이름 출력
            for i in range(5):
                frame_redTeamMember[i].config(text=team_dic[selected_team][i])
            now_match.set_redteam_Name(selected_team)

        combobox_redteam.bind("<<ComboboxSelected>>", redteam_combobox_select)

        #팀 멤버 5명을 위한 frame, label
        label_redTeamMember = []
        frame_redTeamMember = []

        #5개의 label, frame 위치 설정
        for i in range(5):
            frame_redTeamMember.append(0)
            frame_redTeamMember[i] = tkinter.LabelFrame(frame_redTeam, width = width_frame_member, height = height_frame_member, relief="solid", bg="#EE7676", bd=1)
            frame_redTeamMember[i].place(x=0, y=50+height_frame_member*i)

            label_redTeamMember.append(0)
            label_redTeamMember[i] = tkinter.Label(frame_redTeamMember[i], width = width_frame_member,height=int(height_frame_member), relief="solid", bg="#EE7676", bd=0)
            label_redTeamMember[i].pack()
            label_redTeamMember[i].bind('<Button-1>', lambda event, idx=i: paste_image(event, "redTeam_pick", idx))

        
        #Center Frame(champion list Frame)
        width_frame_center = width_window_banPick - width_frame_blueTeam*2;
        height_frame_center = height_window_banPick - height_frame_top

        frame_center = tkinter.Frame(self, width = width_frame_center, height = height_frame_blueTeam, relief="solid", bg="white")
        frame_center.place(x=width_frame_blueTeam, y=height_frame_top)

        frame_champion_search = tkinter.Frame(frame_center, width = width_frame_center-20, height= 30, relief="solid", bg="#111111", bd=1)
        frame_champion_search.place(anchor="center", x=width_frame_center/2, y=25)

        text_champion_search = tkinter.Text(frame_champion_search, width=20, height=1, padx=1, pady=1, fg="#000000", bg="#EEEEEE", font="3")
        text_champion_search.place(x=0,y=0)

        def search():
            # Text 위젯에서 입력된 값 가져오기
            text = text_champion_search.get("1.0", "end-1c")
            text_champion_search.delete("1.0", "end")

            # 입력값을 포함하는 Frame만 저장하기
            filtered_champs = []
            for i in champion_data:
                if text in i[1]:
                    filtered_champs.append(i)

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
                    frame_champions_line[line_num] = tkinter.Frame(frame_scrollable, width = width_frame_champions*6+5*7, height= height_frame_champions+15, bg="gray", bd=5)
                    frame_champions_line[line_num].pack()

                champion = Champion(frame_champions_line[line_num], filtered_champs[i][1], "lck analyzing tool/champ/"+ filtered_champs[i][3] +".png")
                champion.frame_champion.place(x=(i % 6)*width_frame_champions + (i % 6)*5, y=0)
                frame_champions.append(champion)

        # 검색 버튼 바인딩
        text_champion_search.bind("<Return>", lambda event: search())

        #######챔피언 고르는 Frame 설정(scrollbar)
        frame_champion_list = tkinter.Frame(frame_center, width = width_frame_center-20, height= height_frame_center-60, relief="solid", bg="#222222", bd=1)
        frame_champion_list.place(anchor="n", x=width_frame_center/2, y=50)

        # 스크롤바 생성
        scrollbar_champion = tkinter.Scrollbar(frame_champion_list, orient='vertical')
        scrollbar_champion.pack(side='right', fill='y')

        # 스크롤 가능한 Canvas 위젯 생성
        canvas_champions = tkinter.Canvas(frame_champion_list, yscrollcommand=scrollbar_champion.set, width=width_frame_center-40, height=height_frame_center-60, highlightthickness=0)
        canvas_champions.pack(side='left', fill='both', expand=True)

        # 스크롤바와 Canvas 위젯 연결
        scrollbar_champion.config(command=canvas_champions.yview)

        # 스크롤 가능한 영역으로 사용할 Frame 생성
        frame_scrollable = tkinter.Frame(canvas_champions)

        # Frame에 내용 삽입
        width_frame_champions= (width_frame_center-40-35)/6
        height_frame_champions= width_frame_champions

        frame_champions = []
        frame_champions_line = []

        class Champion:
            def __init__(self, parent, champion_name, image_path):
                self.image = Image.open(image_path)
                self.width_image = int(width_frame_champions)
                self.height_image = self.width_image

                self.image_resize = self.image.resize((self.width_image, self.height_image), Image.LANCZOS)
                self.img = ImageTk.PhotoImage(self.image_resize)

                self.frame_champion = tkinter.LabelFrame(parent, width=width_frame_champions, height=height_frame_champions+15, 
                                                         relief="solid", bg="white", highlightthickness=0, text=champion_name,
                                                         labelanchor="s", padx=0, pady=0, border=0)
                
                self.frame_champion.bind("<Button-1>", champion_click)
                
                self.inframe = tkinter.Label(self.frame_champion, image=self.img, text=image_path.split('/')[-1].split('.')[0], 
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
                frame_champions_line[line_num] = tkinter.Frame(frame_scrollable, width=width_frame_champions*6+5*7, height=height_frame_champions+15, bg="gray", bd=5)
                frame_champions_line[line_num].pack()

            champion = Champion(frame_champions_line[line_num], champion_data[i][1], "lck analyzing tool/champ/"+ champion_data[i][3] +".png")
            champion.frame_champion.place(x=(i % 6)*width_frame_champions + (i % 6)*5, y=0)
            frame_champions.append(champion)
        

        # Canvas 위젯에 Frame 삽입
        canvas_champions.create_window((0, 0), window=frame_scrollable, anchor='nw')

        # 스크롤바에도 Canvas 위젯 연결
        frame_scrollable.bind('<Configure>', lambda e: canvas_champions.configure(scrollregion=canvas_champions.bbox('all')))


    def show_window_analyze(self):
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
        analyize_leftb = tkinter.Button(analyize_left, text='Champion', font=('Arial', 14), bg='#322756',command=self.show_window_analyze_champion)
        analyize_leftb.place(relx=0.5, rely=0.5, anchor='center')

        # 우 프레임 생성
        analyize_right = tkinter.Frame(self, bg='#322756', width=200, height=400)

        # 우 프레임에 버튼 배치
        analyize_rightb = tkinter.Button(analyize_right, text='Player', font=('Arial', 14), bg='#322756', command=self.show_window_player)
        analyize_rightb.place(relx=0.5, rely=0.5, anchor='center')

        # 우 프레임을 윈도우 오른쪽에 위치시킴
        analyize_right.pack(side='right')

        label_top=tkinter.Button(analyize_top, text="HOME", font=font1, bg="black", foreground="white",anchor='center',command=self.show_window_main)
        label_top.pack(side='top',fill='x')

    def show_window_analyze_champion(self):
        # Clear window 1 widgets
        for widget in self.winfo_children():
            widget.destroy()

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)
        
        self.title("ANALYZING TOOL")
        self.geometry("{}x{}+100+50".format(width_window, height_window))
        self.resizable(False, False)

        champ_top = tkinter.Frame(self, width= width_window, height = 100,bg='blue')
        champ_top.pack(side="top")

        champ_main = tkinter.Frame(self, width=width_window, height=620, bg='red')
        champ_main.pack(side="bottom")
        
        label_champ=tkinter.Button(champ_top, text="HOME", font=font1, bg="black", foreground="white",anchor='center',command=self.show_window_analyze)
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

    def show_window_player(self):
        # Clear window 1 widgets
        for widget in self.winfo_children():
            widget.destroy()

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)
        
        self.title("ANALYZING TOOL")
        self.geometry("{}x{}+100+50".format(width_window, height_window))
        self.resizable(False, False)

        player_top = tkinter.Frame(self, width= width_window, height = 100,bg='blue')
        player_top.pack(side="top")

        player_main = tkinter.Frame(self, width=width_window, height=620, bg='red')
        player_main.pack(side="bottom")
        
        label_player=tkinter.Button(player_top, text="HOME", font=font1, bg="black", foreground="white",anchor='center',command=self.show_window_analyze)
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
        self.geometry("{}x{}+100+50".format(width_window, height_window))
        self.resizable(False, False)


if __name__ == '__main__':
    app = BackBanpickAnalyzer()
    app.mainloop()


