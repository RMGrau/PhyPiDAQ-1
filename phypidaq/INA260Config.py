import sys
import board
from adafruit_ina260 import INA260

class INA260Config(object):
    """current and voltage sensor INA260"""

    def __init__(self, confdict=None):

        if confdict == None:
            confdict = {}
        if 'I2CADDR' in confdict:
            self.I2CADDR = confdict['I2CADDR']
            print("INA260Config: I2C address set to %x " % self.I2CADDR)
        if 'NChannels' in confdict:
            self.NChannels = confdict["NChannels"]
        else:
            self.NChannels = 2

        if 'maxAmp' in confdict:
            self.maxAmp = confdict['maxAmp']
        else:
            self.maxAmp = 3.19999
            print("INA260Config: Current range set to %.3fA " % self.maxAmp)

        if 'maxVolt' in confdict:
            self.maxVolt = confdict['maxVolt']
        else:
            self.maxVolt = 32.

        self.ChanLims = [[0., self.maxAmp],
                         [0., self.maxVolt],
                         [0., self.maxAmp * self.maxVolt]]
        self.ChanNams = ['I', 'U', 'P']
        self.ChanUnits = ['A', 'V', 'W']

    def init(self):

        if self.maxAmp > 3.2:
            print("!!! INA260Config: Current range must be < 3.2A")
            sys.exit(1)
        elif self.maxVolt > 32.0:
            print("!!! INA260Config: Voltage must be < 32.V")
            sys.exit(1)

        i2c = board.I2C()
        if hasattr(self, "I2CADDR"):
            self.sensor = INA260(i2c, addr=self.I2CADDR)
        else:
            self.sensor = INA260(i2c)

    def acquireData(self, buf):
        buf[0] = self.sensor.current / 1000.0  # in Amps
        if self.NChannels > 1:
            buf[1] = self.sensor.voltage
        if self.NChannels > 2:
            buf[2] = self.sensor.power / 1000.0 # in Watt

    def closeDevice(self):
        # Nothing to do here
        pass
