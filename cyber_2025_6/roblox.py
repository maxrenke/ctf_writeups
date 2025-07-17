flag_numbers = "44971820909144931903087754310756286204097191744733885119826706804223848616183642155139078386095243204445721025953832684650877461"

# Break into 2-digit chunks
ascii_chars = ''.join(chr(int(flag_numbers[i:i+2])) for i in range(0, len(flag_numbers), 2))

print("Possible ASCII flag:", ascii_chars)

hex_flag = bytes.fromhex(flag_numbers).decode("utf-8", errors="ignore")
print("Hex-decoded flag:", hex_flag)

ascii_chars = ''.join(chr(int(flag_numbers[i:i+3]) % 256) for i in range(0, len(flag_numbers), 3))
print("Modulo-decoded flag:", ascii_chars)