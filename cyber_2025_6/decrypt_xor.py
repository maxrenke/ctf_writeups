def xor_decrypt(ciphertexts, keys):
    decrypted_texts = []
    for ciphertext in ciphertexts:
        for key in keys:
            decrypted = bytes([ciphertext[i] ^ key[i % len(key)] for i in range(len(ciphertext))])
            decrypted_texts.append((key, decrypted.decode(errors='ignore')))
    return decrypted_texts

  


# Example usage:
ciphertext1 = bytes.fromhex("5c623c61545f63270c4047724e114d52794e16485f7b4e034433652b1744527b2b0520")  # Replace with actual hex ciphertext
ciphertext2 = bytes.fromhex("40612c0653687b270649477e20065e4667311549566823044f4c7e201e435f762d0a7c")  # Replace with actual hex ciphertext
keys = [b"PLAN", b"NEVER", b"SECRET", b"OUR", b"HIGHER", b"CLASSIFIED", b"WILL", b"BE"]

results = xor_decrypt([ciphertext1, ciphertext2], keys)
for key, text in results:
    print(f"Key: {key.decode()}, Decrypted: {text}")