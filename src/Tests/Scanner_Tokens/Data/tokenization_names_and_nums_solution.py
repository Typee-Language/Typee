#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2018 Philippe Schmouker, Typhee project, http://www.typee.ovh

Permission is hereby granted,  free of charge,  to any person obtaining a copy
of this software and associated documentation files (the "Software"),  to deal
in the Software without restriction, including  without  limitation the rights
to use,  copy,  modify,  merge,  publish,  distribute, sublicense, and/or sell
copies of the Software,  and  to  permit  persons  to  whom  the  Software  is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS",  WITHOUT WARRANTY OF ANY  KIND,  EXPRESS  OR
IMPLIED,  INCLUDING  BUT  NOT  LIMITED  TO  THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT  SHALL  THE
AUTHORS  OR  COPYRIGHT  HOLDERS  BE  LIABLE  FOR  ANY CLAIM,  DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT,  TORT OR OTHERWISE, ARISING FROM,
OUT  OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#=============================================================================
from FrontEnd.IntermediateCode.fe_icode_node import *


#=============================================================================
soluce = [ ICNode_COMMENT( None, " Names and Nums tokens -- tokenization test source" ),
           ICNode_NL(),
           ICNode_COMMENT_ML( None, "**\ni.e. identifiers, function and class names, reserved keywords, integer and float numbers\n**" ),
		   ICNode_NL(),
		   ICNode_IDENT( None, "a"),
		   ICNode_IDENT( None, "b"),
		   ICNode_IDENT( None, "c"),
		   ICNode_IDENT( None, "d"),
		   ICNode_IDENT( None, "e"),
		   ICNode_IDENT( None, "f"),
		   ICNode_IDENT( None, "g"),
		   ICNode_IDENT( None, "h"),
		   ICNode_IDENT( None, "i"),
		   ICNode_IDENT( None, "j"),
		   ICNode_IDENT( None, "k"),
		   ICNode_IDENT( None, "l"),
		   ICNode_IDENT( None, "m"),
		   ICNode_IDENT( None, "n"),
		   ICNode_IDENT( None, "o"),
		   ICNode_IDENT( None, "p"),
		   ICNode_IDENT( None, "q"),
		   ICNode_IDENT( None, "r"),
		   ICNode_IDENT( None, "s"),
		   ICNode_IDENT( None, "t"),
		   ICNode_IDENT( None, "u"),
		   ICNode_IDENT( None, "v"),
		   ICNode_IDENT( None, "w"),
		   ICNode_IDENT( None, "x"),
		   ICNode_IDENT( None, "y"),
		   ICNode_IDENT( None, "z"),
           ICNode_NL(),
		   ICNode_IDENT( None, "A"),
		   ICNode_IDENT( None, "B"),
		   ICNode_IDENT( None, "C"),
		   ICNode_IDENT( None, "D"),
		   ICNode_IDENT( None, "E"),
		   ICNode_IDENT( None, "F"),
		   ICNode_IDENT( None, "G"),
		   ICNode_IDENT( None, "H"),
		   ICNode_IDENT( None, "I"),
		   ICNode_IDENT( None, "J"),
		   ICNode_IDENT( None, "K"),
		   ICNode_IDENT( None, "L"),
		   ICNode_IDENT( None, "M"),
		   ICNode_IDENT( None, "N"),
		   ICNode_IDENT( None, "O"),
		   ICNode_IDENT( None, "P"),
		   ICNode_IDENT( None, "Q"),
		   ICNode_IDENT( None, "R"),
		   ICNode_IDENT( None, "S"),
		   ICNode_IDENT( None, "T"),
		   ICNode_IDENT( None, "U"),
		   ICNode_IDENT( None, "V"),
		   ICNode_IDENT( None, "W"),
		   ICNode_IDENT( None, "X"),
		   ICNode_IDENT( None, "Y"),
		   ICNode_IDENT( None, "Z"),
		   ICNode_NL(),
           ICNode_IDENT( None, "_"),
		   ICNode_IDENT( None, "_name"),
		   ICNode_IDENT( None, "__ident__"),
		   ICNode_IDENT( None, "__"),
		   ICNode_IDENT( None, "set_num"),
		   ICNode_NL(),
		   ICNode_IDENT( None, "qmsli"),
		   ICNode_IDENT( None, "Qbhjken"),
		   ICNode_IDENT( None, "_123"),
		   ICNode_IDENT( None, "a1"),
		   ICNode_IDENT( None, "b2"),
		   ICNode_IDENT( None, "c3d_"),
		   ICNode_IDENT( None, "abstract1"),
		   ICNode_IDENT( None, "_const"),
		   ICNode_IDENT( None, "i_uint32"),
		   ICNode_NL(),
		   ICNode_LANGUAGE( None, "py" ),
		   ICNode_LANGUAGE( None, "python" ),
		   ICNode_LANGUAGE( None, "java" ),
		   ICNode_LANGUAGE( None, "javascript" ),
		   ICNode_LANGUAGE( None, "cpp" ),
		   ICNode_LANGUAGE( None, "m6809" ),
		   ICNode_NL(),
		   ICNode_ABSTRACT(),
		   ICNode_PUBLIC(),
		   ICNode_CONST(),
		   ICNode_SCALAR_TYPE( None, "uint8" ),
		   ICNode_IDENT(None, "my_abstract_function"),
		   ICNode_NL(),
		   ICNode_RETURN(),
		   ICNode_RETURN( None, 'ret' ),
		   ICNode_NL(),
		   ICNode_SCALAR_TYPE( None, "float32" ),
		   ICNode_IDENT( None, "f_num" ),
		   ICNode_NL(),
		   ICNode_VOLATILE(),
		   ICNode_SCALAR_TYPE( None, "bool" ),
		   ICNode_IDENT( None, "is_ok" ),
		   ICNode_NL(),
		   ICNode_ASSERT(),
		   ICNode_IDENT( None, "is_ok" ),
		   ICNode_NL(),
		   ICNode_ENSURE(),
		   ICNode_IDENT( None, "is_ok" ),
		   ICNode_NL(),
		   ICNode_REQUIRE(),
		   ICNode_IDENT( None, "is_ok" ),
		   ICNode_NL(),
		   ICNode_IF(),
		   ICNode_IDENT( None, "is_ok" ),
		   ICNode_AND(),
		   ICNode_IDENT( None, "is_ok" ),
		   ICNode_OR(),
		   ICNode_NOT(),
		   ICNode_IDENT( None, "is_ok" ),
		   ICNode_NL(),
		   ICNode_NOP( None, 'pass'),
		   ICNode_NOP(),
		   ICNode_NL(),
		   ICNode_ELIF(),
		   ICNode_ELIF( None, 'elsif' ),
		   ICNode_ELIF( None, 'elseif' ),
		   ICNode_ELSE(),
		   ICNode_IF(),
		   ICNode_TRUE( None, 'True' ),
		   ICNode_TRUE(),
		   ICNode_FALSE( None, 'False' ),
		   ICNode_FALSE(),
		   ICNode_NL(),
		   ICNode_ELSE(),
		   ICNode_NL(),
		   ICNode_ARRAY(),
		   ICNode_LT(),
		   ICNode_SCALAR_TYPE( None, "uint16" ),
		   ICNode_GT(),
		   ICNode_NL(),
		   ICNode_WITH(),
		   ICNode_IDENT( None, "var" ),
		   ICNode_AS(),
		   ICNode_IDENT( None, "_var" ),
		   ICNode_NL(),
		   ICNode_FROM(),
		   ICNode_IMPORT(),
		   ICNode_ALL(),
           ICNode_NL(),
		   ICNode_FOR(),
		   ICNode_SCALAR_TYPE( None, "int8" ),
		   ICNode_IDENT( None, "i" ),
		   ICNode_IN(),
		   ICNode_NL(),
		   ICNode_FOREVER(),
		   ICNode_NL(),
		   ICNode_BREAK(),
		   ICNode_NL(),
		   ICNode_CONTINUE(),
		   ICNode_NL(),
		   ICNode_LIST(),
		   ICNode_MAP(),
		   ICNode_SET(),
		   ICNode_ENUM(),
           ICNode_FILE(),
		   ICNode_NL(),
		   ICNode_CLASS(),
		   ICNode_NL(),
		   ICNode_HIDDEN(),
           ICNode_HIDDEN( None, 'local' ),
           ICNode_HIDDEN( None, 'private' ),
		   ICNode_PROTECTED(),
		   ICNode_FINAL(),
		   ICNode_NL(),
		   ICNode_SWITCH(),
		   ICNode_CASE(),
		   ICNode_NL(),
		   ICNode_UNNAMED(),
		   ICNode_UNNAMED( None, 'lambda' ),
		   ICNode_NL(),
           ICNode_OPERATOR(),
           ICNode_CAST(),
		   ICNode_NL(),
		   ICNode_TRY(),
		   ICNode_EXCEPT(),
		   ICNode_FINALLY(),
		   ICNode_RAISE(),
		   ICNode_NL(),
		   ICNode_IS(),
		   ICNode_ME(),
           ICNode_NONE(),
           ICNode_NONE( None, 'None' ),
		   ICNode_NL(),
		   ICNode_WHILE(),
		   ICNode_REPEAT(),
		   ICNode_UNTIL(),
           ICNode_NL(),
		   ICNode_EMBED(),
           ICNode_NL(),
		   ICNode_SCALAR_TYPE( None, "char" ),
		   ICNode_SCALAR_TYPE( None, "char16" ),
		   ICNode_DEL(),
		   ICNode_SCALAR_TYPE( None, "float64" ),
		   ICNode_SCALAR_TYPE( None, "int16" ),
		   ICNode_SCALAR_TYPE( None, "int32" ),
		   ICNode_SCALAR_TYPE( None, "int64" ),
		   ICNode_SCALAR_TYPE( None, "str" ),
		   ICNode_SCALAR_TYPE( None, "str16" ),
		   ICNode_SCALAR_TYPE( None, "uint32" ),
		   ICNode_SCALAR_TYPE( None, "uint64" ),
		   ICNode_NL(),
		   ICNode_IDENT( None, "UInt8" ),
		   ICNode_IDENT( None, "Float32" ),
		   ICNode_IDENT( None, "float" ),
		   ICNode_IDENT( None, "double" ),
		   ICNode_IDENT( None, "Str" ),
		   ICNode_IDENT( None, "string" ),
		   ICNode_IDENT( None, "Class" ),
           ICNode_NL(),
		   ICNode_INTEGER( None, "0" ),
		   ICNode_INTEGER( None, "1" ),
		   ICNode_INTEGER( None, "2" ),
		   ICNode_INTEGER( None, "3" ),
		   ICNode_INTEGER( None, "4" ),
		   ICNode_INTEGER( None, "5" ),
		   ICNode_INTEGER( None, "6" ),
		   ICNode_INTEGER( None, "7" ),
		   ICNode_INTEGER( None, "8" ),
		   ICNode_INTEGER( None, "9" ),
		   ICNode_IDENT( None, "_0" ),
		   ICNode_IDENT( None, "_1" ),
		   ICNode_IDENT( None, "_2" ),
		   ICNode_IDENT( None, "_3" ),
		   ICNode_IDENT( None, "_4" ),
		   ICNode_IDENT( None, "_5" ),
		   ICNode_IDENT( None, "_6"),
		   ICNode_IDENT( None, "_7" ),
		   ICNode_IDENT( None, "_8" ),
		   ICNode_IDENT( None, "_9" ),
		   ICNode_NL(),
		   ICNode_FLOAT( None, "123.456" ),
		   ICNode_FLOAT( None, "123e45" ),
		   ICNode_FLOAT( None, "79.46E+13" ),
		   ICNode_FLOAT( None, "79.46e+13" ),
		   ICNode_NL(),
           ICNode_MINUS(),
		   ICNode_INTEGER( None, "12" ),
           ICNode_MINUS(),
		   ICNode_FLOAT( None, "12e008" ),
           ICNode_MINUS(),
		   ICNode_FLOAT( None, "12e-009" ),
           ICNode_MINUS(),
		   ICNode_FLOAT( None, "12.e-9" ),
		   ICNode_NL(),
		   ICNode_INTEGER( None, "123_456_789" ),
		   ICNode_FLOAT( None, "1_234.567_89e1_234" ),
		   ICNode_NL(),
		   ICNode_INTEGER( None, "0x123456789abcdefABCDEF" ),
		   ICNode_NL(),
		   ICNode_INTEGER( None, "0b010_101" ),
		   ICNode_NL(),
		   ICNode_INTEGER( None, "01234567" ),
		   ICNode_NL(),
           ICNode_UNEXPECTED( None, "8" ),
           ICNode_UNEXPECTED( None, "9" ),
		   ICNode_NL(),
		   ICNode_UNEXPECTED( None, "g" ),
		   ICNode_NL(),
		   ICNode_UNEXPECTED( None, "2" ),
		   ICNode_NL(),
		   ICNode_UNEXPECTED( None, "_678" ),
		   ICNode_UNEXPECTED( None, "_789" ),
		   ICNode_UNEXPECTED( None, "" ),
		   ICNode_IDENT( None, "_123_456_789" ),
		   ICNode_NL(),
		   ICNode_IDENT( None, "var_name1" ),
		   ICNode_BITAND(),
		   ICNode_IDENT( None, "var_name2" ),
		   ICNode_NL(),
		   ICNode_INTEGER( None, "45" ),
		   ICNode_PLUS(),
		   ICNode_MINUS(),
		   ICNode_INTEGER( None, "45"),
		   ICNode_NL(),
           ICNode_UNEXPECTED( None, "abc" ),
           ICNode_NL(),
           ICNode_UNEXPECTED( None, "abc" ),
           ICNode_NL(),
           ICNode_TYPE_ALIAS(),
           ICNode_NL(),

           ICNode_EOF()
          ]

#=====   end of   Tests.Data.tokenization_names_and_nums_solution   =====#