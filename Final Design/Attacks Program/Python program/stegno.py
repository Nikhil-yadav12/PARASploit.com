from PIL import Image

def hide_message(image_path, message):
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

def reveal_message(image_path):
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
        return message

# Example usage
hide_message('image.png', 'Hello World!')
message = reveal_message('hidden_message.png')
print(message)
