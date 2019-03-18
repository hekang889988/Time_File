# 这是第一个代码
import os
import time
import datetime

print(datetime.datetime.now().strftime('%F %T'))

class time_user:
    def __init__(self,year_user,mouth_user,day_user,hour_user,min_user,second_user):
        self.Year = year_user
        self.Mouth = mouth_user
        self.Day = day_user
        self.Hour = hour_user
        self.Min = min_user
        self.Second = second_user

    def time_now(self):
        print("Today is" + "  " + self.Year + "-" + self.Mouth + "-" + self.Day)
        print("Time is"  + "  " + self.Hour + ":" + self.Min + ":" + self.Second)


print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
Time_User = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
#Time_User = time_user(year,mouth,day,hour,min,second)
#2019-03-10 11:11:11
#time.strftime('%Y-%M-%D %h:%m:%s',time.localtime(time.time()))
year = Time_User[0:4]
mouth = Time_User[5:7]
day = Time_User[8:10]
hour = Time_User[11:13]
min = Time_User[14:16]
second = Time_User[17:19]

for num in Time_User:
    if num != "-" and num != ":":
        print(num,end = "")
print(" ")
time_now = time_user(year,mouth,day,hour,min,second)
time_now.time_now()
print(Time_User)
#Time_User.time_now()

'''a = [1,2,3,4,5]
b = a

print(id(a))
print(id(b))
print(a)
print(b)
a.append(6)

print(id(b))
print(id(a))
print(a)
print(b)
'''
print("Hello wolrd\n")
file_cwd = os.getcwd()
#os.mknod("first.txt")
#file_name_user = "first"+ "_" + Time_User.Year + Time_User.Mouth + Time_User.Day + Time_User.Hour + Time_User.Min + Time_User.Second

first_txt = open("Test information%s.txt"%(Time_User),'w')
first_txt.write("It's {0} now".format(Time_User))
first_txt.write("\r\n")
first_txt.write("This is second write")

first_txt.write("This is the third write")
first_txt.close()
first_txt = open("Test information%s.txt"%(Time_User),'w')
first_txt.write("This is the fourth write")
first_txt.close()

first_txt = open("Test information{0}.txt".format(Time_User),'r')
print(first_txt.read())

first_txt.close()
#input = open('first.txt','r')
print(os.getcwd())