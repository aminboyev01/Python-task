import pickle

faylname = "C:/pi_million_digits.txt"

with open(faylname, "r") as file:
    file_read = file.read()
    if "30012006" in file_read:
        print("topildi")
    else:
        print("topilmadi")

pi_str = file_read.strip().replace("\n", "")

with open("pickle_file.pkl", "wb") as f:
    pickle.dump(pi_str, f)

with open("pickle_file.pkl", "rb") as f:
    ss = pickle.load(f)

print("Pickledan o‘qildi:", ss)
