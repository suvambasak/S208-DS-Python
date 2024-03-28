class _Node:
    '''One list node for DoubleLinkedList
    - Holds one data item 
    - Next link (address) to next Node
    - Prev link (address) to previous Node
    - The links for the last node is None
    - The links is None by default
    '''

    def __init__(self, data: any) -> None:
        '''Creates a new node

        Paramters
        ------
        data: any
            Data of any type e.g.: int, float, str, etc
        '''
        self._data: any = data

        self._left: _Node | None = None
        self._right: _Node | None = None


def insert(root: _Node, data: any) -> _Node:
    '''Inserts a new node with the given data into the binary search tree.

    Parameters
    ------
    root: _Node
        The root node of the binary search tree
    data: any
        Data to be inserted into the binary search tree

    Returns
    ------
    _Node
        The root node of the modified binary search tree after insertion
    '''


def in_order(root: _Node):
    '''Performs inorder traversal of a binary search tree.

    Parameters
    ------
    root: _Node
        The root node of the binary search tree
    '''


def pre_order(root: _Node):
    '''Performs preorder traversal of a binary search tree.

    Parameters
    ------
    root: _Node
        The root node of the binary search tree
    '''


def post_order(root: _Node):
    '''Performs postorder traversal of a binary search tree.

    Parameters
    ------
    root: _Node
        The root node of the binary search tree
    '''


if __name__ == '__main__':
    root = None

    root = insert(root, 33)
    root = insert(root, 40)
    root = insert(root, 30)
    root = insert(root, 10)
    root = insert(root, 15)
    root = insert(root, 50)
    root = insert(root, 37)

    root = insert(root, 5)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 9)
    root = insert(root, 8)

    print('\nPre-order traversal: ')
    pre_order(root)

    print('\n\nIn-order traversal: ')
    in_order(root)

    print('\n\nPost-order traversal: ')
    post_order(root)

    print()
