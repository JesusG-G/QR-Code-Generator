import qrcode

class QrCodeGenerator:
    def __init__(self, size:int, padding: int) -> None:
        self.qr = qrcode.QRCode(box_size=size, border=padding)
    
    def generate_qr(self, file_name:str,data_qr: str, fill_color: str, background_color: str):
        try:
            self.qr.add_data(data_qr)
            qr_image = self.qr.make_image(fill_color= fill_color,back_color= background_color).convert('RGB')
            qr_image.save(file_name)
            print(f'Successfully created {file_name}')
        except Exception as e:
            print(f"Error: {e}")
    def saveQr(self):
        self.qr.save
    
