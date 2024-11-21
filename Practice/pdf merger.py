import pypdf

i=1
while(i<=5):
    with open("D:/Cource/PYTHON/garbage/{i}.pdf","r+") as f:
        f.a[i]=pypdf.PdfReader("{i}.pdf")
        i+=1