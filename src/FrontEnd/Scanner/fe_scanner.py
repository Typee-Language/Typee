#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2018 Philippe Schmouker, Typee project, http://www.typee.ovh

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
from FrontEnd.IntermediateCode.fe_icode_node         import *  ## to get access to all ICNode_XXX classes

from FrontEnd.IntermediateCode.fe_intermediate_code  import FEIntermediateCode


#=============================================================================
class FEScanner:
    """
    This is the class of the Typhon Front-End Scanner.
    It is the very first stage of the front-end pipeline of  the  Typhon
    compiler.
    It scans Typhon source code and produces tokenized Intermediate Code
    that will be parsed by the Typhon Front-End Parser.
    """
    
    #-------------------------------------------------------------------------
    def __init__(self):
        '''
        Constructor.
        '''
        self.intermediate_code = FEIntermediateCode()
        self.num_line = 1
        self.num_coln = 1
        

    #-------------------------------------------------------------------------
    def scan_file(self, filepath:str, **parse_args) -> FEIntermediateCode:
        '''
        Runs the Typhon scanner on a specified file.
        
        Args:
            filepath: str
                The path to the file to be scanned.
            parse_args: dict
                keyword arguments  that contain the parsing arguments as 
                passed at the global command line.
        
        Returns:
            A reference to the corresponding front-end intermediate code.
        
        Raises:
            IOError: source file not found or unavailable for reading.
        '''
        try:
            with open( filepath, 'r' ) as src_file:
                read_code = src_file.read()
            
            return self.scan_memory( read_code, **parse_args )
        
        except IOError as ioe:
            print( "ERROR: Maybe unable to find or to open file '{:s}'".format(filepath) )
            raise ioe
        
        except Exception as e:
            raise e

   
    #-------------------------------------------------------------------------
    def scan_memory(self, src_code:str, **parse_args) -> FEIntermediateCode:
        '''
        Scans the source code,  according to some parsing arguments  passed  at
        command line, and returns a reference to the corresponding intermediate
        code.
        
        Args:
            src_code: str
                A string containing the source code to be scanned.
            parse_args: dict
                keyword arguments that contain the parsing arguments 
                as passed at the global command.  Please notice that
                this argument is present here for future use.
        
        Returns:
            A reference to the generated Front-End Intermediate Code.
        '''
        self.code = src_code
        self.idx  = 0
        self.len_code = len( src_code )
        
        while not self._eof:
            self._tokenize()
        self._append_node( ICNode_EOF )
        
        return  self.intermediate_code


    #=========================================================================
    #-------------------------------------------------------------------------
    def _tokenize(self):
        if self._current in FEScanner._SIMPLE_TOKEN:
            self._append_node( FEScanner._SIMPLE_TOKEN[self._current], self._current ) 
            self._next_char()
            
        elif self._current in FEScanner._COMPOUND_TOKEN:
            self._COMPOUND_TOKEN[ self._current ]( self )
        
        elif self._current in FEScanner._NAME_ALPHA_CHARS:
            self._name()
        
        elif self._current in FEScanner._NUM_CHARS:
            self._number()
        
        elif self._current in FEScanner._ENDLINE:
            self._next_line( True )
        
        elif self._current in "'\"":
            self._single_string()
        
        elif self._current in FEScanner._SPACE:
            self._skip_space()
            
        else:
            self._append_node( ICNode_UNEXPECTED, self._current )
            self._next_char()


    #=========================================================================
    #-------------------------------------------------------------------------
    def _binary_number(self):
        self._parse_number( self._BIN_CHARS, True )
    #-------------------------------------------------------------------------
    def _check_augmented_operator(self, base_class, augmented_class, data, get_next:bool=True):
        if get_next:
            self._next_char()
        if self._current == '=':
            self._next_char()
            self._append_node( augmented_class, data+'=' )
        else:
            if base_class is ICNode_UNEXPECTED:
                self._append_node( base_class, self._current )
            else:
                self._append_node( base_class, data )
    #-------------------------------------------------------------------------
    def _check_escaped_char(self, count:int, base_chars:str):
        self._next_char()
        for _ in range(count):
            if self._eof:
                self._append_node( ICNode_UNEXPECTED, 'end of file' )
                break
            elif self._current in FEScanner._ENDLINE:
                self._append_node( ICNode_UNEXPECTED, 'end of line' )
                break
            elif self._current not in base_chars:
                self._append_node( ICNode_UNEXPECTED, self._current )
            self._next_char()
    #-------------------------------------------------------------------------
    def _comment(self):
        start = self.idx + 1
        while not self._eof  and  self._current not in self._ENDLINE:
            self._next_char()
        self._append_node( ICNode_COMMENT, self.code[start:self.idx] )
        if not self._eof:
            self._next_line( True )
    #-------------------------------------------------------------------------
    def _decimal_number(self):
        start = self.idx
        if self._decimal_part():
            self._error = False
            fract_part = self._fraction_part()
            expon_part = self._exponent_part()
            if not self._error:
                self._append_node( ICNode_FLOAT if fract_part or expon_part else ICNode_INTEGER,
                                   self.code[start:self.idx] )
    #-------------------------------------------------------------------------
    def _decimal_part(self) -> bool:
        while self._current in self._NUM_CHARS + '_':
            if self._current == '_':
                self._next_char()
                if self._current in self._NUM_CHARS:
                    self._next_char()
                else:
                    start = self.idx
                    while self._current in self._DOTTED_NAME_CHARS:
                        self._next_char()
                    self._append_node( ICNode_UNEXPECTED, self.code[start:self.idx] )
                    return False
            else:
                self._next_char()
        if self._current in self._NOT_DEC_CHARS:
            start = self.idx
            while self._current in self._NOT_DEC_CHARS:
                self._next_char()
            self._append_node( ICNode_UNEXPECTED, self.code[start:self.idx] )
            return False
        else:
            return True
    #-------------------------------------------------------------------------
    def _dot(self) -> bool:
        self._next_char()
        if self._current == '.':
            self._next_char()
            if self._current == '.':
                self._next_char()
                self._append_node( ICNode_ELLIPSIS, '...' )
                return True
            else:
                self._append_node( ICNode_UNEXPECTED, self._current )
                self._next_char()
                return False
        else:
            self._append_node( ICNode_DOT, '.' )
            return True
    #-------------------------------------------------------------------------
    def _embedded_code(self):
        start = self.idx
        while not self._eof:
            if self._current == '}':
                self._next_char()
                if self._current == '}':
                    self._append_node( ICNode_EMBED_CODE, self.code[start:self.idx-1] )
                    self._next_char()
                    break
            self._next_char()
    #-------------------------------------------------------------------------
    def _escaped_char(self):
        self._next_char()
        if self._current in FEScanner._ALPHA_CHARS:
            self._next_char()
        elif self._current == '0':
            self._next_char()
            if self._current in "xX":
                self._check_escaped_char( 4, FEScanner._HEXA_CHARS )
            elif self._current == '0':
                self._check_escaped_char( 3, FEScanner._OCTAL_CHARS )
            else:
                self._append_node( ICNode_UNEXPECTED, self._current )
        else:
            self._append_node( ICNode_UNEXPECTED, self._current )
    #-------------------------------------------------------------------------
    def _exponent_part(self) -> bool:
        if self._current in "eE":
            self._next_char()
            if self._current in "+-":
                self._next_char()
            self._error = self._error or not self._decimal_part()
            return True
        else:
            return False
    #-------------------------------------------------------------------------
    def _fraction_part(self) -> bool:
        if self._current == '.':
            self._next_char()
            self._error = self._error or not self._decimal_part()
            return True
        else:
            return False
    #-------------------------------------------------------------------------
    def _hexadecimal_number(self):
        self._parse_number( self._HEXA_CHARS, True )
    #-------------------------------------------------------------------------
    def _multi_lines_comment(self):
        start = self.idx + 1
        while True:
            if self._current in self._ENDLINE:
                self._next_line()
                ##self._next_char()
            elif self._current == '*':
                self._next_char()
                if self._current == '/':
                    self._next_char()
                    self._append_node( ICNode_COMMENT_ML, self.code[start:self.idx-2] )
                    break
            elif self._eof:
                self._append_node( ICNode_COMMENT_ML, self.code[start:] )
                self._append_node( ICNode_UNEXPECTED, 'end of file' )
                break
            else:
                self._next_char()
    #-------------------------------------------------------------------------
    def _name(self):
        start = self.idx
        while self._current in FEScanner._NAME_CHARS:
            self._next_char()
        name = self.code[start:self.idx]
        if name in FEScanner._KEYWORDS:
            kw_type = FEScanner._KEYWORDS[name]
            self._append_node( kw_type, name )
        elif name in FEScanner._LANGUAGE_KWDS:
            self._append_node( ICNode_LANGUAGE, name )
        else:
            self._append_node( ICNode_IDENT, name )
    #-------------------------------------------------------------------------
    def _number(self):
        if self._current == '0':
            self._octal_hexa_binary_number()
        else:
            self._decimal_number()
    #-------------------------------------------------------------------------
    def _octal_hexa_binary_number(self):
        self._next_char()
        if self._current in "bB":
            self._next_char()
            self._binary_number()
        elif self._current in "xX":
            self._next_char()
            self._hexadecimal_number()
        elif self._current in self._OCTAL_CHARS:
            self._octal_number()
        else:
            self._append_node( ICNode_INTEGER, '0' )
    #-------------------------------------------------------------------------
    def _octal_number(self):
        self._parse_number( self._OCTAL_CHARS )
    #-------------------------------------------------------------------------
    def _parse_number(self, num_chars, spec_char:bool=False) -> bool:
        if self._current in num_chars:
            self._next_char()
            start = self.idx - (3 if spec_char else 2)
            if self._parse_subnumber( num_chars ):
                self._append_node( ICNode_INTEGER, self.code[start : self.idx] )
                return True
            else:
                return False
        else:
            self._append_node( ICNode_UNEXPECTED, self._current )
            return False
    #-------------------------------------------------------------------------
    def _parse_subnumber(self, num_chars ) -> bool:
        while self._current in num_chars + '_':
            if self._current == '_':
                self._next_char()
                if self._current in num_chars:
                    self._next_char()
                else:
                    self._append_node( ICNode_UNEXPECTED, self._current )
                    while self._current in self._NAME_CHARS:
                        self._next_char()          
                    return False
            else:
                self._next_char()
        if self._current in self._NAME_CHARS:
            while self._current in self._NAME_CHARS:
                self._append_node( ICNode_UNEXPECTED, self._current )
                self._next_char()
            return False
        else:
            return True
    #-------------------------------------------------------------------------
    def _single_string(self) -> bool:
        if self._current == '"':
            return self._string_double_quote()
        elif self._current == "'":
            return self._string_quote()
        else:
            return False
    #-------------------------------------------------------------------------
    def _string_content(self, string_marker:str) -> bool:
        self._next_char()
        start = self.idx
        error = None
        while self._current != string_marker:
            if self._current in FEScanner._ENDLINE:
                error = 'line'
                break
            elif self._eof:
                error = 'file'
                break
            elif self._current == '\\':
                self._escaped_char()
            else:
                self._next_char()
        self._append_node( ICNode_STRING, self.code[start:self.idx] )
        if error:
            self._append_node( ICNode_UNEXPECTED, 'end of '+error )
        return True
    #-------------------------------------------------------------------------
    def _string_double_quote(self) -> bool:
        return self._string_content( '"' )
    #-------------------------------------------------------------------------
    def _string_quote(self) -> bool:
        return self._string_content( "'" )
    
    
    #=========================================================================
    #-------------------------------------------------------------------------
    def _arobase(self):
        self._check_augmented_operator( ICNode_AROBASE, ICNode_AUG_AROBASE, '@' )
    #-------------------------------------------------------------------------
    def _assign(self):
        self._check_augmented_operator( ICNode_ASSIGN, ICNode_EQ, '=' )
    #-------------------------------------------------------------------------
    def _bitand(self):
        self._check_augmented_operator( ICNode_BITAND, ICNode_AUG_BITAND, '&' )
    #-------------------------------------------------------------------------
    def _bitor(self):
        self._check_augmented_operator( ICNode_BITOR, ICNode_AUG_BITOR, '|' )
    #-------------------------------------------------------------------------
    def _brace_op(self):
        self._next_char()
        if self._current == '{':
            self._next_char()
            self._embedded_code()
        else:
            self._append_node( ICNode_BRACEOP, '{' )
    #-------------------------------------------------------------------------
    def _caret(self):
        self._next_char()
        if self._current == '^':
            self._check_augmented_operator( ICNode_POWER, ICNode_AUG_POWER, '^^' )
        else:
            self._check_augmented_operator( ICNode_BITXOR, ICNode_AUG_BITXOR, '^', False )
    #-------------------------------------------------------------------------
    def _colon(self):
        self._next_char()
        if self._current == ':':
            self._check_augmented_operator( ICNode_OP_2COLN, ICNode_AUG_2COLN, '::' )
        else:
            self._append_node( ICNode_COLON, ':' )
    #-------------------------------------------------------------------------
    def _div(self):
        self._next_char()
        if self._current == '/':
            self._comment()
        elif self._current == '*':
            self._multi_lines_comment()
        else:
            self._check_augmented_operator( ICNode_DIV, ICNode_AUG_DIV, '/', False )
    #-------------------------------------------------------------------------
    def _eq(self):
        self._check_augmented_operator( ICNode_ASSIGN, ICNode_EQ, '==' )
    #-------------------------------------------------------------------------
    def _excl(self):
        self._next_char()
        if self._current == '!':
            self._check_augmented_operator( ICNode_OP_2EXCL, ICNode_AUG_2EXCL, '!!' )
        else:
            self._check_augmented_operator( ICNode_UNEXPECTED, ICNode_NE, '!', False )
    #-------------------------------------------------------------------------
    def _greater(self):
        self._next_char()
        if self._current == '>':
            self._next_char()
            if self._current == '>':
                self._check_augmented_operator( ICNode_SHIFT0R, ICNode_AUG_SHIFT0R, '>>>' )
            else:
                self._check_augmented_operator( ICNode_SHIFTR, ICNode_AUG_SHIFTR, '>>', False )
        elif self._current == '<':
            self._check_augmented_operator( ICNode_OP_GRLE, ICNode_AUG_GRLE, '><' )
        else:
            self._check_augmented_operator( ICNode_GT, ICNode_GE, '>', False )
    #-------------------------------------------------------------------------
    def _less(self):
        self._next_char()
        if self._current == '<':
            self._next_char()
            if self._current == '<':
                self._check_augmented_operator( ICNode_SHIFT0L, ICNode_AUG_SHIFT0L, '<<<' )
            else:
                self._check_augmented_operator( ICNode_SHIFTL, ICNode_AUG_SHIFTL, '<<', False )
        else:
            self._check_augmented_operator( ICNode_LT, ICNode_LE, '<', False )
    #-------------------------------------------------------------------------
    def _minus(self):
        self._next_char()
        if self._current == '-':
            self._next_char()
            self._append_node( ICNode_DECR, '--' )
        elif self._current == '>':
            self._next_char()
            self._append_node( ICNode_ISOF, '->' )
        else:
            self._check_augmented_operator( ICNode_MINUS, ICNode_AUG_MINUS, '-', False )
    #-------------------------------------------------------------------------
    def _mod(self):
        self._check_augmented_operator( ICNode_MOD, ICNode_AUG_MOD, '%' )
    #-------------------------------------------------------------------------
    def _plus(self):
        self._next_char()
        if self._current == '+':
            self._next_char()
            self._append_node( ICNode_INCR, '++' )
        else:
            self._check_augmented_operator( ICNode_PLUS, ICNode_AUG_PLUS, '+', False )
    #-------------------------------------------------------------------------
    def _quest(self):
        self._next_char()
        if self._current == '?':
            self._check_augmented_operator( ICNode_OP_2QUEST, ICNode_AUG_2QUEST, '??' )
        else:
            self._append_node( ICNode_ANY_TYPE, '?' ) 

    #-------------------------------------------------------------------------
    def _star(self):
        self._next_char()
        if self._current == '*':
            self._check_augmented_operator( ICNode_POWER, ICNode_AUG_POWER, '**' )
        else:
            self._check_augmented_operator( ICNode_MUL, ICNode_AUG_MUL, '*', False )
            
            
    #=========================================================================
    #-------------------------------------------------------------------------
    def _append_node(self, node_class, data='None'):
        self.intermediate_code.append( node_class(self, data) )
    #-------------------------------------------------------------------------
    def _check_skip_char(self, checked_car:str, skip:bool=True) -> bool:
        if self._current == checked_car:
            if skip:
                self._skip_chars( 1, True )
            return True
        else:
            return False
    #-------------------------------------------------------------------------
    def _check_chars(self, chars:str) -> bool:
        n = len( chars )
        return  self._get_next( n ) == chars
    #-------------------------------------------------------------------------
    def _check_kw(self, kw:str) -> bool:
        n = len( kw )
        return  self._get_next( n ) == kw  and  self._is_sep( n+1 )
    #-------------------------------------------------------------------------
    def _get_next(self, n:int) -> str:
        end = min( n+self.idx+1, self.len_code )
        return  self.code[ self.idx+1:end ]
    #-------------------------------------------------------------------------
    def _is_sep(self, offset:int) -> bool:
        return self.code[ self.idx + offset ] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
    #-------------------------------------------------------------------------
    def _next_char(self):
        self.idx += 1
        self.num_coln += 1
    #-------------------------------------------------------------------------
    def _next_line(self, append_nl:bool=False):
        self.num_line += 1
        self.num_coln  = 1
        self._next_char()
        if append_nl:
            self._append_node( ICNode_NL, 'new line' )
    #-------------------------------------------------------------------------
    def _skip_chars(self, n:int, skip_space:bool=True):
        self.idx += n
        self.num_coln += n
        if skip_space:
            self._skip_space()
    #-------------------------------------------------------------------------
    def _skip_kw(self, kw:str):
        self._skip_chars( len(kw) )
    #-------------------------------------------------------------------------
    def _skip_space(self):
        while  not self._eof  and  self._current in [ ' ', '\t' ]:
            self.idx += 1
            self.num_coln += 1
    #-------------------------------------------------------------------------
    @property
    def _current(self): return self.code[ self.idx ]
    #-------------------------------------------------------------------------
    @property
    def _eof(self):     return self.idx >= self.len_code


    #=========================================================================
    _ALPHA_CHARS        = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    _NUM_CHARS          = "0123456789"
    _NOT_DEC_CHARS      = "ABCDFGHIJKLMNOPQRSTUVWXYZabcdfghijklmnopqrstuvwxyz"
    _ALPHA_NUM_CHARS    = _ALPHA_CHARS + _NUM_CHARS
    _NAME_ALPHA_CHARS   = _ALPHA_CHARS + '_'
    _NAME_CHARS         = _ALPHA_NUM_CHARS + '_'
    _DOTTED_NAME_CHARS  = _NAME_CHARS + '.'
    _BIN_CHARS          = _NUM_CHARS[:2] + '_'
    _OCTAL_CHARS        = _NUM_CHARS[:8] + '_'
    _HEXA_CHARS         = _NUM_CHARS + "ABCDEFabcdef"
    _SPACE              = " \t"
    _STRING_START       = "'\""
    _ENDLINE            = "\n\r\f"
    _END_OF_FILE        = 0x00
    
    _SIMPLE_TOKEN = {
        '}':    ICNode_BRACECL,
        ']':    ICNode_BRACKETCL,
        '[':    ICNode_BRACKETOP,
        ',':    ICNode_COMMA,
        '#':    ICNode_HASH,
        '(':    ICNode_PAROP,
        ')':    ICNode_PARCL,
        ';':    ICNode_SEMICOLON,
        '~':    ICNode_TILD,
    }
    
    _COMPOUND_TOKEN = {
        '@':    _arobase,
        '&':    _bitand,
        '|':    _bitor,
        '{':    _brace_op,
        '^':    _caret,
        ':':    _colon,
        '.':    _dot,
        '/':    _div,
        '=':    _assign,
        '!':    _excl,
        '>':    _greater,
        '<':    _less,
        '-':    _minus,
        '%':    _mod,
        '+':    _plus,
        '?':    _quest,
        '*':    _star
    }
    
    _KEYWORDS = {
        'abstract':     ICNode_ABSTRACT,
        'all':          ICNode_ALL,
        'and':          ICNode_AND,
        'array':        ICNode_ARRAY,
        'as':           ICNode_AS,
        'assert':       ICNode_ASSERT,
        'bool':         ICNode_SCALAR_TYPE,
        'break':        ICNode_BREAK,
        'case':         ICNode_CASE,
        'cast':         ICNode_CAST,
        'char':         ICNode_SCALAR_TYPE,
        'char16':       ICNode_SCALAR_TYPE,
        'class':        ICNode_CLASS,
        'continue':     ICNode_CONTINUE,
        'const':        ICNode_CONST,
        'del':          ICNode_DEL,
        'elif':         ICNode_ELIF,
        'else':         ICNode_ELSE,
        'elseif':       ICNode_ELIF,
        'elsif':        ICNode_ELIF,
        'embed':        ICNode_EMBED,
        'ensure':       ICNode_ENSURE,
        'enum':         ICNode_ENUM,
        'except':       ICNode_EXCEPT,
        'file':         ICNode_FILE,
        'False':        ICNode_FALSE,
        'false':        ICNode_FALSE,
        'final':        ICNode_FINAL,
        'finally':      ICNode_FINALLY,
        'float32':      ICNode_SCALAR_TYPE,
        'float64':      ICNode_SCALAR_TYPE,
        'for':          ICNode_FOR,
        'forever':      ICNode_FOREVER,
        'from':         ICNode_FROM,
        'hidden':       ICNode_HIDDEN,
        'if':           ICNode_IF,
        'import':       ICNode_IMPORT,
        'in':           ICNode_IN,
        'int8':         ICNode_SCALAR_TYPE,
        'int16':        ICNode_SCALAR_TYPE,
        'int32':        ICNode_SCALAR_TYPE,
        'int64':        ICNode_SCALAR_TYPE,
        'is':           ICNode_IS,
        'lambda':       ICNode_UNNAMED,
        'list':         ICNode_LIST,
        'local':        ICNode_HIDDEN,
        'map':          ICNode_MAP,
        'me':           ICNode_ME,
        'None':         ICNode_NONE,
        'none':         ICNode_NONE,
        'nop':          ICNode_NOP,
        'not':          ICNode_NOT,
        'operator':     ICNode_OPERATOR,
        'or':           ICNode_OR,
        'pass':         ICNode_NOP,
        'private':      ICNode_HIDDEN,
        'protected':    ICNode_PROTECTED,
        'public':       ICNode_PUBLIC,
        'raise':        ICNode_RAISE,
        'repeat':       ICNode_REPEAT,
        'require':      ICNode_REQUIRE,
        'ret':          ICNode_RETURN,
        'return':       ICNode_RETURN,
        'set':          ICNode_SET,
        'static':       ICNode_STATIC,
        'str':          ICNode_SCALAR_TYPE,
        'str16':        ICNode_SCALAR_TYPE,
        'switch':       ICNode_SWITCH,
        'True':         ICNode_TRUE,
        'true':         ICNode_TRUE,
        'try':          ICNode_TRY,
        'type':         ICNode_TYPE_ALIAS,
        'uint8':        ICNode_SCALAR_TYPE,
        'uint16':       ICNode_SCALAR_TYPE,
        'uint32':       ICNode_SCALAR_TYPE,
        'uint64':       ICNode_SCALAR_TYPE,
        'unnamed':      ICNode_UNNAMED,
        'until':        ICNode_UNTIL,
        'volatile':     ICNode_VOLATILE,
        'while':        ICNode_WHILE,
        'with':         ICNode_WITH
    }
    
    _LANGUAGE_KWDS = (
        'cpp', 'java', 'javascript', 'm6809','python', 'py'
    )
    
#=====   end of   FrontEnd.Scanner.fe_scanner   =====#
        