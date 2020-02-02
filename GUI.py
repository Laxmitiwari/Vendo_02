from guizero import App,Text
from guizero import App,TextBox
from guizero import App,PushButton
app = App(title="Welome to reverse vending mahcine")
welcome_message = Text(app,text="Please enter bottles in reversing vending machine")
my_name = TextBox(app)
update_text = PushButton(app,text="Display number of botles")
app.display

