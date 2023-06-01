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

    #챔피언이 이미 존재하는지 확인해주는 함수
    def check_exist(self, champion_name):
        if champion_name in self.blueteam_Pick:
            return True
        elif champion_name in self.blueteam_Ban:
            return True
        elif champion_name in self.redteam_Pick:
            return True
        elif champion_name in self.redteam_Ban:
            return True
                
        return False
            
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
        self.blueteam_Pick[position] = champion_Name
        self.printInfo()
    def set_redteam_Pick(self, champion_Name, position):
        self.redteam_Pick[position] = champion_Name
        self.printInfo()
            
    #챔피언 밴 정보 설정
    def set_blueteam_Ban(self, champion_Name, location):
        self.blueteam_Ban[location] = champion_Name
        self.printInfo()
    def set_redteam_Ban(self, champion_Name, location):
        self.redteam_Ban[location] = champion_Name
        self.printInfo()

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
        
        print("blueTeam Ban : ")
        for i in range(5):
            print(self.blueteam_Ban[i])
        
        print("red : ", self.redteam_Name)
        for i in range(5):
            print(str(i), " : ", self.redteam_Pick[i], end="")
        
        print("redTeam Ban : ")
        for i in range(5):
            print(self.redteam_Ban[i])


#현재 경기 정보 저장 객체 생성
now_match = Match_info()

now_match.printInfo()
now_match.set_blueteam_Name("T1")
now_match.set_blueteam_Pick("Garejn", 1)