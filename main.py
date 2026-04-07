from PIL import Image

img = Image.open("input.jpg")

resized = img.resize((200, 200))

resized.save("output.jpg")

print("Изображение обработано")