from outputs.output import Output


class StdoutOutput(Output):

    def write(self, message: str) -> None:
        print(message)