from datetime import datetime, timedelta
import time
import uuid
import random
import threading
import os
class OrdersManager:
  __orders = []
  __orders_processed = 0
  __last_printed_log = datetime.now()
  def __init__(self) -> None:
    self.__generate_fake_orders(quantity=1_000)
  def __generate_fake_orders(self, quantity):
    self.__log(f"Generating fake orders")
    self.__orders = [(uuid.uuid4(), x) for x in range(quantity)]
    self.__log(f"{len(self.__orders)} generated...")
  def __log(self, message):
    print(f"{datetime.now()} > {message}")
  def __fake_save_on_db(self, order):
    id, number = order
    self.__log(
            message=f"Order [{id}] {number} was successfully prosecuted."
        )
    time.sleep(random.uniform(0, 1))
  def process_orders(self):
    for order in self.__orders:
      self.__fake_save_on_db(order=order)
      self.__orders_processed += 1
      if datetime.now() > self.__last_printed_log:
        self.__last_printed_log = datetime.now() + timedelta(seconds=5)
        self.__log(
        message=f"Total orders executed: {self.__orders_processed}/{len(self.__orders)}"
        )
        
def task1(start_time):
  orders_manager1=OrdersManager()
  orders_manager1.process_orders()
  delay = time.time() - start_time
  print(f"{datetime.now()} > Tiempo de ejecucion: {delay} segundos...")
  
def task2(start_time):
  orders_manager2=OrdersManager()
  orders_manager2.process_orders()
  delay = time.time() - start_time
  print(f"{datetime.now()} > Tiempo de ejecucion: {delay} segundos...")

def task3(start_time):
  orders_manager3=OrdersManager()
  orders_manager3.process_orders()
  delay = time.time() - start_time
  print(f"{datetime.now()} > Tiempo de ejecucion: {delay} segundos...")
  
def task4(start_time):
  orders_manager4=OrdersManager()
  orders_manager4.process_orders()
  delay = time.time() - start_time
  print(f"{datetime.now()} > Tiempo de ejecucion: {delay} segundos...")
  
def task5(start_time):
  orders_manager5=OrdersManager()
  orders_manager5.process_orders()
  delay = time.time() - start_time
  print(f"{datetime.now()} > Tiempo de ejecucion: {delay} segundos...")
  
start_time=time.time()
t1 = threading.Thread(target=task1(start_time), name='t1')
t2 = threading.Thread(target=task2(start_time), name='t2')
t3 = threading.Thread(target=task3(start_time), name='t3')
t4 = threading.Thread(target=task4(start_time), name='t4')
t5 = threading.Thread(target=task5(start_time), name='t5')
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
