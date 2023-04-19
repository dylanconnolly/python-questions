import concurrent.futures
from collections import deque
import queue
import time

batch_size = 100
aggregate_results = []

def get_health_check(mac_address: str):
  # mocking the API call and putting a sleep timer of 5 seconds to simulate latency
  # the request would be: requests.get(f"http://localhost:8000/device/check/{mac_address}")
  time.sleep(5)
  # mocked response
  return {
    "mac_address": mac_address,
    "status_code": 200,
  }

def get_mac_addresses():
  with open('mac_addresses.txt') as file:
    return file.read().splitlines()

def build_queue(data):     
  q = queue.SimpleQueue()
  for line in data:
    q.put(line)

  return q

def build_batch(q: queue):
   if q.qsize() < batch_size:
      return [q.get() for _ in range(q.qsize())]
   else:
      return [q.get() for _ in range(batch_size)]

def exec_batch(batch):    
  with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    batch_results = []

    for item in batch:
      futures.append(executor.submit(get_health_check, mac_address=item))

    for future in concurrent.futures.as_completed(futures):
      print(future.result())
      batch_results.append(future.result())
      aggregate_results.append(future.result())
  
  # write batch results as opposed to waiting for entire data stream to complete
  with open("health_check_results.txt", "a") as file:
    for br in batch_results:
      file.write(f"{br}\n")

def main():
  start = time.perf_counter()
  data_stream = get_mac_addresses()
  q = build_queue(data_stream)
  while not q.empty():
    batch = build_batch(q)
    exec_batch(batch)

  end = time.perf_counter()  
  print("Completed:", len(aggregate_results), "results in", f"{end-start:0.2f}", "seconds")


main()
