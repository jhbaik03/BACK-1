
# STEP 1
import pymysql
from collections import OrderedDict

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='192.168.219.101', user='back', password='0000',
                       db='back', charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()
 
# STEP 4: SQL문 실행 및 Fetch
# sql = "SELECT table_team.Team_Initial, player.Player_Name, player.Position\
#     FROM 2023_lck_team_player \
#     INNER JOIN player ON 2023_lck_team_player.Player_ID=player.Player_ID\
#     INNER JOIN table_team ON 2023_lck_team_player.Team_ID=table_team.Team_ID"

sql = "SELECT table_team.Team_Initial, player.Player_ID, player.Player_Name, player.Position\
    FROM table_team \
    INNER JOIN 2023_lck_team_player ON 2023_lck_team_player.Team_ID=table_team.Team_ID\
    INNER JOIN player ON 2023_lck_team_player.Player_ID=player.Player_ID AND player.Main=0"
cur.execute(sql)

# 데이타 Fetch
champs = cur.fetchall()
champs = sorted(champs, key=lambda x:x[1])

#champs.sort()

print(champs)

result = {}
for item in champs:
    team = item[0]
    player = item[2]
    result.setdefault(team, []).append(player)

result = {team: tuple(players) for team, players in result.items()}

print(result)
# STEP 5: DB 연결 종료
con.close()