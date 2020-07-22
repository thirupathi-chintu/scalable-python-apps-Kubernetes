names = ['David', 'Peter', 'Michael', 'John', 'Bob']
while True:
    for i in range (len (names)):
        print("{}.{}".format(i + 1, names[i]))
    continue


# import time
# while True:
#   localtime = time.localtime()
#   result = time.strftime("%I:%M:%S %p", localtime)
#   print(result)
#   print("Process 1")
#   time.sleep(50)
