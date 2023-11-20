from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DataRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Sample(_message.Message):
    __slots__ = ["image", "label"]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    image: bytes
    label: int
    def __init__(self, image: _Optional[bytes] = ..., label: _Optional[int] = ...) -> None: ...
