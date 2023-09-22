import tkinter as tk
from dict_images import resized_images

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Mini Games')
    window.config(bg='#6F61C0')
    window.geometry('450x600')
    window.resizable(False, False)
    _images = resized_images()
    Title_label = tk.Label(window, image=_images['Title'], bg='#6F61C0')
    Title_label.pack(pady=20)
    button_frame = tk.Frame(window, bg='white', width=450, height=300)
    button_frame.pack(pady=40)

    window.mainloop()