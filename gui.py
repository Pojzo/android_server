import tkinter as tk
from config import *

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(RESIZABLE, RESIZABLE)
        self.create_widgets()
    
    # i just need a text box, which will be used to display the data
    # the input box will be used to send data to the client
    # the send button will be used to send the data in the input box to the client
    def create_widgets(self) -> None:
        recv_msg_text = tk.Text(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        send_msg_input = tk.Entry(self, width=WINDOW_WIDTH)
        send_button = tk.Button(self, text="Send", width=WINDOW_WIDTH, command=lambda: self.send_data(send_msg_input.get(), recv_msg_text))



gui = GUI()