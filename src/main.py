import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from qr_code import QrCodeGenerator

class GridLayaout(GridLayout):
    #Initialize infinite keywords:
    def __init__(self, **kwargs):
        self.qrcode = QrCodeGenerator(size=30, padding=2)
        #Call grid layout contructor
        super(GridLayaout, self).__init__(**kwargs)
        #Set Columns
        self.cols = 2

        self.add_widget(Label(text="Introduce the name of the file"))
        #Add input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        #Add widgets
        self.add_widget(Label(text="Introduce the URL or the text"))
        #Add input box
        self.data_qr = TextInput(multiline=False)
        self.add_widget(self.data_qr)

        self.add_widget(Label(text="Upload your logo for the Qr Code (Optional)"))
        #Add input box
        self.logo = TextInput(multiline=False)
        self.add_widget(self.logo)

        #Add Button
        self.submit = Button(text="Submit", font_size=32)
        #Bind the button
        self.submit.bind(on_press = self.on_press)
        self.add_widget(self.submit)

    def on_press(self, instance):
        name = self.name.text
        data_qr = self.data_qr.text
        logo = self.logo.text
        self.qrcode.generate_qr(file_name=name,data_qr=data_qr,fill_color='black', background_color='white')
        #self.add_widget(Label(text=f"name: {name} pizza: {pizza}"))

        #clear input
        self.name.text = ""
        self.data_qr.text = ""
        self.logo.text = ""

class QrGeneratorApp(App):
    def build(self):
        return GridLayaout()

if __name__ == "__main__":
    app = QrGeneratorApp()
    app.run()