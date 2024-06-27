singer = ['멜로망스', '잔나비', '이센스', '10센티', '이영지']
  # 1) 맨 뒤에 '비오'를 추가하세요
  # 2) '잔나비' 뒤에 '딥플로우'를 추가하세요
  # 3) '지코', '스윙스'를 한 번에 추가하세요
  # 4) '지코'를 제거하세요
  # 5) 리스트를 모두 제거하세요

singer.append('비오')
print(singer)

singer.insert(2,'딥플로우')
print(singer)

singer.extend(['지코','스윙스'])
print(singer)

singer.remove('지코')
print(singer)