def get_parent(index):
    return (index-1)//2


def get_right(index):
    return 2*index + 2


def get_left(index):
    return 2*index + 1


class BinaryHeap:

    def __init__(self):
        self.tab = []

    def push(self, element):
        self.tab.append(element)
        self._up_heap()

    def _up_heap(self):
        elem_i = len(self.tab) - 1
        while elem_i > 0:
            parent_i = get_parent(elem_i)
            if self.tab[parent_i] <= self.tab[elem_i]:
                break
            self._swap(elem_i, parent_i)
            elem_i = parent_i

    def _swap(self, index1, index2):
        tmp = self.tab[index1]
        self.tab[index1] = self.tab[index2]
        self.tab[index2] = tmp

    def pop(self):
        last_i = len(self.tab) -1
        if len(self.tab) > 1:
            self.tab[0] = self.tab[last_i]
            del self.tab[last_i]

    def _down_heap(self):
        pass

    def print(self):
        print(self.tab)


class prim:
    pass

heap = BinaryHeap()
heap.push(9)
heap.push(11)
heap.push(2)
heap.push(1)
heap.push(4)
heap.push(3)
heap.print()










