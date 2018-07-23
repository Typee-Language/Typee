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
import os.path

from directory   import DirectoryDescr
from html_module import HtmlModule
from utils       import Utils


#=============================================================================
class HtmlPackage:
    """
    All manipulation on packages content.
    """
    # Versions:
    #    0.0.1 - 2016-06-24 - schmoukerp - Creation.
    
    #-------------------------------------------------------------------------
    #def __init__(self, package_descr, root_package_name, html_indent_level=0):
    def __init__(self, package_descr, html_indent_level=0):
        '''
        Evaluates HTML code for the documentation of a  specified  package.
        Once  instantiated,  Package  objects  can  be applied their method
        get_html_code().
        
        Args:
            package_descr: DirectoryDescr
                A reference to the descriptor of this package  -  which  is 
                also a directory on disk.
            html_indent_level: int
                The level of indentation in the HTML code for this package.
                Defaults to 0.
        
        Raises:
            AssertError: the  passed  argument  'package_descr'  is not  an
                instance of class DirectoryDescr.
        '''
        assert isinstance( package_descr, DirectoryDescr )

        self._package_descr     = package_descr
        self._package_dirpath   = Utils.replace_backslash( package_descr.root )
        self._root_package_name = Utils.replace_backslash( os.path.basename(package_descr.root) )
        self._html_indent       = html_indent_level

    #-------------------------------------------------------------------------
    def get_html_code(self):
        '''
        Evaluates HTML code for the documentation of a specified package.
        
        Returns:
            The HTML code, embedded in a string, related to this package.
        '''

        my_html_code  = self._get_package_header_code()
        my_html_code += self._list_sub_packages()
        my_html_code += self._list_modules()
        
        for module_name in sorted( self._package_descr.files ):
            my_html_code += HtmlModule( self._package_dirpath  ,
                                        self._root_package_name, 
                                        module_name            , 
                                        self._html_indent+1      ).get_html_code()
        
        my_html_code += self._get_package_footer_code()
        
        return my_html_code
    
    #-------------------------------------------------------------------------
    def _get_package_footer_code(self):
        '''
        Evaluates HTML code for the footer of the package documentation.
        
        Returns:
            The HTML code, embedded in a string, related to this package.
        '''
        my_parent_package_path = os.path.dirname( self._package_dirpath )
        
        return Utils.html_indent(
                    self._html_indent+1,
                    ('<p class="package_end">end of package <b><a class="package_end" href="#{:s}">' +  \
                     '{:s}</a>{:s}&nbsp;<a class="package_end" href="#{:s}">{:s}</a></b></p>\n').format(
                        Utils.path_to_id( my_parent_package_path ),
                        my_parent_package_path                    ,
                        '/' if my_parent_package_path != '' else '',
                        Utils.path_to_id( self._package_dirpath ) ,
                        self._root_package_name                     )
               ) + \
               Utils.html_indent(
                   self._html_indent,
                   '</div> <!-- end of package container {:s} -->\n\n'.format( Utils.path_to_id( self._package_dirpath )  )
               )
    
    #-------------------------------------------------------------------------
    def _get_package_header_code(self):
        '''
        Evaluates HTML code for the header of the package documentation.
        
        Returns:
            The header HTML code, embedded in a string, related to this package.
        '''
        my_parent_package_path = os.path.dirname( self._package_dirpath )
        my_parent_package_id   = Utils.path_to_id( my_parent_package_path )
        
        my_html_code  = Utils.html_indent( self._html_indent,
                                           '<div class="package_container" id="{:s}">\n'.format( Utils.path_to_id(self._package_dirpath) ) )
        if my_parent_package_id == '':
            my_html_code += Utils.html_indent( self._html_indent+1,
                                               '<p class="package_def">package <b><span class="package_def">{:s}</span></b></p>\n\n'.format( 
                                                    self._root_package_name
                                               ) )
        else:
            my_html_code += Utils.html_indent( self._html_indent+1,
                                               '<p class="package_def">package <b><a class="package_def" href="#{:s}">{:s}</a><span class="package_def">{:s}{:s}</span></b></p>\n\n'.format( 
                                                    my_parent_package_id                       ,
                                                    my_parent_package_path                     ,
                                                    '/' if my_parent_package_path != '' else '',
                                                    self._root_package_name
                                               ) )
        
        return my_html_code
        
    #-------------------------------------------------------------------------
    def _list_sub_packages(self):
        '''
        Evaluates HTML code for the list of sub_packages contained within
        this package.
        
        Returns:
            The HTML code, embedded in a string, related to this package.
        '''
        my_html_code = ''
        
        if len(self._package_descr.dirs) > 0:
            # sub-packages are embedded in current package
            my_html_code += Utils.html_indent( self._html_indent+1, 
                                               '<div class="packages-list">\n' )
            my_html_code += Utils.html_indent( self._html_indent+2,
                                               '<p><b>List of sub-packages for package {:s}</b></p>\n'.format( self._package_dirpath ) )
            my_html_code += Utils.html_indent( self._html_indent+2,
                                               '<p class="packages-names">\n' )
            
            for sub_package_name in sorted( self._package_descr.dirs ):
                my_sub_package_name = '/'.join( (self._package_dirpath, sub_package_name) )
                my_html_code += Utils.html_indent( self._html_indent+3,
                                                   '<a href="#{:s}">{:s}</a><br />\n'.format( Utils.path_to_id(my_sub_package_name),
                                                                                              my_sub_package_name                    ) )
        
            my_html_code += Utils.html_indent( self._html_indent+2, '</p>\n' )
            my_html_code += Utils.html_indent( self._html_indent+1, '</div>\n\n' )
        
        return my_html_code
        
    
    #-------------------------------------------------------------------------
    def _list_modules(self):
        '''
        Evaluates HTML code for the list of modules contained within
        this package.

        Returns:
            The HTML code, embedded in a string, related to this package.
        '''
        if len(self._package_descr.files) == 0:
            return '  <p class="modules-comments"><i>this package contains no modules.</i></p>\n'
        
        my_html_code  = Utils.html_indent( self._html_indent+1,
                                           '<div class="modules-list">\n' )
        my_html_code += Utils.html_indent( self._html_indent+2,
                                           '<p><b>List of modules for package {:s}</b></p>\n'.format( self._root_package_name ) )
        my_html_code += Utils.html_indent( self._html_indent+2,
                                           '<p class="modules-names">\n' )
        
        for module_name in sorted( self._package_descr.files ):
            my_sub_module_name = HtmlModule( self._package_dirpath  ,
                                             self._root_package_name,
                                             module_name            ,
                                             self._html_indent+1      ).get_html_id()
            my_html_code += Utils.html_indent( self._html_indent+3,
                                               '<a href="#{:s}">{:s}</a><br />\n'.format( my_sub_module_name, module_name ) )

        my_html_code += Utils.html_indent( self._html_indent+2, '</p>\n' )
        my_html_code += Utils.html_indent( self._html_indent+1, '</div>\n\n' )
        
        return my_html_code

#=====   end of module   html_package.py  =====#
