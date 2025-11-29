import wx
def on_text_change(event):
    print('Text change to: ',event.GetString())
app = wx.App()
frame = wx.Frame(None,title='text box changes',size =[300,200])
panel = wx.Panel(frame)
text_box = wx.TextCtrl(panel, pos = [20,20])
text_box.Bind(wx.EVT_TEXT,on_text_change)
frame.Show()
app.MainLoop()

