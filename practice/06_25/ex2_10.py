import datetime

menu = {"대들보 밥버거" : 5000, "햄 밥버거" : 5500, "햄 치즈 밥버거" : 6000, "제육 밥버거" : 6500, "치즈제육 밥버거" : 7000}

print("----------------------------------------")

print("              대들보 밥버거              ")

print("----------------------------------------")

selectMenu = {}
orderTime = {} 

# 딕셔너리 menu의 키들을 리스트로 변환하는 코드, 딕셔너리의 키를 인덱스로 접근할 수 있는 형태로 만듦
menu_keys = list(menu.keys())

while True:
    selectMenuNum = int(input('메뉴를 선택해주세요 (0 ~ {}): '.format(len(menu_keys) - 1)))
        
    if 0 <= selectMenuNum < len(menu_keys):
      selected_menu_name = menu_keys[selectMenuNum]
      selected_menu_price = menu[selected_menu_name]
      print(f"{selected_menu_name}의 가격은 {selected_menu_price}원입니다.")
    else:
      print("잘못된 인덱스..! 다시 시도하세요.")
    
    cnt = int(input('몇 개를 드릴까요? :'))
    print(f"{selected_menu_name} X {cnt} = {selected_menu_price * cnt}원입니다.")
    selectMenu[selected_menu_name] = cnt

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    orderTime[selected_menu_name] = current_time
    
    a = input('더 주문하시겠습니까?(y/n)')
    if a == 'y':
      continue
    elif a == 'n':
      break
    else:
      print('잘못된 입력입니다')

def calculateFee(menuInfo, orderInfo):

    totalFee = 0

    print("----------------------------------------")

    for key, value in orderInfo.items():

        fee = value * menuInfo[key]

        outputString = f"{key} : {value} --- {fee}"

        

        print(outputString)

        totalFee += fee # 가격 뽑아와서 주문 개수에 맞게 계산

    print("----------------------------------------")

    print("총 가격 :", totalFee)

    return totalFee

total = calculateFee(menuInfo = menu, orderInfo = selectMenu)


# 주문 내역을 메모장 파일로 출력
fp =  open("주문내역.csv", "w", encoding="utf-8")