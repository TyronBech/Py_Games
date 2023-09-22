from PIL import Image, ImageTk

def resize_img(img_path, length, height):
    image = Image.open(img_path)
    resized_image = image.resize((length, height))
    resized_photo = ImageTk.PhotoImage(resized_image)
    return resized_photo
def resized_images():
    img_path = {
        'Title' : resize_img('Mini_Games.png', 300, 120)
    }
    return img_path