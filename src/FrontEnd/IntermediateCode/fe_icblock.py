# -*- coding: utf-8 -*-
"""
/*** COPYRIGHT AND CONFIDENTIALITY INFORMATION NOTICE ****
Copyright (c) 2019 Thomson Licensing
All Rights Reserved

This program contains proprietary information which  is  a 
trade secret/business secret  of  Thomson Licensing and is 
protected, even if unpublished, under applicable Copyright 
laws (including French droit d'auteur). 
Recipient is to retain this program in confidence  and  is 
not permitted to  use or make copies thereof other than as 
permitted in a written agreement  with  Thomson  Licensing
unless  otherwise  expressly allowed by applicable laws or 
by Thomson Licensing under express agreement.
*********************************************************/
"""

#=============================================================================
from FrontEnd.IntermediateCode.fe_icnode import FEICNode
from FrontEnd.IntermediateCode.fe_icleaf import FEICLeaf


#=============================================================================
class FEICBlock( FEICNode ):
    """
    The class of blocks of tokens in Intermediate Code trees.
    """

    #-------------------------------------------------------------------------
    def __init__(self):  ##, parent:FEICNode=None):
        '''
        Constructor.
        '''
        super().__init__( [] )  ## content is an empty list (of FEICNode-s)
        ##self.parent = parent

    #-------------------------------------------------------------------------
    def __iadd__(self, ic_node:FEICNode):
        '''
        Appends a new node into this block.
        '''
        self.content.append( ic_node )
        return self

    #-------------------------------------------------------------------------
    def walk(self):
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
