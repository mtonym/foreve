# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


class MinMaxStack:
    def __init__(self):
        self.data = []
        self.mindata = []
        self.maxdata = []

    def push(self, value: int):
        self.data.append(value)

        if len(self.data) == 1:
            self.mindata.append(value)
            self.maxdata.append(value)
        else:
            if self.mindata[-1] > value:
                self.mindata.append(value)
            else:
                self.mindata.append(self.min())

            if self.maxdata[-1] < value:
                self.maxdata.append(value)
            else:
                self.maxdata.append(self.max())

    def pop(self):
        self.mindata.pop()
        self.maxdata.pop()
        return self.data.pop()

    def min(self):
        return self.mindata[-1]

    def max(self):
        return self.maxdata[-1]

    def __repr__(self):
        return str(self.data) + f" ------ MIN({self.min()}), ----- MAX({self.max()})"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = MinMaxStack()
    for i in [3, 4, 5, 6, 2, 2, 1, 4, 6, 0, -1]:
        s.push(i)
        print(s)

    print(s)
    s.pop()
    print(s)
    s.pop()
    print(s)
    s.push(100)
    print(s)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
