from abc import ABC, abstractmethod
from calendar import c
from enum import Enum, auto

class FileSizeType(Enum):
    GT = auto()
    EQ = auto()
    LS = auto()
    GE = auto()
    LE = auto()
class FileMatchType(Enum):
    SIZE = 1
    EXTENSION = 2
    NAME = 3
    ALL = 4

class FileMatcher(ABC):
    @abstractmethod
    def match(self, file_name) -> bool:
        pass

class FileSizeMatcher(FileMatcher):
    def __init__(self, size, comparision: FileSizeType):
        self.size = size
        self.comparision = comparision

    def match(self, file_name) -> bool:
        return file_name.size == self.size
    
class FileExtensionMatcher(FileMatcher):
    def __init__(self, extension):
        self.extension = extension

    def match(self, file_name) -> bool:
        return file_name.endswith(self.extension)
    
class FileNameMatcher(FileMatcher):
    def __init__(self, file_name):
        self.file_name = file_name

    def match(self, file_name) -> bool:
        return self.file_name == file_name