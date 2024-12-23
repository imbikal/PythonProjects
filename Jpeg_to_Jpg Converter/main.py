from PIL import Image
import os

def convert_jpeg_to_jpg(source_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpeg"):
            # Construct full file paths
            source_path = os.path.join(source_folder, filename)
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            destination_path = os.path.join(destination_folder, new_filename)

            # Open and save as .jpg
            with Image.open(source_path) as img:
                img.save(destination_path, "JPEG")
                print(f"Converted: {source_path} -> {destination_path}")

# Define folder paths (adjust according to your folder names)
source_folder = os.path.join("jpeg")  # Source folder is 'jpeg'
destination_folder = os.path.join("jpegresized")  # Destination folder is 'jpegresized'

# Run the conversion
convert_jpeg_to_jpg(source_folder, destination_folder)
