from outputs.output import Output


class FileOutput(Output):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def write(self, message: str) -> None:
        with open(self.file_path, "a") as file:
            file.write(message + "\n")