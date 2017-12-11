class ChainHashTable:
    # size of table
    # expansion factor
    def __init__(self, size):
        self.data = [[] for _ in range(size)]
        self.size = size

    def add(self, element):
        index = hash(element) % self.size
        self.data[index].append(element)

    def find(self, element):
        index = hash(element) % self.size
        size = len(self.data[index])
        for i in range(size):
            if element == self.data[index][i]:
                return True
        return False

    def print(self):
        print(self.data)

    def delete(self, element):
        hash = hash(element) % len(self.data)
        self.data[hash].remove(element)


class HashTable:

    # def __init__(self, size):
    #     self.size = size
    #     self.data = [None for _ in range(size)]
    #     self.count = 0

    def __init__(self, size, factor=0.7):
        self.size = size
        self.data = [None for _ in range(size)]
        self.count = 0
        self.factor = factor

    def hash_2(self, element, i):
        return (hash(element) + i) % self.size

    def add(self, element):
        index0 = self.hash_2(element, 0)
        if self.data[index0] is None:
            self.data[index0] = element
            return

        i = 1
        while True:
            index = self.hash_2(element, i)
            if index == index0:
                raise Exception('Out of range')
            if self.data[index] is None:
                self.data[index] = element
                return
            else:
                i += 1

    def print(self):
        print(self.data)

    def find(self, element):
        i = 0
        index = self.hash_2(element, i)
        while self.data[index] is not None:
            if self.data[index] == element:
                return index
            else:
                i += 1
                index = self.hash_2(element, i)
        return -1

    def delete(self, element):
        data_len = len(self.data)
        index0 = self.find(element)
        if index0 != -1:
            self.data[index0] = None
        else:
            return

        index = index0 + 1
        while self.data[index] is not None:
            elem = self.data[index]
            elem_hash = hash(elem) % len(self.data)
            if elem_hash != index:
                self.data[index] = None
                self.add(elem)
            index += 1
            if index > data_len - 1:
                index = 0

    def add_with_rewrite(self, element):
        self.count += 1
        if self.count/self.size > self.factor:
            self.rewrite(element)
        else:
            self.add(element)

    def rewrite(self, element):
        old_tab = self.data
        self.size = 2 * self.size
        self.data = [[] for _ in range(self.size)]
        self.add(element)

        for x in range(len(old_tab)):
            if old_tab[x] is not None:
                self.add(x)


if __name__ == "__main__":
    import random
    import time

    import matplotlib.pyplot as plt

    ##################################################################

    elementsCountList = []
    chainTimeList = []
    openAddressTimeList = []

    findOpenAddTimeList = []
    findChainTimeList = []

    elementsCountList.append(0)
    chainTimeList.append(0)
    openAddressTimeList.append(0)
    findOpenAddTimeList.append(0)
    findChainTimeList.append(0)

    # insert data
    N = 100000
    n = 1000

    while n <= N:
        chainTable = hash_table.ChainHashTable(N)
        openAddressTable = hash_table.HashTable(N)
        elementsCountList.append(n)

        #chain
        timeStart = time.time()
        for y in range(n):
            chainTable.add(random.randint(0, N))
        timeStop = time.time()
        diff = timeStop - timeStart
        chainTimeList.append(diff)
        print('#Chain insert for' + str(n) + 'elements')

        findStart = time.time()
        chainTable.find(random.randint(0, N))
        findStop = time.time()
        findDiff = findStop - findStart
        findChainTimeList.append(findDiff)

        #open adress
        timeStart = time.time()
        for y in range(n):
            openAddressTable.add(random.randint(0, N))
        timeStop = time.time()
        diff = timeStop - timeStart
        openAddressTimeList.append(diff)
        print('#Open address insert for' + str(n) + 'elements')

        findStart = time.time()
        openAddressTable.find(random.randint(0, N))
        findStop = time.time()
        findDiff = findStop - findStart
        findOpenAddTimeList.append(findDiff)
        n += 1000


    plt.figure(1)

    plt.subplot(121)
    plt.xlabel('n elements')
    plt.ylabel('insert time')
    plt.title('chain insert method')
    plt.plot(elementsCountList, chainTimeList)

    plt.subplot(122)
    plt.xlabel('n elements')
    plt.ylabel('insert time')
    plt.title('open addressing insert method')
    plt.plot(elementsCountList, openAddressTimeList)

    plt.show()

    plt.figure(1)
    sumChain = 0
    sumOpen = 0
    count = len(elementsCountList)
    for i in range(count):
        sumChain += findChainTimeList[i]
        sumOpen += findOpenAddTimeList[i]

    avgChainTime = sumChain/count
    avgOpenAddTime = sumOpen/count

    plt.bar(['Open addressing find method avg', 'Chain find method avg'],
            [avgOpenAddTime, avgChainTime])

    plt.show()

    # Remove example
    print('Removing elements with rewrite others')
    openAddressTable = HashTable(10)

    print('Adding elements in order: 5, 55, 555, 9, 6')
    openAddressTable.add(5)
    openAddressTable.add(55)
    openAddressTable.add(9)
    openAddressTable.add(555)
    openAddressTable.add(6)
    openAddressTable.add(10)
    openAddressTable.print()

    print('Deleting element: 5')
    openAddressTable.delete(5)
    openAddressTable.print()

    print('Deleting element: 55')
    openAddressTable.delete(55)
    openAddressTable.print()
