import random

def random_number():
    return random.randint(1, 100)

correct = int(random_number())
guess = 0

while guess != correct:
  guess = int(input("정답을 맞춰주세요:"))
  if(correct > guess):
    print('더 큰 수입니다')
  elif(correct < guess):
    print('더 작은 수입니다')
  elif(correct == guess):
    print('정답입니다')
  else:
    print('범위 내 숫자를 입력해주세요')