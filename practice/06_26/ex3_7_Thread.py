import threading
import time

def func(sec, delay, name):
  print(f'{name}에게 업무가 할당 되었습니다')
  for i in range(sec):
    print(f'{name}이 {i+1}번째 일을 하고 있습니다')
    time.sleep(delay)
  print(f'{name}이 퇴근합니다')

thread1 = threading.Thread(target=func, args =(5, 0.2, '최태산')) # 5초 동안 0.2초 간격
thread1.start()

thread2 = threading.Thread(target=func, args =(8, 0.3, '장태산')) 
thread2.start()

thread3 = threading.Thread(target=func, args =(10, 0.5, 'ADMIN')) # 데몬 쓰레드
thread3.setDaemon(True)
thread3.start()

