import sys

from enum import Enum


class Status(Enum):
    Possible = True
    Impossible = False


class ABBADiv1(object):
    @staticmethod
    def move_one(input_str):
        return input_str + 'A'

    @staticmethod
    def move_two(input_str):
        return 'B' + input_str[::-1]

    def canObtain(self, initial, target):
        if initial == target:
            return Status.Possible
        elif target.find(initial) == -1 and target.find(initial[::-1]) == -1:
            return Status.Impossible
        elif len(initial) < len(target):
            if (self.canObtain(self.move_one(initial), target).value or
                    self.canObtain(self.move_two(initial), target).value):
                return Status.Possible
        else:
            raise Exception('initial should be shorter than or equal to the '
                            'length of target')

        return Status.Impossible

if __name__ == '__main__':
    assert len(sys.argv) == 3
    print(ABBADiv1().canObtain(sys.argv[1], sys.argv[2]).name)
