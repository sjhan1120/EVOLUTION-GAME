import sys
print("버전업 테스트")

POPULATION = 0                  #생물 개체수 구현
CREATURETALENT = []             #생물 특성 구현. 리스트 안에 특성이 쌓여가는 방식.
EVOLUTIONLIST = [               #선택할 수 있는 진화들을 모아둔 리스트.
    '지방층', '방한 털', '표면적 감소'
    
    ]
COLD = 0                        #환경 영향인 추위 구현
COLDRESPONSE = 0                #추위에 대응하는 추위내성 구현

def displayInformation():      #생물 및 환경의 현재 정보 표시 구현
    print("개체수 : " + str(POPULATION))       #개체수 표시
    print("생물 특성 : " + str(CREATURETALENT))#현재 가지고 있는 특성 표시
    print("추위 : " + str(COLD)) #현재 환경 영향 정도 표시. 일단 추위로 고정. 나중에 환경에 따라 나타나는 정보가 달라지도록 구현해야함.
    print("추위내성 : " + str(COLDRESPONSE)) #현재 환경에 대응하는 내성 표시. 일단 추위내성으로 고정. 나중에 환경에 따라 나타나는 정보가 달라지도록 구현해야함.

def environmentEffect(turn):        #환경 영향 구현
    global COLD, COLDRESPONSE, POPULATION                 #전역변수로 접근하기 위한 설정
    if (turn + 1) % 10 == 0:    #10턴마다 영구적으로 추위 스택이 1씩 증가. 이것도 지금은 추위로 고정. 나중에 바꿔야 함.
        COLD += 1

    if COLD - COLDRESPONSE > 0: #만약 추위가 생물의 추위내성보다 높다면
        print("생물이 추위를 느낍니다. 개체수가 감소합니다.")
        POPULATION -= 200 * (COLD - COLDRESPONSE) #추위에서 추위내성을 뺀것의 곱하기 200만큼 개체수가 감소

    if POPULATION <= 0: #만약 생물 개체수가 0 이하가 되면 게임오버
        print("생물이 멸종하였습니다.")
        sys.exit(0)
        

def selectEvolution(turn):          #진화 선택 구현
    global EVOLUTIONLIST, COLD, COLDRESPONSE, CREATURETALENT
    if (turn + 1) % 3 == 0:     #3턴마다 진화 선택 가능.
        print("생물을 진화시키십시오.")
        print("진화 목록 : " + str(EVOLUTIONLIST))    #진화할 수 있는 목록을 나열하여 거기서 플레이어가 선택하는 방식. 원래는 3개가 랜덤하게 나오고 거기서 뽑아야함. 나중에 고치자.
        evol = input("진화할 특성 : ")   #진화 특성에 해당하는 이름을 입력하면 해당 특성이 플레이어의 생물 특성 리스트에 쌓임.
        if evol == "지방층" or evol == "방한 털" or evol == "표면적 감소":  #만약 추위내성을 얻는 진화를 선택했을 경우 추위내성 1스택 추가됨.
            print("생물이 진화에 성공했습니다.")
            COLDRESPONSE += 1
            CREATURETALENT.append(evol)
            
        else:                                       #진화 특성에 해당하는 이름을 입력하지 않았다면 진화 안함.
            print("생물이 진화에 실패했습니다.")
            
        
def main():
    global POPULATION          #전역변수로 접근하기 위한 설정
    for i in range(20):        #턴 구현. 총 20턴 반복. 일단 테스트 용도로 20턴이고 실제는 100턴.
        POPULATION += 100      #기본으로 1턴마다 개체수 100마리 씩 증가
        
        print("현재 " + str(i + 1) + "번째 턴입니다.") #현재 턴 표시
        
        environmentEffect(i)    #환경의 영향을 받음
        displayInformation()    #현재 생물 정보 표시
        
        print()                 #정보와 진화선택 문장을 공백으로 띄움.
        
        selectEvolution(i)       #진화 선택

        next = input("아무키나 눌러 다음턴으로 넘기십시오.") #플레이어가 다음턴으로 넘김
        if next == 'e':  #만약 e를 눌렀다면 즉시 게임승리 후 게임종
            break
        else:
            print("------------------------")
    print("생물이 살아남았습니다. 생물이 생태계를 지배합니다.")
    print("게임에서 승리했습니다.")
        

#---------------------메인-------------------------
main()
