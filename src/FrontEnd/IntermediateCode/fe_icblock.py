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
from FrontEnd.IntermediateCode.fe_icnode import FEICNode
##from FrontEnd.IntermediateCode.fe_icleaf import FEICLeaf


#=============================================================================
class FEICBlock( FEICNode ):
    """
    The class of blocks of tokens in Intermediate Code trees.
    """

    #-------------------------------------------------------------------------
    def __init__(self) -> None:  ##, parent:FEICNode=None):
        '''
        Constructor.
        '''
        super().__init__( [] )  ## content is an empty list (of FEICNode-s)

    #-------------------------------------------------------------------------
    def __iadd__(self, ic_node: FEICNode):
        '''
        Appends a new node into this block.
        '''
        self.content.append( ic_node )
        return self

    #-------------------------------------------------------------------------
    def walk(self) -> None:
        '''
        Walks through the list of nodes contained within
        this block.
        Walk-through is depth-first implemented.
        Returns:
            every content of the leaves in  this  block,
            in a depth-first walking through manner.
        '''
        for icnode in self.content:
            yield from icnode.walk()

#=====   end of   FrontEnd.IntermediateCode.fe_icblock   =====#
