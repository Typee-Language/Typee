#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2018 Philippe Schmouker, Typee project, http://www.typee.ovh

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
# no import.


#=============================================================================
class FESyntaxICodeNode( list ):
    """
    This is the class of nodes for the syntaxic intermediate code as  used  in
    the Front-End of the Typee project.
    
    A Syntaxic Code Node is a symbolic representation of a  block  of  instruct-
    ions  as well as of a single statement.  As such,  since blocks of instruct-
    ions can be nested, a Syntaxic Code Node is a node in a tree,  whose  sibl-
    ings are the other blocks of instructions at the same level within a module
    (i.e. a source file), and whose children are the nested blocks of instruct-
    ions it embeds.
    Each Syntaxic Code Node contains the whole list of  its  nested  blocks  of 
    instructions, i.e. it is represented as a list of FESCodeNodes.
    Representing the Syntaxic Tree this way will help evaluating  the  visibil-
    ity  of  variables  as well as the correct checking of types,  later in the 
    Elaboration step of the Front End.
    
    See definitions of  FESICodeBlockNode  and  FESICodeStatementNode  below in  
    this same module.
    
    Please notice that there are in Typee three kinds of blocks  of  instruct-
    ions:  blocks  with  no instruction,  blocks with a single instruction and 
    blocks with many instructions.
    """    
    #-------------------------------------------------------------------------
    def __init__(self, parent=None, is_block:bool=True):
        '''
        Constructor.
                
        Args:
            parent:
                A reference to an instantiation of FESCodeNode,  which is  the
                parent of this Syntaxic Code Node.  Defaults to None (i.e. the
                root of the Syntaxic Tree).
            is_block:
                Set this to True to create a new level in  the  syntaxic  tree
                for  a new block of instructions, or set it to False to create
                a new level in the syntaxic tree for a new statement. Defaults
                to True (i.e. new block of instructions).
        '''
        self.parent   = parent
        self.is_block = is_block
        super().__init__()
   
    #-------------------------------------------------------------------------
    @property
    def count(self) -> int:          return len(self)
    @property
    def is_statement(self) -> bool:  return not self.is_block


#=============================================================================
class FESICodeBlockNode( FESyntaxICodeNode ):
    """
    This is the class of nodes for the syntaxic intermediate code as used in
    the Front-End of the Typee project,  dedicated to the representation of
    blocks of instructions.
    """
    #-------------------------------------------------------------------------
    def __init__(self, parent=None):
        '''
        Constructor.
                
        Args:
            parent:
                A reference to an instantiation of FESCodeNode,  which is  the
                parent of this Syntaxic Code Node.  Defaults to None (i.e. the
                root of the Syntaxic Tree).
        '''
        super().__init__( parent, True )


#=============================================================================
class FESICodeStatementNode( FESyntaxICodeNode ):
    """
    This is the class of nodes for the syntaxic intermediate code as used in
    the Front-End of the Typee project,  dedicated to the representation of
    single instructions.
    """
    #-------------------------------------------------------------------------
    def __init__(self, parent=None):
        '''
        Constructor.
                
        Args:
            parent:
                A reference to an instantiation of FESCodeNode,  which is  the
                parent of this Syntaxic Code Node.  Defaults to None (i.e. the
                root of the Syntaxic Tree).
        '''
        super().__init__( parent, False )


#=====   end of   FrontEnd.IntermediateCode.fe_syntax_icode_node   =====#
        