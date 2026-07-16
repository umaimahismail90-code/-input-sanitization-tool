def data_cleaner(data):
    clean=[]
    for item in data:
        try:
            item=int(item)
            if item >0:
                clean.append(item)
        except:
            continue
    print(clean)

Data=input("input the items in your list separated by spaces: ")
raw=Data.split()
data_cleaner(raw)
