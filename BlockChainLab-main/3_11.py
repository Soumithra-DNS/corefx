import hashlib
import time


# Create a Block
class Block:

    def __init__(self, transactions, previous_block_hash):

        # Time when block is created
        self.timestamp = time.time()

        # Transactions inside the block
        self.transactions = transactions

        # Hash of the previous block
        self.previous_block_hash = previous_block_hash

        # Start nonce from 0
        self.nonce = 0

        # Calculate initial hash
        self.hash = self.calculate_hash()


    # Calculate SHA-256 hash of the block
    def calculate_hash(self):

        block_data = (
            str(self.timestamp)
            + str(self.transactions)
            + str(self.previous_block_hash)
            + str(self.nonce)
        )

        return hashlib.sha256(
            block_data.encode()
        ).hexdigest()


    # Mine the block using Proof of Work
    def mine_block(self, difficulty):

        print("Mining block...")

        start_time = time.time()

        # Keep changing nonce until hash starts with required zeros
        while self.hash[:difficulty] != "0" * difficulty:

            self.nonce += 1

            self.hash = self.calculate_hash()

        end_time = time.time()

        print("Block mined!")
        print("Hash:", self.hash)
        print("Nonce:", self.nonce)
        print("Time:", end_time - start_time, "seconds")


# -------------------------------------------------
# Main Program
# -------------------------------------------------

difficulty = 2


# ==========================
# Genesis Block
# ==========================

print("\nMining Genesis Block...")

transactions = [
    "transaction1",
    "transaction2",
    "transaction3"
]

previous_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"

block = Block(
    transactions,
    previous_block_hash
)

block.mine_block(difficulty)


# ==========================
# Block 1
# ==========================

print("\nMining Block 1...")

transactions = [
    "transaction4",
    "transaction5",
    "transaction6"
]

previous_block_hash = block.hash

block = Block(
    transactions,
    previous_block_hash
)

block.mine_block(difficulty)


# ==========================
# Block 2
# ==========================

print("\nMining Block 2...")

transactions = [
    "transaction7",
    "transaction8",
    "transaction9"
]

previous_block_hash = block.hash

block = Block(
    transactions,
    previous_block_hash
)

block.mine_block(difficulty)