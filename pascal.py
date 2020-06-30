#!/usr/bin/env/python

from inky import InkyPHAT
from random import randint
from PIL import Image, ImageFont, ImageDraw
import textwrap

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.open("pascal.png")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("roboto.ttf", 14)

quotes = open("allQuotes.txt", "r")
lines = quotes.readlines()
quotes.close()
lengthQuotes = len(lines)
randNo = (randint(1, lengthQuotes - 1))
randQuote = str(lines[randNo])
wrappedQuote = textwrap.wrap(randQuote, width=25)
joinedText = "\n".join(wrappedQuote)

x = 65
y = 5

draw.text((x, y), joinedText, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()
