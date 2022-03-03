import random
score=30
l=[1,2,3,4,5,6,7,8,9,10]
a=random.choice(l)

attempt=1
while(1):
    b=int(input("Guess the number between 1 to 10:"))
    if(b>a):
        print("Lower number please!!!")
    elif(b<a):
        print("Upper number please!!")
    else:
        print("You have guessed correctly in",attempt,"attempt")
        break
    score=score-5
    attempt=attempt+1


if(attempt==1):
    print("Your score:",score)
elif(attempt==2):
    print("Your score:",score)
elif(attempt==3):
    print("Your score:",score)
elif(attempt==4):
    print("Your score:",score)
elif(attempt==5):
    print("Your score:",score)
else:
    print("score cannot be displayed")