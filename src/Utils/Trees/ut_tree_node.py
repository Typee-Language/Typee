# -*- coding: utf-8 -*-
"""
Copyright (c) 2019-2020 Philippe Schmouker, Typee project, http://www.typee.ovh

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
from Utils.Trees.ut_tree_node_base import UTTreeNodeBase

#=============================================================================
class UTTreeNode( UTTreeNodeBase ):
    """
    The class of internal nodes in Trees.
    """

    #-------------------------------------------------------------------------
    def __init__(self, parent: UTTreeNodeBase = None, children: list = None) -> None:
        '''
        Constructor.
        
        Args:
            parent:
                A reference to the parent node in tree.
                Defaults to None (which means this node is a tree root)
            children:
                A reference to the content to be associated with this IC node.
        '''
        super().__init__( parent, children or [] )

    #-------------------------------------------------------------------------
    def __iadd__(self, new_child: UTTreeNodeBase) -> UTTreeNodeBase:
        '''
        Appends a new child to the list of children of this tree node.
        '''
        self.content.append( new_child )
        return self

    #-------------------------------------------------------------------------
    def walk(self):
        '''
        Walks through the tree passing through this node.
        Walk-through is depth-first implemented.
        '''
        for child in self.content:
            yield from child.walk()

#=====   end of   Utils.Trees.ut_tree_node   =====#
