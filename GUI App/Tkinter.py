"""
Author : Prajval Patel (C0911611)
Date : November 26th, 2023
Program : Exploring Tkinter - Building a GUI Application in Python for converting Celsius to Fahrenheit
"""

import tkinter as tk

degree_symbol = '\u00b0'
invalid_output_message = 'Error! Enter valid temperature value'


# Conversion Logic
def celsius_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
    # Error Handling
    except ValueError:
        return invalid_output_message


def convert():
    celsius_value = entry.get()
    result = celsius_to_fahrenheit(celsius_value)
    if result == invalid_output_message:
        result_label.config(text=f'{result}')
    else:
        result_label.config(text=f'Fahrenheit Value: {result}{degree_symbol}F')
    # Change color and message based on the result
    try:
        result = float(result)
        if result <= 68:
            result_label.config(fg='blue')
            message_label.config(text="It's cold outside, considering wearing a sweater or jacket.")
        elif 68 <= result <= 86:
            result_label.config(fg='orange')
            message_label.config(text="It's warm outside, enjoy the bright sunshine!")
        else:
            result_label.config(fg='red')
            message_label.config(text="It's hot outside, don't forget to apply SPF.")
    except ValueError:
        result_label.config(fg='black')
        message_label.config(text='')


# Creating main window
window = tk.Tk()
window.title('Celsius to Fahrenheit Converter')

# Creating widgets

# User Input Area
label = tk.Label(window, text='Enter Celsius Value: ')
entry = tk.Entry(window)
convert_button = tk.Button(window, text='Convert', command=convert)
# Result Display
result_label = tk.Label(window, text='Fahrenheit Value: ')
message_label = tk.Label(window, text='')

# Arranging widget's layout and design in window
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label.grid(row=2, column=0, columnspan=2, pady=10)
message_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main console app
window.mainloop()
