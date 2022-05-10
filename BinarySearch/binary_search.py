import random
import time
import matplotlib.pyplot as plt

def generate_list(n_items: int) -> list:
    """
    Generate a ordered list of size n_items with random integers from 0 to 100 

    Args:
        n_items (int): number of items in the list. List length.

    Returns:
        List: list with random values
    """

    res = [int(100*random.random()) for i in range(n_items)]
    
    return sorted(res)

def binary_search(ordered_list: list, target: int, start_idx=None, end_idx=None):
    """
    Recursive binary search function

    Args:
        ordered_list (list): Ordered list where a target is to be found
        target (int): target value to be found in the ordered list
        start_idx (int, optional): Start index for binary search, only used to make this recursive. Defaults to None.
        end_idx (int, optional): End index for binary search, only used to make this recursive. Defaults to None.

    Returns:
        int or False: return False if target value does not exist in list. If target exists in list this will return the index of the 
        target value in list
    """
    
    start_idx = start_idx or 0
    end_idx = end_idx if end_idx is not None else len(ordered_list)
    
    middle_idx = (end_idx + start_idx) // 2
    
    if start_idx == end_idx:
        return False
    if target == ordered_list[middle_idx]:
        return middle_idx
    elif target < ordered_list[middle_idx]:
        return binary_search(ordered_list, target, start_idx, middle_idx)
    else:
        return binary_search(ordered_list, target, middle_idx+1, end_idx)
    

if __name__ == '__main__':
    """
    Main function
    """
    times = []
    n = []
    for i in range(100,10000):
        list_size = i
        ordered_list = generate_list(list_size)
        target = int(100*random.random())
        start_time = time.time()
        idx = binary_search(ordered_list, target)
        end_time =time.time()
        times.append(end_time - start_time)
        n.append(i)
        print(idx if idx else "Target not found")

    plt.plot(n, times)
    plt.xlabel('List size')
    plt.ylabel('Time')
    plt.title('Linear Complexity')
    plt.show()
