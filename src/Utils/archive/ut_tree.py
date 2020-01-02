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
# no import.


#=============================================================================
## Local declarations
#-------------------------------------------------------------------------
class UTNode:
    '''
    The class of internal nodes for trees.
    '''
    #---------------------------------------------------------------------
    def __init__(self, parent=None) -> None:
        '''Constructor'''
        self._children = []
        self.parent = parent
        self.DBG_count = UTNode.DBG_Count
        UTNode.DBG_Count += 1
    #---------------------------------------------------------------------
    def __iadd__(self, child):
        '''Appends a new child to the children list.'''
        self._children.append( child )
        return self
    #---------------------------------------------------------------------
    def __iter__(self):
        return self
    #---------------------------------------------------------------------
    def __next__(self) -> None:
        for child in self._children:
            if isinstance( child, UTNode ):
                yield child
            else:
                yield child
        raise StopIteration()
    #---------------------------------------------------------------------
    DBG_Count = 0


#-------------------------------------------------------------------------
class UTLeaf:
    '''
    The class of ending nodes (i.e. leaves) for trees.
    '''
    #---------------------------------------------------------------------
    def __init__(self, data=None) -> None:
        '''Constructor'''
        self.data = data
    #---------------------------------------------------------------------
    def __iter__(self):
        return self
    #---------------------------------------------------------------------
    def __next__(self):
        yield self
        raise StopIteration()


#=============================================================================
class UTTree:
    """
    The utility class for Trees management in Typee.
    
    This is a very minimalist implementation of trees, dedicated 
    to the Typee Front-End.
    Do not aim at using this utility as a general tool for trees
    programming. The final deception would only be yours.
    """    
    #-------------------------------------------------------------------------
    def __init__(self) -> None:
        '''
        Constructor.
        Instantiates an empty tree.
        '''
        self._root    = UTNode()
        self._current = self._root
   
    #-------------------------------------------------------------------------
    def append(self, node):
        '''
        Appends a new node to the current node.
        '''
        node.parent = self._current
        self._current += node
        if not isinstance( node, UTLeaf ):
            self._current = node
        return self
   
    #-------------------------------------------------------------------------
    def __iadd__(self, node):
        '''
        Appends a new node to the current node.
        '''
        return self.append( node )
   
    #-------------------------------------------------------------------------
    def __iter__(self):
        return self
   
    #-------------------------------------------------------------------------
    def __next__(self):
        for node in self._root:
            yield from node
        raise StopIteration()
   
    #-------------------------------------------------------------------------
    def up(self):
        '''
        Returns the parent of current node
        '''
        return self._current.parent
            
        
#=====   end of   Utils.ut_tree   =====#
