import wnck
import gtk
import time
 
class ScreenManager:
    """A simple WindowManager to get windows and populate attributes in them"""
    def __init__(self):
        self.screen = wnck.screen_get_default()
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

    def get_screen_size(self):
        return (self.screen_width, self.screen_height)

    def get_active_window(self):
        self.screen.force_update()	
        while gtk.events_pending():
            gtk.main_iteration()		
        return self.screen.get_active_window()
