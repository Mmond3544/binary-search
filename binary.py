data = [1,2,5,9,10,13,14,16,19,21,25,26,28,35]

def binary(target):
    low = 0
    high = len(data) - 1
    count = 0
    mid = (low + high) //2
    while data[mid] != target:
        if low > high:
            return False
            break
        elif data[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) // 2
        count += 1
    print("Step is ",count)
    return True

target = int(input("Input target data : "))
x = binary(target)
if x == True:
    print(target," is in data set")
else:
    print(target," is not in data set")

