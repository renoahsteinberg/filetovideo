#!/usr/bin/env python


import os
import uuid
import re


class File:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.name_ext = os.path.basename(self.file_path)

class CreateImageFile(File):
    def __init__(self, file: File):
        self.file = file

    def _create_file_header(self):
        # UUID as separator for filename.extension to ensure uniqueness
        unique_id = uuid.uuid4()
        seperator = f'###UNIQUE_{unique_id}###'
        encapsulated_data = f'{seperator}{self.file.name_ext}{seperator}IMFUCKINGTIRED'
        return encapsulated_data.encode()

    def _file_to_bits(self):
        pass

    def _bits_to_colors(self):
        pass

    def _create_image(self):
        pass

    def _create_video(self):
        pass

    # Test and later use
    def _read_file_header_for_recreation(self):
        data = self._create_file_header().decode()
        
        pattern = r'###UNIQUE_([a-f0-9\-]{36})###(.*?)###UNIQUE_\1###(.*)'
        
        match = re.match(pattern, data)
        
        if match:
            unique_id = match.group(1)
            filename_ext = match.group(2)
            file_info = match.group(3)

            return {
                'unique_id': unique_id,
                'filename_ext': filename_ext,
                'file_info': file_info
                }
        else:
            raise ValueError('Header format is incorrect')


    def _read_file_binary(self):
        pass



file_path = "/home/clay/projects/filetovideo/testfiles/testfile.txt"

cfi = print(CreateImageFile(File(file_path))._read_file_header_for_recreation())