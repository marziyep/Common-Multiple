# we can set a list with a desired length and desired integer members the code below will calculate the common multiple among them!
def deviders(list):
    king_list=[]
    for member in list:
       deviders=[]
       for item in range(1,member+1):
          if member%item == 0:
            deviders.append(item)

       king_list.append(deviders)
    return king_list

#lets consider we have a list consists of three numbers:
my_list=[4,8,16]
print(list(set.intersection(*map(set,deviders(my_list)))))

#lets consider we have a list consists of 10 numbers:

my_list1=[30,40,50,60,990,90,100,110,170,270]
print(list(set.intersection(*map(set,deviders(my_list1)))))
