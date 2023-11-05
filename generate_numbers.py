import numpy as np

np.random.seed(43)

def generate_numbers(size):
    sorted_nums = []
    random_nums = []
    reversed_nums = []

    for _ in range(size):
        sorted_nums.append(np.random.randint(0, size))
    sorted_nums.sort()

    for _ in range(size):
        random_nums.append(np.random.randint(0, size))
    
    for _ in range(size):
        reversed_nums.append(np.random.randint(0, size))
    reversed_nums.sort(reverse=True)

    return sorted_nums, random_nums, reversed_nums

def write_to_txt(sorted_nums, random_nums, reversed_nums, ukuran):
    sorted_file = open(f'dataset_{ukuran}/sorted.txt', 'w')
    for num in sorted_nums:
        sorted_file.write(f'{num}\n')
    sorted_file.close()

    random_file = open(f'dataset_{ukuran}/random.txt', 'w')
    for num in random_nums:
        random_file.write(f'{num}\n')
    random_file.close()

    reversed_file = open(f'dataset_{ukuran}/reversed.txt', 'w')
    for num in reversed_nums:
        reversed_file.write(f'{num}\n')
    reversed_file.close()
    

KECIL = 2 ** 9
SEDANG = 2 ** 13
BESAR = 2 ** 16


sorted_nums_small, random_nums_small, reversed_nums_small = generate_numbers(KECIL)
sorted_nums_medium, random_nums_medium, reversed_nums_medium = generate_numbers(SEDANG)
sorted_nums_large, random_nums_large, reversed_nums_large = generate_numbers(BESAR)

write_to_txt(sorted_nums_small, random_nums_small, reversed_nums_small, 'kecil')
write_to_txt(sorted_nums_medium, random_nums_medium, reversed_nums_medium, 'sedang')
write_to_txt(sorted_nums_large, random_nums_large, reversed_nums_large, 'besar')