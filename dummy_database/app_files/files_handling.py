class FilesHandling:
    def create_and_save(self, filename, data):
        with open('./' + filename, 'w') as f:
            f.write(data)
