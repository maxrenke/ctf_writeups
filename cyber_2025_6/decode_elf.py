def recover_elf(encoded_bytes):
    key = -63 # Sum the magic number bytes to get the key value

    recovered_bytes = bytearray()
    for byte in encoded_bytes:
        recovered_bytes.append(byte - key)

    return recovered_bytes

# Read the encoded ELF binary
with open("bytes (1).txt", "rb") as f:
    encoded_data = f.read()

# Recover the original ELF binary
recovered_data = recover_elf(encoded_data)

# Write the recovered binary to a new file
with open("recovered_binary.elf", "wb") as f:
    f.write(recovered_data)

print("Recovered ELF binary saved as 'recovered_binary.elf'")