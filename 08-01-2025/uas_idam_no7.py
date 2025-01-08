def sum_lists(list_a, list_b):
    return [a + b for a, b in zip(list_a, list_b)]

list_a = [1, 2, 4, 8]
list_b = [16, 32, 64, 128]
print(list_a)
print(list_b)

result = sum_lists(list_a, list_b)

print("Hasil penjumlahan dari List A dan List B:", result)