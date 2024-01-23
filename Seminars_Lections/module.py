def max1(a,b): # сравнение значений
    if a>b:
        return a
    return b

def fib(n): # пример рекурсии на числе фиббоначи
    if n in [1,2]: # базис или выход из рекурсии
        return 1 
    return fib(n-1) + fib(n-2)
list1 = []
for i in range(1,10):
    list1.append(fib(i))
print(list1)

def quick_sort(array): # быстрая сортировка через рекурсию
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([2, 5, 10, 3]))

def mer_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        mer_sort(left)
        mer_sort(right)
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
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1, 232, 34, 5, 6, 5, 8]
mer_sort(list1)
print(list1)

def txt_separator(separator):
    separator = "!,.?@:;"
    for i in separator:
        text = input(''.join(text.split(i)))
print(len(set(text.split())))

