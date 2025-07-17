import binascii

# Ciphertext (hex encoded)
ciphertext_hex = "5c623c61545f63270c4047724e114d52794e16485f7b4e034433652b1744527b2b0520"
ciphertext = bytes.fromhex(ciphertext_hex)

# List of suspected words
cribs = ["PLAN", "NEVER", "SECRET", "OUR", "HIGHER", "CLASSIFIED", "WILL", "BE"]

def xor_strings(s1, s2):
    """XOR two byte sequences."""
    return bytes(a ^ b for a, b in zip(s1, s2))

def crib_drag(ciphertext, crib):
    """Try XORing the crib at different positions in the ciphertext."""
    crib_bytes = crib.encode()
    crib_length = len(crib_bytes)

    for i in range(len(ciphertext) - crib_length + 1):
        xored = xor_strings(ciphertext[i:i+crib_length], crib_bytes)
        print(f"Position {i}: XOR result (potential key fragment) -> {binascii.hexlify(xored).decode()}")

# Run crib dragging for each word
for crib in cribs:
    print(f"\nTrying crib: {crib}")
    crib_drag(ciphertext, crib)