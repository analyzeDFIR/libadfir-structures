## -*- coding: UTF-8 -*-
## guid.py
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
from construct.lib import Container

'''
NTFS GUID: globally unique identifier
    Group1: first group of (8) hexadecimal digits of the GUID
    Group2: second group of (4) hexadecimal digits of the GUID
    Group3: third group of (4) hexadecimal digits of the GUID
    Group4: fourth group of (4) hexadecimal digits of the GUID
    Group5: fifth group of (12) hexadecimal digits of the GUID
    NOTE:
        A valid, full GUID is of the form:
           (1)    (2)  (3)  (4)     (5)
        6B29FC40-CA47-1067-B31D-00DD010662DA
'''
NTFSGUID = Struct(
    'Group1'                / Int32ul,
    'Group2'                / Int16ul,
    'Group3'                / Int16ul,
    'Group4'                / Int16ul,
    'Group5'                / BytesInteger(6, swapped=True)
)

def _itoh(num, digits=2):
    '''
    Args:
        num: Integer    => integer to convert to hex
        digits: Integer => number of hex digits to print
    Returns:
        String
        Hex representation of num
    Preconditions:
        num is of type Integer
        digits is of type Integer
    '''
    assert isinstance(num, int)
    assert isinstance(digits, int)
    format_str = '%%%02dx'%digits
    return (format_str%num).upper()

def guid_to_string(guid):
    '''
    Args:
        guid: NTFSGUID  => guid struct to convert to string
    Returns:
        String
        String representation of GUID in the form shown above
    Preconditions:
        guid is instance of NTFSGUID
    '''
    return '-'.join([
        _itoh(guid.Group1, 8),
        _itoh(guid.Group2, 4),
        _itoh(guid.Group3, 4),
        _itoh(guid.Group4, 4),
        _itoh(guid.Group5, 12)
    ])

def string_to_guid(guid):
    '''
    Args:
        guid: String    => guid string to convert to NTFSGUID
    Returns:
        Container<String, Any>
        Struct representation of String guid
    Preconditions:
        guid is of the format specified above (assumed True)
    '''
    groups = guid.strip().split('-')
    return Container(
        Group1  = int(groups[0], 16),
        Group2  = int(groups[1], 16),
        Group3  = int(groups[2], 16),
        Group4  = int(groups[3], 16),
        Group5  = int(groups[4], 16)
    )
