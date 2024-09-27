#!/usr/bin/env python


import os
import re
import uuid
import math
import imageio
from PIL import Image
from tqdm import tqdm


class File:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.name_ext = os.path.basename(self.file_path)
        self.binary_data = None

        try:
            with open(self.file_path, 'rb') as f:
                self.binary_data = self._create_file_header() + f.read()
        except Exception as e:
            print(f"An error occurred: {e}")

    def _create_file_header(self):
        # UUID as separator for filename.extension to ensure uniqueness
        unique_id = uuid.uuid4()
        seperator = f'###UNIQUE_{unique_id}###'
        encapsulated_data = f'{seperator}{self.name_ext}{seperator}'
        return encapsulated_data.encode()


class CreateImageFile(File):
    def __init__(self, file: File, image_width=1920, image_height=1080):
        self.file = file
        self.image_width = image_width
        self.image_height = image_height

    # if gif = true -> gif is being created
    # if gif = false -> video (mp4) is being created <- TODO
    def _create_images(self, gif=True):
        block_size = 2 # 2x2 pixel blocks (incase of youtube decompression)
        bits_per_image = (self.image_width // block_size) * (self.image_height // block_size)
        total_bits = len(self.file.binary_data) * 8
        total_images = math.ceil(total_bits / bits_per_image)
        images = []

        bit_idx = 0

        for _ in tqdm(range(total_images), desc="Creating images"):
            image = Image.new('1', (self.image_width, self.image_height))
            pixels = image.load()

            for y in range(0, self.image_height, block_size):
                for x in range(0, self.image_width, block_size):
                    if bit_idx < total_bits:
                        byte_idx = bit_idx // 8
                        inner_bit_idx = bit_idx % 8
                        bit = (self.file.binary_data[byte_idx] >> (7 - inner_bit_idx)) & 1
                        bit_idx += 1
                    else:
                        bit = 0
                    
                    for dy in range(block_size):
                        for dx in range(block_size):
                            pixels[x + dx, y + dy] = bit
            
            images.append(image.convert('L'))

        return images

    # actual video will be implemented later, im kinda tired
    def _create_gif(self):
        images = self._create_images()

        images[0].save(
            f"{self.file.name_ext}.gif",
            save_all=True,
            append_images=images[1:],
            duration = 0.1 * 1000,
            loop=0
        )



file_path = "./testfiles/putty.exe"

cfi = CreateImageFile(File(file_path))._create_gif()