# word.txt 파일을 읽어서 단어문제 출제
# word.txt 읽어와서 리스트에 담아서 출력하기

import os
import random
import time
import sqlite3
import datetime

print("현재폴더 : ", os.getcwd())


f = open("./basic/data/python/word.txt", "r", encoding="utf-8")

words = []
for word in f:

    words.append(word.strip())
f.close()


# print(words)


# 5문제 출제 :
# 리스트 섞어주기
# 임의로 하나 추출

# user는 문제를 타이핑 치기

# 문제와 user가 작성한 값이 일치하는 지 확인
# 정답 개수 couont 처리
# 정답 개수 3개 이상이면 합격


input("게임을 시작할까요? Enter입력")


random.shuffle(words)

for i in range(3, 0, -1):
    print(i, "초")
    time.sleep(1)

print("시작!")

count = 0
start = time.time()  # 시작 시간
for index in range(0, 5):
    print(words[index])
    result = input("따라 적으세요")

    if result.strip() == words[index].strip():
        count += 1
    else:
        continue

end = time.time()
et = format(end - start, ".3f")

print(f"너가 맞춘 개수 {count}")

print("시작 : ", start)
print("종료  : ", end)
print("걸린 시간 : ", et, "초")

check = False
if count >= 3:
    print("합격")
    check = True

else:
    print("탈락")
    check = False


# DB 저장
# records 테이블 생성 (정답개수(integer), 기록(et), regdate)

# 탈락시 기록안함
if check:
    conn = sqlite3.connect(
        "./basic/test.db", isolation_level=None
    )  # isolation_level=None : AutoCommit 비활성화

    cursor = conn.cursor()

    sql = "create table if not exists records(correct_count integer, time_recode float, regdate text)"

    cursor.execute(sql)

    sql = "insert into records(correct_count, time_recode, regdate) "
    sql += "values(?, ?, ?)"
    nowDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M:%S")
    cursor.execute(sql, (count, et, nowDateTime))

    conn.close()
