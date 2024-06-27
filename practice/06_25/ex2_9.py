fp = open('./a.txt','w',encoding='UTF-8')

aaa = '안녕하세요 만나서 반갑습니다'
fp.writelines(aaa+'\n')

aaa = '네에~'
aaa = f'{홍길동},{80},{90},{60}'
fp.writelines(aaa+'\n')

fp.close()

fp = open('./a.txt','r',encoding='UTF-8')
datas = fp.readlines()

for a in datas:
  print(a)

fp.close()