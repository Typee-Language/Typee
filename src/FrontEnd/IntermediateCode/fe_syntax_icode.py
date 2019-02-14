#!/usr/bin/env python
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
from FrontEnd.IntermediateCode.fe_syntax_icode_node  import FESyntaxICodeNode, \
                                                            FESICodeBlockNode, \
                                                            FESICodeStatementNode
from FrontEnd.IntermediateCode.fe_icode_token_node   import FEICodeTokenNode


#=============================================================================
class FESyntaxICode:
    """
    This is the class for syntaxic intermediate code
    generated by the Typee Front-End Parser.
    """    
    #-------------------------------------------------------------------------
    def __init__(self):
        '''
        Constructor.
        '''
        super().__init__()
        self._current_block = self._root = FESICodeBlockNode()

    #-------------------------------------------------------------------------
    def add_statement(self, inode:FEICodeTokenNode ) -> FESyntaxICode:
        self.create_statement_node()
        self.add_inode( inode )
        return self

    #-------------------------------------------------------------------------
    def add_inode(self, inode:FEICodeTokenNode) -> FESyntaxICode:
        self._current_statement.append( inode )
        return self
   
    #-------------------------------------------------------------------------
    def close_block_node(self) -> FESyntaxICode:
        self._current_block = self._current_block.parent
        return self
   
    #-------------------------------------------------------------------------
    def create_block_node(self) -> FESyntaxICode:
        new_node = FESICodeBlockNode( self._current_block )
        self._current.append( new_node )
        self._current = new_node
        return self
   
    #-------------------------------------------------------------------------
    def create_statement_node(self, inode:FEICodeTokenNode) -> FESyntaxICode:
        new_node = FESICodeStatementNode( self._current_block )
        self._current_block.append( new_node )
        self._current_statement = new_node
        return self.add_inode( inode )

    #-------------------------------------------------------------------------
    def walk(self, node:FESyntaxICodeNode=None) -> FESyntaxICodeNode:
        node = node or self._root
        yield node
        for child in node:
            if child.is_block:
                self.walk( child )
            else:
                yield node
            
    #-------------------------------------------------------------------------
    @property
    def count(self) -> int:
        return len( self )
    @property
    def current_level_count(self) -> int:
        return self._current.count
    
#=====   end of   FrontEnd.IntermediateCode.fe_syntax_iscode   =====#
        