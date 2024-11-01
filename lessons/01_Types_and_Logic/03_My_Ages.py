
# Run Me!
# Assign to some variables. 
age = 14
bank_account = 159.99
name = "John"
colors = ["red", "blue", "green"]

print("Age   : ", type(age))
print("Bank  : ", type(bank_account))
print("Name  : ", type(name))
print("Colors: ", type(colors))

# add type integers

a = 10
b = 20

print("a + b = ", a + b)

# add '10' to '20 as strings

a = "10"
b = "20"

print("a + b = ", a + b) # Wait, what????

a = 10
b = "20"
print("a + b = ", a + b)

# String to integer and float

print('int', int('1305'))
print('int',float('1305.32'))

# The int() function can also take a second argument, which is the base of the number to be converted.
# so we can convert all of the other bases

print('octal',int('45', 8))
print('octal',int('0o45', 8))

print('hex',int('25', 16))
print('hex',int('0x25', 16))

print('binary', int('100101', 2))
print('binary', int('0b100101', 2))


print(f"Name: {name}, Age: {age}, Bank Account: {bank_account}, Colors: {colors}")

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

# Ask the user's age

# Use if statements to determine the age group
# and create a message

# Show the message to the user



window.mainloop()  # Keeps the window open


# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.
