import random

# Create an if-main code block


# RANDOM WHOLE NUMBERS
random.randint(1,2)   # random.randint(start,end)
random.random (2)
random.choice(32)   # start = lower bound of random number
random.choice(5)  # end = upper bound of random number

# Prints out 5 random whole numbers between 0 and 100 (0 and 100 both included)
for i in range(5):
    number = random.randint(0, 100)
    print(number)

# TODO Print out 5 random numbers between -50 and 5
for i in range(5):
    number = random.randint(-50, 5)
    print(number)

# RANDOM DECIMAL NUMBERS
random.uniform(1.5) # random.uniform(start,end)
random.random (float) # Generates a random floating(decimal) number
random.choice(random)  # start = lower bound of random number
random.uniform(62)   # end = upper bound of random number

# Prints out 5 random decimal numbers between 1.2 and 34.5 (1.2 and 34.5 both included)
for i in range(5):
    number = random.uniform(1.2, 34.5)
    print(number)

    # TODO Print out 5 random decimal numbers between -123.45 and 67.89
for i in range(5):
    number = random.uniform(-123.45, 67.89)
    print(number)
