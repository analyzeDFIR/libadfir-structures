## -*- coding: UTF-8 -*-
## general.py
##
## Copyright (c) 2018 analyzeDFIR
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

from construct import *

'''
NTFSFILETIME
'''
NTFSFILETIME = Struct(
    'dwLowDateTime'         / Int32ul,
    'dwHighDateTime'        / Int32ul
)

'''
NTFS File Reference: pointer to base (parent) MFT record (0 if this is base record)
    SegmentNumber:  MFT entry index value
    SequenceNumber: MFT entry sequence number
'''
NTFSFileReference = Struct(
    'SegmentNumber'         / Int32ul,
    Padding(2),
    'SequenceNumber'        / Int16ul
)

'''
NTFSFileAttributeFlags
'''
NTFSFileAttributeFlags = FlagsEnum(Int32ul,
    READONLY                = 0x00000001,
    HIDDEN                  = 0x00000002,
    SYSTEM                  = 0x00000004,
    VOLUME                  = 0x00000008,
    DIRECTORY               = 0x00000010,
    ARCHIVE                 = 0x00000020,
    DEVICE                  = 0x00000040,
    NORMAL                  = 0x00000080,
    TEMPORARY               = 0x00000100,
    SPARSE_FILE             = 0x00000200,
    REPARSE_POINT           = 0x00000400,
    COMPRESSED              = 0x00000800,
    OFFLINE                 = 0x00001000,
    NOT_CONTENT_INDEXED     = 0x00002000,
    ENCRYPTED               = 0x00004000,
    VIRTUAL                 = 0x00010000
)
