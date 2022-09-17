#!/usr/bin/env python3
import os
import sys
import struct
import urllib.request

file_name = "tunn3l-v1s10n"

if not os.path.isfile(file_name):
    if len(sys.argv) != 2:
        print('Usage: ./solve.py <url>')
        exit(1)
    with urllib.request.urlopen(sys.argv[1]) as response:
        with open(file_name, 'wb') as f:
            f.write(response.read())

# These are corrupt in the bmp file so we cannot read them
pixel_offset_offset = 0x0A
pixel_offset_size = 0x04
pixel_offset_value = int(struct.pack("<I", 0x36000000).hex(), 16)
dib_header_size_offset = 0x0E
dib_header_size_size = 0x04
dib_header_size_value = int(struct.pack("<I", 0x28000000).hex(), 16)

with open(file_name, "rb") as f:
    bytes_data = f.read()

bmp_file_size_offset = 0x02
bmp_file_size_size = 0x04
bmp_file_size_value = int.from_bytes(bytes_data[bmp_file_size_offset:bmp_file_size_offset + bmp_file_size_size], byteorder="little")

dib_width_offset = 0x12
dib_width_size = 0x04
dib_width_value = int.from_bytes(bytes_data[dib_width_offset:dib_width_offset + dib_width_size], byteorder="little")

bits_per_pixel_offset = 0x1C
bits_per_pixel_size = 0x02
bits_per_pixel_value = int.from_bytes(bytes_data[bits_per_pixel_offset:bits_per_pixel_offset + bits_per_pixel_size], byteorder="little")

# This value is corrupt so we compute it ourselves from the other values
pixels_count = (bmp_file_size_value - pixel_offset_value) // (bits_per_pixel_value // 8)
dib_height_offset = 0x16
dib_height_size = 0x04
dib_height_value = pixels_count // dib_width_value

fixed_bytes_data = (
    bytes_data[:pixel_offset_offset]
    + struct.pack("<I", pixel_offset_value)
    + bytes_data[pixel_offset_offset + pixel_offset_size : dib_header_size_offset]
    + struct.pack("<I", dib_header_size_value)
    + bytes_data[dib_header_size_offset + dib_header_size_size : dib_height_offset]
    + struct.pack("<I", dib_height_value)
    + bytes_data[dib_height_offset + dib_height_size :]
)

with open("tunn3l_v1s10n_fixed.bmp", "wb") as f:
    f.write(fixed_bytes_data)