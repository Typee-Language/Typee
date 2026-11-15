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
from Utils.Trees.ut_tree_node_base import UTTreeNodeBase

#=============================================================================
class UTTreeLeaf( UTTreeNodeBase ):
    """
    The class of leaves in trees.
    """    

    #-------------------------------------------------------------------------
    def __init__(self, content = None) -> None:
        '''
        Constructor.
        
        Args:
            parent:
                A reference to the parent node in tree.
                Defaults to None (which means this node is a tree root)
            content:
                A reference to the content to be associated with this tree leaf.
        '''
        super().__init__( None, content )

    #-------------------------------------------------------------------------
    def walk(self):
        '''
        Walks over this leaf.

        Returns:
            A reference to the content of this leaf inserted in a generator.
        '''
        return (self, )

#=====   end of   Utils.Trees.ut_tree_leaf   =====#
