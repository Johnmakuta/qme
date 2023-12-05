import qrcode
from PIL import Image
# from qrcode.image.pure import PyPNGImage
# from qrcode.image import svg

def generate_colored_qrcode(url, background_color='#FFFFFF', qrcode_color='#000000', filename='qrcode.png'):
    # Create a QR code instance
    qr = qrcode.QRCode(
        # can be 1 to 40 and corresponds to qrcode size starting at 21x21, can be set to none and fit=True will auto set it. 
        version=1,
        # ERROR_CORRECT_L = 7% or less errors corrected, 
        # ERROR_CORRECT_M = 15% or less errors corrected,
        # ERROR_CORRECT_Q = 25% of less errors corrected, 
        # ERROR_CORRECT_H = 30% or less errors corrected,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        # parameter controls how many pixels 
        box_size=10,
        # number of boxes thick the border is. 4 is the minimum. 
        border=4,
        # SVG or PNG factory gen
        # image_factory=svg.SvgImage,
    )


    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color=qrcode_color, back_color=background_color)

    # Save the image to a file
    img.save(filename)

# Example usage:
data_to_encode = "https://github.com/Johnmakuta/qme"
background_hex_color = '#FF0000'  # Red background
qrcode_hex_color = '#00FF00'      # Green QR code

generate_colored_qrcode(data_to_encode, background_color=background_hex_color, qrcode_color=qrcode_hex_color)