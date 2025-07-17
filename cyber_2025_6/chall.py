ELF_bytes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
key = 1
def not_so_fast(ELF_bytes, key):
    message = ""
    for i in range(len(ELF_bytes)):
        message += chr(ord(ELF_bytes[i]) + key)
    return message

with open("bytes2.txt","a") as file:
    file.write("You want your ELF challenge so bad? Well here it is!\n")
    file.write(not_so_fast(ELF_bytes,key))