#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2018-2019 Philippe Schmouker, Typee project, http://www.typee.ovh

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
# no import.


#=============================================================================
class FEICodeTokens:
    """
    The list of tokens for the Typee Front-End Intermediate Code.
    
    These are defined in a class just to use the class as a namespace.
    If  new tokens have to be added,  please append them by the end of
    current list.
    
    Identifiers associated with tokens are said to be 0 but  they  all 
    are set with different values in an automated manner at the end of 
    this module.
    """    
    TK_PLUS         = 0
    TK_MINUS        = 0
    TK_MUL          = 0
    TK_DIV          = 0
    TK_MOD          = 0
    TK_POWER        = 0
    TK_TILD         = 0
    TK_EXCL         = 0

    TK_BITAND       = 0
    TK_BITOR        = 0
    TK_BITXOR       = 0
    TK_SHIFTL       = 0
    TK_SHIFTR       = 0
    TK_SHIFT0L      = 0
    TK_SHIFT0R      = 0
    
    TK_INCR         = 0
    TK_DECR         = 0
    TK_POST         = 0
    TK_PRE          = 0
    
    TK_OP_GRLE      = 0
    TK_OP_2EXCL     = 0
    TK_OP_2COLN     = 0
    TK_OP_2QUEST    = 0
    
    TK_AUG_PLUS     = 0
    TK_AUG_MINUS    = 0
    TK_AUG_MUL      = 0
    TK_AUG_DIV      = 0
    TK_AUG_MOD      = 0
    TK_AUG_POWER    = 0

    TK_AUG_BITAND   = 0
    TK_AUG_BITOR    = 0
    TK_AUG_BITXOR   = 0
    TK_AUG_SHIFTL   = 0
    TK_AUG_SHIFTR   = 0
    TK_AUG_SHIFT0L  = 0
    TK_AUG_SHIFT0R  = 0
    
    TK_AUG_AROBASE  = 0
    
    TK_AUG_GRLE     = 0
    TK_AUG_2EXCL    = 0
    TK_AUG_2COLN    = 0
    TK_AUG_2QUEST   = 0

    TK_GT           = 0
    TK_GE           = 0
    TK_EQ           = 0
    TK_NE           = 0
    TK_LT           = 0
    TK_LE           = 0
    TK_LEG          = 0

    TK_OR           = 0
    TK_AND          = 0

    TK_PAROP        = 0
    TK_PARCL        = 0
    TK_BRACEOP      = 0
    TK_BRACECL      = 0
    TK_BRACKETOP    = 0
    TK_BRACKETCL    = 0
        
    TK_DOT          = 0
    TK_COMMA        = 0
    TK_COLON        = 0
    TK_SEMICOLON    = 0
    TK_ELLIPSIS     = 0
    
    TK_IDENT        = 0
    
    TK_INTEGER      = 0
    TK_FLOAT        = 0
    TK_STRING       = 0
    TK_ANY_TYPE     = 0
    TK_SCALAR_TYPE  = 0
    
    TK_TRUE         = 0
    TK_FALSE        = 0
    
    TK_NONE         = 0
    
    TK_NOT          = 0
    TK_IN           = 0
    TK_IS           = 0
    TK_ISOF         = 0
    
    TK_ASSIGN       = 0
    
    TK_HASH         = 0
    TK_AROBASE      = 0
    
    TK_COMMENT      = 0
    TK_COMMENT_ML   = 0
    
    TK_PUBLIC       = 0
    TK_PROTECTED    = 0
    TK_HIDDEN       = 0
    
    TK_ABSTRACT     = 0
    TK_CONST        = 0
    TK_FINAL        = 0
    TK_VOLATILE     = 0
    TK_STATIC       = 0
    TK_FORWARD      = 0
    
    TK_ARRAY        = 0
    TK_LIST         = 0
    TK_MAP          = 0
    TK_SET          = 0
    TK_FILE         = 0
    
    TK_ENUM         = 0
    TK_OPERATOR     = 0
    
    TK_EMBED        = 0
    TK_EMBED_CODE   = 0
    TK_LANGUAGE     = 0
    
    TK_TYPE_ALIAS   = 0
    TK_CAST         = 0
    
    TK_UNNAMED      = 0

    TK_ASSERT       = 0
    TK_REQUIRE      = 0
    TK_ENSURE       = 0
    TK_RAISE        = 0
    
    TK_FOR          = 0
    TK_FOREVER      = 0
    TK_WHILE        = 0
    TK_REPEAT       = 0
    TK_UNTIL        = 0
    TK_OTHERWISE    = 0
    TK_IF           = 0
    TK_ELIF         = 0
    TK_ELSE         = 0
    TK_SWITCH       = 0
    TK_CASE         = 0
    TK_BREAK        = 0
    TK_CONTINUE     = 0
    TK_TRY          = 0
    TK_EXCEPT       = 0
    TK_FINALLY      = 0
    TK_WITH         = 0
    TK_RETURN       = 0
    
    TK_CLASS        = 0
    TK_ME           = 0
    TK_DEL          = 0
    
    TK_IMPORT       = 0
    TK_FROM         = 0
    TK_ALL          = 0
    TK_AS           = 0
    TK_BUT          = 0
    
    TK_EXCLUDE      = 0
    TK_EXIT         = 0
    
    TK_NOP          = 0
    
    TK_NL           = 0
    TK_EOF          = 0
    
    TK_UNEXPECTED   = 0
    
    ##--- Add new tokens JUST BEFORE this line ---##
    
    #---------------------------------------------------------------------
    _TOKEN_NAMES = dict()
    
    @classmethod
    def token_name(cls, tk_id:int) -> str:
        try:
            return cls._TOKEN_NAMES[ tk_id ]
        except:
            return 'undefined token ({})'.format( tk_id )


#-------------------------------------------------------------------------
# Automated numbering of tokens
_OFFSET = 1000  ## 1000 here is an arbitrary default value - not to be changed right now...
for tk_id, tk_nm in enumerate( [ tk for tk in FEICodeTokens.__dict__ if tk[:3] == 'TK_' ] ):
    setattr( FEICodeTokens, tk_nm, tk_id + _OFFSET )
    FEICodeTokens._TOKEN_NAMES[ tk_id + _OFFSET ] = tk_nm


#=============================================================================
class FEICodeTokensData:
    """
    Data as associated with tokens for the Typee Front-End Intermediate Code.
    """
    _data = {
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_PLUS ]        : '+',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_MINUS ]       : '-',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_MUL ]         : '*',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_DIV ]         : '/',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_MOD ]         : '%',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_POWER ]       : '^^',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_TILD ]        : '~',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_EXCL ]        : '!',
    
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_BITAND ]      : '&',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_BITOR ]       : '|',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_BITXOR ]      : '^',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_SHIFTL ]      : '<<',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_SHIFTR ]      : '>>',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_SHIFT0L ]     : '<<<',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_SHIFT0R ]     : '>>>',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_INCR ]        : '++',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_DECR ]        : '--',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_POST ]        : 'post',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_PRE ]         : 'pre',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_OP_GRLE ]     : '><',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_OP_2EXCL ]    : '!!',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_OP_2COLN ]    : '::',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_OP_2QUEST ]   : '??',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_PLUS ]    : '+=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_MINUS ]   : '-=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_MUL ]     : '*=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_DIV ]     : '/=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_MOD ]     : '%=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_POWER ]   : '^^=',
    
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_BITAND ]  : '&=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_BITOR ]   : '|=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_BITXOR ]  : '^=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_SHIFTL ]  : '<<=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_SHIFTR ]  : '>>=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_SHIFT0L ] : '<<<=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_SHIFT0R ] : '>>>=',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_AROBASE ] : '@=',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_GRLE ]    : '><=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_2EXCL ]   : '!!=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_2COLN ]   : '::=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AUG_2QUEST ]  : '??=',
    
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_GT ]          : '>',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_GE ]          : '>=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_EQ ]          : '==',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_NE ]          : '!=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_LT ]          : '<',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_LE ]          : '<=',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_LEG ]         : '<=>',
    
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_OR ]          : 'or',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AND ]         : 'and',
    
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_PAROP ]       : '(',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_PARCL ]       : ')',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_BRACEOP ]     : '{',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_BRACECL ]     : '}',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_BRACKETOP ]   : '[',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_BRACKETCL ]   : ']',
            
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_DOT ]         : '.',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_COMMA ]       : ',',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_COLON ]       : ':',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_SEMICOLON ]   : ';',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ELLIPSIS ]    : '...',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_IDENT ]       : None,
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_INTEGER ]     : None,
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_FLOAT ]       : None,
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_STRING ]      : None,
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ANY_TYPE ]    : '?',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_SCALAR_TYPE ] : None,
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_TRUE ]        : 'true',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_FALSE ]       : 'false',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_NONE ]        : 'none',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_NOT ]         : 'not',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_IN ]          : 'in',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_IS ]          : 'is',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ISOF ]        : '->',
        
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ASSIGN ]      : '=',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_HASH ]        : '#',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AROBASE ]     : '@',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_COMMENT ]     : None,
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_COMMENT_ML ]  : None,
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_PUBLIC ]      : 'public',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_PROTECTED ]   : 'protected',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_HIDDEN ]      : 'hidden',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ABSTRACT ]    : 'abstract',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_CONST ]       : 'const',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_FINAL ]       : 'final',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_VOLATILE ]    : 'volatile',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_STATIC ]      : 'static',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_FORWARD ]     : 'forward',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ARRAY ]       : 'array',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_LIST ]        : 'list',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_MAP ]         : 'map',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_SET ]         : 'set',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_FILE ]        : 'file',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ENUM ]        : 'enum',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_OPERATOR ]    : 'operator',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_EMBED ]       : 'embed',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_EMBED_CODE ]  : None,
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_LANGUAGE ]    : 'language',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_TYPE_ALIAS ]  : 'type',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_CAST ]        : 'cast',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_UNNAMED ]     : 'unnamed',
    
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ASSERT ]      : 'assert',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_REQUIRE ]     : 'require',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ENSURE ]      : 'ensure',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_RAISE ]       : 'raise',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_FOR ]         : 'for',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_FOREVER ]     : 'forever',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_WHILE ]       : 'while',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_REPEAT ]      : 'repeat',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_UNTIL ]       : 'until',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_OTHERWISE ]   : 'otherwise',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_IF ]          : 'if',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ELIF ]        : 'elif',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ELSE ]        : 'else',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_SWITCH ]      : 'switch',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_CASE ]        : 'case',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_BREAK ]       : 'break',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_CONTINUE ]    : 'continue',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_TRY ]         : 'try',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_EXCEPT ]      : 'except',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_FINALLY ]     : 'finally',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_WITH ]        : 'with',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_RETURN ]      : 'return',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_CLASS ]       : 'class',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ME ]          : 'me',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_DEL ]         : 'del',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_IMPORT ]      : 'import',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_FROM ]        : 'from',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_ALL ]         : 'all',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_AS ]          : 'as',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_BUT ]         : 'but',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_EXCLUDE ]     : 'exclude',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_EXIT ]        : 'exit',

        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_NOP ]         : 'nop',
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_NL ]          : 'new line',
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_EOF ]         : None,
        
        FEICodeTokens._TOKEN_NAMES[ FEICodeTokens.TK_UNEXPECTED ]  : None
    }

    #---------------------------------------------------------------------
    @classmethod
    def get(cls, tk_id:int) -> str:
        try:
            return cls._data[ tk_id ]
        except:
            return "Typee translator internal error: unknown token value {:d}".format( tk_id )

#=====   end of   FrontEnd.fe_icode_tokens   =====#
        