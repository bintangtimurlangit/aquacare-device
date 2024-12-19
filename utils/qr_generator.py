# utils/qr_generator.py
import qrcode
from qrcode.main import QRCode
import uuid

def generate_device_id():
    return str(uuid.uuid4())

def create_device_qr(device_id):
    # Create QR code instance with smaller size
    qr = QRCode(
        version=1,  # Smallest QR Code version that can fit the data
        box_size=1, # Minimum box size
        border=1    # Minimum quiet zone
    )
    qr.add_data(device_id)
    qr.make(fit=True)
    
    # Create ASCII representation
    ascii_qr = qr.get_matrix()
    
    # Convert the QR matrix to a string using double blocks horizontally
    qr_string = ""
    for row in ascii_qr:
        line = ""
        for cell in row:
            if cell:
                line += "██"  # Use double blocks for dark modules
            else:
                line += "  "  # Use double spaces for light modules
        qr_string += line + "\n"
    
    return qr_string