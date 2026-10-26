import hashlib


# ==========================================
# Block
# ==========================================

class Block:

    def __init__(self, data, previous_hash):

        self.data = data
        self.previous_hash = previous_hash

        # Calculate this block's hash
        self.hash = self.calculate_hash()


    def calculate_hash(self):

        sha = hashlib.sha256()

        data = self.data.encode('utf-8')
        previous_hash = self.previous_hash.encode('utf-8')

        sha.update(data + previous_hash)

        return sha.hexdigest()


# ==========================================
# Blockchain
# ==========================================

class Blockchain:

    def __init__(self):

        # Create the first block
        self.chain = [self.create_genesis_block()]


    # Create Genesis Block
    def create_genesis_block(self):

        return Block("Genesis Block", "0")


    # Add a new block
    def add_block(self, new_block):

        # Connect new block with previous block
        new_block.previous_hash = self.chain[-1].hash

        # Recalculate hash
        new_block.hash = new_block.calculate_hash()

        # Add block to blockchain
        self.chain.append(new_block)


    # Validate blockchain
    def validate_chain(self):

        for i in range(1, len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check current block's hash
            if current_block.hash != current_block.calculate_hash():

                print("Invalid hash for block", i)

                return False


            # Check connection with previous block
            if current_block.previous_hash != previous_block.hash:

                print("Invalid previous hash for block", i)

                return False


        print("Blockchain is valid")

        return True


    # Get blockchain length
    def get_chain_length(self):

        return len(self.chain)


    # Calculate total hash value
    def get_chain_hashrate(self):

        total_hashrate = 0

        for block in self.chain:

            total_hashrate += int(block.hash, 16)

        return total_hashrate


    # Check for 51% attack
    def check_for_51_percent_attack(self):

        chain_length = self.get_chain_length()

        total_hashrate = self.get_chain_hashrate()


        for i in range(chain_length):

            block_hash = int(self.chain[i].hash, 16)

            if block_hash / total_hashrate > 0.51:

                print("51% attack detected at block", i)

                return True


        print("No 51% attack detected")

        return False


# ==========================================
# Main Program
# ==========================================

blockchain = Blockchain()


# Add blocks

blockchain.add_block(
    Block("Transaction 1", "")
)

blockchain.add_block(
    Block("Transaction 2", "")
)

blockchain.add_block(
    Block("Transaction 3", "")
)


# Print blockchain

print("\nBlockchain:")

for block in blockchain.chain:

    print("\nData:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)


# Validate blockchain

print("\nChecking Blockchain:")

blockchain.validate_chain()


# Check 51% attack

print("\nChecking 51% Attack:")

blockchain.check_for_51_percent_attack()