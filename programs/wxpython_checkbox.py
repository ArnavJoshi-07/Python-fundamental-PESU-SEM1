import wx 
app = wx.App(False)
frame = wx.Frame(None,title = 'Checkbox Example',size=(300,200))
panel = wx.Panel(frame)
check = wx.CheckBox(panel,label='I Agree',pos=(100,60))
frame.Show()
app.MainLoop()