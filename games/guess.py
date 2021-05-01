print('******************************')
print('********** GAME  *************')
print('******************************')

print("-----------------------------------")
print("Pick it up which level you wish: \n")
print("Level 1 | Level 2 | Level 3")
print("-----------------------------------")

level_has_chosen = int(input("Level has chosen: "))

points = 1000
secret = 10
count = 5

if level_has_chosen == 1:
        print(" You have 20 attempts")
        count = 20
elif level_has_chosen == 2:
    print(" You have 10 attempts")
    count = 10
else:
    print(" You have 5 attempts")
    count = 5
    
        
for tries in range(1,count + 1):
    print("You have {} attempt.\n".format(count))
    print("your points is: {}".format(points))
    number = int(input("Type a number: \n"))
    count -= 1
    if number == secret:
        print("Well done!")
        break
    elif number > secret:
        print("Your number is bigger, you have lost {} points.".format(abs(number)))
        points -= number
    elif number < secret:
        print("Your number is smaller, you have lost {} points.".format(abs(number)))
        points -= number