
from functools import cmp_to_key
def cmp(ele1, ele2):
    if ele1[1] > ele2[1]:
        return 1
    elif ele1[1] < ele2[1]:
        return -1
    else:  # ele1[1] == ele2[1]
        if ele1[0] > ele2[0]:
            return 1
        elif ele1[0] < ele2[0]:
            return -1
        else:  # ele1 == ele2
            return 0


if __name__ == '__main__':
    l = [(-1, 1), (5, 1), (4, 3), (4, 1)]
    print(l)
    l.sort(key=cmp_to_key(cmp), reverse=True)
    print(l)
