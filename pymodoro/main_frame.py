import wx
import math

from about_screen import AboutScreen
from summary_frame import SummaryFrame

class MainFrame(wx.Frame):
    """Main application frame"""

    def __init__(self, steps, *args, **kwargs):
        """Initialize the frame"""

        wx.Frame.__init__(self, *args, **kwargs)

        self.summary_frame = SummaryFrame(self, wx.ID_ANY, "Status")
        self.summary_frame.Show(False)

        self.taskbar_icon = wx.TaskBarIcon()
        self.taskbar_icon.Bind(wx.EVT_TASKBAR_LEFT_UP,
                               self.on_taskbar_left_click)

        self.taskbar_icon.Bind(wx.EVT_TASKBAR_RIGHT_UP,
                               self.on_taskbar_right_click)

        self.popup_menu = self.__build_popup_menu()

        self.current_step = 0
        self.steps = steps

        self.update_tomato()

    def __build_popup_menu(self):

        menu = wx.Menu()

        summary = wx.MenuItem(menu, wx.ID_ANY, "&Summary")
        menu.AppendItem(summary)

        activities = wx.MenuItem(menu, wx.ID_ANY, "&Activities")
        menu.AppendItem(activities)

        properties = wx.MenuItem(menu, wx.ID_PROPERTIES, "&Properties")
        menu.AppendItem(properties)

        about = wx.MenuItem(menu, wx.ID_ABOUT, "A&bout")
        menu.AppendItem(about)

        menu.AppendSeparator()

        exit = wx.MenuItem(menu, wx.ID_EXIT, "&Quit")
        menu.AppendItem(exit)

        # Bind menu events
        menu.Bind(wx.EVT_MENU, self.on_menu_summary, summary)
        menu.Bind(wx.EVT_MENU, self.on_menu_activities, activities)
        menu.Bind(wx.EVT_MENU, self.on_menu_properties, properties)
        menu.Bind(wx.EVT_MENU, self.on_menu_about, about)
        menu.Bind(wx.EVT_MENU, self.on_menu_close, exit)

        return menu

    def on_taskbar_left_click(self, event):
        """Handle left click by showing or hiding the status frame"""
        self.__toggle_summary_frame()


    def __toggle_summary_frame(self):
        """Toggle the showing status of the summary frame"""
        if self.summary_frame.IsShown():
            self.summary_frame.Hide()
        else:
            self.summary_frame.Show()


    def on_taskbar_right_click(self, event):
        """Handle right click by showing the app menu"""
        self.PopupMenu(self.popup_menu)

    def on_menu_close(self, event):
        """Close the frame, so the application ends gracefully"""
        self.Close()

    def on_menu_summary(self, event):
        """Toggle the showing status of the summary frame"""
        self.toggle_summary_frame()

    def on_menu_activities(self, event):
        print "Activities"

    def on_menu_properties(self, event):
        print "Properties"

    def on_menu_about(self, event):
        wx.AboutBox(AboutScreen(self))



    def update_tomato(self):
        """Update the taskbar icon and the image, and increment the
        current_step"""

        self.icon = self.make_icon(self.current_step, self.steps)
        self.taskbar_icon.SetIcon(self.icon, "Hello World")

        self.bitmap = wx.StaticBitmap(self,
                                      bitmap=self.make_bitmap(self.current_step,
                                                              self.steps))
        self.Fit()

        self.current_step = (self.current_step + 1) % self.steps

    def make_icon(self, past_time, total_time):
        """Create an icon image based on diverse factors"""

        bitmap = self.make_bitmap(past_time, total_time)

        # Convert to icon
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(bitmap)
        return icon

    def make_bitmap(self, past_time, total_time):
        """Create an image based on the number of past units and the total
        number of units"""

        # Load the image
        bitmap = wx.Image("tomato_128.png",
                          wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        brush = wx.Brush(wx.Colour(0,200,0),wx.SOLID)

        # Draw slices to represent the past time
        dc = wx.MemoryDC(bitmap)

        dc.SetBrush(brush)
        dc.SetPen(wx.Pen("black",0,wx.TRANSPARENT))

        w,h = dc.GetSize()
        center_w = w / 2.0
        center_h = h / 2.0
        line_length = w / 2

        offset_rad = 2 * math.pi / float(total_time)

        end_point_x = center_w + (math.sin(past_time*offset_rad) * line_length)
        end_point_y = h - (center_h +
                           (math.cos(past_time*offset_rad) * line_length))

        start_point_x = center_w
        start_point_y = 0

        dc.DrawArc(start_point_x, start_point_y,
                   end_point_x, end_point_y,
                   center_w, center_h)

        # Restore old brush
        dc.SetPen(wx.NullPen)
        dc.SetBrush(wx.NullBrush)

        return bitmap
