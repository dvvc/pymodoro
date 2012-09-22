import wx

class SummaryFrame(wx.Frame):
    """A frame to show the status of the current pomodoro"""

    def __init__(self, *args, **kwargs):
        """Initialize the frame"""

        wx.Frame.__init__(self, *args, **kwargs)
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        """Handle closing by just hiding the window"""

        self.Show(False)
