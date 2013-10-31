import wnck
import gtk
import sys
from screenManager import ScreenManager

screen = wnck.screen_get_default()


def f_window_on_this_workspace(window):
    if (window.get_name() == "unity-launcher" or window.get_name() == "unity-panel") and window.get_window_type() == wnck.WindowType.__enum_values__[2] and\
            window.is_on_workspace(screen.get_active_workspace()):
        return True
    return False


def switch_focus():
    while gtk.events_pending(): gtk.main_iteration()
    #gobject.MainLoop.run()

    windows = screen.get_windows_stacked()
    filtered_windows = filter(f_window_on_this_workspace,windows)

    for i in range(0,len(filtered_windows)):
		if (filtered_windows[i].get_name() == "unity-launcher"):
			(x1,y1,x2,y2)=filtered_windows[i].get_geometry()
		if (filtered_windows[i].get_name() == "unity-panel"):
			(a1,b1,a2,b2)=filtered_windows[i].get_geometry()
			
		print filtered_windows[i].get_geometry()," - ",filtered_windows[i].get_name()," - ",filtered_windows[i].get_window_type()

    print 'Total screen size ', screen.get_width(),screen.get_height()
    print 'Usable screen size', screen.get_width()-65,screen.get_height()-24

if __name__ == "__main__":
    switch_focus()
