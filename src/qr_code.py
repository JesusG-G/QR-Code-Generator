import qrcode
from PIL import Image

class QrCodeGenerator:
    def __init__(self) -> None:
            self.qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H)
    def generate_qr(self, file_name:str,data_qr: str,image_path: str, fill_color: str, background_color: str) -> bool:
        try:
            if image_path and ('.png' in image_path  or '.jpg' in image_path):
                logo = Image.open(image_path)
                print(logo)
                #Ajust the size of the image
                hsize = int(float(logo.size[1])*float(100/float(logo.size[0])))
                logo = logo.resize((100,hsize), Image.Resampling.LANCZOS)
                self.qr.add_data(data_qr)
                qr_image = self.qr.make_image(fill_color= fill_color,back_color= background_color).convert('RGB')
                #Position of the image
                position = ((qr_image.size[0] - logo.size[0]) // 2, (qr_image.size[1] - logo.size[1]) // 2)
                qr_image.paste(logo,position)
                qr_image.save(file_name)
                return True
            elif not image_path:
                self.qr.add_data(data_qr)
                qr_image = self.qr.make_image(fill_color= fill_color,back_color= background_color).convert('RGB')
                qr_image.save(file_name)
                return True
        except Exception as e:
            return e
    def saveQr(self):
        self.qr.save
    
