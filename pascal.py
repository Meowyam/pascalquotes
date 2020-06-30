from inky import InkyPHAT
from random import randint
from PIL import Image, ImageFont, ImageDraw

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 16)

quotes = open("allQuotes.txt", "r")
lines = quotes.readlines()
quotes.close()
lengthQuotes = len(lines)
randNo = (randint(1, lengthQuotes - 1))
randQuote = str(lines[randNo])

w, h = font.getsize(randQuote)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

#pascal = Image.open("pascal.png")
#inky_display.set_image(pascal)

draw.text((x, y), randQuote, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()
