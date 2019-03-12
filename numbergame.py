import random
import time

class WordGame():
    def __init__(self, name):
        super(WordGame, self).__init__()
        self.name = name
        self.difficulty = "easy"
        self.difficultyTypes = ["easy", "medium", "hard"]
        self.min = 10
        self.max = 100
        self.score = 0
        self.timeScore = 0
        self.finalScore = 0

    def introduction(self):
        print("Welcome to the game, %s!\n" % self.name)
        time.sleep(2)

        print('THE RULES:')
        print("Numbers will come up, on the screen, you have to type them out",
        "correctly, then press enter.\nTry to get as many right as possible!\n",
        "You'll be scored out of the number you get correct & the time taken to",
        "answer them.\nIf you enter a wrong number, 0 points will be awarded.\n",
        "If you enter a letter or spacebar in your answer, you will lose 3 points!\n")
        time.sleep(2)

    def difficultyLevel(self):
        difficultyDisplay = self.difficultyTypes.copy()
        difficultyDisplay.remove(self.difficulty)
        print("The current difficulty level is '%s'" % self.difficulty)
        print("There are two other difficulty levels, '%s' and '%s'" \
        % (difficultyDisplay[0], difficultyDisplay[1]))
        statement = "\nWould you like to change the difficulty level? Enter \
 [Yes] or [No]\n"
        Yesresult = "Changing difficulty..."
        noResult = "Difficulty stays the same\n"

        if self.continuer(statement, Yesresult, noResult) == True:
            while True:
                print("What difficulty would you like to change it to?")
                print("Enter '%s' or '%s'" % (difficultyDisplay[0], difficultyDisplay[1]))
                inputDifficulty = input()

                if inputDifficulty.lower() == difficultyDisplay[0]:
                    print('Difficulty is not set to %s!\n' % difficultyDisplay[0])
                    self.difficulty = difficultyDisplay[0]
                    break

                elif inputDifficulty.lower() == difficultyDisplay[1]:
                    print('Difficulty is now set to %s!\n' % difficultyDisplay[1])
                    self.difficulty = difficultyDisplay[1]
                    break

                else:
                    print("Invalid input, try again")

            if self.difficulty == "easy":
                self.min = 10
                self.max = 100
            elif self.difficulty == "medium":
                self.min = 1000
                self.max = 10000
            elif self.difficulty == "hard":
                self.min = 100000
                self.max = 1000000

    def ready(self):
        input("All set! Are you ready? Press [Enter] to begin")
        print('Game starting in:')
        print('3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1...')
        time.sleep(1)

    def game(self):
        timeStart = time.time()

        for x in range(1, 11):
            number = random.randint(self.min, self.max)
            print("Number ", x)
            print(number)
            while True:
                try:
                    inputnumber = int(input("Enter number above: "))
                    if number == inputnumber:
                        print('Correct!\n')
                        self.score += 5
                    else:
                        print('Wrong!\n')
                    break
                except ValueError:
                    print("You didn't enter a number! You lost points :(\n")
                    self.score -= 3
                    break

        timeEnd = time.time()
        timeTotal = int(timeEnd - timeStart)
        self.timeScore = (self.score/50)*(40/timeTotal)
        self.finalScore = self.timeScore + self.score


    def results(self):
        print('Here is your final score, %s!' %self.name)
        print('Score from numbers typed correctly: %s/50' % self.score)
        print('Score from time taken:', round(self.timeScore, 2))
        print('FINAL SCORE: ', round(self.finalScore, 2))

        if self.finalScore < 0:
            print("I can't believe you got a negative score, %s D:" % self.name)
        elif self.finalScore < 10:
            print("You're not really good at this game, %s :(" % self.name)
        elif self.finalScore < 30:
            print("Not too bad %s!" % self.name)
        elif self.finalScore < 53:
            print("You're pretty good &s!" % self.name)
        else:
            print("Wow, good job, %s! You did really well!" % self.name)

    def tryAgain(self):
        statement = 'Do you want to play again? Enter [yes] or [no]\n'
        Yesresult = 'Starting again!'
        noResult = "Okay, we'll miss you. Come back soon! :("
        return self.continuer(statement, Yesresult, noResult)

    def resetValues(self):
        print('Reseting values...\n')
        self.score = 0
        self.timeScore = 0
        self.finalScore = 0

    def continuer(self, statement, Yesresult, noResult):
        while True:

            yesno = input(statement)

            if yesno.lower() == 'yes':
                print(Yesresult, '\n')
                return True
                break

            elif yesno.lower() == 'no':
                print(noResult, '\n')
                return False
                break

            else:
                print('Invalid input, try again')


name = input("Please enter your name:")
p1 = WordGame(name)
p1.introduction()
while True:
    p1.difficultyLevel()
    p1.ready()
    p1.game()
    p1.results()
    if p1.tryAgain() == False:
        break
    p1.resetValues()
