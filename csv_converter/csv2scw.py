import struct
import pandas as pd

cts = pd.read_csv('converted.csv', usecols = ['Info2'])

sc3d = cts.iloc[0,0].encode()

head_uint32_length = cts.iloc[1,0]
head = cts.iloc[2,0].encode()
head_version = cts.iloc[3,0]
head_frameRate = cts.iloc[4,0]
head_unk2 = cts.iloc[5,0]
head_AnimFrameEnd = cts.iloc[6,0]
head_mat_length = cts.iloc[7,0]
head_mat_length = int(head_mat_length)
head_mat_name = cts.iloc[8,0]
head_unkBool = cts.iloc[9,0]
head_unkBool = 0
head_crc32 = cts.iloc[10,0]

b_head_uint32_length = struct.pack('>I', int(head_uint32_length))
b_head_version = struct.pack('>H', int(head_version))
b_head_frameRate = struct.pack('>H', int(head_frameRate))
b_head_unk2 = struct.pack('>H', int(head_unk2))
b_head_AnimFrameEnd = struct.pack('>H', int(head_AnimFrameEnd))
b_head_mat_length = struct.pack('>h', int(head_mat_length))
b_head_unkBool = struct.pack('>?', 0)
b_head_crc32 = struct.pack('>I', int(head_crc32))

if head_mat_length == 0:
    scw_file = sc3d + b_head_uint32_length + head + b_head_version + b_head_frameRate + b_head_unk2 + b_head_AnimFrameEnd + b_head_mat_length + b_head_unkBool + b_head_crc32
else:
    scw_file = sc3d + b_head_uint32_length + head + b_head_version + b_head_frameRate + b_head_unk2 + b_head_AnimFrameEnd + b_head_mat_length + head_mat_name.encode() + b_head_unkBool + b_head_crc32

print('Successfully!')

save_scw = open('converted.scw', 'wb')
save_scw.write(scw_file)
save_scw.close()