import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)

#resp = spi.xfer2([0xA])
#print(hex(resp[0]))

#spi.writebytes([5,6])
x=0
while x<20:
  x=x+1
  deneme = spi.readbytes(10)
  print(type(deneme))
  print(type(deneme[0]))
  print(deneme)
  time.sleep(0.5)
