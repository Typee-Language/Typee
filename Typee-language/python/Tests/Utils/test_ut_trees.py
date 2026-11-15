# -*- coding: utf-8 -*-
"""
Copyright (c) 2019-2021 Philippe Schmouker, Typee project, http://www.typee.ovh

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
from Utils.Trees.ut_tree       import UTTree
from Utils.Trees.ut_tree_leaf  import UTTreeLeaf
from Utils.Trees.ut_tree_node  import UTTreeNode

#=============================================================================
if __name__ == '__main__':
    my_tree = UTTree()
    
    my_tree += UTTreeNode()
    my_tree += UTTreeNode()
    my_tree.up_level()
    my_tree += UTTreeLeaf( 'A' )
    my_tree += UTTreeLeaf( 'B' )
    my_tree.up_level()
    my_tree += UTTreeNode()
    my_tree += UTTreeLeaf( 'C' )
    my_tree.up_level()
    my_tree += UTTreeLeaf( 'D' )

    for node in my_tree.walk():
        if isinstance(node, UTTreeLeaf ):
            print( 'Leaf:', node.content )
        else:
            print( 'Node:', node.content )

    print( '-- done!' )

#=====   end of   Tests.Utils.test_ut_trees   =====#