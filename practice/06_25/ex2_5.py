# 1
# for i in range(10):
#   print('*'*i)

# 2
# for i in range(10):
#   if i > 5:
#     for j in range(4,0,-1):
#       print('*'*j)
#     break
#   else:
#     print('*'*i)

#3
# i = 0
# for j in range(5, 0, -1):
#   i += 1
#   print(' '*j,end='')
#   print('*'*i)
# i = 5
# for j in range(2, 6, 1):
#   i -= 1
#   print(' '*j,end='')
#   print('*'*i)
    

#4      
# n = 10  

# # 상단 삼각형 부분
# for i in range(n):
#     # 공백을 (n-i-1)번 출력
#     print(' ' * (n - i - 1), end='')
#     # '*' 문자를 (2*i+1)번 반복하여 출력
#     print('*' * (2 * i + 1))

# # 하단 삼각형 부분
# for i in range(n - 2, -1, -1):
#     # 공백을 (n-i-1)번 출력
#     print(' ' * (n - i - 1), end='')
#     # '*' 문자를 (2*i+1)번 반복하여 출력
#     print('*' * (2 * i + 1))

#5
n = 5  

# 상단 삼각형 부분
for i in range(n - 2, -1, -1):
    # 공백을 (n-i-1)번 출력
    print(' ' * (n - i - 1), end='')
    # '*' 문자를 (2*i+1)번 반복하여 출력
    print('*' * (2 * i + 1))

# 하단 삼각형 부분
for i in range(n):
    # 공백을 (n-i-1)번 출력
    print(' ' * (n - i - 1), end='')
    # '*' 문자를 (2*i+1)번 반복하여 출력
    print('*' * (2 * i + 1))


