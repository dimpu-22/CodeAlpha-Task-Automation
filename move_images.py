import os
import shutil

source_folder = "Source"
destination_folder = "Destination"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Move all JPG files
for file in os.listdir(source_folder):
    print("Found:", file)      # Debug
    if file.lower().endswith(".jpg"):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )
        print("Moved:", file)
        
print("All JPG files moved successfully!")

