import qrcode
from PIL import Image

def generate_qr_code(data: str, filename: str, fill_color: str, back_color: str, border: int):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=border,
    )
    
    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image to a file
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")

    # Show the generated QR code
    img.show()

if __name__ == "__main__":
    # Input data for QR code
    data = input("Enter the data or URL for the QR Code: ")
    filename = input("Enter the filename to save the QR Code (e.g., 'qrcode.png'): ")
    fill_color = input("Enter the fill color (default 'black'): ") or 'black'
    back_color = input("Enter the background color (default 'white'): ") or 'white'
    border = int(input("Enter the border size (default 4): ") or 4)

    # Generate the QR code
    try:
        generate_qr_code(data, filename, fill_color, back_color, border)
    except Exception as e:
        print(f"An error occurred: {e}")
