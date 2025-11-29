import wx
app = wx.App(False)
frame = wx.Frame(None,title='Draw Rectangle EXample ',size =(300,200))
panel = wx.Panel(frame)
def on_paint(event):
    dc = wx.PaintDC(panel)
    dc.SetPen(wx.Pen('blue',width = 2))
    dc.SetBrush(wx.Brush('Pink'))
    dc.DrawRectangle(100,40,150,80)
panel.Bind(wx.EVT_PAINT,on_paint)
frame.Show()
app.MainLoop()
