from PIL import Image, ImageTk

def resize_img(img_path, length, height):
    image = Image.open(img_path)
    resized_image = image.resize((length, height))
    resized_photo = ImageTk.PhotoImage(resized_image)
    return resized_photo
def resized_images():
    img_path = {
        'Title' : resize_img('Title.png', 330, 180),
        'RPS' : resize_img('RPS.png', 140, 75),
        'RPS_hover' : resize_img('RPS_hover.png', 140, 75),
        'TTT' : resize_img('TTT.png', 140, 75),
        'TTT_hover' : resize_img('TTT_hover.png', 140, 75),
        'HM' : resize_img('HM.png', 140, 75),
        'HM_hover' : resize_img('HM_hover.png', 140, 75)
    }
    return img_path