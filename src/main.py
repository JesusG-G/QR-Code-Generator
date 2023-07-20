import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from qr_code import QrCodeGenerator
from file_manager import file_manager
from shared.popup.popup import *

#Load de kv file with the design of the app
Builder.load_file('main.kv')
Builder.load_file("shared/popup/popup.kv")

class MainLayout(Widget):
    #Class imports
    qrcode = QrCodeGenerator()
    success_popup = SuccessPopup()
    fail_popup = FailPopup()
    message_error = MessageErrorPopup()
    file_error = FileErrorPopup()

    #Data biding of the kv file
    data_qr = ObjectProperty(None)

    logo_path_file: str = ''    
    def on_press(self) -> None:
        data_qr = self.data_qr.text
        logo = self.logo_path_file if self.logo_path_file else ''
        print(logo)
        if not data_qr:
            self.message_error.open()
        elif  logo != '' and not '.png' in logo:
            self.file_error.open()
        else:    
            path_to_save = self.save_file_path()
            if not path_to_save:
                self.fail_popup.open()
            else:
                generated_qr = self.qrcode.generate_qr(path_to_save,data_qr,logo)
                if generated_qr:
                    self.success_popup.open()
                else:
                    self.fail_popup.open()
        #clear input
        self.data_qr.text = ""

    def choose_file_logo(self) -> str :
        self.logo_path_file: str = file_manager.FileManager().get_path_logo()

    def save_file_path(self) -> str :
        path_file: str = file_manager.FileManager().get_path_to_file()
        return path_file

class QrGeneratorApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    app = QrGeneratorApp()
    app.run()