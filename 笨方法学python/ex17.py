from sys import argv
from os.path import exists

script,from_file,to_file=argv
print("Copying from %s to %s" %(from_file,to_file))

# we could do this two on one line too,how?
in_file=open(from_file)
indata=in_file.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r"% exists(to_file))
# exists()将文件名作为参数，文件存在返回True，不存在返回False
print("Ready,hit the return to continue,CTRL-C to abort")
input()

out_file=open(to_file,'w')
out_file.write(indata)

print("Allright,all done")

out_file.close()
in_file.close()