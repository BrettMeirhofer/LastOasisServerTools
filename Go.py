from PIL import Image
import os
import shutil
import subprocess
from pathlib import Path

# List of folder paths you want to delete
folder_paths = [
    'E:\SteamLibrary\steamapps\common\Last Oasis Testing SDK\Game\Content\Mods\OasisAdriftCanyons\Height',
    'E:\SteamLibrary\steamapps\common\Last Oasis Testing SDK\Game\Content\Mods\OasisAdriftCanyons\OasisAdriftCanyons_sharedassets',
]

"""
for folder_path in folder_paths:
    folder = Path(folder_path)
    if folder.is_dir():
        shutil.rmtree(folder)
        print(f"Deleted: {folder}")
    else:
        print(f"Folder not found: {folder}")
"""


# Configuration
source_folder = 'E:\SteamLibrary\steamapps\common\Last Oasis Testing SDK\Game\Content\Mods\OasisAdriftCanyons\External\HardMedium\Out'
destination_folder = 'E:\SteamLibrary\steamapps\common\Last Oasis Testing SDK\Game\Content\Mods\OasisAdriftCanyons\External\HardMedium\Tiles'
TilesNumX = 8  # Number of horizontal tiles
TilesNumY = 8  # Number of vertical tiles

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Process each PNG file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".png"):
        image_path = os.path.join(source_folder, filename)
        img = Image.open(image_path)

        img_width, img_height = img.size
        tile_width = img_width // TilesNumX
        tile_height = img_height // TilesNumY

        for x in range(TilesNumX):
            for y in range(TilesNumY):
                # Define the bounding box for the tile
                left = x * tile_width
                upper = y * tile_height

                # Adjust right and lower for overlap, except for the last tiles in each row/column
                right = left + tile_width + (1 if x < TilesNumX - 1 else 0)
                lower = upper + tile_height + (1 if y < TilesNumY - 1 else 0)

                # Ensure we don't go out of bounds
                right = min(right, img_width)
                lower = min(lower, img_height)

                bbox = (left, upper, right, lower)

                # Crop the image to the bounding box to create the tile
                tile = img.crop(bbox)
                tile = tile.resize((1009, 1009))

                # Define the tile's filename
                base_name = os.path.splitext(filename)[0]

                out_folder = destination_folder
                if base_name == "Height":
                    out_folder += '\Height'

                tile_filename = f"{base_name}_X{x}_Y{y}.png"
                tile_path = os.path.join(out_folder, tile_filename)

                # Save the tile
                tile.save(tile_path, format='PNG')

print("Tiling complete.")


#try:
 #   result = subprocess.run(["E:\SteamLibrary\steamapps\common\Last Oasis Testing SDK\RunDevKit.bat"], check=True, text=True, capture_output=True)
#    print(f"STDOUT: {result.stdout}")
#    print(f"STDERR: {result.stderr}")
#except subprocess.CalledProcessError as e:
 #   print(f"Error occurred: {e}")

