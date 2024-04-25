from PIL import Image
import numpy as np
import noise
import os


def generate_perlin_noise_heightmap(width, height, scale=100, octaves=6, persistence=0.5, lacunarity=2.0,
                                    output_dir='output', file_name='PerlinMask.png'):
    """Generate a Perlin noise heightmap and save to the specified output directory."""

    os.makedirs(output_dir, exist_ok=True)

    # Create a grid of points (x, y)
    x_indices = np.linspace(0, width / scale, width, endpoint=False)
    y_indices = np.linspace(0, height / scale, height, endpoint=False)
    x_grid, y_grid = np.meshgrid(x_indices, y_indices)

    # Vectorized evaluation of the Perlin noise over the grid
    vectorized_noise = np.vectorize(noise.pnoise2)
    heightmap = vectorized_noise(x_grid, y_grid, octaves=octaves, persistence=persistence, lacunarity=lacunarity,
                                 repeatx=width, repeaty=height, base=0)

    # Normalize the heightmap to the range [0, 1]
    heightmap_normalized = (heightmap + 1) / 2

    # Convert the heightmap to an image
    image = Image.fromarray(np.uint8(heightmap_normalized * 255), 'L')
    image_path = os.path.join(output_dir, file_name)
    image.save(image_path)
    print(f"Heightmap saved to {image_path}")


# Example usage
generate_perlin_noise_heightmap(width=8129, height=8129, scale=25, output_dir='E:\SteamLibrary\steamapps\common\Last Oasis Testing SDK\Game\Content\Mods\OasisAdriftCanyons\External\HardMedium\Python')