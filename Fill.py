data = input("enter groceries: ")
with open("Groceries.txt", "w") as f:
    f.writelines(data)
    print("Done")
