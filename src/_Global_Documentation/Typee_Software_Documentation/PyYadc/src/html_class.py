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
from html_function   import HtmlFunction
from utils           import Utils


#=============================================================================
class HtmlClass:
    """
    All manipulations on classes content.
    """
    # Versions:
    #    0.0.1 - 2016-06-26 - PhSch - Creation.
    
    #-------------------------------------------------------------------------
    def __init__(self, module_ref   ,
                       parsed_module,
                       class_name   ,
                       class_descr  ,
                       indent_level  ):
        '''
        Constructor.
        
        Args:
            module_ref: HtmlModule
                A reference to the HTML descriptor of  the  embedding 
                module.
            parsed_module: ModuleParser - see module_parser.py
                A reference to the module parser as a result  of  the 
                ast parsing of the embedding module.
            class_name: str
                The name of this class.
            class_descr: ClassDescr - see module_parser.py
                A reference to the internal descriptor of this class.
            indent_level: int
                The level of indentation in the  HTML  code  for  the
                container of this class.
        '''
        self._module_ref    = module_ref
        self._parsed_module = parsed_module
        self._class_name    = class_name
        self._class_descr   = class_descr
        self._indent_level  = indent_level

    #-------------------------------------------------------------------------
    @staticmethod
    def get_class_id(html_module_id, class_name):
        '''
        Evaluates the HTML id to be associated to some class.
        
        Args:
            html_module_id: str
                The HTML id associated with the embedding module.
            class_name: str
                The name of the class.
        
        Returns:
            A string containing the HTML  id  for  the  specified
            class.
        '''
        return '_'.join( (html_module_id, class_name) )

    #-------------------------------------------------------------------------
    def get_html_code(self):
        '''
        Evaluates HTML code for the documentation of this module.
        
        Returns:
            The HTML code, embedded in a string, related to this module.
        '''

        my_html_code  = self._get_class_header_code()
        my_html_code += self._get_class_body_code()
        my_html_code += self._get_class_footer_code()
        
        return my_html_code

    #-------------------------------------------------------------------------
    def get_html_id(self):
        '''
        Gets an HTML identifier associated with a module and its embedding package.
        
        Returns:
            A string containing the CSS id associated with the specified module. 
        '''
        return HtmlClass.get_class_id( self._module_ref.get_html_id(), self._class_name )

    #-------------------------------------------------------------------------
    def _get_class_body_code(self):
        '''
        Evaluates the HTML code for the internal description  of  this  class 
        documentation.
        
        Returns:
            The header HTML code, embedded in a string, related to this class.
        '''
        my_html_code = ''
        
        my_html_code += self._insert_docstring()
        my_html_code += self._insert_assigns()
        my_html_code += self._insert_methods()
        
        return my_html_code

    #-------------------------------------------------------------------------
    def _get_class_footer_code(self):
        '''
        Evaluates the HTML code for the footer of this class documentation.
        
        Returns:
            The header HTML code, embedded in a string, related to this class.
        '''
        my_html_code = Utils.html_indent( self._indent_level+1,
                                          '<p>up to class <a class="class_end" href="#{:s}">{:s}</a><br />\n'.format(
                                                self.get_html_id(),
                                                self._class_name    ) )
        
        my_html_code += Utils.html_indent( self._indent_level+1,
                                           'back to module <a class="module_end" href="#{:s}">{:s}</a></p>\n'.format(
                                                self._module_ref.get_html_id(),
                                                self._module_ref._module_name   ) )
        
        my_html_code += Utils.html_indent( self._indent_level,
                                           '</div> <!-- end of class {:s} -->\n\n'.format(
                                                self._class_name ) )
        
        return my_html_code

    #-------------------------------------------------------------------------
    def _get_class_header_code(self):
        '''
        Evaluates the HTML code for the header of this class documentation.
        
        Returns:
            The header HTML code, embedded in a string, related to this class.
        '''
        #---------------------------------------------------------------------
        def _my_list_bases(ast_node):
            html_code = ''
            for ast_base in ast_node.bases:
                try:
                    # is this an ast.Name?
                    html_code += ast_base.id + ', '
                except:
                    try:
                        # is this an ast.Attribute?
                        html_code += '.'.join( (ast_base.value.id, ast_base.attr) ) + ', '
                    except:  
                        # this is an unprocessed type of ast.Node
                        pass
            return html_code
        
        #---------------------------------------------------------------------
        my_html_code  = Utils.html_indent( self._indent_level,
                                           '<div class="class_container" id="{:s}">\n'.format( self.get_html_id() ) )

        my_html_code += Utils.html_indent( self._indent_level+1,
                                           '<p class="class_def">class <b>{:s}</b>'.format( self._class_name ) )
        
        my_ast_node = self._class_descr['class_descr'].class_node

        my_text_inserted = False
        try:
            if len(my_ast_node.bases) > 0 or len(my_ast_node.keywords) > 0:
                my_html_code += '&nbsp;( {:s}'.format( _my_list_bases(my_ast_node) )
                my_text_inserted = True
                                
                if len(my_ast_node.keywords) > 0:
                    if len(my_ast_node.bases) > 0:
                        my_html_code += ', '
                    for ast_keyword in my_ast_node.keywords:
                        my_html_code += '{:s}={:s}, '.format( ast_keyword.arg, ast_keyword.value.id )
                
        except Exception as _e:
            # Python 2.x - no 'keywords' attribute
            pass
            #===================================================================
            # if len(my_ast_node.bases) > 0:
            #     my_html_code += '&nbsp;( {:s}'.format( _my_list_bases(my_ast_node) )
            #     my_text_inserted = True
            #===================================================================
                
        
        if my_text_inserted:
            my_html_code = my_html_code[:-2] + ' )'

        my_html_decorators = self._insert_decorators()
        if my_html_decorators:
            my_html_code += '<br />\n' + my_html_decorators

        return my_html_code + Utils.html_indent( self._indent_level+1, '</p>\n' )

    #-------------------------------------------------------------------------
    def _insert_assigns(self):
        '''
        Returns:
            The HTML code related to the assignments of class data.
        '''
        K_MAX_LINES = Utils.K_MAX_ASSIGNS_LINES

        my_assigns_list = self._parsed_module.module_descr.classes_dict[self._class_name]['assigns_descrs']

        if len( my_assigns_list ) == 0:
            return ''

        my_html_code  = Utils.html_indent( self._indent_level+1,
                                           '<div class="imports-list">\n' )
        my_html_code += Utils.html_indent( self._indent_level+2,
                                           '<p class="imports-def"><b>List of data</b> for class <b><span class="blue">{:s}</span></b></p>\n<pre>\n'.format(self._class_name) )

        max_lineno = max( [assign_descr.assign_node.lineno for assign_descr in my_assigns_list] )
        my_format_str    = "<i>line {:%d}</i> | {:s}\n" % len( str(max_lineno) )

        for assign_descr in my_assigns_list:
            
            my_start_line = assign_descr.assign_node.lineno-1
            my_end_line   = assign_descr.assign_node.value.lineno

            if my_end_line - my_start_line <= K_MAX_LINES:
                for line_no in range(my_start_line, my_end_line):
                    my_html_code += Utils.html_indent( 1, my_format_str.format( line_no,
                                                                                self._parsed_module.module_lines[ line_no ] ) )
            else:
                for line_no in range(my_start_line, my_start_line+K_MAX_LINES):
                    my_html_code += Utils.html_indent( 1, my_format_str.format( line_no,
                                                                                self._parsed_module.module_lines[ line_no ] ) )
                my_more_lines = my_end_line-my_start_line-K_MAX_LINES
                my_html_code += Utils.html_indent( 1, ' '*(len(my_format_str.format(my_start_line, ''))-5) )
                my_html_code += Utils.html_indent( 1,
                                                   '... (<i>{:d} more line{:s}</i>)'.format( my_more_lines,
                                                                                             's' if my_more_lines > 1 else '' ) )

        
        my_html_code = my_html_code.rstrip()
        my_html_code += Utils.html_indent( self._indent_level+2, '</pre>\n' )
        my_html_code += Utils.html_indent( self._indent_level+1, '</div>\n' )

        return my_html_code

    #-------------------------------------------------------------------------
    def _insert_decorators(self):
        '''
        Returns:
            The HTML code related to the decorators applied to this class.
        '''
        my_str = Utils.get_decorators_str( self._class_descr['class_descr'].class_node.decorator_list,
                                           self._parsed_module.module_lines                            )
        if my_str:
            return Utils.html_indent( self._indent_level+1,
                                      '{:s}\n'.format(my_str) )
        else:
            return '' 

    #-------------------------------------------------------------------------
    def _insert_docstring(self):
        '''
        Returns:
            The HTML code related to the docstring associated with this class.
        '''
        my_html_code = Utils.html_indent( self._indent_level+1, '<pre>\n' )
        
        if self._class_descr['class_descr'].docstring:
            try:
                my_html_code += Utils.html_indent( 1, self._class_descr['class_descr'].docstring.strip() )
                #my_html_code += Utils.html_indent( 1, self._class_descr['class_descr'].docstring.replace('<', '&lt;').replace('>', '&gt;').strip() )
            except:
                my_html_code += '<unknown error detected in docstring - maybe string encoding/decoding failure>'
        
        my_html_code += '</pre>\n'

        return my_html_code

    #-------------------------------------------------------------------------
    def _insert_methods(self):
        '''
        Returns:
            The HTML code related to all the methods defined within this class.
        '''
        #---------------------------------------------------------------------
        def my_list_function(f_name, f_descr):
            my_html_function = HtmlFunction( self._parsed_module ,
                                             f_name              ,
                                             f_descr             ,
                                             self._indent_level+1  )
            return my_html_function.get_html_code()
        
        #---------------------------------------------------------------------
        my_functions_dict = self._class_descr['functions_descrs']
        
        if len( my_functions_dict ) == 0:
            return ''

        my_html_code = ''
        
        for func_name, func_descr in sorted( my_functions_dict.items() ):
            if func_name.startswith('__') and func_name.endswith('__'):
                my_html_code += my_list_function( func_name, func_descr )

        for func_name, func_descr in sorted( my_functions_dict.items() ):
            if not func_name.startswith('_'):
                my_html_code += my_list_function( func_name, func_descr )

        for func_name, func_descr in sorted( my_functions_dict.items() ):
            try:
                if func_name.startswith('_') and not func_name.endswith('__'):
                    my_html_code += my_list_function( func_name, func_descr )
            except:
                pass

        return my_html_code

#=====   end of module   html_class.py   =====#
