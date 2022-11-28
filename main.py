import random

def guess_number():
    r_number = random.randint(0,100)
    print("Hi, just try to guess number between 0 - 100")

    playing = True
    counter = 0

    while playing == True:
        user_number = int(input())

        if user_number == r_number:
            counter += 1
            if counter <= 1:
                print(f"Congratz, you win in {counter} move! That's incredible")
            elif counter > 1:
                print(f"Congratz, you win in {counter} moves!")
            playing = False
        elif user_number < r_number:
            print("sheesh bro, try a bigger number")
            counter += 1
        elif user_number > r_number:
            print("hold on man, you are going in wrong way! The number is too big")
            counter += 1

guess_number()