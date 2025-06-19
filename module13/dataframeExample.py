import pandas as pd

data={"name":["alice", "bob","charlie"],
      "age":[25,30,32],
      "city:"["nyc", "san francisco", "LA"]
      }

df=pd.DataFrame(data)
print(df)