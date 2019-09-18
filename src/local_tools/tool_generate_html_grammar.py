"""
Copyright (c) 2019 Philippe Schmouker, Typee project, http://www.typee.ovh

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
#-------------------------------------------------------------------------
def translate( grm_path: str, html_path: str) -> None:
    '''
    Translates .grm file into its HTML equivalence.
    
    Args:
        grm_path: str
            The path to the EBFN .grm source.
        html_path: str
            The path to the HTML destination file.
    '''
    with open( grm_path, 'r') as fsrc:
        content = fsrc.read()
    
    with open( html_path, 'w' ) as fdst:
        fdst.write( content.replace('<', '&lt;').replace('>', '&gt;').replace(" '", " '<b>").replace("' ", "</b>' ") )


#=============================================================================
if __name__ == '__main__':
    """
    Script for the translation of EBNF.grm files into their HTML equivalence.
    """
    #-------------------------------------------------------------------------
    translate( '../../Language-specifications/typee_specs_LL1-v10-EBNF.grm',
               './tmp_data/typee_specs_LL1-v10-EBNF.html' )

    print( '-- done!' )

#=====   end of   local_tools.tool_generate_html_grammar   =====#
