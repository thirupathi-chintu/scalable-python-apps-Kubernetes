import time

names = ['Process 1']
while True:
    for i in range (len (names)):
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(result)
        print("{}.{}".format(i + 1, names[i]))
    continue


# import time
# while True:
#   localtime = time.localtime()
#   result = time.strftime("%I:%M:%S %p", localtime)
#   print(result)
#   print("Process 1")
#   time.sleep(50)
