def caesar(input, k):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ketqua = ""
    input = input.upper() 
    for char in input:
        if char in alphabet:  
            mahoa = (alphabet.index(char) + k) % 26  
            ketqua += alphabet[mahoa]
        else:
            ketqua += char  

    return ketqua


k = 14
input = "VO THI TUYET SINH"

ketqua = caesar(input, k)
print("Ciphertext:", ketqua)