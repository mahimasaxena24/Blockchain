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

# Create the blockchain
def create_blockchain():
    blockchain = []
    genesis_block = Block(0, time.time(), "Genesis Block", "0")
    blockchain.append(genesis_block)

    for i in range(1, 4):
        new_block = Block(i, time.time(), f"Block {i} Data", blockchain[i-1].hash)
        blockchain.append(new_block)

    return blockchain

# Display the blockchain
def display_blockchain(blockchain):
    for block in blockchain:
        print(f"Block {block.index}:")
        print(f"  Timestamp: {block.timestamp}")
        print(f"  Data: {block.data}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Hash: {block.hash}\n")

# Create and display the blockchain
blockchain = create_blockchain()
display_blockchain(blockchain)

# Challenge: Change data of Block 1 and recalculate hashes
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].calculate_hash()

# Recalculate hashes for subsequent blocks
for i in range(2, len(blockchain)):
    blockchain[i].previous_hash = blockchain[i-1].hash
    blockchain[i].hash = blockchain[i].calculate_hash()

print("After tampering with Block 1:")
display_blockchain(blockchain)
