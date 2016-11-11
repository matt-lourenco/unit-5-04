# Created on 11 Nov 2016
# Created by: Matthew Lourenco
# This is a program that lets you input numbers and averages them

import ui
from numpy import random

my_numbers = []
count = 0

def add_number_touch_up_inside(sender):
    global my_numbers
    global count
    number_input = view['input_textfield'].text
    try:
        number_input = int(number_input)
        if number_input >= 0 and number_input <= 100:
            my_numbers.append(number_input)
            view['display_textview'].text = view['display_textview'].text + str(my_numbers[count]) + '\n'
            count = count + 1
            average = 0
            for index in my_numbers:
                average = average + index
            average = average / len(my_numbers)
            view['average_label'].text = "Average: " + str(average)
        else:
            view['error_label'].text = 'Please enter a number between 0 and 100.'
    except:
        view['error_label'].text = 'Please enter a real number. ' + str(number_input) + ' is not a real number.'

view = ui.load_view()
view.present('fullscreen')
