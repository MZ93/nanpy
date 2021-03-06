from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)


class Servo(ArduinoObject):
    cfg_h_name = 'USE_Servo'

    def __init__(self, pin, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', pin)

    @arduinoobjectmethod
    def write(self, value):
        pass

    @returns(int)
    @arduinoobjectmethod
    def read(self):
        pass

    @arduinoobjectmethod
    def writeMicroseconds(self, value):
        pass

    @returns(int)
    @arduinoobjectmethod
    def readMicroseconds(self, value):
        pass

    @arduinoobjectmethod
    def attach(self, value):
        """
        The servo is attached by default.
        Use this method only if you have
        detached it previously.

        Parameters
        ___________
        value: int
            the pin to attach the servo to.
        """
        pass

    @arduinoobjectmethod
    def attached(self):
        pass

    @arduinoobjectmethod
    def detach(self):
        pass
