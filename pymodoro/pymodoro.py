#!/usr/bin/python

"""
This application implements a pomodoro-based time tracking tool. Its main
window is a taskbar icon
Features:
  * Show time progression in taskbar
  * Show alert when pomodoro ends
  * Keep track of current activity
  * Produce a list of activities at the end of the day or week
"""

import wx

from main_frame import MainFrame

class PomodoroApp(wx.App):

    def __init__(self, *args, **kwargs):
        """Initialize the application"""

        wx.App.__init__(self, *args, **kwargs)

        # Create a hidden frame to act as the applications main frame
        self.frame = MainFrame(25, None, wx.ID_ANY, "Test Frame")
        self.frame.Show(False)

        self.frame.Bind(wx.EVT_CLOSE, self.on_close)

        # Create the timer in charge of the ticks
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(1000)

        self.MainLoop()

    def on_close(self, event):
        """Handle closing event"""

        # destroy the timer
        self.timer.Destroy()
        event.Skip()

    def on_timer(self, event):
        """Handle timer event"""
        self.frame.update_tomato()

if __name__ == "__main__":
    PomodoroApp()
