from PIL import Image
import numpy as np

def subtract_images(image_path_1, image_path_2, output_path):
    """
    Subtract the second image from the first and save the result.

    Parameters:
    - image_path_1: Path to the first PNG image.
    - image_path_2: Path to the second PNG image to subtract from the first.
    - output_path: Path where the output image will be saved.
    """
    # Open the images
    image1 = Image.open(image_path_1).convert('RGBA')
    image2 = Image.open(image_path_2).convert('RGBA')

    # Convert images to numpy arrays for subtraction
    arr1 = np.array(image1, dtype=np.uint8)
    arr2 = np.array(image2, dtype=np.uint8)

    result_arr = np.power(arr1, 5)

    # Perform subtraction and ensure values stay within the valid range
    # result_arr = arr1 ** 2
    result_arr = np.clip(result_arr, 0, 255)

    # Convert the result back to an image
    result_image = Image.fromarray(result_arr.astype('uint8'), 'RGBA')

    # Save the result
    result_image.save(output_path)
    print(f"Result saved to {output_path}")



base_path = 'E:\SteamLibrary\steamapps\common\Last Oasis Testing SDK\Game\Content\Mods\OasisAdriftCanyons\External\HardMedium'
# Example usage
subtract_images(base_path + '\Python\PerlinMask.png',
                base_path + '\Out\Lakes.png',
                base_path + '\Python\SaltLakes.png')