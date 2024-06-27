def func(cnt):
  sum = 0;
  for i in range(cnt, 0, -1):
    if(i % 2 ==0):
        sum += i
  return sum

cnt = int(input("cnt의 값을 입력하세요:"))

print(func(cnt))