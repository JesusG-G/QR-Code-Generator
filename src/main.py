import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from qr_code import QrCodeGenerator

#Load de kv file with the design of the app
Builder.load_file('main.kv')
class MainLayout(Widget):
    qrcode = QrCodeGenerator()
    file_name = ObjectProperty(None)
    data_qr = ObjectProperty(None)
    logo = ObjectProperty(None)
        
    def on_press(self):
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
    def choose_file_logo() -> str :
        path_file: str = ''
        return path_file
class QrGeneratorApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    app = QrGeneratorApp()
    app.run()