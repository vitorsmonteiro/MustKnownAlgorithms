import random

def generate_list(n_items: int) -> list:
    """
    Generate a ordered list of size n_items with random integers from 0 to 100 

    Args:
        n_items (int): number of itens in the list. List length.

    Returns:
        List: list with random values
    """

    res = [int(100*random.random()) for i in range(n_items)]
    
    return sorted(res)

def binary_search(ordered_list: list, target: int):
    
    list_size = len(ordered_list)
    middle_idx = list_size // 2
    idx = 0
    
    while middle_idx > 0:   
        list_size = len(ordered_list)
        middle_idx = list_size // 2
        if target == ordered_list[middle_idx]:
            return idx + middle_idx
        elif target < ordered_list[middle_idx]:
            ordered_list = ordered_list[: middle_idx]
        else:
            ordered_list = ordered_list[middle_idx :]
            idx = idx + middle_idx
    
    return False
    

if __name__ == '__main__':
    list_size = 100
    ordered_list = generate_list(list_size)
    target = int(100*random.random())
    print(f"Ordered_list = {ordered_list}")
    print(f"Target = {target}")
    idx = binary_search(ordered_list, target)
    print(idx if idx else "Target not found")