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

palette = Image.new('P', (1, 1))
palette.putpalette(
[
    255, 255, 255,   # 0 = White
    0, 0, 0,         # 1 = Black
    255, 0, 0,       # 2 = Red (255, 255, 0 for yellow)
] + [0, 0, 0] * 253  # Zero fill the rest of the 256 colour palette

pascal = Image.open("pascal.png")
pascalQuant = pascalQuant.quantize(colors=3, palette=palette)
inky_display.set_image(pascal)

draw.text((x, y), randQuote, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()
