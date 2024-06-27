import time

def running_time_decorator(func):
  def wrapper(*arg):
    start_time = time.time()
    func(*arg)
    end_time = time.time()
    running_time = end_time - start_time
    print(f"{func.__name__} 함수를 실행하는데 {running_time:.4f}초 걸렸습니다")
  return wrapper

    
@running_time_decorator
def count_down(num):
    while num:
        num-= 1

@running_time_decorator
def sum_up_to(num):
    result = 0
    for i in range(0, num+1):
        result += i
    print('누적 합계는', result)


count_down(100000)
sum_up_to(100000)
