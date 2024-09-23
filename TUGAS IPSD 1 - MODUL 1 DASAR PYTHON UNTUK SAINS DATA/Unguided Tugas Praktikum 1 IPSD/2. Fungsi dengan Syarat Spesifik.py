def extract_odd_elements(list1, list2):
    result = []
    for i in range(1, len(list1), 2):
        result.append(list1[i])
    for i in range(1, len(list2), 2):
        result.append(list2[i])
    return sorted(result, reverse=True)

# Contoh penggunaan
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(extract_odd_elements(list1, list2))