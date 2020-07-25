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
class UTTreeNodeBase:
    """
    Basic interface for all types of nodes in Trees.
    """

    #-------------------------------------------------------------------------
    def __init__(self, parent=None, content=None) -> None:
        '''
        Constructor.
        
        Args:
            parent:
                A reference to the parent node in tree.
            content:
                A reference to the content to be associated with this tree node.
        '''
        self.parent  = parent
        if content is None:
            self.content = []
        elif isinstance( content, list ):
            self.content = content
        else:
            self.content = [ content ]

    #-------------------------------------------------------------------------
    def walk(self) -> None:
        '''
        Walks through the tree passing through this node.
        Walk-through is depth-first implemented.
        HAS TO BE IMPLEMENTED IN INHERITING CLASSES.
        See UTTreeNode and UTTreeLeaf to get examples of implementation.
        '''
        raise NotImplementedError()

#=====   end of   Utils.Trees.ut_tree_node_base   =====#
