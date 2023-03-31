import time
# Import time module for calulate the execution time of each function


def bin_search(x, s):
    """
    This function find key "x" in list "s" by binary search.

    Parameters:
        x (int): The key that we Search for
        s (list): The list we look for key in that

    Returns:
        Boolean: If "x" in "s" it returns "True" and if isn't it doesn't return anything.
    """
    start_binary_time = time.perf_counter()
    # Define "start_binary_time" variable for calculate the execution time of this function.
    low = 0
    high = len(s) - 1
    # "low" indicates start and "high" indicates end of the list
    while low <= high:
        mid = (low + high) // 2
        if x == s[mid]:
            end_binary_time = time.perf_counter()
            print("binary search time = {:.6f}".format(end_binary_time - start_binary_time))
            # Define "end_binary_time" to calculate the duration of function execution by
            # "end_binary_time - start_binary_time" and print it.
            return True
        elif x < s[mid]:
            high = mid - 1
        else:
            low = mid + 1
    # In this while loop calculate "mid" that refers to middle of the list,
    # We divide the list into two parts in the middle.
    # If key is bigger than "s[mid]" we set"high" equal to "mid - 1" and if it is smaller than "s[mid]"
    # we set "low" equal to "mid + 1".
    # If key is equal to "s[mid]" we found the key and return "True".
    end_binary_time = time.perf_counter()
    print("binary search time = {:.6f}".format(end_binary_time - start_binary_time))
    # It same as line 24 and 25


def seq_search(m, ls):
    """
    This function find key "m" in list "s" by sequence search.

    Parameters:
        m (int): The key that we search for
        ls (list): The list we look for key in that

    Returns:
        Boolean: If "m" in "ls" it returns "True" and if isn't it returns "False".
    """
    start_sequence_time = time.perf_counter()
    # Define "start_seqeunce_time" variable for calculate the execution time of this function.
    location = 0
    while (location <= (len(ls) - 1)) and (ls[location] != m):
        location += 1
    if location > len(ls) - 1:
        end_sequence_time = time.perf_counter()
        print("sequence serchtime = {:.6f}".format(end_sequence_time - start_sequence_time))
        # Define "end_sequence_time" to calculate the duration of function execution by
        # "end_sequence_time - start_sequence_time" and print it.
        return False
    else:
        end_sequence_time = time.perf_counter()
        print("sequenece search time = {:.6f}".format(end_sequence_time - start_sequence_time))
        # It same is line 58 and 59
        return True
    # We define "location" as a pointer. While this pointer is on a number in list
    # and that element isn't equal to the key the poiter one index moves forward.
    # If we find an elemant that equals to the key returns "True".
    # and if the value of "location" is bigger than the last index of list it shows that
    # the pointer go through the list and doesn't found an element that equals to the key and function returns "False".


# test = []
# for i in range(10001):
#     test.append(i)
# bin_search(10000, test)
# seq_search(10000, test)
# Uncommand the upper lines to see the time difference of execution of functions.
