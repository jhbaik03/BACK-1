
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
champs = cur.fetchall()
print(champs)     # 전체 rows

# STEP 5: DB 연결 종료
con.close()

for i in range(len(champs)):
    print("lck analyzing tool/champ/"+ champs[i][2] +".png")