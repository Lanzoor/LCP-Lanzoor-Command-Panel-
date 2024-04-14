import random
from datetime import datetime

def tryIntInput(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except:
            print("You dumdum, that is not an integer!")
def golt():
    number = random.randint(0, 100)
    attempts = 0
    print(
        '''
Let's play the \"Greater or lower than\" game!
The rules are simple, I pick a random number between 1 and 100.
If you make a guess, I'll tell you whenever your guess is greater than my guess, 
or your guess is lower than my guess until you guess the value! Let's get started.
''',
    )

    while True:
        inputValue = tryIntInput("Enter your guess!\n  >>> ")
        if inputValue > number:
            if inputValue <= 100:
                print(f"The number is lower than {inputValue}, try again!")
            attempts += 1
        elif inputValue < number:
            print(f"The number is greater than {inputValue}, try again!")
            attempts += 1
        elif inputValue == number:
            print(f"You've guessed it right! The answer was {number}, and you used {attempts} attempts in this game.")
            break
        elif inputValue > 100:
            print("You dumdum, this number is out of the value!")
            attempts += 1
    
def rps():
    UserChoice = input("Choose one! Rock, Paper, or Scissors!\n  >>> ").capitalize().replace(" ","")
    CPUChoice = random.choice(["Rock", "Paper", "Scissors"])
    RpsChoice = ["Rock", "Paper", "Scissors"]
    while UserChoice not in RpsChoice:
        UserChoice = input("You dumdum, that is not a valid choice! Try again.\n  >>> ")
    if CPUChoice == UserChoice:
        WinOrLose = "It's a draw!"
    else:
        WinningConditions = [
            ("rock", "scissors"),
            ("scissors", "paper"),
            ("paper", "rock")
        ]
        if (UserChoice, CPUChoice) in WinningConditions:
            WinOrLose = "You won!"
        else:
            WinOrLose = "I won!"
    print(f"You picked {UserChoice}, I pick {CPUChoice}! {WinOrLose}")
        
def ordinal(n: int) -> str:
    if 11 <= n % 100 <= 13:
        return str(n) + "th"
    return str(n) + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    
def isLeapYear(year: int = int(datetime.now().strftime("%Y"))) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
