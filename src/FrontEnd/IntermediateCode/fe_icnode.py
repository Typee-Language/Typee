#!/usr/bin/env python 
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
#no imports


#=============================================================================
class FEICNode:
    """
    Basic interface for all types of nodes in Intermediate Code Trees.
    This is a virtual item of a mental construction. It might be later suppressed! 
    """

    #-------------------------------------------------------------------------
    def __init__(self, content=None):
        '''
        Cnstructor.
        
        Args:
            content:
                A reference to the content to be associated with this IC node.
        '''
        self.content = content

    #-------------------------------------------------------------------------
    def set_parent(self, parent:FEICNode):
        '''
        Sets the parent of this node.
        '''
        self.parent = parent

    #-------------------------------------------------------------------------
    def walk(self) -> FEICNode:
        '''
        Walks through the list of nodes contained within this block.
        Walk-through is depth-first implemented.
        HAS TO BE IMPLEMENTED IN INHERITING CLASSES.
        '''
        raise NotImplementedError()

#=====   end of   FrontEnd.IntermediateCode.fe_icnode   =====#
