import time
while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result)
  print("Process 3")
  time.sleep(50)
