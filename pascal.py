from inky import InkyPHAT
from random import randint
from PIL import Image, ImageFont, ImageDraw
import textwrap

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(inkyphat.fonts.AmaticSC, 12)

quotes = open("allQuotes.txt", "r")
lines = quotes.readlines()
quotes.close()
lengthQuotes = len(lines)
randNo = (randint(1, lengthQuotes - 1))
randQuote = str(lines[randNo])
wrappedQuote = textwrap.wrap(randQuote, width=18)
joinedText = "\n".join(wrappedQuote)

x = 70
y = 5

pascal = Image.open("pascal.png")
inky_display.set_image(pascal)

inky_display.text((x, y), joinedText, inky_display.BLACK, font)
inky_display.show()
