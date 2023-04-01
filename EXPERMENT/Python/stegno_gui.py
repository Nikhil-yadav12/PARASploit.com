from tkinter import *
from PIL import Image

class App:
    def __init__(self, master):
        # Create a frame for the widgets
        frame = Frame(master)
        frame.pack()

        # Add label and entry widgets for the message and image file
        self.message_label = Label(frame, text="Message:")
        self.message_label.pack()
        self.message_entry = Entry(frame)
        self.message_entry.pack()

        self.image_label = Label(frame, text="Image file:")
        self.image_label.pack()
        self.image_entry = Entry(frame)
        self.image_entry.pack()

        # Add buttons for hiding and revealing messages
        self.hide_button = Button(frame, text="Hide message", command=self.hide_message)
        self.hide_button.pack()
        self.reveal_button = Button(frame, text="Reveal message", command=self.reveal_message)
        self.reveal_button.pack()

    def hide_message(self):
        # Get the message and image file paths from the entry widgets
        message = self.message_entry.get()
        image_path = self.image_entry.get()

        # Call the hide_message function from the original code to hide the message in the image
        with Image.open(image_path) as image:
            # get image size
            width, height = image.size
            # convert message to binary
            binary_message = ''.join(format(ord(i), '08b') for i in message)
            # pad message to fit in image
            message_length = len(binary_message)
            if message_length > width * height * 3:
                raise ValueError("Message is too long to fit in the image.")
            padded_message = binary_message + '0' * (width * height * 3 - message_length)
            # iterate over image pixels and hide message
            image_data = image.getdata()
            pixels = list(image_data)
            for i, pixel in enumerate(pixels):
                pixel = list(pixel)
                for j, channel in enumerate(pixel):
                    if padded_message:
                        bit = int(padded_message[0])
                        padded_message = padded_message[1:]
                        pixel[j] = (channel & ~1) | bit
                pixels[i] = tuple(pixel)
            image_data = Image.new(mode=image.mode, size=image.size)
            image_data.putdata(pixels)
            # save the modified image
            image_data.save('hidden_message.png')

        # Show a message box to indicate that the message has been hidden in the image
        message = "The message has been hidden in the image."
        messagebox.showinfo("Message Hidden", message)

    def reveal_message(self):
        # Get the image file path from the entry widget
        image_path = self.image_entry.get()

        # Call the reveal_message function from the original code to reveal the message from the image
        with Image.open(image_path) as image:
            # get image size
            width, height = image.size
            # retrieve message from image
            binary_message = ''
            pixels = list(image.getdata())
            for pixel in pixels:
                for channel in pixel:
                    binary_message += str(channel & 1)
            # remove padding from message
            binary_message = binary_message.rstrip('0')
            # convert message from binary to string
            message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

        # Show a message box to display the revealed message
        if message:
            messagebox.showinfo("Message Revealed", message)
        else:
            messagebox.showwarning("No Message Found", "No hidden message was")