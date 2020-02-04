s1="helloabcabc"
s3=''
for i in s1:
    count=0
    if(i not in s3):
        s3=s3+i
        for j in s1:
            if(i==j):
                # s3=s3+i
                count+=1
        print(f"i:{i} and count:{count}")

