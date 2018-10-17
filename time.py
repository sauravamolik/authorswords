import time
t= time.localtime()
print("local time",t)
print("the time is",time.ctime())
later=time.time() + 15
print("15 sec from now",time.ctime(later))
