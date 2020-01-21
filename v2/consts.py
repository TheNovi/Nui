from enum import Enum, auto


class RetCode(Enum):
	NONE = auto()
	EXIT = auto()
	OK = auto()
	UNKNOWN = auto()
	ERROR = auto()
	ARGS_ERROR = auto()
	PATH_ERROR = auto()
