import requests
from bs4 import BeautifulSoup

# Set the URL of the website
url = "https://convert.leiapix.com/"

# Set the path of the image file to upload
image_path = r"C:\Users\chris\OneDrive\Documents\history-queefs\image-to-video-automation\images\Mhodzic_Vintage_photo_of_massive_molasses_storage_tank_in_Bosto_36558462-be85-4e68-bd71-d3ed0f03c885.png"

# Set the animation length in seconds
animation_length = 6

# Make a GET request to the website
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the form on the page that uploads an image
form = soup.find("form", {"action": "/upload"})

# Extract the CSRF token from the form
csrf_token = form.find("input", {"name": "csrf_token"})["value"]

# Set the payload data to upload the image
payload = {"csrf_token": csrf_token}
files = {"file": open(image_path, "rb")}

# Make a POST request to upload the image
response = requests.post(url + "upload", data=payload, files=files)

# Parse the JSON content of the response to get the ID of the uploaded image
image_id = response.json()["id"]

# Set the payload data to generate the video
payload = {"id": image_id, "duration": animation_length}

# Make a POST request to generate the video
response = requests.post(url + "generate", data=payload)

# Parse the JSON content of the response to get the ID of the generated video
video_id = response.json()["id"]

# Make a GET request to download the video
response = requests.get(url + "download/" + video_id)

# Save the video file to disk
with open("output.mp4", "wb") as f:
    f.write(response.content)