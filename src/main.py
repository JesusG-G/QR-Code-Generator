import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from qr_code import QrCodeGenerator


class MainGridLayout(GridLayout):
    #Initialize infinite keywords:
    def __init__(self, **kwargs):
        self.qrcode = QrCodeGenerator()
        #Call grid layout contructor
        super(MainGridLayout, self).__init__(**kwargs)
        #Set Columns
        self.cols = 1

        #Created other gridLayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text="Introduce the name of the file.*"))
        #Add input box
        self.file_name = TextInput(multiline=False)
        self.top_grid.add_widget(self.file_name)

        #Add widgets
        self.top_grid.add_widget(Label(text="Introduce the URL or the text.*"))
        #Add input box
        self.data_qr = TextInput(multiline=False)
        self.top_grid.add_widget(self.data_qr)

        self.top_grid.add_widget(Label(text="Upload your logo for the Qr Code (Optional)"))
        #Add input box
        self.logo = TextInput(multiline=False)
        self.top_grid.add_widget(self.logo)

        #Add top_gird to the app
        self.add_widget(self.top_grid)

        #Add Button
        self.submit = Button(
            text="Generate QR CODE", 
            font_size=32,
            size_hint= (0.5,None),
            width = 300,
            height = 200,
            pos_hint = {'y':.5}
        )
        #Bind the button
        self.submit.bind(on_press = self.on_press)
        self.add_widget(self.submit)

    def on_press(self, instance):
        file_name = self.file_name.text
        file_name += '.png'
        data_qr = self.data_qr.text
        logo = self.logo.text
        if file_name == '':
            self.add_widget(Label(text='Please introduce the file name.'))
        elif data_qr == '':
            self.add_widget(Label(text='Please introduce the text or url for the QR Code.'))
        else:    
            generated_qr = self.qrcode.generate_qr(file_name,data_qr,logo,fill_color='black', background_color='white')
            if generated_qr:
                self.add_widget(Label(text=f'Successfully created {file_name}'))
            else:
                self.add_widget(Label(text='An error ocurred'))
        #clear input
        self.file_name.text = ""
        self.data_qr.text = ""
        self.logo.text = ""

class QrGeneratorApp(App):
    def build(self):
        return MainGridLayout()

if __name__ == "__main__":
    app = QrGeneratorApp()
    app.run()