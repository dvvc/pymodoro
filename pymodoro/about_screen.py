import wx
from wx.lib.wordwrap import wordwrap

desc = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec mattis tortor sodales tellus pulvinar mattis porttitor diam tristique. Curabitur rutrum augue sit amet tellus ultricies dignissim laoreet purus tempus. Proin sem lectus, iaculis non consectetur ut, placerat quis lectus. Donec pulvinar, arcu non iaculis consectetur, tortor diam tincidunt augue, eleifend aliquet augue erat mollis neque. 

Morbi iaculis blandit orci et laoreet. Ut nec est nunc, sit amet ultricies nulla. Nunc consectetur, nisi sit amet venenatis placerat, lorem augue feugiat justo, at ultricies urna risus ut nulla. Duis fermentum leo vel neque tempor quis sagittis justo dapibus. Curabitur nec nulla elit, at ullamcorper nunc. Curabitur eleifend sem id tortor aliquet quis volutpat velit aliquet. Duis facilisis convallis viverra."""


class AboutScreen(wx.AboutDialogInfo):
    """Pymodoro application about dialog"""
    
    def __init__(self, frame):
        """Initialize the dialog"""

        wx.AboutDialogInfo.__init__(self)

        self.Name = "Pymodoro"
        self.Version = "0.1.1"
        self.Copyright = "(C) Foobar 2009"
        self.Description = wordwrap(desc, 350, wx.ClientDC(frame))
        self.WebSite = "http://www.no-sync.com"
        self.Developers = ["Foo Bar", "John Doe"]
        self.License = wordwrap(desc, 500, wx.ClientDC(frame))




