import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix_str = '0' * difficulty
        while not self.hash.startswith(prefix_str):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined with nonce: {self.nonce} and hash: {self.hash}")

# Simulate mining the blockchain
def mine_blockchain():
    blockchain = []
    genesis_block = Block(0, time.time(), "Genesis Block", "0")
    blockchain.append(genesis_block)

    # Mine the 2nd block
    new_block = Block(1, time.time(), "Block 1 Data", blockchain[0].hash)
    
    # Measure time taken for mining
    start_time = time.time()
    new_block.mine_block(4)  # Difficulty of 4
    end_time = time.time()
    
    # Calculate and print the time taken
    time_taken = end_time - start_time
    print(f"Time taken to mine Block 1: {time_taken:.2f} seconds")
    
    blockchain.append(new_block)

    return blockchain

# Mine and display the blockchain
blockchain = mine_blockchain()
