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
    print("type done to exit")
data=""
while data!="done":
     data=input("input:" )
     data=data.lower()
     if data=="done":
         break
     raw=data.split()
     data_cleaner(raw)                    
