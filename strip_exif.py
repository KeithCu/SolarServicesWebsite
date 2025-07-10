from PIL import Image
import os

image_dir = 'C:/Users/keith/OneDrive/Desktop/SolarWebsite/static'

# Get all files in the directory
all_files = os.listdir(image_dir)

# Filter for .webp files
image_files = [f for f in all_files if f.lower().endswith('.webp')]

print(f"Found {len(image_files)} .webp files to process.")

for filename in image_files:
    filepath = os.path.join(image_dir, filename)
    try:
        image = Image.open(filepath)
        # The 'info' dictionary holds metadata. For WebP, it might contain EXIF.
        exif_data = image.info.get('exif')

        if exif_data:
            print(f"Found EXIF data in {filename}. Removing it.")
            # Re-saving the image without the exif data
            image.save(filepath)
            print(f"Removed EXIF data from {filename}")
        else:
            print(f"No EXIF data found in {filename}. No changes made.")

    except Exception as e:
        print(f"Could not process {filename}: {e}")
