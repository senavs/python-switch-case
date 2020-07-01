from typing import Any, MutableSequence, Optional, Union, Type


class Switch:
    _value: Any = None
    _suppress: MutableSequence[Type[Exception]] = None

    def __init__(self, value: Any, *,
                 suppress: Optional[Union[Type[Exception], MutableSequence[Type[Exception]]]] = None):
        self._value = value
        if not isinstance(suppress, MutableSequence):
            self._suppress = [suppress]
        else:
            self._suppress = suppress

    @property
    def value(self) -> Any:
        return self._value

    def __call__(self, value: Any, *args):
        return self._value in (value,) + args

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and exc_type in self._suppress:
            return True
        return False
