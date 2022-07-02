times = 0
right = [20]
print("You can choose value 5 times only")
while(True):
    times = times + 1
    item = int(input("Enter the value : "))
    print(item) 
    print("You printed no. of times : ",times)
    if item in right and times <= 5:
        print("You guessed right number in number of attempt : ",times)
        break
    elif times <= 5 and item not in right:
        if times == 5:
            print("You have crossed the limit")   
            break
        # continue 