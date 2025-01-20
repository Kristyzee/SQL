import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
from urllib.parse import urljoin

git_user = input("Enter the GitHub username: ")

# Validate user input
if not git_user:
    print("Invalid username")
    exit()

url = f"https://github.com/{git_user}"

# Make the request to the GitHub profile
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

# Find the profile image
profile_image = soup.find("img", {"class": "avatar"})

if not profile_image:
    print("Profile image not found")
    exit()

# Get the image URL and handle relative URLs
image_url = profile_image["src"]
image_url = urljoin(url, image_url)  # Ensure it's an absolute URL

# Request the image data
image_response = requests.get(image_url)

image_data = BytesIO(image_response.content)

# Open the image using PIL
image = Image.open(image_data)

# Ask the user for the directory to save the image
save_dir = input("Enter the directory path where you want to save the image file: ")

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Ask for the filename and ensure it has a valid extension
filename = input("Enter the name for your image: ")

filename += '.jpg'  

image_path = os.path.join(save_dir, filename)

# Save the image to the specified path
image.save(image_path)
print("Success! Your image has been successfully saved")

