# tunn3l v1s10n

[tunn3l v1s10n](https://play.picoctf.org/practice/challenge/112)

## Description

We found this file. Recover the flag.

## Solution

We can open the file in a hex editor and we can observe that it starts with `\x42\x4D` which is "BM" in ascii. I have googled the header format since I kind of knew it was related to images from the past. I have found the BMP format header and checked if I can open the file using `feh` but it didn't work. So I tried to look in the header bytes to see if there are any errors. Something that jumped to me was the bytes `BAD00000` which made me think that this is what we have to modify. In fact those are the sizes of the BMP and DIB headers, which are (I think) always `36 00 00 00` and `28 00 00 00`. So we can modify those values to the correct ones and check now the image. However, this results in an image that contains the text `notaflag{sorry}`. But somehow the image seems that it should be larger, at least on the height dimension. So I computed the number of pixels, the width and height (using the DIB header). I observed that `width * height != pixels` so I changed the bytes for height to `pixels // width` and the new image also displayed the flag at the top `picoCTF{qu1t3_a_v13w_2020}`.