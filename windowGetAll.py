import wnck
import gtk
import sys

s = wnck.screen_get_default()

'''
def f_window_on_this_workspace(window):
    if window.get_window_type() == wnck.WindowType.__enum_values__[0] and\
            window.is_on_workspace(s.get_active_workspace()):
        return True
    return False
'''

def switch_focus():
    while gtk.events_pending(): gtk.main_iteration()
    #gobject.MainLoop.run()

    windows = s.get_windows_stacked()
    #filtered_windows = filter(f_window_on_this_workspace,windows)

    for i in range(0,len(windows)):
		print windows[i].get_geometry()," - ",windows[i].get_name()," - ",windows[i].get_window_type()

if __name__ == "__main__":
    switch_focus()
