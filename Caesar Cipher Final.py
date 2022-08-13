#Syed Haider Naqvi
#10th October, 2020
#PA3
#This program takes a text or file input from the user and then either decodes it or encodes it in a key of their choice in the caeser cipher

from random import randrange
from time import sleep
from graphics import *
from string import ascii_lowercase
from string import ascii_uppercase
#Used to import required modules

def clickChecker():

    button1 = False
    button2 = False
    #Used to initialise the while loop conditions as false to enter the loop
    
    while (button1 == False) and (button2 == False):
        click_name = Cipher.getMouse()
        if not (click_name.getX() >= 15 and click_name.getX() <= 40 and click_name.getY() >=15  and click_name.getY() <= 30):
            button1 = False
        else:
            button1 = True
        if not (click_name.getX() >= 60 and click_name.getX() <= 85 and click_name.getY() >=15  and click_name.getY() <= 30):
            button2 = False
        else:
            button2 = True
    return click_name
    #Keeps checking for a click until the user clicks one of the two buttons on screen
            
def circlemaker(Center, Radius, Color = "red"):

    circle_maker = Circle(Center, Radius)
    circle_maker.setFill(Color)
    circle_maker.draw(Cipher)
    #Draws a circle with the required specs every time it is called

def bubblemaker(number):

    for i in range(number):
        circlemaker(Point(randrange(100),randrange(80,100)),randrange(10), color_rgb(randrange(256),randrange(256),randrange(256)))
        circlemaker(Point(randrange(100),randrange(20)),randrange(10), color_rgb(randrange(256),randrange(256),randrange(256)))
        sleep(0.01)
    #Used draws the required number of bubbles in a random fashion in the designated area

def introAnimation():

    intro_button, intro_text = buttonmaker(Point(1,30),Point(99,70),Point(50,50),\
    "Welcome to the Caesar Cipher Program!\nThis program can encode or decode entire text files\nor just a small phrase.\n\nClick anywhere to continue", color_rgb(65,179,247),"black", 5)

    for i in range(5,20,1):
        intro_text.setSize(i)
        intro_text.undraw()
        intro_text.draw(Cipher)
        sleep(0.04)
    #Used to draw the intro text

    bubblemaker(150)
    #Used to animate bubbles

    Cipher.getMouse()
    #Used to run intro animation and then wait for a mouseclick to continue with program

def clearscreen():

    background = Rectangle(Point(0,0),Point(100,100))
    background.setFill(color_rgb(0,82,165))
    background.draw(Cipher)
    #Used to clear the screen with a solid background
    
def setTitle():

    description = Text(Point(50,85), "This program can encode and decode\n Caesar Ciphers with a Cipher key of your choice!")
    description.setFill("black")
    description.setSize(15)
    description.setFace("arial")
    description.draw(Cipher)
    #Used to set description

    title = Text(Point(50,95), "Caesar Cipher")
    title.setFill("black")
    title.setSize(30)
    title.setFace("arial")
    title.draw(Cipher)
    #Used to set Title
    

def buttonmaker(Point1,Point2,Text_point, Label, buttoncolor = "white", labelcolor = "black", labelsize = 20):

    button = Rectangle(Point1, Point2)
    button.setFill(buttoncolor)
    button.draw(Cipher)
    #Draws button box in program
    
    buttonLabel = Text(Text_point,Label)
    buttonLabel.setFill(labelcolor)
    buttonLabel.setSize(labelsize)
    buttonLabel.draw(Cipher)
    #Draws button label in program

    return button, buttonLabel
    #returns values of buttons to be stored as variables

def output(method, output_text):

    output_box = Rectangle(Point(10,30),Point(90,70))
    output_box.setFill(color_rgb(65,179,247))
    output_box.draw(Cipher)

    output_heading = "The "+ str(method) + "ed text is:"

    output_text_1 = Text(Point(50, 60), output_heading)
    output_text_1.setFill("black")
    output_text_1.setSize(25)
    output_text_1.draw(Cipher)

    output_text_2 = Text(Point(50,45), output_text)
    output_text_2.setFill("black")
    output_text_2.setSize(15)
    output_text_2.draw(Cipher)

    buttonmaker(Point(5,10),Point(95,20),Point(50,15),"Please click anywhere to close the program", color_rgb(65,179,247),"black")
    #Used to output the result of the encoding or decoding to the user at the end of the program and inform the user that they can click anywhere to close the program


def decode(text, key):

    new_decoded = ""

    for i in range(len(text)):

        if text[i] in ascii_uppercase or text[i] in ascii_lowercase:

            if text[i] in ascii_uppercase:

                asciikey = ord(text[i])
                asciikey = asciikey - key
                if asciikey < 65:
                    asciikey =  ord("Z") - (ord("A") - asciikey) + 1
                #Used to loop around the alphabet if character goes behind "A"

                new_decoded = new_decoded + chr(asciikey)

            if text[i] in ascii_lowercase:

                asciikey = ord(text[i])
                asciikey = asciikey - key
                if asciikey < 97:
                    asciikey =  ord("z") - (ord("a") - asciikey) + 1
                #Used to loop around the alphabet if character goes behind "a"

                new_decoded = new_decoded + chr(asciikey)

        else:
            new_decoded = new_decoded + text[i]

    return new_decoded
    #Used to decode the text and return it to the main program to be stored as a variable

def encode(text, key):

    new_encoded = ""

    for i in range(len(text)):

        if text[i] in ascii_uppercase or text[i] in ascii_lowercase:

            if text[i] in ascii_uppercase:
                asciikey = ord(text[i])
                asciikey = asciikey + key
                if asciikey > 90:
                    asciikey = ord("A") - (ord("Z") - asciikey) - 1
                #Used to loop around the alphabet if character goes after "Z"

                new_encoded = new_encoded + chr(asciikey)

            if text[i] in ascii_lowercase:
                asciikey = ord(text[i])
                asciikey = asciikey + key
                if asciikey > 122:
                    asciikey =  ord("a") - (ord("z") - asciikey) - 1
                #Used to loop around the alphabet if character goes behind "a"

                new_encoded = new_encoded + chr(asciikey)

        else:
            new_encoded = new_encoded + text[i]

    return new_encoded
    #Used to encode the text and return it to the main program to be stored as a variable

def caeser_cipher():

    global Cipher
    Cipher = GraphWin("Caesar Cipher", 600, 600)
    Cipher.setCoords(0,0,100,100)
    #Used to initialise graphics window

    clearscreen()
    introAnimation()
    #Used to run introductory animation screen

    clearscreen()
    setTitle()
    #Used to set GUI after intro screen

    file_button, file_label = buttonmaker(Point(15,15),Point(40,30),Point(27.5,22.5),"File", color_rgb(65,179,247),"black")
    #Used to draw file option

    text_button, text_label = buttonmaker(Point(60,15),Point(85,30),Point(72.5,22.5),"Text", color_rgb(65,179,247),"black")
    #Used to draw text button

    option_button, option_label = buttonmaker(Point(10,40),Point(90,60),Point(50,50),\
    "Please choose whether you want to\nencode/decode a file or a text phrase", color_rgb(65,179,247),"black", 20)
    #Used to draw button which explains users options

    file_or_text_click = clickChecker()
    #Used to keep getting a mouseclick until one of the two buttons on screen is clicked
            
    clearscreen()
    setTitle()
    #Used to clear GUI

    entry_text = Entry(Point(50,70),40)
    entry_text.setText("Enter Text or file name without extension here")
    entry_text.setFill(color_rgb(65,179,247))
    entry_text.draw(Cipher)
    #Used to set Entry box for text

    cipher_key = Entry(Point(50,50), 20)
    cipher_key.setText("Enter Key")
    cipher_key.setFill(color_rgb(65,179,247))
    cipher_key.draw(Cipher)
    #Used to set Entry box for key

    decode_button, decode_label = buttonmaker(Point(15,15),Point(40,30),Point(27.5,22.5),"Decode", color_rgb(65,179,247),"black")
    #Used to draw decode button

    encode_button, encode_label = buttonmaker(Point(60,15),Point(85,30),Point(72.5,22.5),"Encode", color_rgb(65,179,247),"black")
    #Used to draw encode button

    command = clickChecker()
    #Used to keep getting a mouseclick until one of the two buttons on screen is clicked and save it to a variable

    original_text = entry_text.getText()
    key = eval(cipher_key.getText())
    #Used to get the text and key in the entry boxes

    clearscreen()
    entry_text.undraw()
    cipher_key.undraw()
    #Used to clear the GUI

    if file_or_text_click.getX() >= 60 and file_or_text_click.getX() <= 85 and file_or_text_click.getY() >= 15  and file_or_text_click.getY() <= 30:

        if command.getX() >= 15 and command.getX() <= 40 and command.getY() >=15  and command.getY() <= 30:

            output_text = decode(original_text, key)
            output("decode", output_text)

        elif command.getX() >= 60 and command.getX() <= 85 and command.getY() >= 15 and command.getY() <= 30:

            output_text = encode(original_text, key)
            output("encode", output_text)
        #This set of conditional statements checks which button was clicked and then proceeds to decode/encode and then output the text to user

    elif file_or_text_click.getX() >= 15 and file_or_text_click.getX() <= 40 and file_or_text_click.getY() >=15  and file_or_text_click.getY() <= 30:

        text_file = open(original_text + ".txt", "r", encoding = "utf-8")
        input_text = text_file.read()
        output_text_file = open(original_text + "_new.txt", "w", encoding = "utf-8")
        #Opens the orginal text file and a new text file in which the encoded/decoded text will be stored

        if command.getX() >= 15 and command.getX() <= 40 and command.getY() >=15  and command.getY() <= 30:

            output_text = decode(input_text, key)
            output_text_file.write(output_text)
            output_text_file.close()

            buttonmaker(Point(2,30),Point(98,70),Point(50,50),\
            "Your decoded file has been created\n in the same folder as this program\n\nPlease click anywhere to close this program", color_rgb(65,179,247),"white")
            #informs the user their new file has been decoded
            

        elif command.getX() >= 60 and command.getX() <= 85 and command.getY() >= 15 and command.getY() <= 30:

            output_text = encode(input_text, key)
            output_text_file.write(output_text)
            output_text_file.close()

            buttonmaker(Point(2,30),Point(98,70),Point(50,50),\
            "Your encoded file has been created\n in the same folder as this program.\n\nPlease click anywhere to close this program", color_rgb(65,179,247),"white")
            #informs the user their new file has been encoded

        #This set of conditional statements checks which button was clicked and then proceeds to decode/encode the file to the user and provide them with a new file.

    Cipher.getMouse()
    Cipher.close()
    #Used to wait for a mouse click and then close program


caeser_cipher()
    























