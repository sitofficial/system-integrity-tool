import os
import sys
import hashlib
import argparse

parser = argparse.ArgumentParser()

def fngenhash(filepath,outpath):
    if os.path.exists(outpath) == 0:
        os.mkdir(outpath)
    if(os.path.isfile(filepath)):
        file=open(filepath,"r",encoding="UTF-8")
        content=file.read()
        result=hashlib.md5(content.encode())
        hashfilepath=outpath+'/'+os.path.basename(filepath)+".hash"
        if os.path.exists(os.path.dirname(hashfilepath)) == 0:
            os.mkdir(os.path.dirname(hashfilepath))
        hashfile=open(hashfilepath,"w")
        print('Creating hash for',filepath,'at',hashfilepath)
        hashfile.write(result.hexdigest())
        file.close()
        hashfile.close()
    else:
        filenames=os.listdir(filepath)
        for filename in filenames:
            fngenhash(filepath+'/'+filename,outpath)

def fncomphash(filepath,outpath):
    if os.path.exists(outpath) == 0:
        print("The hashes have yet to be created or wrong location has been input.")
        sys.exit()
    if(os.path.isfile(filepath)):
        file=open(filepath,"r",encoding="UTF-8")
        content=file.read()
        result=hashlib.md5(content.encode())
        hashfilepath=outpath+'/'+os.path.basename(filepath)+".hash"
        hashfile=open(hashfilepath,"r")
        hashcontent=hashfile.read()
        if(result.hexdigest()==hashcontent):
            print(filepath,": Integrity Maintained")
        else:
             print(filepath,": Integrity NOT Maintained")
        file.close()
        hashfile.close()
    else:
        filenames=os.listdir(filepath)
        for filename in filenames:
            fncomphash(filepath+'/'+filename,outpath)

parser.add_argument("-g",help="Generate hashes for files at a location.")
parser.add_argument("-c",help="Compare and verify file integrity for files at a location.")

args=parser.parse_args()

print("System Integrity Tool [Use argument -h for help.]")

if args.g:
    outpath=input("Enter save location for hash files: ")
    fngenhash(args.g,outpath)
if args.c:
    outpath=input("Enter save location for hash files: ")
    fncomphash(args.c,outpath)