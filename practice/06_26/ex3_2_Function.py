# def d(firstName, lastName):
#   print(firstName, lastName)

# d(lastName = 'last', firstName = 'first') # 키워드 매개변수 : 전달 인자 순서를 바꾸어서 보내더라도 해당 코드 처럼 하면 정상 전달
#---------------------------------------------------------------------------------------------------------------------------

# def d(c, **arg):
#   print(arg)

# d(c=100,a=10,b=20,c=30)
#---------------------------------------------------------------------------------------------------------------------------

def a():
  global l 
  l = '바나나가 좋아'
  print(l)

l = '사과가 좋아'
a()
print(l)