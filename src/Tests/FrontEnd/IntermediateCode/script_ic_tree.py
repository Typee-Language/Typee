# -*- coding: utf-8 -*-

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
from FrontEnd.IntermediateCode.fe_icblock    import FEICBlock
from FrontEnd.IntermediateCode.fe_icleaf     import FEICLeaf
from FrontEnd.IntermediateCode.fe_icnode     import FEICNode
from FrontEnd.IntermediateCode.fe_ictree     import FEICTree


#=============================================================================

#-------------------------------------------------------------------------
def create_test_tree() -> FEICTree:
    '''
    '''
    my_tree = FEICTree()
    
    new_block = FEICBlock()
    my_tree += new_block
    new_block += FEICLeaf( 'C' )

    new_block_2 = FEICBlock()
    new_block += new_block_2
    new_block_2 += FEICLeaf( 'E' )
    
    my_tree += FEICLeaf( 'A' )
    my_tree += FEICLeaf( 'B' )
    
    new_block = FEICBlock()
    my_tree += new_block
    new_block += FEICLeaf( 'D' )

    return my_tree
    


#-------------------------------------------------------------------------
def walk_through_tree( ic_tree: FEICTree ) -> int:
    '''
    '''
    errors_count = 0
    for expected_content, node_content in zip( ['C','E','A','B','D'], ic_tree.walk() ):
        if expected_content != node_content:
            errors_count += 1
        print( expected_content, '->', node_content, end=',  ' )
    print()
    
    return errors_count


#=============================================================================
if __name__ == '__main__':
    """
    Script description.
    """
    #-------------------------------------------------------------------------
    test_tree = create_test_tree()
    print( walk_through_tree(test_tree), 'error(s)' )
    
    print( "\n\n-- 2nd test on an empty tree" )
    print( walk_through_tree(FEICTree()), 'error(s)' )
    
    
    print( '\n-- done!')
   

#=====   end of   Tests.FrontEnd.IntermediateCode.script_ic_tree   =====#
