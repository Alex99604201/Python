def sumnumbers(n): # (*args) неоганиченное коллво аргументов
    summa = 0
    for i in range(1, n+1):
        summa += 1
    print(summa)  # return summa

sumnumbers(5)     # print(sumnumbers(5))


# rekursia

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

# быстрая сортировка

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pylot = array[0]
    less = [i for i in array[1:] if i <= pylot]
    greator = [i for i in array[1:] if i > pylot]
    return quick_sort(less) + [pylot] + quick_sort(greator)

print(quick_sort([1, 5, 3]))

# сортировка слияния

def marge_sort(nums):
    if len(nums) > 1:
        min = len(nums) // 2
        left = nums[:min]
        right = nums[min:]
        marge_sort(left)
        marge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k +=1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k +=1

list1 = [1, 2, 6, 7, 8, 4, 11, 35, 57]
print(marge_sort(list1))