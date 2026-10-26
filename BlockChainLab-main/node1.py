import hashlib
import base58
import socket

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# SHA256 Function
def sha256(data):
    return hashlib.sha256(data).digest()

# RIPEMD160 Function
def ripemd160(data):
    return hashlib.new("ripemd160", data).digest()

print(" <- NODE 1 ->n")

# Step 1: Private Key
private_key_hex = "0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1"

print("Private Key:")
print(private_key_hex)

# Step 2: Generate Public Key
private_key = ec.derive_private_key(
    int(private_key_hex, 16),
    ec.SECP256K1()
)

public_key = private_key.public_key()

public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
)

print("\nPublic Key:")
print(public_key_bytes.hex())

# Step 3: SHA256
sha_hash = sha256(public_key_bytes)

print("\nSHA256:")
print(sha_hash.hex())

# Step 4: RIPEMD160
hash160 = ripemd160(sha_hash)

print("\nHash160:")
print(hash160.hex())

# Step 5: Add Version Byte
payload = b"\x00" + hash160

print("\nPayload:")
print(payload.hex())

# Step 6: Generate Checksum
checksum = sha256(sha256(payload))[:4]

print("\nChecksum:")
print(checksum.hex())

# Step 7: Generate Bitcoin Address
address = base58.b58encode(payload + checksum).decode()
# address = address[:10] + "A" + address[11:]
# address = address[:-1] + 'b'
print("\nBitcoin Address:")
print(address)

# Step 8: Connect to Node 2

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("\nConnecting to Node 2...")

client.connect((HOST, PORT))

print("Connected Successfully!")

# Send Address

client.send(address.encode())

print("\nBitcoin Address Sent Successfully!")

client.close()

print("\nConnection Closed.")