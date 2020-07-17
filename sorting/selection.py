
# O(n^2)

def selection(elements):

    start = 0
    small_pos = 0

    while start < len(elements) - 1:
        for i in range(start, len(elements)):
            if elements[i] < elements[small_pos]:
                small_pos = i
        old_small = elements[start]
        elements[start] = elements[small_pos]
        elements[small_pos] = old_small
        start += 1
        small_pos = start
        print elements

    print elements




if __name__ == '__main__':
    selection([29, 64, 73, 34, 20])
    print '\n'
    selection([5, 7, 3, 1, 8, 4, 2, 9, 0, 6])
