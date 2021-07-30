#REVERSE ARRAY


list = [1,5,6,2,9,3,4,8]

def reverse(lst):

    start_index = 0

    last_index = len(list) - 1

    while last_index > start_index:
        list[start_index], list[last_index] = list[last_index], list[start_index]
        start_index = start_index + 1
        last_index = last_index - 1

if __name__ == '__main__' :
    reverse(list)
    print(list)