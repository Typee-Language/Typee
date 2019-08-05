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
from datetime import date
import os

#=============================================================================
class CopyrightYearsModif:
    """
    The utility to modify years of copyright 
    notices in directories and in files.
    """    
    #-------------------------------------------------------------------------
    def __init__(self) -> None:
        '''
        Constructor.
        
        Initializes current year value.
        '''
        self._current_year = date.today().year

    #-------------------------------------------------------------------------
    def modify_file(self, file_path: str):
        '''
        Modifies copyright notices in a specified file.
        '''
        print( file_path, end='' )
        try:
            
            with open( file_path, 'r' ) as fp:
                file_content = fp.readlines()
            
            modified = False
            for num_line, line in enumerate( file_content ):
                if 'opyright (c)' in line:
                    parsed_line = line.split( '(c)' )
                    parsed_years = parsed_line[1].split()
                    years = parsed_years[0].split( '-' )
                    try:
                        if int(years[-1]) != self._current_year:
                            if len( years ) > 1:
                                years[-1] = '{}'.format( self._current_year )
                                parsed_years[0] = '-'.join( years )
                            else:
                                parsed_years[0] = '{}-{}'.format( years[0], self._current_year )
                            parsed_line[1] = " {:s}\n".format( ' '.join( parsed_years ) )
                            file_content[ num_line ] = '(c)'.join( parsed_line )
                            modified = True
                            print( ' - modified:', file_content[num_line] )
                    except:
                        pass
            
            if modified:
                with open( file_path, 'w' ) as fp:
                    fp.writelines( file_content )
            else:
                print( ' - ok' )

        except Exception:
            print( ' - unprocessed' )

        return self

    #-------------------------------------------------------------------------
    def modify_files(self, files_list: list):
        '''
        Modifies copyright notices in every specified files.
        '''
        for file_path in files_list:
            self.modify_file( file_path )
        
        return self

    #-------------------------------------------------------------------------
    def modify_directory(self, rootdir_path: str = '.'):
        '''
        Modifies copyright notices in every file of specified directory.
        '''
        for current_dir_path, _dir_names, file_names in os.walk( rootdir_path ):
            self.modify_files( [os.path.join(current_dir_path, file_name) for file_name in file_names] )
        
        return self

    #-------------------------------------------------------------------------
    def modify_directories(self, dirs_list: list):
        '''
        Automates the modification of coyright notices in many directories.
        '''
        for dir_path in dirs_list:
            self.modify_directory( dir_path )
        
        return self

#=====   end of   scripts.utils.copyright_years_modif   =====#

