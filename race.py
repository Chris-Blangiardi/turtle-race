import random as r
import time
import turtle


# creates a class to store the color and wins of each turtle
class Racer:
    def __init__(self, color):
        self.color = color
        self.wins = 0
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.turtle.speed(20)


# loads in stats of each turtle if there is any
def load_data(racers):
    r_File = open("RacerStats.txt", "r")  # opens the save file
    lines = r_File.readlines()  # creates an array storing each line

    if not lines:  # skips over loading data if there is no data
        return
    else:
        j = 0
        for line in lines:
            line = line.split(" ")  # splits each line from color and wins
            racers[j].wins = int(line[1])  # updates the # of wins for each turtle
            j += 1
    r_File.close()  # closes the file


# saves the amount of wins each turtle has
def write_data(racers):
    w_File = open("RacerStats.txt", "w")  # creates or overwrites save file

    for racer in racers:
        w_File.write("{} {}\n".format(racer.color, racer.wins))

    w_File.close()  # closes the file


def race():
    win = turtle.Screen()  # displays the turtle race

    racer1 = Racer("red")
    racer2 = Racer('blue')
    racer3 = Racer("orange")
    racer4 = Racer("green")
    racer5 = Racer("purple")
    racers = [racer1, racer2, racer3, racer4, racer5]

    load_data(racers)

    xCord = -400
    for i in racers:  # brings each turtle to their starting position
        i.turtle.penup()
        i.turtle.left(90)
        i.turtle.goto(xCord, -400)
        xCord += 200

    racing = True
    while racing:
        for racer in racers:  # turtle movement
            racer.turtle.forward(r.randint(1, 15))
            if racer.turtle.ycor() >= 400:  # ends and prints winner of the race
                racing = False
                print("\t   " + racer.color + " wins\n")
                racer.wins += 1
                break

    time.sleep(1)  # delays the window from instantly closing
    win.bye()  # closes turtle window
    turtle.Turtle._screen = None
    turtle.TurtleScreen._RUNNING = True

    write_data(racers)

    return racers


file = open("RacerStats.txt", "w")  # creates a stats file if there isn't one
file.close()
while True:  # runs until user chooses to exit
    print("----- Enter 1 to race, 2 for stats or 3 to quit -----\n")
    choice = input("\t   What would you like to do?: ")

    if choice == "1":  # makes the turtles race
        results = race()

    if choice == "2":  # prints out the wins for each turtle
        try:
            print("\t   Career Stats: ")
            for turtles in results:
                print("\t  ", turtles.color, turtles.wins)
            print()
        except:
            print("\t   Run a race first\n")

    if choice == "3":  # breaks out of the while loop
        break
 