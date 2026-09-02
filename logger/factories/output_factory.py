from enums import OutputType
from outputs.file_output import FileOutput
from outputs.output import Output
from outputs.stdout_output import StdoutOutput


class OutputFactory:

    @staticmethod
    def get_output(
        output_type: OutputType,
        file_path: str | None = None,
    ) -> Output:

        if output_type == OutputType.STDOUT:
            return StdoutOutput()

        if output_type == OutputType.FILE:
            if file_path is None:
                raise ValueError(
                    "file_path is required for file output"
                )

            return FileOutput(file_path)

        raise ValueError(
            f"Unsupported output type: {output_type}"
        )