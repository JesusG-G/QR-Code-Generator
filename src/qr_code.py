import qrcode
from PIL import Image

class QrCodeGenerator:
    def __init__(self) -> None:
            self.qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H)
    def generate_qr(self,path_to_save:str,data_qr: str,image_path: str) -> bool:
        try:
            if image_path and '.png' in image_path:
                logo = Image.open(image_path)
                print(logo)
                #Ajust the size of the image
                hsize = int(float(logo.size[1])*float(100/float(logo.size[0])))
                logo = logo.resize((100,hsize), Image.Resampling.LANCZOS)
                self.qr.add_data(data_qr)
                self.qr_image = self.qr.make_image(fill_color='black', background_color='white').convert('RGB')
                #Position of the image
                position = ((self.qr_image.size[0] - logo.size[0]) // 2, (self.qr_image.size[1] - logo.size[1]) // 2)
                self.qr_image.paste(logo,position)
                self.saveQr(path_to_save)
                return True
            elif not image_path:
                self.qr.add_data(data_qr)
                self.qr_image = self.qr.make_image(fill_color='black', background_color='white').convert('RGB')
                self.saveQr(path_to_save)
                return True
        except Exception as e:
            return e
    def saveQr(self, path_save):
        full_path = f"{path_save}.png"
        self.qr_image.save(full_path)
    
