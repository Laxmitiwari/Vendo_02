from guizero import App, Window, Text, PushButton
def open_window():
    window.show()
def close_window():
    window.hide()
app = App(title="Welocme to reverse Vending Machine")
text = Text(app,text="Please enter bottlein RVM")
window = Window(app,title="welcome to reverse Vending Machine")
text = Text(window,text="Thank you for entering bottles in RVM")
window.hide()
open_button = PushButton(app, text="Start", command=open_window)
close_button = PushButton(window,text="End", command=close_window)

app.display
