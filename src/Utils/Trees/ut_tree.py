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
from Utils.Trees.ut_tree_leaf      import UTTreeLeaf 
from Utils.Trees.ut_tree_node      import UTTreeNode 
from Utils.Trees.ut_tree_node_base import UTTreeNodeBase 


#=============================================================================
class UTTree:
    """
    The utility class of Trees.
    """

    #-------------------------------------------------------------------------
    def __init__(self) -> None:
        '''
        Constructor.
        '''
        self._root = UTTreeNode()
        self._current = self._root

    #-------------------------------------------------------------------------
    def __iadd__(self, new_node: UTTreeNodeBase):
        '''
        In-place appends a new node or leaf to this tree.
        If new_node is a tree node (and not a tree leaf), new_node
        becomes the current node of the tree for next appends.
        
        Returns a reference to this tree.
        '''
        new_node.parent = self._current
        
        self._current += new_node
        if isinstance( new_node, UTTreeNode ):
            self._current = new_node
            
        return self

    #-------------------------------------------------------------------------
    def up_level(self):
        '''
        Goes one level up in the tree, i.e. back to parent block in the IC Tree.
        '''
        self._current = self._current.parent
        return self

    #-------------------------------------------------------------------------
    def walk(self):
        '''
        Walks through this Intermediate Code tree, starting at its root.
        Walk-through is depth-first implemented.
        '''
        if self._root is not None:
            yield from self._root.walk()

#=====   end of   Utils.Trees.ut_tree   =====#
