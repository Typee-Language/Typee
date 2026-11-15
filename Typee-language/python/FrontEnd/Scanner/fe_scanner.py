# -*- coding: utf-8 -*-
"""
Copyright (c) 2018-2021 Philippe Schmouker, Typee project, http://www.typee.ovh

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
from FrontEnd.IntermediateCode.fe_icode_token_node   import *  ## to get direct access to all ICTokenNode_XXX classes
from FrontEnd.IntermediateCode.fe_tokenized_icode    import FETokenizedICode


#=============================================================================
class FEScanner:
    """
    This is the class of the Typee Front-End Scanner.
    It is the very first stage of the front-end  pipeline of  the  Typee
    translator.
    It scans Typee source code and produces tokenized Intermediate  Code
    that will be parsed by the Typee Front-End Parser.
    """
    
    #-------------------------------------------------------------------------
    def __init__(self) -> None:
        '''
        Constructor.
        '''
        self.intermediate_code = FETokenizedICode()
        self.num_line = 1
        self.num_coln = 1
        

    #-------------------------------------------------------------------------
    def scan_file(self, filepath: str, **parse_args) -> FETokenizedICode:
        '''
        Runs the Typee scanner on a specified file.
        
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
    def scan_memory(self, src_code: str, **parse_args) -> FETokenizedICode:
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
        self._append_node( ICTokenNode_EOF )
        
        return  self.intermediate_code


    #=========================================================================
    #-------------------------------------------------------------------------
    def _tokenize(self) -> None:
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
            self._append_node( ICTokenNode_UNEXPECTED, self._current )
            self._next_char()


    #=========================================================================
    #-------------------------------------------------------------------------
    def _binary_number(self) -> None:
        self._parse_number( self._BIN_CHARS, True )
    #-------------------------------------------------------------------------
    def _check_augmented_operator(self, base_class, 
                                        augmented_class, 
                                        data, 
                                        get_next: bool = True) -> None:
        if get_next:
            self._next_char()
        if self._current == '=':
            self._next_char()
            self._append_node( augmented_class, data+'=' )
        else:
            if base_class is ICTokenNode_UNEXPECTED:
                self._append_node( base_class, self._current )
            else:
                self._append_node( base_class, data )
    #-------------------------------------------------------------------------
    def _check_escaped_char(self, count: int, base_chars: str) -> None:
        self._next_char()
        for _ in range(count):
            if self._eof:
                self._append_node( ICTokenNode_UNEXPECTED, 'end of file' )
                break
            elif self._current in FEScanner._ENDLINE:
                self._append_node( ICTokenNode_UNEXPECTED, 'end of line' )
                break
            elif self._current not in base_chars:
                self._append_node( ICTokenNode_UNEXPECTED, self._current )
            self._next_char()
    #-------------------------------------------------------------------------
    def _comment(self) -> None:
        start = self.idx + 1
        while not self._eof  and  self._current not in self._ENDLINE:
            self._next_char()
        self._append_node( ICTokenNode_COMMENT, self.code[start:self.idx] )
        if not self._eof:
            self._next_line( True )
    #-------------------------------------------------------------------------
    def _decimal_number(self) -> None:
        start = self.idx
        if self._decimal_part():
            self._error = False
            fract_part = self._fraction_part()
            expon_part = self._exponent_part()
            if not self._error:
                self._append_node( ICTokenNode_FLOAT if fract_part or expon_part else ICTokenNode_INTEGER,
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
                    self._append_node( ICTokenNode_UNEXPECTED, self.code[start:self.idx] )
                    return False
            else:
                self._next_char()
        if self._current in self._NOT_DEC_CHARS:
            start = self.idx
            while self._current in self._NOT_DEC_CHARS:
                self._next_char()
            self._append_node( ICTokenNode_UNEXPECTED, self.code[start:self.idx] )
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
                self._append_node( ICTokenNode_ELLIPSIS, '...' )
                return True
            else:
                self._append_node( ICTokenNode_UNEXPECTED, self._current )
                self._next_char()
                return False
        else:
            self._append_node( ICTokenNode_DOT, '.' )
            return True
    #-------------------------------------------------------------------------
    def _embedded_code(self) -> None:
        start = self.idx
        while not self._eof:
            if self._current == '}':
                self._next_char()
                if self._current == '}':
                    self._append_node( ICTokenNode_EMBED_CODE, self.code[start:self.idx-1] )
                    self._next_char()
                    break
            self._next_char()
    #-------------------------------------------------------------------------
    def _escaped_char(self) -> None:
        self._next_char()
        if self._current in FEScanner._ALPHA_CHARS:
            self._next_char()
        elif self._current == '0':
            self._next_char()
            if self._current in "xX":
                self._check_escaped_char( 2, FEScanner._HEXA_CHARS )
                if self._current in FEScanner._HEXA_CHARS:
                    self._check_escaped_char( 2, FEScanner._HEXA_CHARS )
            elif self._current == '0':
                self._check_escaped_char( 3, FEScanner._OCTAL_CHARS )
            else:
                self._append_node( ICTokenNode_UNEXPECTED, self._current )
        else:
            self._append_node( ICTokenNode_UNEXPECTED, self._current )
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
    def _hexadecimal_number(self) -> None:
        self._parse_number( self._HEXA_CHARS, True )
    #-------------------------------------------------------------------------
    def _multi_lines_comment(self) -> None:
        start = self.idx + 1
        while True:
            if self._current in self._ENDLINE:
                self._next_line()
                ##self._next_char()
            elif self._current == '*':
                self._next_char()
                if self._current == '/':
                    self._next_char()
                    self._append_node( ICTokenNode_COMMENT_ML, self.code[start:self.idx-2] )
                    break
            elif self._eof:
                self._append_node( ICTokenNode_COMMENT_ML, self.code[start:] )
                self._append_node( ICTokenNode_UNEXPECTED, 'end of file' )
                break
            else:
                self._next_char()
    #-------------------------------------------------------------------------
    def _name(self) -> None:
        start = self.idx
        while self._current in FEScanner._NAME_CHARS:
            self._next_char()
        name = self.code[start:self.idx]
        if name in FEScanner._KEYWORDS:
            kw_type = FEScanner._KEYWORDS[name]
            self._append_node( kw_type, name )
        elif name in FEScanner._LANGUAGE_KWDS:
            self._append_node( ICTokenNode_LANGUAGE, name )
        else:
            self._append_node( ICTokenNode_IDENT, name )
    #-------------------------------------------------------------------------
    def _number(self) -> None:
        if self._current == '0':
            self._octal_hexa_binary_number()
        else:
            self._decimal_number()
    #-------------------------------------------------------------------------
    def _octal_hexa_binary_number(self) -> None:
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
            self._append_node( ICTokenNode_INTEGER, '0' )
    #-------------------------------------------------------------------------
    def _octal_number(self) -> None:
        self._parse_number( self._OCTAL_CHARS )
    #-------------------------------------------------------------------------
    def _parse_number(self, num_chars, spec_char: bool = False) -> bool:
        if self._current in num_chars:
            self._next_char()
            start = self.idx - (3 if spec_char else 2)
            if self._parse_subnumber( num_chars ):
                self._append_node( ICTokenNode_INTEGER, self.code[start : self.idx] )
                return True
            else:
                return False
        else:
            self._append_node( ICTokenNode_UNEXPECTED, self._current )
            return False
    #-------------------------------------------------------------------------
    def _parse_subnumber(self, num_chars ) -> bool:
        while self._current in num_chars + '_':
            if self._current == '_':
                self._next_char()
                if self._current in num_chars:
                    self._next_char()
                else:
                    self._append_node( ICTokenNode_UNEXPECTED, self._current )
                    while self._current in self._NAME_CHARS:
                        self._next_char()          
                    return False
            else:
                self._next_char()
        if self._current in self._NAME_CHARS:
            while self._current in self._NAME_CHARS:
                self._append_node( ICTokenNode_UNEXPECTED, self._current )
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
    def _string_content(self, string_marker: str) -> bool:
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
        self._append_node( ICTokenNode_STRING, self.code[start:self.idx] )
        if error:
            self._append_node( ICTokenNode_UNEXPECTED, 'end of '+error )
        return True
    #-------------------------------------------------------------------------
    def _string_double_quote(self) -> bool:
        return self._string_content( '"' )
    #-------------------------------------------------------------------------
    def _string_quote(self) -> bool:
        return self._string_content( "'" )
    
    
    #=========================================================================
    #-------------------------------------------------------------------------
    def _arobase(self) -> None:
        self._next_char()
        if self._current == '@':
            self._check_augmented_operator( ICTokenNode_OP_2AROB, ICTokenNode_AUG_2AROB, '@@' )
        else:
            self._check_augmented_operator( ICTokenNode_AROBASE, ICTokenNode_AUG_AROBASE, '@', False )
    #-------------------------------------------------------------------------
    def _assign(self) -> None:
        self._check_augmented_operator( ICTokenNode_ASSIGN, ICTokenNode_EQ, '=' )
    #-------------------------------------------------------------------------
    def _bitand(self) -> None:
        self._check_augmented_operator( ICTokenNode_BITAND, ICTokenNode_AUG_BITAND, '&' )
    #-------------------------------------------------------------------------
    def _bitor(self) -> None:
        self._check_augmented_operator( ICTokenNode_BITOR, ICTokenNode_AUG_BITOR, '|' )
    #-------------------------------------------------------------------------
    def _brace_op(self) -> None:
        self._next_char()
        if self._current == '{':
            self._next_char()
            self._embedded_code()
        else:
            self._append_node( ICTokenNode_BRACEOP, '{' )
    #-------------------------------------------------------------------------
    def _caret(self) -> None:
        self._next_char()
        if self._current == '^':
            self._check_augmented_operator( ICTokenNode_POWER, ICTokenNode_AUG_POWER, '^^' )
        else:
            self._check_augmented_operator( ICTokenNode_BITXOR, ICTokenNode_AUG_BITXOR, '^', False )
    #-------------------------------------------------------------------------
    def _colon(self) -> None:
        self._next_char()
        if self._current == ':':
            self._check_augmented_operator( ICTokenNode_OP_2COLN, ICTokenNode_AUG_2COLN, '::' )
        else:
            self._check_augmented_operator( ICTokenNode_COLON, ICTokenNode_AUG_COLN, ':', False )
    #-------------------------------------------------------------------------
    def _div(self) -> None:
        self._next_char()
        if self._current == '/':
            self._comment()
        elif self._current == '*':
            self._multi_lines_comment()
        else:
            self._check_augmented_operator( ICTokenNode_DIV, ICTokenNode_AUG_DIV, '/', False )
    #-------------------------------------------------------------------------
    def _eq(self) -> None:
        self._check_augmented_operator( ICTokenNode_ASSIGN, ICTokenNode_EQ, '==' )
    #-------------------------------------------------------------------------
    def _excl(self) -> None:
        self._next_char()
        if self._current == '!':
            self._check_augmented_operator( ICTokenNode_OP_2EXCL, ICTokenNode_AUG_2EXCL, '!!' )
        else:
            self._check_augmented_operator( ICTokenNode_EXCL, ICTokenNode_NE, '!', False )
    #-------------------------------------------------------------------------
    def _greater(self) -> None:
        self._next_char()
        if self._current == '>':
            self._next_char()
            if self._current == '>':
                self._check_augmented_operator( ICTokenNode_SHIFT0R, ICTokenNode_AUG_SHIFT0R, '>>>' )
            else:
                self._check_augmented_operator( ICTokenNode_SHIFTR, ICTokenNode_AUG_SHIFTR, '>>', False )
        elif self._current == '<':
            self._check_augmented_operator( ICTokenNode_OP_GRLE, ICTokenNode_AUG_GRLE, '><' )
        else:
            self._check_augmented_operator( ICTokenNode_GT, ICTokenNode_GE, '>', False )
    #-------------------------------------------------------------------------
    def _less(self) -> None:
        self._next_char()
        if self._current == '<':
            self._next_char()
            if self._current == '<':
                self._check_augmented_operator( ICTokenNode_SHIFT0L, ICTokenNode_AUG_SHIFT0L, '<<<' )
            else:
                self._check_augmented_operator( ICTokenNode_SHIFTL, ICTokenNode_AUG_SHIFTL, '<<', False )
        elif self._current == '=':
            self._next_char()
            if self._current == '>':
                self._next_char()
                self._append_node( ICTokenNode_LEG, '<=>' )
            else:
                self._append_node( ICTokenNode_LE, '<=' )
        elif self._current == '>':
            self._check_augmented_operator( ICTokenNode_OP_LEGR, ICTokenNode_AUG_LEGR, '<>' )
        else:
            self._append_node( ICTokenNode_LT, '<' )
    #-------------------------------------------------------------------------
    def _minus(self) -> None:
        self._next_char()
        if self._current == '-':
            self._next_char()
            self._append_node( ICTokenNode_DECR, '--' )
        elif self._current == '>':
            self._next_char()
            self._append_node( ICTokenNode_ISOF, '->' )
        else:
            self._check_augmented_operator( ICTokenNode_MINUS, ICTokenNode_AUG_MINUS, '-', False )
    #-------------------------------------------------------------------------
    def _mod(self) -> None:
        self._check_augmented_operator( ICTokenNode_MOD, ICTokenNode_AUG_MOD, '%' )
    #-------------------------------------------------------------------------
    def _plus(self) -> None:
        self._next_char()
        if self._current == '+':
            self._next_char()
            self._append_node( ICTokenNode_INCR, '++' )
        else:
            self._check_augmented_operator( ICTokenNode_PLUS, ICTokenNode_AUG_PLUS, '+', False )
    #-------------------------------------------------------------------------
    def _quest(self) -> None:
        self._next_char()
        if self._current == '?':
            self._check_augmented_operator( ICTokenNode_OP_2QUEST, ICTokenNode_AUG_2QUEST, '??' )
        else:
            self._append_node( ICTokenNode_ANY_TYPE, '?' ) 

    #-------------------------------------------------------------------------
    def _star(self) -> None:
        self._next_char()
        if self._current == '*':
            self._check_augmented_operator( ICTokenNode_POWER, ICTokenNode_AUG_POWER, '**' )
        else:
            self._check_augmented_operator( ICTokenNode_MUL, ICTokenNode_AUG_MUL, '*', False )
            
            
    #=========================================================================
    #-------------------------------------------------------------------------
    def _append_node(self, node_class, data='None') -> None:
        self.intermediate_code.append( node_class(self, data) )
    #-------------------------------------------------------------------------
    def _check_skip_char(self, checked_car: str, skip: bool = True) -> bool:
        if self._current == checked_car:
            if skip:
                self._skip_chars( 1, True )
            return True
        else:
            return False
    #-------------------------------------------------------------------------
    def _check_chars(self, chars: str) -> bool:
        n = len( chars )
        return  self._get_next( n ) == chars
    #-------------------------------------------------------------------------
    def _check_kw(self, kw: str) -> bool:
        n = len( kw )
        return  self._get_next( n ) == kw  and  self._is_sep( n+1 )
    #-------------------------------------------------------------------------
    def _get_next(self, n: int) -> str:
        end = min( n+self.idx+1, self.len_code )
        return  self.code[ self.idx+1:end ]
    #-------------------------------------------------------------------------
    def _is_sep(self, offset: int) -> bool:
        return self.code[ self.idx + offset ] not in FEScanner._NAME_CHARS
    #-------------------------------------------------------------------------
    def _next_char(self) -> None:
        self.idx += 1
        self.num_coln += 1
    #-------------------------------------------------------------------------
    def _next_line(self, append_nl: bool = False) -> None:
        self.num_line += 1
        self.num_coln  = 1
        self._next_char()
        if append_nl:
            self._append_node( ICTokenNode_NL, 'new line' )
    #-------------------------------------------------------------------------
    def _skip_chars(self, n: int, skip_space: bool = True) -> None:
        self.idx += n
        self.num_coln += n
        if skip_space:
            self._skip_space()
    #-------------------------------------------------------------------------
    def _skip_kw(self, kw: str) -> None:
        self._skip_chars( len(kw) )
    #-------------------------------------------------------------------------
    def _skip_space(self) -> None:
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
    _BIN_CHARS          = _NUM_CHARS[:2]  ## + '_'
    _OCTAL_CHARS        = _NUM_CHARS[:8]  ## + '_'
    _HEXA_CHARS         = _NUM_CHARS + "ABCDEFabcdef"
    _SPACE              = " \t"
    _STRING_START       = "'\""
    _ENDLINE            = "\n\r\f"
    _END_OF_FILE        = 0x00
    
    _SIMPLE_TOKEN = {
        '}':    ICTokenNode_BRACECL,
        ']':    ICTokenNode_BRACKETCL,
        '[':    ICTokenNode_BRACKETOP,
        ',':    ICTokenNode_COMMA,
        '#':    ICTokenNode_HASH,
        '(':    ICTokenNode_PAROP,
        ')':    ICTokenNode_PARCL,
        ';':    ICTokenNode_SEMICOLON,
        '~':    ICTokenNode_TILD,
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
        '_float_':      ICTokenNode_GENERIC_TYPE,
        '_int_':        ICTokenNode_GENERIC_TYPE,
        '_numeric_':    ICTokenNode_GENERIC_TYPE,
        '_uint_':       ICTokenNode_GENERIC_TYPE,
        'abstract':     ICTokenNode_ABSTRACT,
        'all':          ICTokenNode_ALL,
        'and':          ICTokenNode_AND,
        'array':        ICTokenNode_ARRAY,
        'as':           ICTokenNode_AS,
        'assert':       ICTokenNode_ASSERT,
        'bool':         ICTokenNode_SCALAR_TYPE,
        'break':        ICTokenNode_BREAK,
        'but':          ICTokenNode_BUT,
        'case':         ICTokenNode_CASE,
        'cast':         ICTokenNode_CAST,
        'char':         ICTokenNode_SCALAR_TYPE,
        'char16':       ICTokenNode_SCALAR_TYPE,
        'class':        ICTokenNode_CLASS,
        'continue':     ICTokenNode_CONTINUE,
        'const':        ICTokenNode_CONST,
        'del':          ICTokenNode_DEL,
        'elif':         ICTokenNode_ELIF,
        'else':         ICTokenNode_ELSE,
        'elseif':       ICTokenNode_ELIF,
        'elsif':        ICTokenNode_ELIF,
        'embed':        ICTokenNode_EMBED,
        'ensure':       ICTokenNode_ENSURE,
        'enum':         ICTokenNode_ENUM,
        'except':       ICTokenNode_EXCEPT,
        'exclude':      ICTokenNode_EXCLUDE,
        'exit':         ICTokenNode_EXIT,
        'file':         ICTokenNode_FILE,
        'False':        ICTokenNode_FALSE,
        'false':        ICTokenNode_FALSE,
        'final':        ICTokenNode_FINAL,
        'finally':      ICTokenNode_FINALLY,
        'float32':      ICTokenNode_SCALAR_TYPE,
        'float64':      ICTokenNode_SCALAR_TYPE,
        'for':          ICTokenNode_FOR,
        'forever':      ICTokenNode_FOREVER,
        'forward':      ICTokenNode_FORWARD,
        'from':         ICTokenNode_FROM,
        'fwd':          ICTokenNode_FORWARD,
        'hidden':       ICTokenNode_HIDDEN,
        'if':           ICTokenNode_IF,
        'import':       ICTokenNode_IMPORT,
        'in':           ICTokenNode_IN,
        'int8':         ICTokenNode_SCALAR_TYPE,
        'int16':        ICTokenNode_SCALAR_TYPE,
        'int32':        ICTokenNode_SCALAR_TYPE,
        'int64':        ICTokenNode_SCALAR_TYPE,
        'is':           ICTokenNode_IS,
        'lambda':       ICTokenNode_UNNAMED,
        'list':         ICTokenNode_LIST,
        'local':        ICTokenNode_HIDDEN,
        'map':          ICTokenNode_MAP,
        'me':           ICTokenNode_ME,
        'None':         ICTokenNode_NONE,
        'none':         ICTokenNode_NONE,
        'nop':          ICTokenNode_NOP,
        'not':          ICTokenNode_NOT,
        'operator':     ICTokenNode_OPERATOR,
        'or':           ICTokenNode_OR,
        'otherwise':    ICTokenNode_OTHERWISE,
        'pass':         ICTokenNode_NOP,
        'post':         ICTokenNode_POST,
        'pre':          ICTokenNode_PRE,
        'private':      ICTokenNode_HIDDEN,
        'protected':    ICTokenNode_PROTECTED,
        'public':       ICTokenNode_PUBLIC,
        'raise':        ICTokenNode_RAISE,
        'repeat':       ICTokenNode_REPEAT,
        'require':      ICTokenNode_REQUIRE,
        'ret':          ICTokenNode_RETURN,
        'return':       ICTokenNode_RETURN,
        'set':          ICTokenNode_SET,
        'slice':        ICTokenNode_SCALAR_TYPE,
        'static':       ICTokenNode_STATIC,
        'str':          ICTokenNode_SCALAR_TYPE,
        'str16':        ICTokenNode_SCALAR_TYPE,
        'switch':       ICTokenNode_SWITCH,
        'True':         ICTokenNode_TRUE,
        'true':         ICTokenNode_TRUE,
        'try':          ICTokenNode_TRY,
        'type':         ICTokenNode_TYPE_ALIAS,
        'uint8':        ICTokenNode_SCALAR_TYPE,
        'uint16':       ICTokenNode_SCALAR_TYPE,
        'uint32':       ICTokenNode_SCALAR_TYPE,
        'uint64':       ICTokenNode_SCALAR_TYPE,
        'unnamed':      ICTokenNode_UNNAMED,
        'until':        ICTokenNode_UNTIL,
        'volatile':     ICTokenNode_VOLATILE,
        'while':        ICTokenNode_WHILE,
        'with':         ICTokenNode_WITH
    }
    
    _LANGUAGE_KWDS = (
        'cpp', 'ccs', 'csharp', 'java', 'javascript', 'm6809', 'py', 'python'
    )
    
#=====   end of   FrontEnd.Scanner.fe_scanner   =====#
        