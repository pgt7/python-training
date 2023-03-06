from converter import Converter

# This is our message
paragraph = """
This is simple paragraph for test this project. This is a python project. I am Pouria Ghafarbeigi.
I want to learn python for fun, so this project is just a simple game.
"""

paragraph2 = """
This is another example to check the converter class. I want to say thanks for watching this code. I hope it is helpful 
for you.
"""

# call converter class to work with on
print("==============================First Example===================================")

con = Converter(paragraph)
print(con.convert())

print("=============================Second Example===================================")

con2 = Converter(paragraph2)
print((con2.convert()))

print("==================================End=========================================")

