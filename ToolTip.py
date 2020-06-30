from tkinter import *

class ToolTip(object):
    """
    This class creates a tip with the info box
    when you hoover the mouse's pointer on the label
    
    :param widget: Tkinter Label
    """

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def _showtip(self, text):
        """Display text in tooltip window"""
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 30
        y = y + cy + self.widget.winfo_rooty() - 20
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                    background="#ffffe0", relief=SOLID, borderwidth=1,
                    font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def _hidetip(self):
        """Hide tooltip when pointer is moved away"""
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip._showtip(text)
    def leave(event):
        toolTip._hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)