import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

quit=False
range = 20

while not quit:
    random_number = random.randint(1,range)
    count = 0
    number = -1
    
    while number != random_number:
        number = input("Guess a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("Pick a number.")
        else:
            number=int(number)
            count=count+1
            if number > random_number:
                print("Too high!")
            elif number < random_number:
                print("Too low!")
    print("Noice!")
    str(count)
    print("You guess it! It took you {} tries.".format(count))
    play_again = input("Would you like to play?" )
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
      quit=False
    else:
      quit = True
      print("Game Over")
