import io

from typing import TypedDict
from backend.loader.decorator import KatzukiNode
from backend.nodes.builtin import BaseNode


class PlayMusic(BaseNode):

    @KatzukiNode()
    def __init__(self) -> None:
        pass

    class ReturnDict(TypedDict):
        music: bytes

    def execute(self, path: str) -> ReturnDict:
        binary_stream = io.BytesIO()

        input_path = self.INPUT_PATH / path
        with open(input_path, "rb") as f:
            binary_stream.write(f.read())

        binary_data = binary_stream.getvalue()
        return self.ReturnDict(music=binary_data)
