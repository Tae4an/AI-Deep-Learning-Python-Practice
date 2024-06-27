age = 1
while age != 0:
  age = int(input('나이를 입력해주세요:'))
  price = 3000
  if(65 <= age or age <= 7):
    print('무료입니다')
  elif(8<= age <= 18):
    print(price - 2000)
  else:
    print(price)