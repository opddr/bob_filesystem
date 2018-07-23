import struct





f = open("gpt_128.dd","rb")
f.seek(1024)
print("=======================================")

for i in range(1,129):
	data = f.read(128)
	if struct.unpack_from("<I", data, 0)[0] == 0:
		print("=======================================")
		exit()
	start = struct.unpack_from("<I", data, 32)[0]
	last = struct.unpack_from("<I", data, 40)[0]
	print("start : ",start)
	print("last : ",last)
	
exit()
