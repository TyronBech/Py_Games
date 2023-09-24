from PIL import Image, ImageTk

def resize_img(img_path, length, height):
    image = Image.open(img_path)
    resized_image = image.resize((length, height))
    resized_photo = ImageTk.PhotoImage(resized_image)
    return resized_photo
def resized_images():
    img_path = {
        'Title' : resize_img('Images\\Title.png', 330, 180),
        'RPS' : resize_img('Images\\RPS.png', 140, 75),
        'TTT' : resize_img('Images\\TTT.png', 140, 75),
        'HM' : resize_img('Images\\HM.png', 140, 75),
        'RPS_title' : resize_img('Images\\RPS_title.png', 330, 150),
        'Rock' : resize_img('Images\\Rock.png', 130, 65),
        'Paper': resize_img("Images\\Paper.png", 130, 65),
        'Scissors' : resize_img('Images\\Scissors.png', 130, 65),
        'Exit' : resize_img('Images\\Exit.png', 130, 65),
        'Rock_hand' : resize_img('Images\\Rock_hand.png', 70, 70),
        'Paper_hand' : resize_img('Images\\Paper_hand.png', 70, 70),
        'Scissors_hand' : resize_img('Images\\Scissors_hand.png', 70, 70),
        'vs' : resize_img('Images\\vs.png', 50, 50),
        'Rock_computer' : resize_img('Images\\Rock_computer.png', 70, 70),
        'Paper_computer' : resize_img('Images\\Paper_computer.png', 70, 70),
        'Scissors_computer' : resize_img('Images\\Scissors_computer.png', 70, 70),
        'Try_again' : resize_img('Images\\Try_again.png', 130, 65),
        'TTT_title' : resize_img('Images\\TTT_title.png', 330, 130),
        'blank_b' : resize_img('Images\\blank_button.png', 130, 130),
        'x_b' : resize_img('Images\\x_button.png', 130, 130),
        'o_b' : resize_img('Images\\o_button.png', 130, 130),
        'green_x_b' : resize_img('Images\\green_x_button.png', 130, 130),
        'green_o_b' : resize_img('Images\\green_o_button.png', 130, 130),
        'red_x_b' : resize_img('Images\\red_x_button.png', 130, 130),
        'red_o_b' : resize_img('Images\\red_o_button.png', 130, 130),
    }
    return img_path