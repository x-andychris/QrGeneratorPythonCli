import requests

# getting the text to be embedded from the user
text = input("Enter text to be embedded: ")

# passing in the text into the url
url = f"https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl={text}&choe=UTF-8"

page = requests.get(url)

# choosing the name of the file where the image would be saved
image = input("Enter the destination image file: ")

# connecting to the image file
file = open(f"{image}.png","wb")
file.write(page.content)
print("Image saved successfully")