lt=[0x4e, 0x2e, 0x60, 0x14, 0xc4, 0x36, 0xaa, 0xcf, 0x6f, 0x4a, 0x92, 0xd9, 0x4b, 0x58, 0xe4, 0x6a, 0xee, 0x20, 0xa1, 0x2b, 0x73, 0xc7, 0x41, 0x51, 0xf0, 0x6e, 0xde, 0xbe, 0xcd, 0x5e, 0x9e, 0x46, 0x22, 0x84, 0x78, 0x1f, 0x7a, 0xb4, 0xae, 0x42, 0x23, 0x3d, 0xc9, 0x77, 0x26, 0x9b, 0xc5, 0x0a, 0x89, 0x44, 0xd7, 0x38, 0xa4, 0xad, 0xfc, 0xe5, 0x64, 0x0d, 0x6b, 0x19, 0x59, 0x06, 0x97, 0x63, 0xb9, 0xf5, 0x69, 0x10, 0x09, 0x5d, 0x15, 0x82, 0x5f, 0x72, 0x31, 0xd8, 0x50, 0x05, 0x08, 0xa3, 0xf8, 0xd3, 0xf2, 0xf6, 0xc8, 0x1d, 0xd4, 0xb1, 0xa8, 0xf9, 0x98, 0x4f, 0x1e, 0x61, 0xd5, 0xeb, 0x7f, 0x49, 0x99, 0x48, 0x0e, 0xba, 0xb5, 0xf3, 0xe1, 0xcb, 0x53, 0xd2, 0xbb, 0x2f, 0x74, 0xc1, 0xb2, 0x86, 0xbc, 0xe7, 0xc6, 0x3e, 0xef, 0x9d, 0xdb, 0xed, 0x00, 0x9c, 0x3a, 0x1a, 0x2d, 0x76, 0x83, 0xb3, 0xd6, 0x02, 0x1c, 0x30, 0xea, 0x43, 0x94, 0x52, 0xc2, 0x5b, 0xcc, 0xf7, 0xdc, 0x13, 0xa6, 0xec, 0xda, 0xfb, 0x3c, 0xca, 0x7b, 0xa9, 0xe8, 0x56, 0x79, 0xa2, 0x85, 0x32, 0x5c, 0x93, 0x55, 0xd1, 0x8a, 0x16, 0x67, 0x0c, 0x47, 0x11, 0xa5, 0x24, 0x37, 0x88, 0xa0, 0x6c, 0x45, 0x40, 0xe9, 0xdd, 0xa7, 0x62, 0x70, 0xdf, 0x54, 0x9a, 0x95, 0x17, 0x75, 0x18, 0x4c, 0x68, 0x0b, 0xbf, 0x27, 0x7e, 0xc0, 0x87, 0x1b, 0x3b, 0xb7, 0x91, 0xc3, 0x29, 0xb6, 0x34, 0x07, 0x7d, 0x9f, 0x33, 0xf1, 0x3f, 0xd0, 0xbd, 0xe2, 0x57, 0x96, 0xe6, 0xac, 0x04, 0xff, 0x12, 0x01, 0xb0, 0x66, 0xaf, 0x7c, 0xf4, 0x03, 0x8b, 0x25, 0x0f, 0x21, 0x28, 0x4d, 0x8d, 0x65, 0x71, 0xfe, 0xe0, 0x8f, 0x80, 0xfa, 0x8e, 0xe3, 0x90, 0xfd, 0xb8, 0x5a, 0x35, 0x8c, 0xce, 0x2c, 0x6d, 0xab, 0x39, 0x2a, 0x81]
ct=[ 0xbc, 0x0e, 0x0c, 0x7b, 0xfc, 0x72, 0x82, 0xe3, 0x83, 0x53, 0xfc, 0x9f, 0x0b, 0x38, 0x48, 0xcf, 0x32, 0xec, 0x2b, 0x77, 0x11, 0x8c, 0xed, 0xf6, 0x53, 0x6b, 0xf1, 0x94, 0x9b, 0xb5, 0x25, 0x68, 0x86, 0xba, 0x09, 0xe8, 0x43 ]
rotate = 0
for i in range(0x25):
    iVar1 = i + 0x17
    iVar1 = iVar1 % 0x25
    print(iVar1)
    if i == 0:
        rotate = iVar1

print(rotate)

ot = ""
for i,c in enumerate(ct):
    ii = ((((i + 0x25 - 23) % 0x25) * 1337) % 256)
    im = (lt.index(c) ^ ii) % 256
    ot += chr(im)
print(ot)
print(ot[rotate:]+ot[:rotate])    