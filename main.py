import tkinter as tk
from dict_images import resized_images


def hover_image(event, flag):
    if flag == 0:
        RPS_button.config(image=images['RPS_hover'])
    elif flag == 1:
        RPS_button.config(image=images['RPS'])
    elif flag == 2:
        TTT_button.config(image=images['TTT_hover'])
    elif flag == 3:
        TTT_button.config(image=images['TTT'])
    elif flag == 4:
        HM_button.config(image=images['HM_hover'])
    elif flag == 5:
        HM_button.config(image=images['HM'])

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Mini Games')
    window.config(bg='#6F61C0')
    window.geometry('450x600')
    window.resizable(False, False)
    images = resized_images()
    Title_label = tk.Label(window, image=images['Title'], bg='#6F61C0')
    Title_label.pack(pady=20)
    button_frame = tk.Frame(window, bg='#6F61C0', width=180, height=300)
    button_frame.pack(pady=30)
    RPS_button = tk.Button(
        button_frame, image=images['RPS'], bg='#6F61C0', borderwidth=0, activebackground='#6F61C0')
    RPS_button.grid(row=0, column=0, pady=5)
    RPS_button.bind('<Enter>', lambda event, flag=0: hover_image(event, flag))
    RPS_button.bind('<Leave>', lambda event, flag=1: hover_image(event, flag))
    TTT_button = tk.Button(
        button_frame, image=images['TTT'], bg='#6F61C0', borderwidth=0, activebackground='#6F61C0')
    TTT_button.grid(row=1, column=0, pady=5)
    TTT_button.bind('<Enter>', lambda event, flag=2: hover_image(event, flag))
    TTT_button.bind('<Leave>', lambda event, flag=3: hover_image(event, flag))
    HM_button = tk.Button(
        button_frame, image=images['HM'], bg='#6F61C0', borderwidth=0, activebackground='#6F61C0')
    HM_button.grid(row=2, column=0, pady=5)
    HM_button.bind('<Enter>', lambda event, flag=4: hover_image(event, flag))
    HM_button.bind('<Leave>', lambda event, flag=5: hover_image(event, flag))
    window.mainloop()
