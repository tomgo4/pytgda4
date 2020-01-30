from app_files.files_handling import FilesHandling


class CreateLogic:
    def create(self, data):
        fh = FilesHandling()
        fh.create_and_save(data["document"] + ".ddb",
                           data["columns"])
