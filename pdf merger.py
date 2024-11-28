import pypdf


a=[]
i=1

while(i<=5):
    a[i]=pypdf.PdfReader(f"D:/Cource/PYTHON/garbage/{i}.pdf")
    i+=1

data=""
for i in len(a):
    data=data+a[i]