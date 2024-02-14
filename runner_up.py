if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    largest_num = int(arr[-1])  # The most right number of a sorted list is the largest
    # iterating to get the runner-up
    i = -1
    while (int(arr[i])== largest_num):
        i-= 1
    print(int(arr[i])) 