from wnck import Window
import gtk
import time

class PIWindow():
    """Controller to abstract out window functions"""

    _gravity =0
    _resizeMask = 255
    
    def __init__(self, window):
        self._window = window
       
    def get_window_size(self):
        (xPos, yPos, curLength, curHeight) = self._window.get_geometry()
        return (xPos, yPos, curLength, curHeight)

    def set_position(self, xPos, yPos):
        (xCur, yCur, length, height) = self._window.get_geometry()
        self._window.set_geometry(PIWindow._gravity, PIWindow._resizeMask, xPos, yPos, length, height)

    def set_size(self, length, height):
        (xPos, yPos, curLength, curHeight) = self._window.get_geometry()
        self._window.set_geometry(PIWindow._gravity, PIWindow._resizeMask, xPos, yPos, length, height)

    def resize(self, xPos, yPos, length, height):
        self._window.set_geometry(PIWindow._gravity, PIWindow._resizeMask, xPos, yPos, length, height)

    def maximize(self):
        if not self._window.is_maximized():        
            self._window.maximize()

    def unmaximize(self):
        if self._window.is_maximized():
            self._window.unmaximize()
            
    def minimize(self):
        self._window.minimize()

    def get_window(self):
        return self._window
    
    
