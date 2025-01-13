import random

num_addresses = 100000

file_name = 'random_addresses.txt'

with open(file_name, 'w') as file:
    for _ in range(num_addresses):
        random_address = random.randint(0, 2**32 - 1)
        
        binary_address = f"{random_address:032b}"
        
        file.write(f"0b{binary_address}\n")

