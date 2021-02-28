import struct
import sys

sf = scwfile = open('scwfile.scw', 'rb')

sc3d = struct.unpack('4s', sf.read(4))[0].decode()

head_uint32_length = struct.unpack('>I', sf.read(4))[0]
head = struct.unpack('4s', sf.read(4))[0].decode() 
head_version = struct.unpack('>H', sf.read(2))[0]
head_frameRate = struct.unpack('>H', sf.read(2))[0]
head_unk2 = struct.unpack('>H', sf.read(2))[0]
head_AnimFrameEnd = struct.unpack('>H', sf.read(2))[0]
head_mat_length = struct.unpack('>h', sf.read(2))[0]
head_mat_name = struct.unpack(f'>{head_mat_length}s', sf.read(head_mat_length))[0].decode()
head_unkBool= struct.unpack('?', sf.read(1))[0]
head_crc32 = struct.unpack('>I', sf.read(4))[0]

geom_uint32_length = struct.unpack('>I', sf.read(4))[0]
geom = struct.unpack('4s', sf.read(4))[0].decode()
geom_name_length = struct.unpack('>h', sf.read(2))[0]
geom_name = struct.unpack(f'>{geom_name_length}s', sf.read(geom_name_length))[0].decode()
geom_group_length = struct.unpack('>h', sf.read(2))[0]
geom_group = struct.unpack(f'>{geom_group_length}s', sf.read(geom_group_length))[0].decode()
geom_vertices_count = struct.unpack('B', sf.read(1))[0]

if sc3d != 'SC3D':
    print('SC3D Not Found')
    sys.exit()

elif geom == 'MATE':
    print('Mate Unsupported')
    sys.exit()

save_parsed = open('converted.csv', 'w')
save_parsed.write(f'Signatures,,\n')
save_parsed.write(f'{sc3d},File Format\n')
save_parsed.write(f'Head,Head Length,{head_uint32_length}\n')
save_parsed.write(f'Head,SCW Version,{head_version}\n')
save_parsed.write(f'Head,Unknown 2,{head_unk2}\n')
save_parsed.write(f'Head,Anim Frame End,{head_AnimFrameEnd}\n')
save_parsed.write(f'Head,Material Length,{head_mat_length}\n')
save_parsed.write(f'Head,Material Path,{head_mat_name}\n')
save_parsed.write(f'Head,Unknown B,{head_unkBool}\n')
save_parsed.write(f'Head,Crc32,{head_crc32}\n')
save_parsed.write(f'Geom,Geom Length,{geom_uint32_length}\n')
save_parsed.write(f'Geom,Name,{geom_name}\n')
save_parsed.write(f'Geom,Group,{geom_group}\n')
save_parsed.write(f'Geom,Vertices Count,{geom_vertices_count}')
save_parsed.close()