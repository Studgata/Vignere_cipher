print("********************************************************Vignere Ciphere*******************************************************")
print("********************************************************Vignere Table*******************************************************")
count = 0
ext_alph = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alph_table = []
for y in range(26):
    new_row = []
    for x in range(26):
        new_row.append(ext_alph[x+count])
    count += 1
    alph_table.append(new_row)
for x in alph_table:
    print(x)


def encrypt():
    data = raw_input("Enter the data for cipher and Deciphering : ")
    k = raw_input("Enter the key for the same : ")
    data_length = len(data)
    key_length = len(k)
    nk = ""
    kkkk=""
    if data_length > key_length :
        qout = data_length//key_length
        
        diff = data_length % key_length
        d = k*qout  
    for x in range(0,diff):
        sliced = k[x]
        kkkk = kkkk+sliced

        
    nk = nk + d+ kkkk
    print(nk)
    key_length= len(nk)
    print(data_length)
    print(len(nk))
    row = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    column = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    encrypted_data = ""
    if data_length == len(nk):    
        for x in range(0,key_length):
            fill= data[x]
            keyto = nk[x]
            c = row.find(fill)
            r = column.find(keyto)
            encr = alph_table[c][r]
            encrypted_data = encrypted_data + encr
        print(encrypted_data)
    decrypt(encrypted_data,nk)



    
def decrypt(data,key):
    print("*******Decryption********")
    dta = data
    keu = key
    row = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    column = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    
    
    

def main():
    encrypt()
    
if __name__ == "__main__":
    main()
