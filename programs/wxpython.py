import wx 
def on_click(event):
    wx.MessageBox('BUTTON CLICKED!', 'Info')
app = wx.App()
frame = wx.Frame(None,title='Panel EXample',size=[300,200])
panel = wx.Panel(frame,style=wx.SIMPLE_BORDER)
panel.SetBackgroundColour('light blue')
btn = wx.Button(panel,label='Im on the panel',pos=[20,20])
btn.Bind(wx.EVT_BUTTON,on_click)
text = wx.TextCtrl(panel,value='TEXT',pos=[20,70],size = [200,25])
frame.Show()
app.MainLoop()

