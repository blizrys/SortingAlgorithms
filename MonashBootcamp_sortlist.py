'''
Task:
Write a function that sorts a list of numbers in ascending order.

Include:
- A comment at the top of the file explaining how the code works (to a beginner) and why it works (i.e. the intuition).
- Your sorting code, which is entirely in the body of a function
- Comments that explain the purpose of sections/lines of code
- Entry code to run your function, including some test cases that show the code works and covers some edge cases

Comments:
- Do not use variables outside the scope of the function unless they are only used in the test cases
- Do not use Python's sorting functions or other functions that would make the task trivial
- Do not use libraries for the sorting
- The code should be written such that anyone with basic programming knowledge can follow and reasonably understand what's going on
'''

''' 
### Personal comment ###
This is code I have create when prepare and practice for python exam in sem1 2020.
There are multiple ways of sorting. For the BootCamp task I'll only explain bubble_sort since it's the very basic.
If you want more explaination on other type of sort. Contact me.
The code will start from the 'main' section.
'''


def bubble_sort(raw_list):
    # get length of the list
    n = len(raw_list)

    '''Concept : bubble sort
    # bubble sort idea is that the we will the high number will keep floating up to the top of the list
    # for example
    # [5,2,3,4,1] raw
    # [2,3,4,1,5] 1st loop
    # [2,3,1,4,5] 2nd loop
    # [2,1,3,4,5] 3nd loop
    # [1,2,3,4,5] 4nd loop
    '''

    # Think of i & j is the cursor that point into the list
    # i run loops from n-1 to 0 to point the location highest number of each round should be float to.
    #          i            i            i
    # [5,2,3,4,1] >> [2,3,4,1,5] >> [2,3,1,4,5] >> ...
    for i in range(n - 1, 0, -1):
        # j run loops from 0 to i
        #  j       i        j     i          j   i
        # [5,2,3,4,1] >> [2,5,3,4,1] >> [2,3,5,4,1] >> ...
        for j in range(i):
            # if number in 'position j' is larger than 'next position j+1' then swap values
            if (raw_list[j] > raw_list[j + 1]):
                temp = raw_list[j]
                raw_list[j] = raw_list[j + 1]
                raw_list[j + 1] = temp
        # print(raw_list)
    return raw_list


def selection_sort(raw_list):
    n = len(raw_list)

    for i in range(n):
        index_min = i
        for j in range(i + 1, n):
            if (raw_list[j] < raw_list[index_min]):
                index_min = j
        temp = raw_list[index_min]
        raw_list[index_min] = raw_list[i]
        raw_list[i] = temp
        # print(raw_list)
    return raw_list


def insertion_sort(raw_list):
    n = len(raw_list)

    for i in range(n):
        for j in range(i, 0, -1):
            # print(j, j - 1)
            if (raw_list[j] < raw_list[j - 1]):
                temp = raw_list[j]
                raw_list[j] = raw_list[j - 1]
                raw_list[j - 1] = temp
            else:
                break
        # print(raw_list)
    return raw_list


def shake_sort(raw_list):
    n = len(raw_list)

    for i in range(0, n-1):
        # print("up")
        for j in range(i,n-1-i):
            # print(j,j+1)
            if (raw_list[j] > raw_list[j + 1]):
                temp = raw_list[j]
                raw_list[j] = raw_list[j + 1]
                raw_list[j + 1] = temp

        # print("down")
        for j in range(n-2-i,i,-1):
            # print(j,j-1)
            if (raw_list[j-1] > raw_list[j]):
                temp = raw_list[j-1]
                raw_list[j-1] = raw_list[j]
                raw_list[j] = temp

    return raw_list


def merge_sort(raw_list):
    n = len(raw_list)

    if (n > 1):
        index_mid = n // 2
        left_list = raw_list[0:index_mid]
        right_list = raw_list[index_mid:]
        # print("Split", left_list, right_list)
        merge_sort(left_list)
        merge_sort(right_list)

        # print("before merge", left_list, right_list)
        i = 0
        l = 0
        r = 0
        while (l < len(left_list) and r < len(right_list)):
            if (left_list[l] < right_list[r]):
                raw_list[i] = left_list[l]
                l += 1
            else:
                raw_list[i] = right_list[r]
                r += 1
            i += 1

        while (l < len(left_list)):
            raw_list[i] = left_list[l]
            l += 1
            i += 1

        while (r < len(right_list)):
            raw_list[i] = right_list[r]
            r += 1
            i += 1
        # print("Merge",raw_list)
    return raw_list


def quick_sort_partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quick_sort_aux(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = quick_sort_partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort_aux(arr, low, pi - 1)
        quick_sort_aux(arr, pi + 1, high)


def quick_sort(raw_list):
    n = len(raw_list)
    quick_sort_aux(raw_list, 0, n - 1)
    return raw_list


def main():
    # Getting input
    # raw_string = input() # read from standard input
    # raw_list = raw_string.split() # split the string into list
    # items = [int(x) for x in raw_list] # convert each item in list from string into integer

    # Or use predefine input
    items = [5, 3, 1, 9, 7, 8, 3, 6, 1, 3, 4, 7, 8, 9, 4, 4, 63, 51, 234, 23, 7, 573, 2, 43, 64, 3743, 56, 436]

    # call function of each type of sort.
    print("raw :", items)
    print("bub :", bubble_sort(items.copy())) # We will only explore this type of sort for Bootcamp
    print("sel :", selection_sort(items.copy()))
    print("ins :", insertion_sort(items.copy()))
    print("mgr :", merge_sort(items.copy()))
    print("qik :", quick_sort(items.copy()))
    print("shk :", shake_sort(items.copy()))

if __name__ == '__main__':
    main()