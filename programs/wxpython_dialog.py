import wx
app = wx.App(False)
frame = wx.Frame(None, title='Dialogue Box',size=(300,200))
dialog = wx.TextEntryDialog(frame,"Enter your name","Name Input")
if dialog.ShowModal()==wx.ID_OK:
    name = dialog.GetValue()
    