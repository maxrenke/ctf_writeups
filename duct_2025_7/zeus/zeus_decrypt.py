#!/usr/bin/env python3

# Encrypted data from the binary (little-endian format)
encrypted_data = [
    0x0C1F1027392A3409,  # var_50
    0x011512515C6C561D,  # var_48
    0x5A411E1C18043E08,  # var_40
    0x3412090606125952,  # var_38
    0x12535C546E170B15,  # var_30
    0x03A110315320F0E,   # var_28
    0x4E4A5A00           # var_28+7 (last 4 bytes)
]

# Convert to byte array (little-endian)
encrypted_bytes = b''
for i, qword in enumerate(encrypted_data[:-1]):  # Process first 6 qwords (8 bytes each)
    encrypted_bytes += qword.to_bytes(8, 'little')

# Add the last 4 bytes (but check all bytes, don't strip nulls yet)
encrypted_bytes += encrypted_data[-1].to_bytes(4, 'little')

print(f"Raw encrypted bytes with nulls: {encrypted_bytes.hex()}")
print(f"Raw length: {len(encrypted_bytes)}")

# Let's also try without removing nulls first
encrypted_bytes_with_nulls = encrypted_bytes

print(f"Encrypted bytes length: {len(encrypted_bytes)}")
print(f"Encrypted bytes (hex): {encrypted_bytes.hex()}")
print(f"Encrypted bytes: {encrypted_bytes}")

# XOR key
key = b"Maimaktes1337"
key_len = len(key)

print(f"Key: {key}")
print(f"Key length: {key_len}")

# Decrypt both versions
print("\n=== With null bytes removed ===")
encrypted_clean = encrypted_bytes.rstrip(b'\x00')
decrypted_clean = b''
for i, byte in enumerate(encrypted_clean):
    key_byte = key[i % key_len]
    decrypted_byte = byte ^ key_byte
    decrypted_clean += bytes([decrypted_byte])

print(f"Decrypted message: {decrypted_clean}")
print(f"Decrypted (as string): {decrypted_clean.decode('ascii', errors='ignore')}")

print("\n=== With all bytes (including nulls) ===")
decrypted_full = b''
for i, byte in enumerate(encrypted_bytes_with_nulls):
    key_byte = key[i % key_len]
    decrypted_byte = byte ^ key_byte
    decrypted_full += bytes([decrypted_byte])

print(f"Decrypted message: {decrypted_full}")
print(f"Decrypted (as string): {decrypted_full.decode('ascii', errors='ignore')}")
