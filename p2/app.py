import time
while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result)
  print("Process 2")
  time.sleep(50)
