from threading import Thread,semaphore
import time

def my_function1():
  for i in range(10000):
    with semaphore:
      print("123")
      print("456")
      print("789")
      time.sleep(1)

def my_function2():
  for i in range(10000):
    with semaphtore:
      print("abc")
      print("def")
      print("ghi")
      time.sleep(1)

def my_function3():
  for i in range(10000):
    with semaphore:
      print("ABC")
      print("DEF")
      print("GHI")
      time.sleep(1)

if __name__ == "__main__":
  semaphore=Semaphore(1)
  t1 = Thread(target = my_function1)
  t2 = Thread(target = my_function2)
  t3 = Thread(target = my_function3)
  t1.start()
  t2.start()
  t3.start()
  t1.join()
  t2.join()
  t3.join()
