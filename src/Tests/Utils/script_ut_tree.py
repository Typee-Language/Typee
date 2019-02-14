#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
/*** COPYRIGHT AND CONFIDENTIALITY INFORMATION NOTICE ***
Copyright (c) 2019 Thomson Licensing
All Rights Reserved

This program contains proprietary information which is  a 
trade  secret/business secret  of  Technicolor R&D France 
and is protected, even if unpublished,  under  applicable 
Copyright laws (including French droit d'auteur). 
Recipient is to retain this program in confidence and  is 
not  permitted  to  use or make copies thereof other than 
as    permitted   in   a    written    agreement     with 
Technicolor R&D France unless otherwise expressly allowed 
by applicable laws  or  by  Technicolor R&D France  under 
express agreement.
*********************************************************/
"""

#=============================================================================
from Utils.ut_tree import UTTree, UTNode, UTLeaf


#=============================================================================

#-----------------------------------------------------------------------------
def test_ut_tree() -> int:
    '''
    This is the testing of class UTTree.
    '''
    errors_count = 0
    
    my_tree = UTTree()
    
    my_tree.append( UTNode() ).append( UTNode() )
    my_tree += UTLeaf( 'A' )
    my_tree += UTLeaf( 'B' )
    my_tree.up()
    my_tree += UTLeaf( 'C' )

    for node in my_tree:
        print( node.data )
    
    return errors_count


#=============================================================================
if __name__ == '__main__':
    '''
    Description of this script.
    '''
                
    #-------------------------------------------------------------------------
    print( 'UTTree validation tests' )
    count = test_ut_tree()
    if count == 0:
        print( '  Tests OK')
    else:
        print( 'detected {} error{}'.format( count, 's' if count > 1 else '') )        

    print( '\n-- done!' )


#=====   end of Tests.Utils.script_utils   =====#
