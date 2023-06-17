import tkinter
import tkinter.font
from tkinter import ttk
from PIL import Image, ImageTk

# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='172.30.1.18', user='back', password='0000',
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


con = pymysql.connect(host='172.30.1.18', user='back', password='0000',
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

                self.winnerTeam_Name = None

                self.blueteam_KDA = [[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]
                self.redteam_KDA = [[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]
                    
            #팀 이름 정보 설정
            def set_blueteam_Name(self, team_Name):
                self.blueteam_Name = team_Name
                self.printInfo()
            def set_redteam_Name(self, team_Name):
                self.redteam_Name = team_Name
                self.printInfo()
        
            #승리 팀 정보 설정
            def set_winnerTeam_Name(self, team_Name):
                self.winnerTeam_Name = team_Name
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
                elif self.winnerTeam_Name is None:
                    return False

                return True 

            def printInfo(self):
                print("blue : ", self.blueteam_Name)
                for i in range(5):
                    print(str(i), " : ", self.blueteam_Pick[i], end="  ")
                    print(self.blueteam_KDA[i][0], self.blueteam_KDA[i][1],self.blueteam_KDA[i][2])
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
                
                print("winner team : ", self.winnerTeam_Name)
                print()

            def insert_db(self):                
                conn = pymysql.connect(host='172.30.1.18', user='back', password='0000',
                       db='back', charset='utf8')

                sql_pick_and_KDA = """INSERT INTO match_result (blueTeamName, blueTopChampion, blueTopKill, blueTopDeath, blueTopAssist,
                    blueJglChampion, blueJglKill, blueJglDeath, blueJglAssist,
                    blueMidChampion, blueMidKill, blueMidDeath, blueMidAssist,
                    blueBtmChampion, blueBtmKill, blueBtmDeath, blueBtmAssist,
                    blueSupChampion, blueSupKill, blueSupDeath, blueSupAssist,
                    redTeamName, redTopChampion, redTopKill, redTopDeath, redTopAssist,
                    redJglChampion, redJglKill, redJglDeath, redJglAssist,
                    redMidChampion, redMidKill, redMidDeath, redMidAssist,
                    redBtmChampion, redBtmKill, redBtmDeath, redBtmAssist,
                    redSupChampion, redSupKill, redSupDeath, redSupAssist, winTeamName) 
                    VALUES (%s, %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, 
                    %s, %s, %s, %s, 
                    %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s)"""
                
                sql_ban = """INSERT INTO match_ban (matchID, blueteam_ban1, blueteam_ban2, blueteam_ban3, blueteam_ban4, 
                    blueteam_ban5, redteam_ban1, redteam_ban2, redteam_ban3, redteam_ban4, redteam_ban5) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                with conn:
                    with conn.cursor() as cur:
                        cur.execute(sql_pick_and_KDA, (self.blueteam_Name, self.blueteam_Pick[0], self.blueteam_KDA[0][0], self.blueteam_KDA[0][1], self.blueteam_KDA[0][2],
                                          self.blueteam_Pick[1], self.blueteam_KDA[1][0], self.blueteam_KDA[1][1], self.blueteam_KDA[1][2],
                                          self.blueteam_Pick[2], self.blueteam_KDA[2][0], self.blueteam_KDA[2][1], self.blueteam_KDA[2][2],
                                          self.blueteam_Pick[3], self.blueteam_KDA[3][0], self.blueteam_KDA[3][1], self.blueteam_KDA[3][2],
                                          self.blueteam_Pick[4], self.blueteam_KDA[4][0], self.blueteam_KDA[4][1], self.blueteam_KDA[4][2],
                                          self.redteam_Name, self.redteam_Pick[0], self.redteam_KDA[0][0], self.redteam_KDA[0][1], self.redteam_KDA[0][2],
                                          self.redteam_Pick[1], self.redteam_KDA[1][0], self.redteam_KDA[1][1], self.redteam_KDA[1][2],
                                          self.redteam_Pick[2], self.redteam_KDA[2][0], self.redteam_KDA[2][1], self.redteam_KDA[2][2],
                                          self.redteam_Pick[3], self.redteam_KDA[3][0], self.redteam_KDA[3][1], self.redteam_KDA[3][2],
                                          self.redteam_Pick[4], self.redteam_KDA[4][0], self.redteam_KDA[4][1], self.redteam_KDA[4][2],
                                          self.winnerTeam_Name))
                        conn.commit()

                    last_insert_id = cur.lastrowid

                    with conn.cursor() as cur:
                        # matchID 값을 다른 테이블에 사용
                        cur.execute(sql_ban, (last_insert_id, self.blueteam_Ban[0],self.blueteam_Ban[1],self.blueteam_Ban[2],self.blueteam_Ban[3],self.blueteam_Ban[4],
                                          self.redteam_Ban[0],self.redteam_Ban[1],self.redteam_Ban[2],self.redteam_Ban[3],self.redteam_Ban[4]))
                        conn.commit()

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
        button_blueteam = tkinter.Button(frame_blueTeam, width=width_frame_blueTeam, height=height_frame_blueTeam, text='승리', bg='blue',command=lambda : self.show_window_info(now_match))
        button_blueteam.pack(side="left")

        combobox_blueteam=ttk.Combobox(frame_blueTeam, height=10, values=(list(team_dic.keys())), font="6",state='readonly')
        combobox_blueteam.pack()
        combobox_blueteam.set("Select Team")
        combobox_blueteam.place(x=10, y=10)

        #블루팀 콤보박스에서 임의의 팀을 선택시 해당 팀의 팀원 이름을 labelframe에 출력시키는 함수
        def blueteam_combobox_select(event):
            selected_team = combobox_blueteam.get()  # 콤보박스에서 선택한 값 가져오기
            
            #선택한 팀에 따라 팀원 labelframe에 이름 출력
                        #선택한 팀에 따라 팀원 labelframe에 이름 출력
            for i in range(5):
                frame_blueTeamMember[i].config(text=team_dic[selected_team][i])
            if combobox_redteam.get() == selected_team:
                combobox_redteam.set('Select Team')
                for i in range(5):
                    frame_redTeamMember[i].config(text="")
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

        button_redteam = tkinter.Button(frame_redTeam,width=width_frame_redTeam,height=height_frame_redTeam,bg='red',command=lambda : self.show_window_info(now_match))
        button_redteam.pack(side='right')

        combobox_redteam=ttk.Combobox(frame_redTeam, height=10, values=(list(team_dic.keys())), font="6",state='readonly')
        combobox_redteam.pack()
        combobox_redteam.set("Select Team")
        combobox_redteam.place(x=10, y=10)
        
        #레드팀 콤보박스에서 임의의 팀을 선택시 해당 팀의 팀원 이름을 labelframe에 출력시키는 함수
        def redteam_combobox_select(event):
            selected = combobox_redteam.get()  # 콤보박스에서 선택한 값 가져오기
            
            #선택한 팀에 따라 팀원 labelframe에 이름 출력
            for i in range(5):
                frame_redTeamMember[i].config(text=team_dic[selected][i])
            if combobox_blueteam.get() == selected:
                combobox_blueteam.set("Select Team")
                for i in range(5):
                    frame_blueTeamMember[i].config(text="")
            now_match.set_redteam_Name(selected)

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

    def show_window_info(self, match_info):
        # Clear window 1 widgets
        for widget in self.winfo_children():
            widget.destroy()

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)
        font3 = tkinter.font.Font(family="맑은 고딕", size=16)

        width_info=640
        height_info=120
        width_frame = int(width_window/4)

        self.title("Save Info")
        self.geometry("{}x{}+100+50".format(width_window, height_window))
        self.resizable(False, False)

        def update_bluelabel(event=None, Match_info=None):
            for i in range(5):
                k_text = blue_kill[i].get()
                d_text = blue_death[i].get()
                a_text = blue_assist[i].get()
                Match_info.blueteam_KDA[i][0] = k_text
                Match_info.blueteam_KDA[i][1] = d_text
                Match_info.blueteam_KDA[i][2] = a_text
                print(i)
                print(k_text)
                print(d_text)
                print(a_text)
                print(match_info.blueteam_KDA[i][0])
                label_text = f"Kill: {k_text}\nDeath: {d_text}\nAssist: {a_text}"
                label_blueteam[i].config(text=label_text)
                print(label_blueteam[i].cget('text'))
                blue_kill[i].delete(0, tkinter.END)
                blue_death[i].delete(0, tkinter.END)
                blue_assist[i].delete(0, tkinter.END)
                Match_info.printInfo()

        def update_redlabel(event=None, Match_info=None):
            for i in range(5):
                k_text = red_kill[i].get()
                d_text = red_death[i].get()
                a_text = red_assist[i].get()
                Match_info.redteam_KDA[i][0] = k_text
                Match_info.redteam_KDA[i][1] = d_text
                Match_info.redteam_KDA[i][2] = a_text
                label_text = f"Kill: {k_text}\nDeath: {d_text}\nAssist: {a_text}"
                label_redteam[i].config(text=label_text)
                print(label_redteam[i].cget('text'))
                red_kill[i].delete(0, tkinter.END)
                red_death[i].delete(0, tkinter.END)
                red_assist[i].delete(0, tkinter.END)


        # 상단 프레임 생성
        info_top = tkinter.Frame(self, bg="#322756", width=400, height=50,bd='2')
        info_top.pack(side="top", fill='both')

        # 좌 프레임 생성
        info_left = tkinter.Frame(self, bg='skyblue',width=width_window/2, bd=3)
        info_left.pack(side='left',fill='y')

        frame_blueinfo = []
        frame_blueteam = []
        frame_bluekda = []
        label_blueteam = []
        label_bluekda = []
        blue_kill = []
        blue_death = []
        blue_assist = []

        for i in range(5):
            frame_blueinfo.append(tkinter.LabelFrame(info_left, width=int(width_window/2), height=int(height_info), relief="solid", bg="#EE7676", bd=1))
            frame_blueinfo[i].place(x=0, y=int(height_info*i))

            frame_blueteam.append(tkinter.LabelFrame(frame_blueinfo[i], width=width_frame, height=int(height_info), relief="solid", bg="blue", bd=1, text=team_dic[match_info.blueteam_Name][i]+" : "+match_info.blueteam_Pick[i]))
            frame_blueteam[i].pack(side='left', fill='none')

            label_blueteam.append(tkinter.Label(frame_blueteam[i],width=int(45),height=int(height_info),relief="solid",bg='purple',bd=0))
            label_blueteam[i].pack()

            frame_bluekda.append(tkinter.Frame(frame_blueinfo[i], width=width_frame, height=int(height_info), relief="solid", bg="red", bd=1))
            frame_bluekda[i].pack(side='right', fill='y',expand=True)

            blue_kill.append(tkinter.Entry(frame_bluekda[i],width=width_frame,font=font3))
            blue_kill[i].bind("<Return>", lambda event : update_bluelabel(event, Match_info=match_info))
            blue_kill[i].pack()

            blue_death.append(tkinter.Entry(frame_bluekda[i],width=width_frame,font=font3))
            blue_death[i].bind("<Return>", lambda event : update_bluelabel(event, Match_info=match_info))
            blue_death[i].pack()

            blue_assist.append(tkinter.Entry(frame_bluekda[i],width=width_frame,font=font3))
            blue_assist[i].bind("<Return>", lambda event : update_bluelabel(event, Match_info=match_info))
            blue_assist[i].pack()

# 우 프레임 생성
        info_right = tkinter.Frame(self, bg='pink', width=width_window/2, bd=3)

# 우 프레임을 윈도우 오른쪽에 위치시킴
        info_right.pack(side='right', fill='y')

        frame_redinfo = []
        frame_redteam = []
        frame_redkda = []
        label_redteam = []
        label_redkda = []
        red_kill = []
        red_death = []
        red_assist = []

        for i in range(5):
            frame_redinfo.append(tkinter.LabelFrame(info_right, width=int(width_window/2), height=int(height_info), relief="solid", bg="#EE7676", bd=1))
            frame_redinfo[i].place(x=0, y=int(height_info*i))

            frame_redteam.append(tkinter.LabelFrame(frame_redinfo[i], width=width_frame, height=int(height_info), relief="solid", bg="red", bd=1, text=team_dic[match_info.redteam_Name][i]+" : "+match_info.redteam_Pick[i]))
            frame_redteam[i].pack(side='left', fill='none')

            label_redteam.append(tkinter.Label(frame_redteam[i],width=int(45),height=int(height_info),relief="solid",bg='purple',bd=0))
            label_redteam[i].pack()

            frame_redkda.append(tkinter.Frame(frame_redinfo[i], width=width_frame, height=int(height_info), relief="solid", bg="red", bd=1))
            frame_redkda[i].pack(side='right', fill='y',expand=True)

            red_kill.append(tkinter.Entry(frame_redkda[i],width=width_frame,font=font3))
            red_kill[i].bind("<Return>", lambda event : update_redlabel(event, Match_info=match_info))
            red_kill[i].pack()

            red_death.append(tkinter.Entry(frame_redkda[i],width=width_frame,font=font3))
            red_death[i].bind("<Return>", lambda event : update_redlabel(event, Match_info=match_info))
            red_death[i].pack()

            red_assist.append(tkinter.Entry(frame_redkda[i],width=width_frame,font=font3))
            red_assist[i].bind("<Return>", lambda event : update_redlabel(event, Match_info=match_info))
            red_assist[i].pack()

        def click_bluteam_win(event, self):
            match_info.set_winnerTeam_Name(match_info.blueteam_Name)
            match_info.printInfo()
            match_info.insert_db()
            self.show_window_analyze()

        def click_redteam_win(event, self):
            match_info.set_winnerTeam_Name(match_info.redteam_Name)
            match_info.printInfo()
            match_info.insert_db()
            self.show_window_analyze()

        button_home = tkinter.Button(info_top, text="HOME", font=font1, bg="black", foreground="white", anchor='center',command=self.show_window_main)
        button_home.pack(side='top')
        button_blue = tkinter.Button(info_top, text='BLUE WIN', font=font1, bg="blue", foreground="white", anchor='center')
        button_blue.bind("<Button-1>", lambda event : click_bluteam_win(event, self))
        button_blue.pack(side="left")
        button_red = tkinter.Button(info_top, text='RED WIN', font=font1, bg="red", foreground="white", anchor='center', command=lambda : self.click_redteam_win(match_info, self))
        button_red.pack(side='right')


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
        #SQL 접근
        
        # STEP 2: MySQL Connection 연결
        con_champ = pymysql.connect(host='172.30.1.18', user='back', password='0000',
                       db='back', charset='utf8') # 한글처리 (charset = 'utf8')
 
        # STEP 3: Connection 으로부터 Cursor 생성
        cur_champ = con_champ.cursor()

        # STEP 4: SQL문 실행 및 Fetch
        sql = "SELECT * FROM champion"
        cur_champ.execute(sql)
 
        # 데이타 Fetch
        re_champion_data = cur_champ.fetchall() #(id, kor_name, eng_name, img_name)
        re_champion_data = sorted(re_champion_data, key=lambda x:x[1])

        sql2 = "SELECT COUNT(*) FROM match_result;"
        cur_champ.execute(sql2)
        row_count = cur_champ.fetchone()[0]
        print(row_count)

        # STEP 5: DB 연결 종료
        con_champ.close()        # Clear window 1 widgets

        for widget in self.winfo_children():
            widget.destroy()

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)
        
        self.title("Champion Analyze")
        self.geometry("{}x{}+100+50".format(width_window, height_window))
        self.resizable(False, False)

        champ_top = tkinter.Frame(self, width= width_window, height = 100,bg='blue')
        champ_top.pack(side="top")

        champ_main = tkinter.Frame(self, width=width_window, height=620, bg='red')
        champ_main.pack(side="top")
        
        label_champ=tkinter.Button(champ_top, text="BACK", font=font1, bg="black", foreground="white",anchor='center',command=self.show_window_analyze)
        label_champ.place(relx=0.8, rely=0.23)

        champ_treeview = ttk.Treeview(champ_main, columns=["champ",'W.R','B.R','P.R','K/D/A','SIDE Preference'],displaycolumns=["champ",'W.R','B.R','P.R','K/D/A','SIDE Preference'],height=30)
        champ_treeview.pack(ipadx=40)

        champ_treeview.column('champ',width=200,anchor='center')
        champ_treeview.heading("champ",text="champ",anchor="center")

        champ_treeview.column('W.R',width=200)
        champ_treeview.heading("W.R",text="W.R")

        champ_treeview.column('B.R',width=200)
        champ_treeview.heading("B.R",text="B.R")

        champ_treeview.column('P.R',width=200)
        champ_treeview.heading("P.R",text="P.R")

        champ_treeview.column('K/D/A',width=200)
        champ_treeview.heading("K/D/A",text="K/D/A")

        champ_treeview.column('SIDE Preference',width=280)
        champ_treeview.heading("SIDE Preference",text="SIDE Preference")

        champ_treeview["show"]="headings"
        
        treeview_data = [(row[1], "{:.2f}%".format(row[4] / (row[10] + row[11]) * 100) if row[10] + row[11]!=0 and row[4]!=0 else 0, 
                          round(row[5]/row_count*100, 2), round(row[6]/row_count*100, 2), 
                          round((int(row[7])+int(row[9]))/int(row[8]), 2) if int(row[8])!=0 else "PERFECT", 
                          "RED : {:.2f}%".format(row[10] / (row[10] + row[11]) * 100) if row[10]>row[11] else "BLUE : {:.2f}%".format(row[11] / (row[10] + row[11]) * 100) if row[10]+row[11] != 0 else "NONE") for row in re_champion_data]
            
        for i in range(len(treeview_data)):
            champ_treeview.insert('', 'end', values=treeview_data[i])

    def show_window_player(self):
        # STEP 2: MySQL Connection 연결
        con_player = pymysql.connect(host='172.30.1.18', user='back', password='0000',
                       db='back', charset='utf8') # 한글처리 (charset = 'utf8')
 
        # STEP 3: Connection 으로부터 Cursor 생성
        cur_player = con_player.cursor()

        # STEP 4: SQL문 실행 및 Fetch
        sql = "SELECT * FROM match_result ORDER BY winTeamName;"
        cur_player.execute(sql)
 
        # 데이타 Fetch
        player_data = cur_player.fetchall() #(id, kor_name, eng_name, img_name)

        sql2 = "SELECT COUNT(*) FROM match_result;"
        cur_player.execute(sql2)
        match_count = cur_player.fetchone()[0]

        
        sql3 = "SELECT table_team.Team_Initial, player.Player_ID, player.Player_Name, player.Position\
            FROM table_team \
            INNER JOIN 2023_lck_team_player ON 2023_lck_team_player.Team_ID=table_team.Team_ID\
            INNER JOIN player ON 2023_lck_team_player.Player_ID=player.Player_ID AND player.Main=0"
        cur_player.execute(sql3)

        team_member = cur_player.fetchall()
        team_member = sorted(team_member, key=lambda x:x[1])

        team_dic = {}
        for item in team_member:
            team = item[0]
            player = item[2]
            team_dic.setdefault(team, []).append(player)

        #(team:(member_list))
        team_dic = {team: tuple(players) for team, players in team_dic.items()}
        print(team_dic)

        # STEP 5: DB 연결 종료
        con_player.close() 

        member_data = []

        for team in team_dic:
            for member in team:
                print(member)

        for row in player_data:
            print(row[-1]) #winner
            print(row[1]) #blueteam
            print(row[22]) #redteam
            member_data.append(("팀", "포지션", "승", "킬", "데스", "어시스트"))

        print(member_data)
        

        # Clear window 1 widgets
        for widget in self.winfo_children():
            widget.destroy()

        font1=tkinter.font.Font(family="맑은 고딕", size=20)
        font2=tkinter.font.Font(family="맑은 고딕", size=10)
        
        self.title("Player Analyze")
        self.geometry("{}x{}+100+50".format(width_window, height_window))
        self.resizable(False, False)

        player_top = tkinter.Frame(self, width= width_window, height = 100,bg='blue')
        player_top.pack(side="top")

        player_main = tkinter.Frame(self, width=width_window, height=620, bg='red')
        player_main.pack(side="top")
        
        label_player=tkinter.Button(player_top, text="BACK", font=font1, bg="black", foreground="white",anchor='center',command=self.show_window_analyze)
        label_player.place(relx=0.8, rely=0.23)

        player_treeview = ttk.Treeview(player_main, columns=["Player","MOST1",'MOST2','MOST3','MOST4','MOST5'],displaycolumns=["Player","MOST1",'MOST2','MOST3','MOST4','MOST5'],height=50,selectmode="browse")
        player_treeview.pack()
        
        player_treeview.column('#0',width=100)
        player_treeview.heading("#0",text="Player")

        player_treeview.column('#1',width=236)
        player_treeview.heading("#1",text="MOST1")

        player_treeview.column('#2',width=236)
        player_treeview.heading("#2",text="MOST2")

        player_treeview.column('#3',width=236)
        player_treeview.heading("#3",text="MOST3")

        player_treeview.column('#4',width=236)
        player_treeview.heading("#4",text="MOST4")

        player_treeview.column('#5',width=236)
        player_treeview.heading("#5",text="MOST5")

        player_treeview["show"]="tree headings"

        treeview_data = [row[2] for row in team_member]
        my_tag='T1'
        player_treeview.tag_configure('T1',background='red')
        player_treeview.tag_configure('Gen',background='lightyellow')
        player_treeview.tag_configure('KT',background='red')
        player_treeview.tag_configure('DK',background='lightgrey')
        player_treeview.tag_configure('HLE',background='orange')
        player_treeview.tag_configure('LSB',background='lightyellow')
        player_treeview.tag_configure('KDF',background='red')
        player_treeview.tag_configure('DRX',background='lightblue')
        player_treeview.tag_configure('BRO',background='lightgreen')
        player_treeview.tag_configure('NS',background='red')

        
        
        for i in range(len(treeview_data)):
            player_treeview.insert('', 'end', text=treeview_data[i],tags=(my_tag))
            if (i+1<=4):my_tag='T1'
            elif (i+1<=9):my_tag='Gen'
            elif (i+1<=14):my_tag='KT'
            elif (i+1<=19):my_tag='DK'
            elif (i+1<=24):my_tag='HLE'
            elif (i+1<=29):my_tag='LSB'
            elif (i+1<=34):my_tag='KDF'
            elif (i+1<=39):my_tag='DRX'
            elif (i+1<=44):my_tag='BRO'
            elif (i+1<=49):my_tag='NS'

if __name__ == '__main__':
    app = BackBanpickAnalyzer()
    app.mainloop()