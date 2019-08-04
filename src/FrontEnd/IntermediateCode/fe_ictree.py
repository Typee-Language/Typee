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
from FrontEnd.IntermediateCode.fe_icblock import FEICBlock 
from FrontEnd.IntermediateCode.fe_icnode  import FEICNode 


#=============================================================================
class FEICTree:
    """
    The class of Intermediate Code trees.
    """

    #-------------------------------------------------------------------------
    def __init__(self):
        '''
        Constructor.
        '''
        self._root = FEICBlock()
        self._current = self._root

    #-------------------------------------------------------------------------
    def __iadd__(self, ic_node:(FEICBlock,FEICNode)):
        '''
        Appends a new node into this block.
        '''
        ic_node.set_parent( self._current )
        self._current += ic_node
        if isinstance( ic_node, FEICBlock ):
            self._current = ic_node

    #-------------------------------------------------------------------------
    def up_level(self):
        '''
        Goes one level up in the tree, i.e. back to parent block in the IC Tree.
        '''
        self._current = self._current.parent

    #-------------------------------------------------------------------------
    def walk(self):
        '''
        Walks through this Intermediate Code tree.
        Walk-through is depth-first implemented.
        '''
        self._root.walk()

#=====   end of   FrontEnd.IntermediateCode.fe_ictree   =====#
