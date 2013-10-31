from wnck import Window

import wnck

from screenManager import ScreenManager
from piWindow import PIWindow
if __name__ == '__main__':
    manager = ScreenManager()
    window = PIWindow(manager.get_active_window())
    #print window.set_position(0,0)
    #print manager.get_screen_size()
    #window.set_geometry(5, 15, 1900, 24, 500, 500)
    #window.maximize()
    #print type(window.get_window().get_workspace())

    print dir(wnck.Screen)
