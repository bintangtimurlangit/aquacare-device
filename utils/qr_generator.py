# utils/qr_generator.py
import qrcode
from qrcode.main import QRCode
import uuid

def generate_device_id():
    return str(uuid.uuid4())

def create_device_qr(device_id):
    # Create QR code instance
    qr = QRCode()
    qr.add_data(device_id)
    qr.make()
    
    # Create ASCII representation
    ascii_qr = qr.get_matrix()
    
    # Convert the QR matrix to a string
    qr_string = ""
    for row in ascii_qr:
        line = ""
        for cell in row:
            if cell:
                line += "██"  # Use full block for dark modules
            else:
                line += "  "  # Use spaces for light modules
        qr_string += line + "\n"
    
    return qr_string