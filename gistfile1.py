import wx
import os

class MyFrame(wx.Frame):
  def __init__(self):
  wx.Frame.__init__(self, None, -1, 'File Convertor',
        size=(420, 160),
        style=wx.DEFAULT_FRAME_STYLE&~(wx.MAXIMIZE_BOX))
    panel = wx.Panel(self, -1)
    sourceLabel = wx.StaticText(panel, -1, "Source file:")
    self.sourceText = wx.TextCtrl(panel, -1, "", size=(220, -1))
    self.browseButton = wx.Button(panel, -1, "Browse")
    self.Bind(wx.EVT_BUTTON, self.OnClickBrowseButton, self.browseButton)
    destLabel = wx.StaticText(panel, -1, "Dest file:")
    self.destText = wx.TextCtrl(panel, -1, "", size=(220, -1))
    sizer = wx.FlexGridSizer(cols=4, hgap=6, vgap=6)
    self.convertButton = wx.Button(panel, -1, "Convert it!")
    self.Bind(wx.EVT_BUTTON, self.OnClickConvertButton, self.convertButton)
    sizer.AddMany([
      wx.StaticText(panel, size=(20,10)), wx.StaticText(panel), wx.StaticText(panel), wx.StaticText(panel),
      wx.StaticText(panel), sourceLabel, self.sourceText, self.browseButton,
      wx.StaticText(panel), destLabel, self.destText, wx.StaticText(panel),
      wx.StaticText(panel), wx.StaticText(panel), self.convertButton])
    panel.SetSizer(sizer)
    self.CreateStatusBar()
    self.SetStatusText("Select source file")
   
  # event handler for BrowseButton   
  def OnClickBrowseButton(self, event):
    wildcard = "Source file (*.dat)|*.dat|" \
      "All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
      self.sourceText.SetValue(dialog.GetPath())
      self.destText.SetValue(dialog.GetPath())
      statusMessage = "%s is selected."%(dialog.GetPath())
      self.SetStatusText(statusMessage)
    dialog.Destroy()
     
  # event handler for ConvertButton
  def OnClickConvertButton(self, event):
    print self.sourceText.GetValue()
    print self.destText.GetValue()
    wx.MessageBox("Success", "MessageBox", wx.OK)
    self.SetStatusText("Success")

if __name__ == '__main__':
  app = wx.PySimpleApp()
  frame = MyFrame()
  frame.Show()
  app.MainLoop()