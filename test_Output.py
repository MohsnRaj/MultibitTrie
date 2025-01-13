import random
from multibit_trie import MultibitTrie


rules = [
    (16, 0b0, 1),  # Rule: 0*, Next hop: 16, Length: 1
    (2, 0b0, 0),  # Rule: *, Next hop: 2, Length: 0 (default rule)
    (15, 0b001, 3),  # Rule: 001*, Next hop: 15, Length: 3
    (25, 0b010, 3),  # Rule: 010*, Next hop: 25, Length: 3
    (21, 0b010100, 6),  # Rule: 010100*, Next hop: 21, Length: 6
    (46, 0b010101, 6),  # Rule: 010101*, Next hop: 46, Length: 6
    (11, 0b0001, 4),  # Rule: 0001*, Next hop: 11, Length: 4
    (4, 0b0110, 4),  # Rule: 0110*, Next hop: 4, Length: 4
    (45, 0b10, 2),  # Rule: 10*, Next hop: 45, Length: 2
    (7, 0b1001, 4),  # Rule: 1001*, Next hop: 7, Length: 4
    (21, 0b1011, 4),  # Rule: 1011*, Next hop: 21, Length: 4
    (11, 0b110, 3),  # Rule: 110*, Next hop: 11, Length: 3
    (12, 0b1100, 4),  # Rule: 1100*, Next hop: 12, Length: 4
    (14, 0b11010, 5),  # Rule: 11010*, Next hop: 14, Length: 5
    (36, 0b11011, 5),  # Rule: 11011*, Next hop: 36, Length: 5
]

trie = MultibitTrie(stride=4)

for nexthop, prefix, length in rules:
    trie.insert(prefix, length, nexthop,2)

print("Trie structure:")
trie.tprint()

# random_addresses = [random.randint(0, 2**32 - 1) for _ in range(20)]
# print("\nRandom address lookups:")
# for address in random_addresses:
#     length = len(bin(address)) - 2
#     result = trie.lookup(address, length)
#     print(f"Address {bin(address)}: Next hop -> {result}")

randomaddress = 3723879263
result = trie.lookup(randomaddress)
print(f"Address {bin(randomaddress)}: Next hop -> {result}")