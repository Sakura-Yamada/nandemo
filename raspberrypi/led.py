import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 30)

pixels[0] = (255, 0, 0)
#pixels.fill((0, 255, 0))

for i in range(30):
	pixels[i] = (255, 0, 0)
	time.sleep(0.1)
	if i==0:
		continue
	pixels[i-1] = (0,0,0)

time.sleep(3)
pixels.fill((0, 0, 0))
