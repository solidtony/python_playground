from enum import Enum


class StrCompEnum(Enum):
    def __str__(self):
        return self.value

    def __eq__(self, other):
        return str(self).lower() == str(other).lower()


class Layout(StrCompEnum):
    VERTICAL = 'vertical'
    HORIZONTAL = 'horizontal'
