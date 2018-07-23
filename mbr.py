import struct

def process_image(f,sectors):
        f.seek(sectors * 512)
        data = f.read(512)
        partition = data[446:446+64]

        table = [ partition[0:16] , partition[16:32],partition[32:48],partition[48:64]]
 
        for i in range(0,4):
                if table[i][4] == 0:
                        return 0;
                if table[i][4] == 7:
                        print("=======================================")
                        print("Starting LBA : ", (sectors + struct.unpack_from("<I", table[i], 8)[0])*512)
                        print("size : ", struct.unpack_from("<I", table[i], 12)[0] * 512)
                if table[i][4] == 5:
                        return process_image(f,sectors + struct.unpack_from("<I", table[i], 8)[0])
                        

filename = 'mbr_128.dd'
f = open(filename,"rb")
process_image(f,0)
print('================================')
