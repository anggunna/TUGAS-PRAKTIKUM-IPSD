def binary_search_even(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:   
            right = mid - 1

    if target % 2 != 0:
        print(f"Maaf, nilai {target} tidak ditemukan dalam daftar.")
    return -1

# Contoh penggunaan
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(binary_search_even(numbers, 6))  
print(binary_search_even(numbers, 16))  