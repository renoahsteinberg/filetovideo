class later:# Test and later use
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