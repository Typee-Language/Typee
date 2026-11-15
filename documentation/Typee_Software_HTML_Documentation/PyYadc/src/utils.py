#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2016-2021 Philippe Schmouker, PyYadc project, https://github.com/schmouk/PyYadc

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
class Utils:
    """
    This class is used as a namespace for utilities definitions
    """

    #-------------------------------------------------------------------------
    # Class Data
    K_HTML_INDENT_SPACES = 2
    K_MAX_ASSIGNS_LINES  = 10
    
    #-------------------------------------------------------------------------
    @staticmethod
    def html_indent(indent_level, html_str):
        '''
        Inserts spaces in front of html string according to specified level 
        of indentation.
        
        Args:
            indent_level: int
                The level of indentation.  Please notice that this function
                uses the class constant K_HTML_INDENT_SPACES which defaults
                to 2.
            html_str: str
                The HTML code to be indented.
        
        Returns:
            The indented HTML code, every inner '\\n' being modified accord-
            ingly.
        '''
        my_indent = ' '*(indent_level * Utils.K_HTML_INDENT_SPACES)
        try:
            html_split = html_str.split( '\n' )
            if html_split[-1] == '':
                html_str = ('\n'+my_indent).join( html_split[:-1] ) + '\n'
            else:
                html_str = ('\n'+my_indent).join( html_split )
        except:
            pass 
        return '{:s}{:s}'.format( my_indent, html_str )
    
    
    #-------------------------------------------------------------------------
    @staticmethod
    def get_decorators_str(decorator_list, module_lines):
        '''
        Transforms a list of decorators as specified in ast into a string.
        
        Args:
            decorator_list: list
                A reference to a list of decorators descriptors.
            module_lines: list
                A reference to the content of the parsed module,
                one line per entry.
        
        Returns:
            A string describing the whole decorators.
        '''
        myk_decorators_count = len(decorator_list)
        if myk_decorators_count == 0:
            return None
        
        my_str = '<span class="class_decorators"><i>[&nbsp;class decorator{:s}:</i> '.format( 's' if myk_decorators_count > 1 else '' )
        
        for decorator_descr in decorator_list:
            my_decorator_line = module_lines[ decorator_descr.lineno-1 ]
            try:
                my_decorator_line = my_decorator_line.split('#',1)[0]
            except:
                pass
            my_decorator_line = my_decorator_line.strip()
            my_str += '{:s}, '.format( my_decorator_line )
            
        return my_str[:-2] + '&nbsp;<i>]</i></span>'
    
    
    #-------------------------------------------------------------------------
    @staticmethod
    def path_to_id(path):
        '''
        Evaluates an HTML id from a path.
        
        Args:
            path: str
                The path name to be transformed as an id.
        
        Returns:
            A string corresponding to the transformed path.
        '''
        return Utils.replace_backslash( path ).replace( '/', '_' )
    
    
    #-------------------------------------------------------------------------
    @staticmethod
    def replace_backslash(path):
        '''
        Replaces every backslash with a slash.
        
        Args:
            path: str
                The path name to be transformed.
        
        Returns:
            A string corresponding to the transformed path.
        '''
        return path.replace( '\\', '/' )

#=====   end of module   utils.py   =====#
        