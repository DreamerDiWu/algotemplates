def sortBinary(array):
    num_ones = sum(array)
    zero_idx = []
    one_idx = []
    for i in range(len(array)):
        if array[i] == 0:
            zero_idx.append(i)
        else:
            one_idx.append(i)

    # assume ones are all in left side
    need_move_zeros = 0
    left_length = num_ones
    for i in range(left_length):
        if array[i] == 0:
            need_move_zeros += one_idx.pop() - i 

    # assume ones are all in right side 
    need_move_ones = 0
    left_length = len(array)-num_ones
    for i in range(left_length):
        if array[i] == 1:
            need_move_ones += zero_idx.pop() - i 
    return min(need_move_ones, need_move_zeros)

if __name__ == '__main__':
    cases = [
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 1]
    ]
    for case in cases:
        print(case, sortBinary(case))