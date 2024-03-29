""" This is the final version of my Integration project
This is a Trivia Game that also serves as a GUI
revolving around JOJO's Bizzare adventures.
__author__ = Christian Apostoli
This program utilizes the external module created by John Zelle.
"""
# Christian Apostoli
# This will  be a trivia quiz which has
# a main theme based on JOJO's Bizzare Adventures.
# The game has two sets of questions: one with
# a level of difficulty dependent on the user and
# a gauntlet style set of questions.
# Caution: If you are not a fan you will not get these right.


# Notes:
# Use dictionary for answers 
# use function for seeing if player is right
# use a lag function for if the player is right

from graphics import *

# ------------- POP UP Graphics----------------------
win = GraphWin("JOJO Trivia Game", 600, 600)


def make_new_scene(message):
    """
    make_new_scene passes the message argument as text to the screen
    and will also place the logo above the text.
    :param message: The text on the GUI window
    """
    # make_new_scene uses functions from the graphics module to create the
    # and input text on to the screen along with the logo. It initializes the
    # txt object and configures the color and size
    win.setBackground(color_rgb(0, 0, 0))

    txt = Text(Point(250, 350), message)
    txt.setTextColor(color_rgb(0, 255, 200))
    txt.setSize(15)
    txt.draw(win)

    img = Image(Point(250, 180), "Jojo.png")
    img.draw(win)

    win.getMouse()


def clear():
    """
    Clear erases the screen for the scene.
    """
    # Clears the screen for the next scene by placing a rectangle in
    # with the same size as the window to simulate erasing
    # the content on the screen

    rect = Rectangle(Point(0, 0), Point(600, 600))
    rect.setOutline(color_rgb(0, 0, 0))
    rect.setFill(color_rgb(0, 0, 0))
    rect.draw(win)


## def text_box(message):
##    Function that creates textbox for the user to enter info
##    Function was very difficult to incorporate with other
##    code, so it was commented for possible future use
##    
##    win.setBackground(color_rgb(0,0,0))
##
##    txt = Text(Point(250,300), message)
##    txt.setTextColor(color_rgb(0,255, 200))
##    txt.setSize(15)
##    txt.draw(win)
##
##    img = Image(Point(250,180), "Jojo.png")
##    img.draw(win)
##
##    input_box = Entry(Point(250, 400), 15)
##    input_box.draw(win)
##    answer = input_box.getText()
##
##    while True:
##        txt.setText(input_box.getText())
##
##    win.getMouse()


def set_one(n, arr):
    """
    This is the first set of questions. The question will vary based on the
    user's desired difficulty. Then the function will see if the user got
    the question correct or not.
    :param n: The desired level of difficulty.
    :param arr: The array that the function appends 1 to create a score.
    :return: The question of certain difficulty that the user will answer.
    """
    # The passed parameter n will be from the input function inside the while
    # loop. The function will create a new scene with text inside the game 
    # window and the python shell. If the user inputs the correct answer,
    # arr will append 1 to it which will be how many questions were answered 
    # correctly.
    if n == 0:
        answer = input("In what part did Johnathan Joestar die? ")
        if answer == '1' or answer == 'part 1' or answer == 'Part 1':
            make_new_scene("Correct. Click to Continue.")
            clear()
            arr.append(1)
        else:
            make_new_scene("Sorry, incorrect. Click to continue.")
            clear()
    elif n == 1:
        answer = input("Who was Joseph's German friend\n" +
                       "who helped him defeat the pillar men? ")
        if (answer == 'Stronheim') or (answer == 'Victor Von Stronheim'):
            make_new_scene("Correct, Click to continue.")
            clear()
            arr.append(1)
        else:
            make_new_scene("Sorry, incorrect. Click to continue.")
            clear()
    elif n == 2:
        answer = input("What was the tarot card of the Ship stand in part 3? ")
        if answer == 'Strength':
            make_new_scene("Correct. Click to Continue.")
            clear()
            arr.append(1)
        else:
            make_new_scene("Sorry, incorrect. Click to continue.")
            clear()
    elif n == 3:
        answer = input("What famous phrase does DIO\n" +
                       "say as he is about to fight Jotaro? ")
        if answer == 'oh, so you are approaching me':
            make_new_scene("Correct. Click to continue.")
            clear()
            arr.append(1)
        else:
            make_new_scene("Sorry, incorrect. Click to continue.")
            clear()
    elif n == 4:
        answer = input("What is the final opening to part 4" +
                       "(Just say the first two words)? ")
        if (answer == 'Breakdown') or (answer == 'Shining Justice'):
            make_new_scene("Correct. Click to continue.")
            clear()
            arr.append(1)
        else:
            make_new_scene("Sorry, incorrect. Click to continue.")
            clear()
    elif n == 5:
        answer = input("What is Giorno Giovana's famous line (in Japanese)? ")
        if answer == 'kono giorno giovana niwa yume ga aru':
            make_new_scene("Correct. Click to continue.")
            clear()
            arr.append(1)
        else:
            make_new_scene("Sorry, incorrect. Click to continue.")
            clear()


# -------------------------------------------------


def main():
    """
    Initializes the game and continues the game until the user is finished.
    """
    make_new_scene("Hello user, welcome to my JOJO Trivia Game!\n" +
                   "Continue the game by clicking the black window.")
    clear()

    make_new_scene(
        "All new players will start out with a score of " + str(0) + ".")
    clear()

    make_new_scene(
        "A player's final score will be determined by the number\n" +
        "of questions correct divided by the number of total questions.")
    clear()

    # The next four lines performs the arithmetic behind
    # the example for the user's score.
    num_correct = 100
    num_questions = 100
    score_final = num_correct / num_questions
    score_final *= 100

    make_new_scene("For example, a perfect score" +
                   " will result in a " + str(score_final) + ".")
    clear()

    make_new_scene(
        "First we will begin with a question that depends on your\n" +
        "desired difficulty, then we will move on to a set of five\n" +
        "         questions. Please remember to answer your questions ASAP.")
    clear()

    make_new_scene(
        "What question level would you like to start at for your\n" +
        "first set? Please return to the Python shell to insert your\n" +
        "          input and drag the shell window beside the game window")
    clear()

    # The program asks the user what level they would like to start at for
    # their first set of questions. The while loop will further validate
    # the user's input.
    n = int(input("What question level would you like to start\n" +
                  "at for your first set? (0-5, whole number)"))
    input_bad = True
    while input_bad:
        try:
            # If the user inputs a number out of range
            while n > 5 or n < 0:
                print("Number is out of range")
                n = int(input("What question level would you like to start\n" +
                              "at for your first set? (0-5, whole number)"))
            input_bad = False
        # If the user does not input a whole number
        except ValueError:
            print("This is not a whole number")

    # This array is created to see if the user answered the question correctly
    # by inserting a value in the array and checking  if the value is present.
    arr = []

    set_one(n, arr)

    score = (arr.count(1) * 100)
    make_new_scene("Your Score for your first set is " + str(score) + ".")
    clear()

    make_new_scene("Now time for your second set! There \n" +
                   "will be five questions. Click to continue.")
    clear()

    make_new_scene("Remember to click until the question appears\n" +
                   "on the shell and then put in your answer.")
    clear()

    # The following two arrays contain the questions
    # and answers for the next set of questions.
    second_set = ["What is the stand of Fugo in part 5? ",
                  "What is D'arby the younger's stand in part 3?  ",
                  "What is Shigechi's stand in part 4? ",
                  "What does Jotaro have a PhD in? ",
                  "What was the name of the supposed alien from part 4? "]

    second_set_answers = ["Purple Haze", "Atum", "Harvest", "Marine Biology",
                          "Mikitaka"]

    # If the user got the first set correct then
    # a point is added to this next array.
    score_arr = []
    if arr.count(1) == 1:
        score_arr.append(1)

    is_on = True

    while is_on:
        #   Loop will iterate through second_set
        #   and validate if the user's response is correct by seeing
        #   if it is the same as the corresponding value in second_set_answers.
        for i in range(len(second_set)):
            make_new_scene(second_set[i] + "\nClick to continue.")
            clear()
            question = input(second_set[i])
            if question == second_set_answers[i]:
                make_new_scene("That's correct. Click to continue.")
                clear()
                print("That's correct")
                score_arr.append(1)
            else:
                print("Sorry, incorrect.")
                make_new_scene("That's not correct. Click to continue")
                clear()

        is_on = False
    # The score is calculated by checking how many times
    # 1 is present in the score_arr array.
    score_final = (int(score_arr.count(1)) / 6.0) * 100
    print("Your final score is: ", format(score_final, '.2f'))
    make_new_scene("Your final score is: " + format(score_final, '.2f'))
    clear()
    make_new_scene("Thanks for playing!")
    win.close()


main()
