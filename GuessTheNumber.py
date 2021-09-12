n = 18    #  <- this is the correct answer.if user will guess this number exactly in 9 attempt then they will win.
try:
    
    print("RULE -> You Only Have 9 attempt To Win This Game")
    print("Please Choose Between 1 to 30")
    print("============================================")
    number_of_guess = 1
    while(number_of_guess<=9):
        guess_number = int(input("Guess The Number: "))
        if (guess_number>18):
            print("OOPS choose Lesser value")
            print("----------------------")
        elif(guess_number<18):
            print("OOPS choose Greater value")
            print("----------------------")
        else:
            print("*******************************************************")
            print("OHHOOOO! You Guess The Right Number...")
            print("You Won This Game In ",number_of_guess,"Attempt")
            print("*******************************************************")
            break
        print(9-int(number_of_guess),"Attempt Left")
        number_of_guess = number_of_guess + 1
    if(number_of_guess>9):
        print("Game Over")
except Exception as e:
    print("Please Enter a valid Integer Value")

    