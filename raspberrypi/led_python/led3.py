import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 60)
import time




for i in range(2,60):
	pixels[i] = (255, 0, 0)
	time.sleep(0.1)

for i in range(1,60):
	pixels[i] = (0,255,0)
	time.sleep(0.1)

for i in range(60):
	pixels[i] = (0,0,255)
	time.sleep(0.1)
	pixels[i] = (0,0,0)


