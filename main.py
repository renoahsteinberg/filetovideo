#!/usr/bin/env python

import os
import uuid


class File:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.name_ext = os.path.basename(self.file_path)

class CreateImageFile(File):
    def __init__(self, file: File):
        self.file = file

    def _get_file_header(self):
        # uuid as seperator for filename.extension to ensure
        # a certain degree of uniqueness,
        # probability of breaking is minimized, i guess
        unique_id = uuid.uuid4()
        seperator = f'###UNIQUE_{unique_id}###'
        encapsulated_data = f'{seperator}{self.file.name_ext}{seperator}IMFUCKINGTRED'
        return encapsulated_data.encode()

    # just for testing and later usage 
    def _read_file_header_for_recreation(self):
        data = self._get_file_header().decode()
        file = data.split(data[:49])
        # file[1] -> filename.extension
        # file[2] -> file information


    def _read_file_binary(self):
        pass



file_path = "/home/clay/projects/filetovideo/testfiles/testfile.txt"

cfi = CreateImageFile(File(file_path))._read_file_header_for_recreation()








"""
class RecreateFile:
    def recreate_file(file_destination):
        # create path if not exist
        if not os.path.exist(file_destination):
            os.makedirs(file_destination)

        # will be read from created file later on, just for now
        new_file = os.path.join(file_destination, file_name_extension)

        # create new file and write contents
        with open(new_file, 'w') as f:
            pass
"""
