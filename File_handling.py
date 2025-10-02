import pickle

faylname = "C:/pi_million_digits.txt"


with open(faylname,"r") as file:
    file_read = file.read()
    if "30012006" in file_read:
        print("topildi")
    else:
        print("topilmadi")


pi_float = float(file_read)


with open("pickle_file","wb") as f:
    pickle.dump(pi_float, f)


with open("pickle_file","rb") as f:
    ss = pickle.load(f)

print("Pickledan o‘qildi:", ss)