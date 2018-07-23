"""
Copyright (c) 2016-2018 Philippe Schmouker, PyYadc project, https://github.com/schmouk/PyYadc

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
from utils import Utils


#=============================================================================
class HtmlFunction:
    """
    All manipulations on functions content.
    """
    # Versions:
    #    0.0.1 - 2016-07-04 - schmoukerp - Creation.
    
    #-------------------------------------------------------------------------
    def __init__(self, parsed_module ,
                       function_name ,
                       function_descr,
                       indent_level   ):
        '''
        Constructor.
        
        Args:
            parsed_module: ModuleParser - see module_parser.py
                A reference to the module parser as a result of the 
                ast parsing of the embedding module.
            function_name: str
                The name of this function.
            function_descr: FunctionDescr - see module_parser.py
                A reference to  the  internal  descriptor  of  this 
                function.
            indent_level: int
                The level of indentation in the HTML code  for  the
                container of this class.
        '''
        self._parsed_module  = parsed_module
        self._function_name  = function_name
        self._function_descr = function_descr
        self._indent_level   = indent_level


    #-------------------------------------------------------------------------
    def get_html_code(self):
        '''
        Evaluates HTML code for the documentation of this function.
        
        Returns:
            The HTML code, embedded in a string, related to this function.
        '''

        my_html_code  = self._get_function_header_code()
        my_html_code += self._get_function_body_code()
        my_html_code += self._get_function_footer_code()
        
        return my_html_code


    #-------------------------------------------------------------------------
    def _get_function_body_code(self):
        '''
        Evaluates the HTML code for the body of this function documentation.
        
        Returns:
            The header HTML code, embedded in a string,  related to this function.
        '''
        if self._function_descr.docstring:
            my_html_code  = Utils.html_indent( self._indent_level, '<pre>' )

            if self._function_descr.docstring[0] != '\n':
                my_html_code += Utils.html_indent( 2, ' ' )
            my_html_code += self._function_descr.docstring.rstrip( ' \n' )

            my_html_code += Utils.html_indent( self._indent_level, '\n</pre>\n\n' )

            return my_html_code

        else:
            return ''


    #-------------------------------------------------------------------------
    def _get_function_footer_code(self):
        '''
        Evaluates the HTML code for the footer of this function documentation.
        
        Returns:
            The header HTML code, embedded in a string,  related to this function.
        '''
        my_html_code = ''
        
        return my_html_code


    #-------------------------------------------------------------------------
    def _get_function_header_code(self):
        '''
        Evaluates the HTML code for the header of this function documentation.
        
        Returns:
            The header HTML code, embedded in a string,  related to this function.
        '''
        my_args_count = len( self._function_descr.function_node.args.args )
        
        my_html_code = ''
        
        start_lineno = self._function_descr.function_node.lineno
        if my_args_count > 0:
            end_lineno = self._function_descr.function_node.args.args[-1].lineno
        else:
            end_lineno = start_lineno
            while 'def ' not in self._parsed_module.module_lines[end_lineno-1]:
                end_lineno += 1 
        
        for lineno in range(start_lineno-1, end_lineno):
            my_substring = self._parsed_module.module_lines[lineno].strip()
            my_substring = my_substring.replace( ' ', '' ).replace( ',', ', ' )
            my_html_code += my_substring + ' '
        
        my_html_code = my_html_code[:-1]
        
        last_par_index = my_html_code.rfind( ')' )
        if last_par_index != -1:
            my_substring = my_html_code[last_par_index:].replace( ' ', '' )
            if my_substring[-1] != ':':
                my_html_code += ')'
        else:
            my_html_code += ')'
            
        my_html_code = my_html_code.rstrip(':').replace( '->', ' -> ' )
        
        my_html_split_code = my_html_code.split( self._function_name, 1)
        my_html_code = Utils.html_indent( self._indent_level,
                                          '<p class="function_def">{:s} <b>{:s}</b> {:s}</p>\n'.format( 
                                            my_html_split_code[0],
                                            self._function_name  ,
                                            my_html_split_code[1]  ) )
        return my_html_code
        

    #-------------------------------------------------------------------------
    def _insert_decorators(self):
        '''
        Returns:
            The HTML code related to the decorators applied to this class.
        '''
        my_str = Utils.get_decorators_str( self._function_descr.function_node.decorator_list,
                                           self._parsed_module.module_lines                   )
        if my_str:
            return Utils.html_indent( self._indent_level+1,
                                      '{:s}\n'.format(my_str) )
        else:
            return '' 

#=====   end of module   html_function.py  =====#
