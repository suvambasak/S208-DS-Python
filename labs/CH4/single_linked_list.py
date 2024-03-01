class _Node:
    '''One list node for SingleLinkedList
    - Holds one data item 
    - One link (address) to next Node
    - The link for the last node is None
    - The link is None by default
    '''

    def __init__(self, data: any) -> None:
        '''Creates a new node

        Paramters
        ------
        data: any
            Data of any type e.g.: int, float, str, etc
        '''
        self._data: any = data
        self._next: _Node | None = None


class SingleLinkedList:
    '''Linked list with a single link to the next node'''

    def __init__(self) -> None:
        'Creates Single linked list'
        self.__head: _Node | None = None

    def append(self, data: any) -> None:
        '''Adds new data item at the end of the list

        Paramters
        ------
        data: any
            Data of any type e.g.: int, float, str, etc
        '''

        if self.__head is None:
            self.__head = _Node(data)
        else:
            _thead = self.__head
            while _thead._next is not None:
                _thead = _thead._next
            _thead._next = _Node(data)

    def __repr__(self) -> str:
        'Gives the view of the entire list'
        _thead = self.__head
        _view = ''
        while _thead is not None:
            _view += f'{_thead._data}, '
            _thead = _thead._next
        return _view

    def __len__(self) -> int:
        'Gives the length of the list'
        _thead = self.__head
        _count = 0
        while _thead is not None:
            _count += 1
            _thead = _thead._next
        return _count

    def add_item(self, data: any, index: int) -> None:
        '''Add new data item at the given index

        Paramters
        ------
        data: any
            Data of any type e.g.: int, float, str, etc
        index: int
            The index of the list
        '''

    def remove_item(self, index: int) -> None:
        '''Remove data item from the given index

        Paramters
        ------
        index: int
            The index of the list
        '''

    def search(self, item: any) -> int:
        '''Search for the data item in the list

        Paramters
        ------
        item: any
            Data

        Returns
        ------
        int | None:
            Index of the item if found else -1
        '''

    def reverse(self) -> None:
        '''Reverse the links of the list i.e.: a -> b will become a <- b'''


if __name__ == '__main__':

    l = SingleLinkedList()

    for i in range(10):
        l.append(i)

    print(l)
    print(len(l))

    l.reverse()
    l.add_item(33, 1)
    l.remove_item(3)

    print(l)
