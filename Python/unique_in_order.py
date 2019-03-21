#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    result = [iterable[0]]
    for i in iterable:
        if result[-1] != i:
            result.append(i)
    return result
