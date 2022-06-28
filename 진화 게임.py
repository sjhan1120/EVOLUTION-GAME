import sys
import random

POPULATION = 0                  #생물 개체수 구현
CREATURETALENT = []             #생물 특성 구현. 리스트 안에 특성이 쌓여가는 방식.
EVOLUTIONLIST = [               #선택할 수 있는 진화들을 모아둔 리스트.
    '지방층', '방한 털', '표면적 감소'
    ]
COLD = 0                        #환경 영향인 추위 구현
COLDRESPONSE = 0                #추위에 대응하는 추위내성 구현
HUNT = 0.5                      #사냥성공확률 구현. 초기값은 0.5로 성공 실패 각각 절반 확률
HUNGRY = 0                      #사냥성공확률에 따른 굶주림 구현

def displayInformation():      #생물 및 환경의 현재 정보 표시 구현
    print("개체수 : " + str(POPULATION))       #개체수 표시
    print("생물 특성 : " + str(CREATURETALENT))#현재 가지고 있는 특성 표시
    print("추위 : " + str(COLD)) #현재 환경 영향 정도 표시. 일단 추위로 고정. 나중에 환경에 따라 나타나는 정보가 달라지도록 구현해야함.
    print("추위내성 : " + str(COLDRESPONSE)) #현재 환경에 대응하는 내성 표시. 일단 추위내성으로 고정. 나중에 환경에 따라 나타나는 정보가 달라지도록 구현해야함.
    print("사냥성공확률 : " + str(round(HUNT, 2)))      #사냥성공확률을 표시
    print("굶주림 : " + str(HUNGRY))       #굶주림 정도 표시

def environmentEffect(turn):        #환경 영향 구현
    global COLD, COLDRESPONSE, POPULATION                 #전역변수로 접근하기 위한 설정
    if (turn + 1) % 10 == 0:    #10턴마다 영구적으로 추위 스택이 1씩 증가. 이것도 지금은 추위로 고정. 나중에 바꿔야 함.
        COLD += 1

    if COLD - COLDRESPONSE > 0: #만약 추위가 생물의 추위내성보다 높다면
        print("생물이 추위를 느낍니다. 개체수가 감소합니다.")
        POPULATION -= 200 * (COLD - COLDRESPONSE) #추위에서 추위내성을 뺀것의 곱하기 200만큼 개체수가 감소

    if POPULATION <= 0: #만약 생물 개체수가 0 이하가 되면 게임오버
        print("생물이 멸종하였습니다.")
        print("게임에서 패배했습니다.")
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

def massExtinctions():  #생물 대멸종 구현
    print("생물 대멸종이 일어나고 있습니다.")
    global COLD, POPULATION, HUNT
    COLD += 5               #매 턴마다 추위 5씩 증가
    HUNT -= 0.05            #매 턴마다 사냥성공확률 5퍼센트씩 감소

def preyHunting():          #사냥성공확률에 따른 굶주림 증감 구현. HUNT가 클수록 사냥성공확률이 높음
    global HUNGRY, HUNT, POPULATION
    huntingpercent = random.random()
    if huntingpercent > HUNT:                   #0부터 1까지의 랜덤한 수가 HUNT보다 크다면 사냥 실패. 굶주림 1스택 추가
        print("생물이 사냥에 실패했습니다.")
        HUNGRY += 1
    else:                                       #0부터 1까지의 랜덤한 수가 HUNT보다 작다면 사냥 성공. 굶주림 1스택 감소
        print("생물이 사냥에 성공했습니다.")
        if HUNGRY == 0:                         #굶주림은 0보다 작아질 수 없음. 0이 최소
            None
        else:
            HUNGRY -= 1

    if HUNGRY > 5:                              #굶주림이 5보다 크다면 (HUNGRY - 5) 에 비례하여 개체수가 감소함.
        print("생물이 극심한 굶주림을 느낍니다. 생물이 죽어갑니다.")
        POPULATION -= (HUNGRY - 5) * 100

    if POPULATION <= 0:                         #만약 생물 개체수가 0 이하가 되면 게임오버
        print("생물이 멸종하였습니다.")
        print("게임에서 패배했습니다.")
        sys.exit(0)
        
def main():
    global POPULATION          #전역변수로 접근하기 위한 설정
    for i in range(60):        #턴 구현. 총 60턴 반복. 일단 테스트 용도로 20턴이고 실제는 100턴.
        POPULATION += 100      #기본으로 1턴마다 개체수 100마리 씩 증가
        
        print("현재 " + str(i + 1) + "번째 턴입니다.") #현재 턴 표시
        if (i+1 >= 50):                                 #50턴부터 생물대멸종 이벤트 시작
            massExtinctions()
        
        environmentEffect(i)    #환경의 영향을 받음
        preyHunting()           #굶주림의 영향을 받음
        displayInformation()    #현재 생물 정보 표시
        
        print()                 #정보와 진화선택 문장을 공백으로 띄움.
        
        selectEvolution(i)       #진화 선택

        next = input("엔터를 눌러 다음턴으로 넘기십시오.") #플레이어가 다음턴으로 넘김
        if next == 'e':  #만약 e를 눌렀다면 즉시 게임승리 후 게임종료
            break
        else:
            print("------------------------")
    print("생물이 살아남았습니다. 생물이 생태계를 지배합니다.")
    print("게임에서 승리했습니다.")
        

#---------------------메인-------------------------
print("#####진화 게임을 시작합니다.#####")
print()
main()
