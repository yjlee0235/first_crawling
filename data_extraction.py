import time

#subjects.txt 파일에서 데이터 가져옴
file_name = 'subjects-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.txt'
with open(file_name, "r") as f:
    datas = f.readlines()

#해당 학년과 전학년 대상 수업만을 가져옴
with open("third_grade.txt", "w") as f:
    count = 0
    for data in datas:
        d = data.split()
        if d[7] == '3' or d[7] == '전학년':
            f.write(' '.join(d) + '\n')
            count = count + 1
    #총 개수 파일에 출력
    #f.write(str(count - 1))

#해당 학년 수업 데이터를 datas변수로 가져옴
with open("third_grade.txt", "r") as f:
    datas = f.readlines()

mon = []
tues = []
wed = []
thur = []
fri = []
online = []
#각 요일에 맞는 수업을 분류
for data in datas:
    d = data.split()
    ld = d[len(d)-1]
    if d[10].find("3시간") != -1:
        online.append(d)
        continue
    if ld.find("월") != -1:
        mon.append(d)
    if ld.find("화") != -1:
        tues.append(d)
    if ld.find("수") != -1:
        wed.append(d)
    if ld.find("목") != -1:
        thur.append(d)
    if ld.find("금") != -1:
        fri.append(d)


"""
#각 과목을 콘솔에 출력
print("월요일 수업")
for sj in mon:
    print(sj)
print('\n\n화요일 수업')
for sj in tues:
    print(sj)
print('\n\n수요일 수업')
for sj in wed:
    print(sj)
print('\n\n목요일 수업')
for sj in thur:
    print(sj)
print('\n\n금요일 수업')
for sj in fri:
    print(sj)
print('\n\n온라인 수업')
for sj in online:
    print(sj)
"""

#각 과목을 파일에 출력
file_name = 'sort_by_day-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.txt'
with open(file_name, "w") as f:
    f.write("월요일 수업\n")
    for sj in mon:
        f.writelines(' '.join(sj) + '\n')
    f.write("\n\n화요일 수업\n")
    for sj in tues:
        f.writelines(' '.join(sj) + '\n')
    f.write("\n\n수요일 수업\n")
    for sj in wed:
        f.writelines(' '.join(sj) + '\n')
    f.write("\n\n목요일 수업\n")
    for sj in thur:
        f.writelines(' '.join(sj) + '\n')
    f.write("\n\n금요일 수업\n")
    for sj in fri:
        f.writelines(' '.join(sj) + '\n')
    f.write("\n\n온라인 수업\n")
    for sj in online:
        f.writelines(' '.join(sj) + '\n')