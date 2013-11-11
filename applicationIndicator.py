
import pygtk
pygtk.require('2.0')
import gtk
import appindicator
import pynotify

from piWindow import PIWindow 
from screenManager import ScreenManager

manager = ScreenManager()
window_handle = PIWindow(manager.get_active_window())	
(usable_width,usable_height,xorigin, yorigin)=manager.get_usable_size()

class PlaceItIndicator:
    
    def __init__(self):
        self.ind = appindicator.Indicator ("example-simple-client", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status (appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon ("indicator-messages-red")
        self.ind.set_icon("distributor-logo")
        
        self.menu = gtk.Menu()
        
        agr = gtk.AccelGroup()

	#Add menu items
	#First Batch	 Maximize,Minimize,Restore
        menuMaximize = gtk.MenuItem("Maximize")
        menuMaximize.connect("activate", self.win_maximize,"Maximize")
        
        self.menu.append(menuMaximize)
        
        menuMinimize = gtk.MenuItem("Minimize")
        key, mod = gtk.accelerator_parse("<Ctrl><Alt>N")
        menuMinimize.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
        menuMinimize.connect("activate", self.win_minimize,"Minimize")
        
         
        self.menu.append(menuMinimize)
        
        menuRestore = gtk.MenuItem("Restore")
        menuRestore.connect("activate",self.win_restore,"Restore")
        self.menu.append(menuRestore)
        
        seperator1 = gtk.SeparatorMenuItem()
        self.menu.append(seperator1)
	
	#Second Batch	Right,Left,Top,Down
        menuRight = gtk.MenuItem("Right")
        menuRight.connect("activate", self.win_right,"Right")
        self.menu.append(menuRight)
        
        menuLeft = gtk.MenuItem("Left")
        menuLeft.connect("activate", self.win_left,"Left")
        self.menu.append(menuLeft)
        
        menuTop = gtk.MenuItem("Top")
        menuTop.connect("activate", self.win_top,"Top")
        self.menu.append(menuTop)
        
        menuDown = gtk.MenuItem("Down")
        menuDown.connect("activate", self.win_down,"Down")
        self.menu.append(menuDown)
        
        seperator2 = gtk.SeparatorMenuItem()
        self.menu.append(seperator2)
       
	#Third Batch		Upper Right,Upper Left,Lower Right,Lower Left
        menuUpRight = gtk.MenuItem("Upper Right")
        menuUpRight.connect("activate", self.win_upRight,"upperRight")
        self.menu.append(menuUpRight)
        
        menuUpLeft = gtk.MenuItem("Upper Left")
        menuUpLeft.connect("activate", self.win_upLeft,"upperLeft")
        self.menu.append(menuUpLeft)
        
        menuLowRight = gtk.MenuItem("Lower Right")
        menuLowRight.connect("activate", self.win_lowRight,"lowerRight")
        self.menu.append(menuLowRight)
        
        menuLowLeft = gtk.MenuItem("Lower Left")
        menuLowLeft.connect("activate", self.win_lowLeft,"lowerLeft")
        self.menu.append(menuLowLeft)
        
        menuCenter = gtk.MenuItem("Center")
        menuCenter.connect("activate", self.win_center,"center")
        self.menu.append(menuCenter)
        
        seperator3 = gtk.SeparatorMenuItem()
        self.menu.append(seperator3)
        
        #Fourth Batch          About,Preferences
        menuAbout = gtk.MenuItem("About Place-It")
        menuAbout.connect("activate", self.win_about,"About")
        self.menu.append(menuAbout)
        
        menuPref = gtk.MenuItem("Preferences...")
        menuPref.connect("activate", self.win_app_Pref,"Preferences")
        self.menu.append(menuPref)
        
	## Quit
        menuQuit = gtk.MenuItem('Quit')
        menuQuit.connect('activate', self.quit)
        self.menu.append(menuQuit)  
		            
        self.menu.show_all()
        self.ind.set_menu(self.menu)
		
	##Menu Listener
	
    def quit(self, widget, data=None):
        gtk.main_quit()
       
    def win_maximize(self, widget, param):
	window_handle.maximize()
        print param

    def win_minimize(self, widget, param):
    	window_handle.minimize()
        print param

    def win_restore(self, widget, param):
        window_handle.unmaximize()
        print param
        
    def win_center(self, widget, param):
    	(xPos, yPos, curWidth, curHeight) = window_handle.get_window_size()
    	window_handle.resize( (((usable_width/2)+xorigin)-(curWidth/2)), (((usable_height/2)+yorigin)-(curHeight/2)), curWidth, curHeight)
    	print param
    	#(xPos, yPos, curWidth, curHeight) = self._window.get_geometry()
    	#window_handle.resize( (((usable_width/2)+xorigin)-(curWidth/2)), (((usable_height/2)+yorigin)-(curHeight/2)), curWidth, curHeight)
	

    def win_right(self, widget, param):
    	window_handle.resize((usable_width/2)+xorigin, yorigin, usable_width/2, usable_height)
    	print ((usable_width/2)+xorigin, yorigin, usable_width/2, usable_height)
        print param

    def win_left(self, widget, param):
	window_handle.resize(xorigin, yorigin, usable_width/2, usable_height)
    	print (xorigin, yorigin, usable_width/2, usable_height)
        print param

    def win_top(self, widget, param):
    	window_handle.resize(xorigin, yorigin,usable_width,usable_height/2)
        print param

    def win_down(self, widget, param):
    	window_handle.resize(xorigin, (usable_height/2)+yorigin,usable_width,usable_height/2)
    	print (xorigin, (usable_height/2)+yorigin,usable_width,usable_height/2)
        print param

    def win_upRight(self, widget, param):
    	window_handle.resize((usable_width/2)+xorigin, yorigin, usable_width/2, usable_height/2)
        print param

    def win_upLeft(self, widget, param):
        window_handle.resize(xorigin, yorigin, usable_width/2, usable_height/2)
        print param

    def win_lowRight(self, widget, param):
    	window_handle.resize((usable_width/2)+xorigin, (usable_height/2)+yorigin, usable_width/2, usable_height/2)
        print param

    def win_lowLeft(self, widget, param):
    	window_handle.resize(xorigin, (usable_height/2)+yorigin, usable_width/2, usable_height/2)
        print param

    def win_about(self, widget, param):
           print param

    def win_app_Pref(self, widget, param):
           print param
           pynotify.init('wallch_indicator')
	   n = pynotify.Notification('hello there')
           n.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    indicator = PlaceItIndicator()
    main()
