#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2018-2019 Philippe Schmouker, Typhee project, http://www.typee.ovh

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
from FrontEnd.IntermediateCode.fe_icode_token_node import *


#=============================================================================
soluce = [ ICTokenNode_COMMENT( None, " Names and Nums tokens -- tokenization test source" ),
           ICTokenNode_NL(),
           ICTokenNode_COMMENT_ML( None, "**\ni.e. identifiers, function and class names, reserved keywords, integer and float numbers\n**" ),
		   ICTokenNode_NL(),
		   ICTokenNode_IDENT( None, "a"),
		   ICTokenNode_IDENT( None, "b"),
		   ICTokenNode_IDENT( None, "c"),
		   ICTokenNode_IDENT( None, "d"),
		   ICTokenNode_IDENT( None, "e"),
		   ICTokenNode_IDENT( None, "f"),
		   ICTokenNode_IDENT( None, "g"),
		   ICTokenNode_IDENT( None, "h"),
		   ICTokenNode_IDENT( None, "i"),
		   ICTokenNode_IDENT( None, "j"),
		   ICTokenNode_IDENT( None, "k"),
		   ICTokenNode_IDENT( None, "l"),
		   ICTokenNode_IDENT( None, "m"),
		   ICTokenNode_IDENT( None, "n"),
		   ICTokenNode_IDENT( None, "o"),
		   ICTokenNode_IDENT( None, "p"),
		   ICTokenNode_IDENT( None, "q"),
		   ICTokenNode_IDENT( None, "r"),
		   ICTokenNode_IDENT( None, "s"),
		   ICTokenNode_IDENT( None, "t"),
		   ICTokenNode_IDENT( None, "u"),
		   ICTokenNode_IDENT( None, "v"),
		   ICTokenNode_IDENT( None, "w"),
		   ICTokenNode_IDENT( None, "x"),
		   ICTokenNode_IDENT( None, "y"),
		   ICTokenNode_IDENT( None, "z"),
           ICTokenNode_NL(),
		   ICTokenNode_IDENT( None, "A"),
		   ICTokenNode_IDENT( None, "B"),
		   ICTokenNode_IDENT( None, "C"),
		   ICTokenNode_IDENT( None, "D"),
		   ICTokenNode_IDENT( None, "E"),
		   ICTokenNode_IDENT( None, "F"),
		   ICTokenNode_IDENT( None, "G"),
		   ICTokenNode_IDENT( None, "H"),
		   ICTokenNode_IDENT( None, "I"),
		   ICTokenNode_IDENT( None, "J"),
		   ICTokenNode_IDENT( None, "K"),
		   ICTokenNode_IDENT( None, "L"),
		   ICTokenNode_IDENT( None, "M"),
		   ICTokenNode_IDENT( None, "N"),
		   ICTokenNode_IDENT( None, "O"),
		   ICTokenNode_IDENT( None, "P"),
		   ICTokenNode_IDENT( None, "Q"),
		   ICTokenNode_IDENT( None, "R"),
		   ICTokenNode_IDENT( None, "S"),
		   ICTokenNode_IDENT( None, "T"),
		   ICTokenNode_IDENT( None, "U"),
		   ICTokenNode_IDENT( None, "V"),
		   ICTokenNode_IDENT( None, "W"),
		   ICTokenNode_IDENT( None, "X"),
		   ICTokenNode_IDENT( None, "Y"),
		   ICTokenNode_IDENT( None, "Z"),
		   ICTokenNode_NL(),
           ICTokenNode_IDENT( None, "_"),
		   ICTokenNode_IDENT( None, "_name"),
		   ICTokenNode_IDENT( None, "__ident__"),
		   ICTokenNode_IDENT( None, "__"),
		   ICTokenNode_IDENT( None, "set_num"),
		   ICTokenNode_NL(),
		   ICTokenNode_IDENT( None, "qmsli"),
		   ICTokenNode_IDENT( None, "Qbhjken"),
		   ICTokenNode_IDENT( None, "_123"),
		   ICTokenNode_IDENT( None, "a1"),
		   ICTokenNode_IDENT( None, "b2"),
		   ICTokenNode_IDENT( None, "c3d_"),
		   ICTokenNode_IDENT( None, "abstract1"),
		   ICTokenNode_IDENT( None, "_const"),
		   ICTokenNode_IDENT( None, "i_uint32"),
		   ICTokenNode_NL(),
		   ICTokenNode_LANGUAGE( None, "py" ),
		   ICTokenNode_LANGUAGE( None, "python" ),
		   ICTokenNode_LANGUAGE( None, "java" ),
		   ICTokenNode_LANGUAGE( None, "javascript" ),
		   ICTokenNode_LANGUAGE( None, "cpp" ),
		   ICTokenNode_LANGUAGE( None, "m6809" ),
		   ICTokenNode_NL(),
		   ICTokenNode_ABSTRACT(),
		   ICTokenNode_PUBLIC(),
		   ICTokenNode_CONST(),
		   ICTokenNode_SCALAR_TYPE( None, "uint8" ),
		   ICTokenNode_IDENT(None, "my_abstract_function"),
		   ICTokenNode_NL(),
		   ICTokenNode_RETURN(),
		   ICTokenNode_RETURN( None, 'ret' ),
		   ICTokenNode_NL(),
		   ICTokenNode_SCALAR_TYPE( None, "float32" ),
		   ICTokenNode_IDENT( None, "f_num" ),
		   ICTokenNode_NL(),
		   ICTokenNode_VOLATILE(),
		   ICTokenNode_SCALAR_TYPE( None, "bool" ),
		   ICTokenNode_IDENT( None, "is_ok" ),
		   ICTokenNode_NL(),
		   ICTokenNode_ASSERT(),
		   ICTokenNode_IDENT( None, "is_ok" ),
		   ICTokenNode_NL(),
		   ICTokenNode_ENSURE(),
		   ICTokenNode_IDENT( None, "is_ok" ),
		   ICTokenNode_NL(),
		   ICTokenNode_REQUIRE(),
		   ICTokenNode_IDENT( None, "is_ok" ),
		   ICTokenNode_NL(),
		   ICTokenNode_IF(),
		   ICTokenNode_IDENT( None, "is_ok" ),
		   ICTokenNode_AND(),
		   ICTokenNode_IDENT( None, "is_ok" ),
		   ICTokenNode_OR(),
		   ICTokenNode_NOT(),
		   ICTokenNode_IDENT( None, "is_ok" ),
		   ICTokenNode_NL(),
		   ICTokenNode_NOP( None, 'pass'),
		   ICTokenNode_NOP(),
		   ICTokenNode_NL(),
		   ICTokenNode_ELIF(),
		   ICTokenNode_ELIF( None, 'elsif' ),
		   ICTokenNode_ELIF( None, 'elseif' ),
		   ICTokenNode_ELSE(),
		   ICTokenNode_IF(),
		   ICTokenNode_TRUE( None, 'True' ),
		   ICTokenNode_TRUE(),
		   ICTokenNode_FALSE( None, 'False' ),
		   ICTokenNode_FALSE(),
		   ICTokenNode_NL(),
		   ICTokenNode_ELSE(),
		   ICTokenNode_NL(),
		   ICTokenNode_ARRAY(),
		   ICTokenNode_LT(),
		   ICTokenNode_SCALAR_TYPE( None, "uint16" ),
		   ICTokenNode_GT(),
		   ICTokenNode_NL(),
		   ICTokenNode_WITH(),
		   ICTokenNode_IDENT( None, "var" ),
		   ICTokenNode_AS(),
		   ICTokenNode_IDENT( None, "_var" ),
		   ICTokenNode_NL(),
		   ICTokenNode_FROM(),
		   ICTokenNode_IMPORT(),
		   ICTokenNode_ALL(),
           ICTokenNode_NL(),
		   ICTokenNode_FOR(),
		   ICTokenNode_SCALAR_TYPE( None, "int8" ),
		   ICTokenNode_IDENT( None, "i" ),
		   ICTokenNode_IN(),
		   ICTokenNode_NL(),
		   ICTokenNode_FOREVER(),
		   ICTokenNode_NL(),
		   ICTokenNode_BREAK(),
		   ICTokenNode_NL(),
		   ICTokenNode_CONTINUE(),
		   ICTokenNode_NL(),
		   ICTokenNode_LIST(),
		   ICTokenNode_MAP(),
		   ICTokenNode_SET(),
		   ICTokenNode_ENUM(),
           ICTokenNode_FILE(),
		   ICTokenNode_NL(),
		   ICTokenNode_CLASS(),
		   ICTokenNode_NL(),
		   ICTokenNode_HIDDEN(),
           ICTokenNode_HIDDEN( None, 'local' ),
           ICTokenNode_HIDDEN( None, 'private' ),
		   ICTokenNode_PROTECTED(),
		   ICTokenNode_FINAL(),
		   ICTokenNode_NL(),
		   ICTokenNode_SWITCH(),
		   ICTokenNode_CASE(),
		   ICTokenNode_NL(),
		   ICTokenNode_UNNAMED(),
		   ICTokenNode_UNNAMED( None, 'lambda' ),
		   ICTokenNode_NL(),
           ICTokenNode_OPERATOR(),
           ICTokenNode_CAST(),
		   ICTokenNode_NL(),
		   ICTokenNode_TRY(),
		   ICTokenNode_EXCEPT(),
		   ICTokenNode_FINALLY(),
		   ICTokenNode_RAISE(),
		   ICTokenNode_NL(),
		   ICTokenNode_IS(),
		   ICTokenNode_ME(),
           ICTokenNode_NONE(),
           ICTokenNode_NONE( None, 'None' ),
		   ICTokenNode_NL(),
		   ICTokenNode_WHILE(),
		   ICTokenNode_REPEAT(),
		   ICTokenNode_UNTIL(),
           ICTokenNode_NL(),
           ICTokenNode_EMBED(),
           ICTokenNode_EXCLUDE(),
           ICTokenNode_NL(),
		   ICTokenNode_SCALAR_TYPE( None, "char" ),
		   ICTokenNode_SCALAR_TYPE( None, "char16" ),
		   ICTokenNode_DEL(),
		   ICTokenNode_SCALAR_TYPE( None, "float64" ),
		   ICTokenNode_SCALAR_TYPE( None, "int16" ),
		   ICTokenNode_SCALAR_TYPE( None, "int32" ),
		   ICTokenNode_SCALAR_TYPE( None, "int64" ),
		   ICTokenNode_SCALAR_TYPE( None, "str" ),
		   ICTokenNode_SCALAR_TYPE( None, "str16" ),
		   ICTokenNode_SCALAR_TYPE( None, "uint32" ),
		   ICTokenNode_SCALAR_TYPE( None, "uint64" ),
		   ICTokenNode_NL(),
		   ICTokenNode_IDENT( None, "UInt8" ),
		   ICTokenNode_IDENT( None, "Float32" ),
		   ICTokenNode_IDENT( None, "float" ),
		   ICTokenNode_IDENT( None, "double" ),
		   ICTokenNode_IDENT( None, "Str" ),
		   ICTokenNode_IDENT( None, "string" ),
		   ICTokenNode_IDENT( None, "Class" ),
           ICTokenNode_NL(),
		   ICTokenNode_INTEGER( None, "0" ),
		   ICTokenNode_INTEGER( None, "1" ),
		   ICTokenNode_INTEGER( None, "2" ),
		   ICTokenNode_INTEGER( None, "3" ),
		   ICTokenNode_INTEGER( None, "4" ),
		   ICTokenNode_INTEGER( None, "5" ),
		   ICTokenNode_INTEGER( None, "6" ),
		   ICTokenNode_INTEGER( None, "7" ),
		   ICTokenNode_INTEGER( None, "8" ),
		   ICTokenNode_INTEGER( None, "9" ),
		   ICTokenNode_IDENT( None, "_0" ),
		   ICTokenNode_IDENT( None, "_1" ),
		   ICTokenNode_IDENT( None, "_2" ),
		   ICTokenNode_IDENT( None, "_3" ),
		   ICTokenNode_IDENT( None, "_4" ),
		   ICTokenNode_IDENT( None, "_5" ),
		   ICTokenNode_IDENT( None, "_6"),
		   ICTokenNode_IDENT( None, "_7" ),
		   ICTokenNode_IDENT( None, "_8" ),
		   ICTokenNode_IDENT( None, "_9" ),
		   ICTokenNode_NL(),
		   ICTokenNode_FLOAT( None, "123.456" ),
		   ICTokenNode_FLOAT( None, "123e45" ),
		   ICTokenNode_FLOAT( None, "79.46E+13" ),
		   ICTokenNode_FLOAT( None, "79.46e+13" ),
		   ICTokenNode_NL(),
           ICTokenNode_MINUS(),
		   ICTokenNode_INTEGER( None, "12" ),
           ICTokenNode_MINUS(),
		   ICTokenNode_FLOAT( None, "12e008" ),
           ICTokenNode_MINUS(),
		   ICTokenNode_FLOAT( None, "12e-009" ),
           ICTokenNode_MINUS(),
		   ICTokenNode_FLOAT( None, "12.e-9" ),
		   ICTokenNode_NL(),
		   ICTokenNode_INTEGER( None, "123_456_789" ),
		   ICTokenNode_FLOAT( None, "1_234.567_89e1_234" ),
		   ICTokenNode_NL(),
		   ICTokenNode_INTEGER( None, "0x123456789abcdefABCDEF" ),
		   ICTokenNode_NL(),
		   ICTokenNode_INTEGER( None, "0b010_101" ),
		   ICTokenNode_NL(),
		   ICTokenNode_INTEGER( None, "01234567" ),
		   ICTokenNode_NL(),
           ICTokenNode_UNEXPECTED( None, "8" ),
           ICTokenNode_UNEXPECTED( None, "9" ),
		   ICTokenNode_NL(),
		   ICTokenNode_UNEXPECTED( None, "g" ),
		   ICTokenNode_NL(),
		   ICTokenNode_UNEXPECTED( None, "2" ),
		   ICTokenNode_NL(),
		   ICTokenNode_UNEXPECTED( None, "_678" ),
		   ICTokenNode_UNEXPECTED( None, "_789" ),
		   ICTokenNode_UNEXPECTED( None, "" ),
		   ICTokenNode_IDENT( None, "_123_456_789" ),
		   ICTokenNode_NL(),
		   ICTokenNode_IDENT( None, "var_name1" ),
		   ICTokenNode_BITAND(),
		   ICTokenNode_IDENT( None, "var_name2" ),
		   ICTokenNode_NL(),
		   ICTokenNode_INTEGER( None, "45" ),
		   ICTokenNode_PLUS(),
		   ICTokenNode_MINUS(),
		   ICTokenNode_INTEGER( None, "45"),
		   ICTokenNode_NL(),
           ICTokenNode_UNEXPECTED( None, "abc" ),
           ICTokenNode_NL(),
           ICTokenNode_UNEXPECTED( None, "abc" ),
           ICTokenNode_NL(),
           ICTokenNode_TYPE_ALIAS(),
           ICTokenNode_NL(),

           ICTokenNode_EOF()
          ]

#=====   end of   Tests.Data.tokenization_names_and_nums_solution   =====#
