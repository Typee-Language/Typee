# -*- coding: utf-8 -*-
"""
Copyright (c) 2018-2021 Philippe Schmouker, Typee project, http://www.typee.ovh

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
class FEICNode:
    """
    Basic interface for all types of nodes in Intermediate Code Trees.
    This is a virtual item of a mental construction. It might be later suppressed! 
    """

    #-------------------------------------------------------------------------
    def __init__(self, content=None) -> None:
        '''
        Cnstructor.
        
        Args:
            content:
                A reference to the content to be associated with this IC node.
        '''
        self.content = content

    #-------------------------------------------------------------------------
    def set_parent(self, parent):
        '''
        Sets the parent of this node.
        '''
        self.parent = parent

    #-------------------------------------------------------------------------
    def walk(self) -> None:
        '''
        Walks through the list of nodes contained within this block.
        Walk-through is depth-first implemented.
        HAS TO BE IMPLEMENTED IN INHERITING CLASSES.
        '''
        raise NotImplementedError()

#=====   end of   FrontEnd.IntermediateCode.fe_icnode   =====#
