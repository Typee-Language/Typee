#!/usr/bin/env python
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
from FrontEnd.IntermediateCode.fe_icnode import FEICNode 


#=============================================================================
class FEICLeaf( FEICNode ):
    """
    Class description.
    """    
    #-------------------------------------------------------------------------
    def __init__(self, content):
        '''
        Constructor.
        
        Args:
            content: a reference to the content opf this leaf
        '''
        super().__init__( content )

    #-------------------------------------------------------------------------
    def walk(self) -> FEICNode:
        '''
        Walks through the list of nodes contained within this block.
        Walk-through is depth-first implemented.
        Returns:
            A reference to the content of this leaf.
        '''
        return self.content

#=====   end of   FrontEnd.IntermediateCode.fe_icleaf   =====#