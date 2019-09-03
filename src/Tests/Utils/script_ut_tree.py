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
from Utils.ut_tree import UTTree, UTNode, UTLeaf


#=============================================================================

#-----------------------------------------------------------------------------
def test_ut_tree() -> int:
    '''
    This is the testing of class UTTree.
    '''
    errors_count = 0
    
    my_tree = UTTree()
    
    my_tree.append( UTNode() ).append( UTNode() )
    my_tree += UTLeaf( 'A' )
    my_tree += UTLeaf( 'B' )
    my_tree.up()
    my_tree += UTLeaf( 'C' )

    for node in my_tree:
        print( node.data )
    
    return errors_count


#=============================================================================
if __name__ == '__main__':
    '''
    Description of this script.
    '''
                
    #-------------------------------------------------------------------------
    print( 'UTTree validation tests' )
    count = test_ut_tree()
    if count == 0:
        print( '  Tests OK')
    else:
        print( 'detected {} error{}'.format( count, 's' if count > 1 else '') )        

    print( '\n-- done!' )


#=====   end of Tests.Utils.script_ut_tree   =====#
