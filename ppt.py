import win32com
from win32com.client import Dispatch,constants

ppt = win32com.client.Dispatch('PowerPoint.Application')
ppt.Visible = 1
pptSel = ppt.Presentations.Open('E:/1/1.ppt')
win32com.client.gencache.EnsureDispatch('PowerPoint.Application')
f = open("E:/1/1.txt","w",encoding='utf-8')
slide_count = pptSel.Slides.Count
for i in range(1,slide_count + 1):
    shape_count = pptSel.Slides(i).Shapes.Count
    print(shape_count)
    for j in range(1,shape_count + 1):
        if pptSel.Slides(i).Shapes(j).HasTextFrame:
            s = pptSel.Slides(i).Shapes(j).TextFrame.TextRange.Text
            f.write(s + "\n")


f.close()
ppt.Quit()