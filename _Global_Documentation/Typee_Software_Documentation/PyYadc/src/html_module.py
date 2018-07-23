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
##import ast 

from html_class      import HtmlClass
from html_function   import HtmlFunction
from module_parser   import ModuleParser
from utils           import Utils


#=============================================================================
class HtmlModule:
    """
    All manipulations on modules content.
    """
    # Versions:
    #    0.0.1 - 2016-06-26 - PhSch - Creation.
    
    #-------------------------------------------------------------------------
    def __init__(self, package_path, package_name, module_name, html_indent_level):
        '''
        Constructor.
                
        Args:
            package_path: str
                the path to the embedding package.
            module_name: str
                the name of this embedded module.
            html_indent_level: int
                The level of indentation in the HTML code for this module.
        '''
        self._package_path  = package_path
        self._package_name  = package_name
        self._module_name   = module_name
        self._parsed_module = self._parse_module()
        self._indent_level  = html_indent_level
    
    #-------------------------------------------------------------------------
    def get_html_code(self):
        '''
        Evaluates HTML code for the documentation of this module.
        
        Returns:
            The HTML code, embedded in a string, related to this module.
        '''

        my_html_code  = self._get_module_header_code()

        if self._is_empty_module():
            my_html_code += self._empty_module()
        
        else:
            my_html_code += self._insert_docstring()
            my_html_code += self._list_imports()
            my_html_code += self._list_functions()
            my_html_code += self._list_classes()
            my_html_code += self._list_assigns()
            
            for class_name, class_descr in sorted( self._parsed_module.module_descr.classes_dict.items() ):
                my_html_code += HtmlClass( self                  ,
                                           self._parsed_module   ,
                                           class_name            ,
                                           class_descr           ,
                                           self._indent_level + 1  ).get_html_code()
            
        my_html_code += self._get_module_footer_code()
        
        return my_html_code

   
    #-------------------------------------------------------------------------
    def get_html_id(self):
        '''
        Gets an HTML identifier associated with a module and its embedding package.
        
        Returns:
            A string containing the CSS id associated with the specified module. 
        '''
        return '_'.join( (Utils.path_to_id(self._package_name), self._module_name) )

   
    #-------------------------------------------------------------------------
    def _empty_module(self):
        '''
        Sets the HTML code for stating that this module contains no definition
        or even nothing at all.
        '''
        if len( self._parsed_module.module_content ) == 0:
            return Utils.html_indent( self._indent_level+1,
                                      '<p class="modules-comments"><i>This is an empty module.</i></p>\n' )
        else:
            return Utils.html_indent( self._indent_level+1,
                                      '<p class="modules-comments"><i>This module contains no class ' +  \
                                      'and no function definitions, no data and no import declarations.</i></p>\n' )

   
    #-------------------------------------------------------------------------
    def _get_module_footer_code(self):
        '''
        Evaluates HTML code for the footer of the module documentation.
        
        Returns:
            The HTML code, embedded in a string, related to this module.
        '''
        my_html_code = Utils.html_indent( self._indent_level+1,
                                          '<p>back to package <a class="package_end" href="#{:s}">{:s}</a></p>\n'.format( Utils.path_to_id( self._package_path ),
                                                                                                                  self._package_path                      ) )
        my_html_code += Utils.html_indent(self._indent_level,
                                          '</div> <!-- end of module {:s} -->\n\n'.format( self.get_html_id() ) )

        return my_html_code


    #-------------------------------------------------------------------------
    def _get_module_header_code(self):
        '''
        Evaluates HTML code for the header of the module documentation.
        
        Returns:
            The header HTML code, embedded in a string, related to this module.
        '''
        #self._root_package_name = Utils.replace_backslash( self._package_path )
        self._root_package_name = Utils.replace_backslash( self._package_name )
        
        my_html_code  = Utils.html_indent(self._indent_level,
                                          '<div class="module_container" id="{:s}">\n'.format( Utils.path_to_id(self.get_html_id()) ) )
        my_html_code += Utils.html_indent(self._indent_level+1,
                                          '<p class="module_def">module <b>{:s}</b></p>\n\n'.format( self._module_name ) )
        
        return my_html_code
        

    #-------------------------------------------------------------------------
    def _insert_docstring(self):
        '''
        Inserts docstring for this module.
        '''
        my_html_code = Utils.html_indent( self._indent_level+1, '<pre>\n' )
        
        if self._parsed_module.docstring:
            try:
                my_html_code += Utils.html_indent( 1, self._parsed_module.docstring.strip() )
                #my_html_code += Utils.html_indent( 1, self._parsed_module.docstring.replace('<', '&lt;').replace('>', '&gt;').strip() )
            except:
                my_html_code += '<unknown error detected in docstring - maybe string encoding/decoding failure>'
        
        my_html_code += '</pre>\n'

        return my_html_code
    
    
    #-------------------------------------------------------------------------
    def _is_empty_module(self):
        '''
        Returns:
            True if this module contains no definition or is fully empty.
        '''
        if len( self._parsed_module.module_content ) == 0:
            return True
        if len( self._parsed_module.module_descr.assigns_list )   == 0 and  \
           len( self._parsed_module.module_descr.classes_dict )   == 0 and  \
           len( self._parsed_module.module_descr.functions_dict ) == 0 and  \
           len( self._parsed_module.module_descr.imports_list )   == 0 and  \
           len( self._parsed_module.docstring )                   == 0:
            return True

    
    #-------------------------------------------------------------------------
    def _list_assigns(self):
        '''
        Evaluates the HTML code for all the assignments defined in this module.
        
        Returns:
            The HTML code associated with the list of all assignments  defined
            in this module.
        '''
        K_MAX_LINES = Utils.K_MAX_ASSIGNS_LINES

        if len( self._parsed_module.module_descr.assigns_list ) == 0:
            return ''

        my_html_code  = Utils.html_indent( self._indent_level+1, '<div class="classes_list">\n' )
        my_html_code += Utils.html_indent( self._indent_level+2,
                                           '<p class="imports-def"><b>List of data</b> defined in module <b><span class="module-color">{:s}</span></b></p>\n'.format( self._module_name ) )
        my_html_code += Utils.html_indent( self._indent_level+2,
                                           '<pre class="modules-data-list">\n' )
        
        max_lineno = max( [assign_descr.assign_node.lineno for assign_descr in self._parsed_module.module_descr.assigns_list] )
        my_format_str    = "<i>line {:%d}</i> | {:s}\n" % len( str(max_lineno) )
        for assign_descr in self._parsed_module.module_descr.assigns_list:

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
                my_html_code += ' '*(len(my_format_str.format(my_start_line, ''))-5)  #Utils.html_indent( 1, ' '*(len(my_format_str.format(my_start_line, ''))-5) )
                my_html_code += Utils.html_indent( 1,
                                                   '... (<i>{:d} more line{:s}</i>)'.format( my_more_lines,
                                                                                             's' if my_more_lines > 1 else '' ) )
                
        my_html_code = my_html_code.rstrip()
        my_html_code += Utils.html_indent( self._indent_level+2, '</pre>\n' )
        my_html_code += Utils.html_indent( self._indent_level+1, '</div>\n\n' )
        
        return my_html_code


    #-------------------------------------------------------------------------
    def _list_classes(self):
        '''
        Evaluates the HTML code for all the classes defined in this module.
        
        Returns:
            The HTML code associated with the list of all classes  defined  in
            this module.
        '''
        if len( self._parsed_module.module_descr.classes_dict ) == 0:
            return ''

        my_html_code  = Utils.html_indent( self._indent_level+1, '<div class="classes_list">\n' )
        my_html_code += Utils.html_indent( self._indent_level+2,
                                           '<p class="imports-def"><b>List of classes</b> for module <b><span class="module-color">{:s}</span></b></p>\n'.format( self._module_name ) )
        my_html_code += Utils.html_indent( self._indent_level+2,
                                           '<p class="modules-names">\n' )
        
        for class_name in sorted( self._parsed_module.module_descr.classes_dict.keys() ):
            my_class_id = HtmlClass.get_class_id( self.get_html_id(), class_name )
            my_html_code += Utils.html_indent( self._indent_level+3,
                                               'class <a href="#{:s}">{:s}</a><br />\n'.format( my_class_id, class_name ) )

        my_html_code += Utils.html_indent( self._indent_level+2, '</p>\n' )
        my_html_code += Utils.html_indent( self._indent_level+1, '</div>\n\n' )
        
        return my_html_code


    #-------------------------------------------------------------------------
    def _list_functions(self):
        '''
        Evaluates the HTML code for all the functions defined at the  module
        level within this module.
        
        Returns:
            The HTML code associated with the list of all classes defined in
            this module.
        '''
        #---------------------------------------------------------------------
        def my_list_function(f_name, f_descr):
            my_html_function = HtmlFunction( self._parsed_module ,
                                             f_name              ,
                                             f_descr             ,
                                             self._indent_level+1  )
            return my_html_function.get_html_code()
        
        #---------------------------------------------------------------------
        if len( self._parsed_module.module_descr.functions_dict ) == 0:
            return ''

        my_html_code = ''
        
        for func_name, func_descr in sorted(self._parsed_module.module_descr.functions_dict.items()):
            if func_name.startswith('__') and func_name.endswith('__'):
                my_html_code += my_list_function( func_name, func_descr )

        for func_name, func_descr in sorted(self._parsed_module.module_descr.functions_dict.items()):
            if not func_name.startswith('_'):
                my_html_code += my_list_function( func_name, func_descr )

        for func_name, func_descr in sorted(self._parsed_module.module_descr.functions_dict.items()):
            try:
                if func_name.startswith('_') and not func_name.endswith('__'):
                    my_html_code += my_list_function( func_name, func_descr )
            except:
                pass

        return my_html_code

   
    #-------------------------------------------------------------------------
    def _list_imports(self):
        '''
        Evaluates HTML code for listing all the 'import' and 'from ... import'
        instructions inf this module
        '''
        if len( self._parsed_module.module_descr.imports_list ) == 0:
            if self._module_name == '__init__.py':
                return ''
            else:
                return Utils.html_indent( self._indent_level+1,
                                          '<p class="modules-comments"><i>no imports.</i></p>\n' )

        my_html_code =  Utils.html_indent( self._indent_level+1, '<div class="imports-list">\n' )
        my_html_code += Utils.html_indent( self._indent_level+2, '<p class="imports-def"><b>Imports</b></p>\n<pre>\n' )
            
        for import_descr in self._parsed_module.module_descr.imports_list:
            my_line_no = import_descr.import_node.lineno
            my_import_code = self._parsed_module.module_lines[my_line_no-1].lstrip()
            my_colored_keywords = [ 'from ', 'import ', ' as ']
            for kw in my_colored_keywords:
                my_import_code = my_import_code.replace( kw, '<span class="keyword">{:s}</span>'.format(kw) )
            my_html_code += Utils.html_indent( self._indent_level, '{:s}\n'.format(my_import_code) )
            
        
        my_html_code += Utils.html_indent( self._indent_level+2, '</pre>\n' )
        my_html_code += Utils.html_indent( self._indent_level+1, '</div>\n' )
            
        return my_html_code

   
    #-------------------------------------------------------------------------
    def _parse_module(self):
        '''
        Parses this module.
        
        Returns:
            The overall structure of the parsed module, with information on:
              - classes definitions, and associated docstring;
              - functions and methods definitions, and associated docstring;
              - list of imports;
              - and maybe list of attributes.
        '''
        return ModuleParser( self._package_path, self._module_name )

#=====   end of module   html_module.py   =====#
        