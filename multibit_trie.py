import sys
import time
import statistics

class TrieNode:
    def __init__(self, next_hop = None, length = 0):
        self.children = {}  
        self.next_hop = None 
        self.next_hop = next_hop
        self.length = length

class MultibitTrie:
    def __init__(self, stride=1,Base=2):
        self.root = TrieNode()
        self.stride = stride  
        self.Base = Base  

    def insert(self, prefix, length, next_hop):
        stride= self.stride
        current_node = self.root  
        integer_prefix = int(prefix[:length],self.Base)
        binary_number = bin(integer_prefix)[2:]
        rjusted = binary_number.rjust(length, '0')
        binary_prefix = rjusted.ljust(32, '0')

        for i in range(0, length, stride):
            bit_pattern = binary_prefix[i:i+stride]
            if i + stride > length:
                curr_pattern = str(binary_prefix[i:length]) 
                remaining_bits = stride - (length - i)
                num_combinations = 2 ** (remaining_bits)
                for j in range(num_combinations):
                    combination = bin(j)[2:].zfill(remaining_bits)
                    pattern = curr_pattern + combination 
                    if pattern not in current_node.children:
                        current_node.children[pattern] = TrieNode(next_hop=next_hop, length= length)
                    else:
                        if current_node.children[pattern].length < length:
                            current_node.children[pattern].next_hop = next_hop
                            current_node.children[pattern].length = length
            else:

                if bit_pattern not in current_node.children:
                    current_node.children[bit_pattern] = TrieNode()
                current_node = current_node.children[bit_pattern]

            if (i + stride == length ):
                    current_node.next_hop = next_hop
                    current_node.length = length

    def lookup(self, address):
        binary_ip = bin(int(address,self.Base))[2:].zfill(32)
        current_node = self.root
        best_match = self.root.next_hop
        for i in range(0, len(binary_ip), self.stride):
            bit_pattern = binary_ip[i:i + self.stride]
            if bit_pattern in current_node.children:
                current_node = current_node.children[bit_pattern]
                if current_node.next_hop is not None:
                    best_match = current_node.next_hop
            else:
                break
        return best_match

    def tprint(self, node=None, depth=0):
        if node is None:
            node = self.root
        indent = "  " * depth
        if node.next_hop is not None:
            print(f"{indent}Node: Next Hop: {node.next_hop}, Length: {node.length}")
        for chunk, child in sorted(node.children.items()):
            print(f"{indent}Chunk: {chunk}")
            self.tprint(child, depth + 1)
    
    def get_size(self, obj):
        size = sys.getsizeof(obj)  
        if isinstance(obj, TrieNode):
            for child in obj.children.values():
                size += self.get_size(child)  
        return size

    def calculate_memory_usage(self):
        total_size = self.get_size(self.root) 
        print(f"Total memory usage of the trie(Stride:{self.stride}): {total_size} bytes")
        
    def measure_search_time(self, address):
        start_time = time.perf_counter()  # Use perf_counter for better precision
        self.lookup(address)  # Perform the lookup
        end_time = time.perf_counter()  # Get the precise end time
        return end_time - start_time  # Return the time taken for the lookup    
    
    def calculate_statistics(self, addresses):
        times = []
        for address in addresses:
            search_time = self.measure_search_time(address)
            times.append(search_time)
        avg_time = sum(times) / len(times)  # Mean
        min_time = min(times)  # Minimum time
        max_time = max(times)  # Maximum time
        std_dev = statistics.stdev(times)  # Standard deviation
        print(f"Average search time(Stride: {self.stride}): {avg_time:.6f} seconds")
        print(f"Minimum search time(Stride: {self.stride}): {min_time:.6f} seconds")
        print(f"Maximum search time(Stride: {self.stride}): {max_time:.6f} seconds")
        print(f"Standard deviation(Stride: {self.stride}): {std_dev:.6f} seconds")

