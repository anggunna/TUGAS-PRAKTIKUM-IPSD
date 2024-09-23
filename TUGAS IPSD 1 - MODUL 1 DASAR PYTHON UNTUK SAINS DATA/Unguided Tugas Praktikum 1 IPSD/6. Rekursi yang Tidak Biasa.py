def calculate_sequence(n):
    if n == 1:
        return [1]
    else:
        prev_sequence = calculate_sequence(n - 1)
        current_factorial = 1
        for i in range(1, n + 3):
            current_factorial *= i
        return prev_sequence + [current_factorial]

# Contoh penggunaan
n = 4
print(', '.join(map(str, calculate_sequence(n)))) 