import qrcode
from random_word import RandomWords


def generator_qr():
    # pip install uuid
    # pip install qrcode
    r = RandomWords()
    text = r.get_random_word()
    list = [text]
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")
    list.append("C:/Users/abdul/PycharmProjects/sab/bot/qr.png")
    return list
