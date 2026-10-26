import hashlib
import base58
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# SHA256 Function
def sha256(data):
    return hashlib.sha256(data).digest()

# RIPEMD160 Function
def ripemd160(data):
    return hashlib.new("ripemd160", data).digest()


# Node 1 : Generate Address

print("<- NODE 1 -> ")

# Step 1: Private Key
private_key_hex = "0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1"

print("\nPrivate Key:")
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

print("\nGenerated Bitcoin Address:")
print(address)


# Node 2 : Receive & Validate Address

print("\n\n<- NODE 2 ->")

# Receive Address from Node 1
received_address = address +'A'

print("\nReceived Address:")
print(received_address)

# Decode Address
decoded = base58.b58decode(received_address)

print("\nDecoded Data:")
print(decoded.hex())

# Separate Payload and Checksum
received_payload = decoded[:-4]
received_checksum = decoded[-4:]

print("\nReceived Payload:")
print(received_payload.hex())

print("\nReceived Checksum:")
print(received_checksum.hex())

# Calculate New Checksum
calculated_checksum = sha256(sha256(received_payload))[:4]

print("\nCalculated Checksum:")
print(calculated_checksum.hex())

# Compare Checksums
if received_checksum == calculated_checksum:
    print("\nAddress Validation: VALID")
else:
    print("\nAddress Validation: INVALID")