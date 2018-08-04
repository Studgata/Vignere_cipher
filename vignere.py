print("\n")
print("********************************************************Vignere Ciphere******************************************************* \n")
print("********************************************************Vignere Table********************************************************* \n")
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
print("\n")



print("********************************************************Encryption************************************************************")
print("\n")

def encrypt():
    data = input("Enter the data for cipher and Deciphering : ")
    print("\n")
    k = input("Enter the key for the same : ")
    print("\n")
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
    print("Calculated key is :",nk,"\n")
    key_length= len(nk)
    print("Length of data is :",data_length, "\n")
    print("Length of the key is ",len(nk),"\n")
    row = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    column = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    encrypted_data = ""
    if data_length == len(nk):    
        for x in range(0,key_length):
            fill= data[x]
            keyto = nk[x]
            r = row.find(fill)
            c = column.find(keyto)
            encr = alph_table[c][r]
            encrypted_data = encrypted_data + encr
        print("Encrypted data is : ",encrypted_data,"\n")
    decrypt(encrypted_data,nk)



    
def decrypt(data,key):
    print("**************************************************Decryption*****************************************************************")
    print("\n")
    dta = data
    keu = key
    row = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    column = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    decrypted_data = ""
    for x in range(0,len(keu)):
            fill= dta[x]
            keyto = keu[x]
            c = column.find(keyto)
            d = alph_table[c].index(fill)
            s = row[d]
            decrypted_data = decrypted_data + s        
    print("Decrypted data is :",decrypted_data.replace("z"," "))
    

def main():
    encrypt()
    
if __name__ == "__main__":
    main()
