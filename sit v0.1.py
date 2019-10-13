import hashlib
import argparse
parser = argparse.ArgumentParser()
def fngenhash(filename):
    file=open(filename,"r",encoding="UTF-8")
    content=file.read()
    result=hashlib.md5(content.encode())
    #print(result.hexdigest())
    hashfilename=filename+".hash"
    hashfile=open(hashfilename,"w")
    hashfile.write(result.hexdigest())
    file.close()
    hashfile.close()
def fncomphash(filename):
    file=open(filename,"r",encoding="UTF-8")
    content=file.read()
    result=hashlib.md5(content.encode())
    hashfilename=filename+".hash"
    hashfile=open(hashfilename,"r",encoding="UTF-8")
    hashcontent=hashfile.read()

    """a=""
    a=input("Enter Hash Value:  ")"""
    if(result.hexdigest()==hashcontent):
        print("Comp Success")
    else:
        print("Comp fail")

parser.add_argument("-g",help="genhash")
parser.add_argument("-c",help="comphash")
args=parser.parse_args()
print("System Integrity Tool")
if args.g:
    print("genhash")
    fngenhash(args.g)
if args.c:
    print("comphash")
    fncomphash(args.c)