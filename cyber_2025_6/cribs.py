from binascii import unhexlify
import string

# Step 1: Load the ciphertexts
c1_hex = "5c623c61545f63270c4047724e114d52794e16485f7b4e034433652b1744527b2b0520"
c2_hex = "40612c0653687b270649477e20065e4667311549566823044f4c7e201e435f762d0a7c"

c1 = unhexlify(c1_hex)
c2 = unhexlify(c2_hex)

# Step 2: XOR them to get P1 ⊕ P2
xored = bytes([a ^ b for a, b in zip(c1, c2)])

# Step 3: Crib-dragging known words across xored text
cribs = ["PLAN", "NEVER", "SECRET", "OUR", "HIGHER", "CLASSIFIED", "WILL", "BE"]

def xor_bytes(b1, b2):
    return bytes([a ^ b for a, b in zip(b1, b2)])

def try_crib(xored, crib):
    print(f"\n[+] Trying crib: {crib}")
    crib_bytes = crib.encode()
    for i in range(len(xored) - len(crib_bytes) + 1):
        fragment = xored[i:i+len(crib_bytes)]
        guess = xor_bytes(fragment, crib_bytes)
        try:
            text = guess.decode()
            if all(chr(b) in string.ascii_uppercase + ' ' for b in guess):
                print(f"  Match at position {i}:")
                print(f"    P1: {crib}")
                print(f"    P2: {text}")
                yield (i, crib, text)
        except UnicodeDecodeError:
            continue

# Step 4: Save successful matches and reconstruct message parts
recovered_p1 = bytearray(b"?" * len(c1))
recovered_p2 = bytearray(b"?" * len(c2))

for crib in cribs:
    for pos, p1_word, p2_word in try_crib(xored, crib):
        for i in range(len(p1_word)):
            recovered_p1[pos+i] = ord(p1_word[i])
            recovered_p2[pos+i] = ord(p2_word[i])

# XOR ciphertexts with known plaintext to recover key bytes
key = bytearray(len(c1))
for i in range(len(c1)):
    if recovered_p1[i] != ord('?'):
        key[i] = c1[i] ^ recovered_p1[i]
    elif recovered_p2[i] != ord('?'):
        key[i] = c2[i] ^ recovered_p2[i]
    else:
        key[i] = ord('?')  # Unknown key byte

# Decrypt full messages using recovered key
final_p1 = bytearray(len(c1))
final_p2 = bytearray(len(c2))

for i in range(len(c1)):
    if key[i] != ord('?'):
        final_p1[i] = c1[i] ^ key[i]
        final_p2[i] = c2[i] ^ key[i]
    else:
        final_p1[i] = final_p2[i] = ord('?')

print("\n=== Recovered Message 1 ===")
print(final_p1.decode())

print("\n=== Recovered Message 2 ===")
print(final_p2.decode())