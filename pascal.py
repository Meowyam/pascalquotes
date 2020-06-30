from inky import inkyPHAT
from random import randint
from PIL import Image, ImageFont, ImageDraw

inky_display = inkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_amatic_sc import AmaticSC
font = ImageFont.truetype(AmaticSC, 16)

quotes = open("allQuotes.txt", "r")
lines = quotes.readlines()
quotes.close()
lengthQuotes = len(lines)
randQuote = (randint(1, lengthQuotes - 1))

w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

pascal = Image.open("pascal.png")
inky_display.set_image(pascal)

draw.text((x, y), randQuote, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()
