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
from datetime import datetime

from FrontEnd.IntermediateCode.fe_icode_tokens import FEICodeTokens, FEICodeTokensData


#=============================================================================

#-------------------------------------------------------------------------
def generate_baseclass_properties(fp):
    '''
    Generates the "is_XXX" properties in class FEICodeTokenNode.
    
    Args:
        fp: file
            The reference to the generated module file.
    '''
    fp.write('    #-------------------------------------------------------------------------' )
    for tk_nm in sorted( [tk for tk in FEICodeTokens.__dict__ if tk[:3] == 'TK_'] ):
        fp.write( "\n    @property\n    def is_{:s}(self) -> bool:\n        return self.tk_ident == FEICodeTokens.{:s}".format(
            tk_nm[3:], tk_nm) )

#-------------------------------------------------------------------------
def generate_module_footer(fp):
    '''
    Generates the footer of the generated module.
    
    Args:
        fp: file
            The reference to the generated module file.
    '''
    fp.write( "\n#=====   end of   FrontEnd.IntermediateCode.fe_icode_token_node   =====#\n" )

#-------------------------------------------------------------------------
def generate_nodes_classes(fp):
    '''
    Generates the Intermediate Code Nodes classes.
    
    Args:
        fp: file
            The reference to the generated module file.
    '''
    protection_classes = ( 'TK_HIDDEN', 'TK_PROTECTED', 'TK_PUBLIC' )
    
    fp.write( '\n\n\n#=============================================================================' )
    for tk_nm in sorted( [tk for tk in FEICodeTokens.__dict__ if tk[:3] == 'TK_'] ):
        if tk_nm in protection_classes:
            fp.write( """
class ICTokenNode_{:s}( FEICodeTokenNodeProtection ):
    def __init__(self, scanner=None, data='{:s}') -> None:
            super().__init__( scanner, Access.{:s}, FEICodeTokens.{:s}, data )
""".format( tk_nm[3:], str(FEICodeTokensData.get(tk_nm)), tk_nm[3:], tk_nm) )
        else:
            fp.write( "\nclass ICTokenNode_{:s}( FEICodeTokenNode ):\n    def __init__(self, scanner=None, data='{:s}'):\n        super().__init__( scanner, FEICodeTokens.{:s}, data )\n".format(
                tk_nm[3:], str(FEICodeTokensData.get(tk_nm)), tk_nm) )

#-------------------------------------------------------------------------
def generate_protection_class(fp) -> None:
    '''
    Generates the definition of the class of protection-mode nodes.
    
    Args:
        fp: file
            The reference to the generated module file.
    '''
    fp.write("""


#=============================================================================
class FEICodeTokenNodeProtection( FEICodeTokenNode ):
    \"\"\"
    The class of nodes describing protection modes for the Front End 
    Intermediate Code Token Nodes of the Typee Scanner.
    \"\"\"
    #-------------------------------------------------------------------------
    def __init__(self, scanner, protection_mode:Access, tk_id:int, tk_data=None):
        '''
        Creates a node describing protection modes of Intermediate Code 
        Token Nodes for the Front-End Typee Scanner.
        
        Args:
            scanner: FEScanner
                A reference to the calling scanner.
            protection_mode: Access
                An enumerated value corresponding to the protection
                mode.
            tk_id: int
                The token identifier for this node.
            tk_data:
                The data related to this node. Defaults to None.
        '''
        super().__init__( scanner, tk_id, tk_data )
        self.tk_protection = protection_mode""")

#-------------------------------------------------------------------------
def generate_template_header(fp, class_name: str) -> None:
    '''
    Loads template header for class module and puts it in the
    generated module file.

    Args:
        fp: file
            The reference to the generated module file.
        class_name: str
            The name of the class defined within the generated module.

    Raises:
        IOError: template file not found or not accessible.
    '''
    #-----------------------------------------------------------------
    def crc_16( val: int ) -> int:
        return (val // 10) + (val % 10)
    #-----------------------------------------------------------------
    def milli_sec( micro_sec: int ) -> int:
        return (micro_sec + 500) // 1000
    
    #-----------------------------------------------------------------
    header_length = 24  # copy only the 25 first lines of template
    with open( 'template_class.py', 'r' ) as tfp:
        fp.writelines( tfp.readlines()[:header_length] )

    my_today = datetime.today()
    my_now   = datetime.now()
    simple_crc_code = crc_16( my_today.year // 100 ) + crc_16( my_today.year % 100 ) +              \
                        crc_16( my_today.month ) + crc_16( my_today.day ) +                         \
                        crc_16( my_now.hour ) + crc_16( my_now.minute ) + crc_16( my_now.second ) + \
                        crc_16( milli_sec(my_now.microsecond) )
    simple_crc_code = chr( ord('A') + (simple_crc_code % 26) )
    
    fp.write(
f"""## THIS FILE HAS BEEN AUTOMATICALLY GENERATED BY Typee FRAMEWORK.
## DO NOT MODIFY IT: ANY MODIFICATION WOULD BE LOST ON NEXT SCRIPTED GENERATION.
## Last modification version: {my_today.year:04d}{my_today.month:02d}-{my_today.day:02d}{my_now.hour:02d}{my_now.minute:02d}-{my_now.second:02d}{(my_now.microsecond+500)//1000:03d}{simple_crc_code}


#=============================================================================
from Commons.access                             import Access
from FrontEnd.IntermediateCode.fe_icode_tokens  import FEICodeTokens


#=============================================================================
class {class_name}:
    \"""
    The class of nodes for the Front End Intermediate Code of the Typee Scanner.
    \"""    
    #-------------------------------------------------------------------------
    def __init__(self, scanner, tk_id:int, tk_data=None) -> None:
        '''
        Creates a node of Intermediate Code for the Front-End Typee Scanner.
        
        Args:
            tk_id: int
                The token identifier for this node.
            tk_data:
                The data related to this node. Defaults to None.
            scanner: FEScanner
                A reference to the calling scanner.
        '''
        self.num_line = scanner.num_line if scanner else 0
        self.num_coln = scanner.num_coln if scanner else 0
        self.tk_data  = tk_data
        self.tk_ident = tk_id

    #-------------------------------------------------------------------------
    def __eq__(self, other):
        return self.tk_ident == other.tk_ident  and  self.tk_data == other.tk_data
""" ##.format( my_today.year, my_today.month, my_today.day,
    ##        my_now.hour, my_now.minute, my_now.second, (my_now.microsecond+500)//1000,
    ##        simple_crc_code,
    ##        class_name )
    )


#=============================================================================
if __name__ == '__main__':
    """
    Automated generation of module FeontEnd.fe_icode_node.py.
    """
    #-------------------------------------------------------------------------
    with open( "../FrontEnd/IntermediateCode/fe_icode_token_node.py", 'w' ) as fp:
        generate_template_header( fp, 'FEICodeTokenNode')
        generate_baseclass_properties( fp )
        generate_protection_class( fp )
        generate_nodes_classes( fp )
        generate_module_footer( fp )
   
    print( '-- done!' )

#=====   end of   local_tools.tool_generate_feicode_token_node_module   =====#
        