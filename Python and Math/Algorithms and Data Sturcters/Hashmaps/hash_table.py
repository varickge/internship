# Hash Map big(O)=1

class hashTable:
    def __init__(self,size):
        self.size=size
        self.hash_table=[[] for _ in range(size)]

    def set_value(self,key,value):
        hashed_key=hash(key) % self.size
        bucket=self.hash_table[hashed_key]
        for index,record in enumerate(bucket):
            record_key,record_value=record
            if record_key==key:
                bucket[index]=(key,value)
                return
        bucket.append((key, value))

    def get_value(self,key):
        hashed_key=hash(key)%self.size
        bucket=self.hash_table[hashed_key]
        for index,record in enumerate(bucket):
            record_key,record_vlue=record
            if record_key==key:
                return record
        return "Not found"

    def __str__(self):
        return str(self.hash_table)

'''hash_table=hashTable(256)
hash_table.set_value("varuzhangevorgian@gmail.com","Varuzhan Gevorgyan, 2003, Armenia")
hash_table.set_value("varujaa7@gmail.com","Varuzhan Gevorgyan, 2000, Armenia")
print(hash_table)
print(hash_table.get_value("varujaa7@gmil.com"))'''