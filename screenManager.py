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
        
    def get_usable_size(self):
	    windowStack = self.screen.get_windows_stacked()
	    for i in range(0,len(windowStack)):
		if (windowStack[i].get_name() == "unity-launcher"):
		        (xPos1,yPos1,wid1,hei1)=windowStack[i].get_geometry()
	        if (windowStack[i].get_name() == "unity-panel"):
		        (xPos2,yPos2,wid2,hei2)=windowStack[i].get_geometry()
		
	    useWidth = self.screen.get_width()-wid1
       	    useHeight = self.screen.get_height()-hei2
	    #print windowStack[i].get_geometry()," - ",windowStack[i].get_name()," - ",windowStack[i].get_window_type()
 	    #print 'Total screen size ', self.screen.get_width(),self.screen.get_height()
	    #print 'Usable screen size',useWidth ,useHeight
	    #print 'Origin is',wid1,',',hei2
	    return (useWidth,useHeight,wid1,hei2)
