import hashlib
import base58
import socket

# SHA256 Function
def sha256(data):
    return hashlib.sha256(data).digest()

print(" <- NODE 2 ->n")

# Create Server Socket
HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(1)

print("Waiting for Node 1...\n")

# Accept Connection
connection, address_info = server.accept()

print("Connected with:", address_info)

# Receive Bitcoin Address
received_address = connection.recv(1024).decode()

print("\nReceived Bitcoin Address:")
print(received_address)

# Decode Bitcoin Address
decoded = base58.b58decode(received_address)

print("\nDecoded Data:")
print(decoded.hex())

# Extract Payload and Checksum
payload = decoded[:-4]
received_checksum = decoded[-4:]

print("\nPayload:")
print(payload.hex())

print("\nReceived Checksum:")
print(received_checksum.hex())

# Calculate New Checksum
calculated_checksum = sha256(sha256(payload))[:4]

print("\nCalculated Checksum:")
print(calculated_checksum.hex())

# Validate Address
print("\nValidation Result:")

if received_checksum == calculated_checksum:
    print("Address is VALID")
else:
    print("Address is INVALID")

# Close Connection
connection.close()
server.close()

print("\nConnection Closed.")