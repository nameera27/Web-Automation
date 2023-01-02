from pywinauto import application
import time

app = application.Application()
app.start('Notepad.exe')

dlg = app.window(title='Untitled - Notepad')
time.sleep(1)
n = 'Hello World!!'
for i in n:
    app.Notepad.Edit.type_keys(i)
    time.sleep(1)
time.sleep(2)
app.Notepad.menu_select('File->SaveAs')
time.sleep(1)
app.SaveAs.Edit.set_edit_text('Automated Notepad')
time.sleep(1)
app.SaveAs.Save.click(double=True)