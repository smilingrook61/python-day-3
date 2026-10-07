# 2 kinds of loops: while loops, and For loops
#While loops - you don't know how many times it's going to happen
#risk of creating infinite loop
#2 ways to avoid the infinite loop 1. make a condition that can be false 2. use the break keyword
#For loops - when you know the amount of times

#while True:
    #borrow_sweater = input("Can I borrow your sweater?")
    #if borrow_sweater == "Yes":
       # print("that's what i thought")
        #break
    #else:
       # print("nooooooooooooooooo")



#blastoff
#create a countdown before a spaceship launches
count = 10
while count >= 1:
    print(count)
    count = count - 1

print("blastoff!")