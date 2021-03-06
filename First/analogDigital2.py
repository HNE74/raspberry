from spidev import SpiDev
import time
 
class MCP3008:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = SpiDev()
        self.open()
 
    def open(self):
        self.spi.open(self.bus, self.device)
    
    def read(self, channel = 0):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data
            
    def close(self):
        self.spi.close()
        

adc = MCP3008()
while True:
    value = adc.read(channel=0) 
    print("Anliegende Spannung: %.2f" % (value / 1023.0 * 3.3))
    time.sleep(1)
