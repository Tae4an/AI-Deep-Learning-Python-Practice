# ### 해보기 2) 편의점 재고관리

# 1. 엔터만 입력할 때까지 계속 입력 받는다
# 2. 물건 이름이 존재하면 수정, 존재하지 않으면 추가
# 3. 입력이 끝나면 재고 현황을 물건 이름으로 정렬하여 출력

d = {}

prod = input('제품 이름을 입력하세요 :')

while prod.strip() != '': 
  cnt = int(input('개수를 입력하세요 '))
  stock = d.get(prod, 0)

  stock += cnt
  d[prod] = stock
  prod = input('제품 이름을 입력하세요 :')



print(d)