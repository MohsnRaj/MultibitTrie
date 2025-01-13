from multibit_trie import MultibitTrie
from collections import defaultdict
file_path = 'prefix-list.txt'  
LookUpfile= 'random_addresses.txt'

def read_lookup_file(file_name):
    binary_numbers = []  
    
    with open(file_name, 'r') as file:
        for line in file:
           
            binary_number = line.strip()[2:]  # Remove the '0b' part
            binary_numbers.append(binary_number)  # Append to the list
    
    return binary_numbers

def process_table(file_name):
    length_dict = defaultdict(list)
    
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 3:
                try:
                    prefix, length, next_hop = parts[0], int(parts[1]), int(parts[2])
                    length_dict[length].append([prefix, length, next_hop])
                except ValueError:
                    # Handle invalid lines
                    print(f"Invalid line format (not able to parse): {line.strip()}")
    
    # Sort each list of prefixes in the dictionary
    for key, value in length_dict.items():
        value.sort(key=lambda x: x[0])
    
    # Convert defaultdict to a regular dict with keys from 0 to 32
    return {length: length_dict[length] for length in range(33)}

trie = MultibitTrie(stride=1
                    
                    
                    ,Base=16)

Forwarding_table= process_table(file_path)

for length, entries in Forwarding_table.items():
    for prefix, _, next_hop in entries:
        if length == 0:
            trie.root.next_hop = next_hop
        else:
            trie.insert(prefix, length, next_hop)
            
            
addresses_to_lookup = read_lookup_file(LookUpfile)
# for address in addresses_to_lookup:
#     search_time = trie.measure_search_time(address)
#     print(f"Time to search for address {address}: {search_time:.6f} seconds")
    
trie.calculate_statistics(addresses_to_lookup)
# trie.calculate_memory_usage()
# trie.tprint()
# for address in addresses_to_lookup:
#     result = trie.lookup(address)
#     binaddress = bin(int(address,trie.Base))[2:]
#     print(f"Address {binaddress}: Next hop -> {result}")

