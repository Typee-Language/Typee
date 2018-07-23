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

from directory       import DirectoryTree
from css_code        import myDoc_css_code
from html_package    import HtmlPackage


#=============================================================================
class HtmlGenerator:
    """
    This is the generator of the HTML documentation.
    """
    # Versions:
    #    0.0.1 - 2016-06-23 - schmoukerp - Creation.
    
    #-------------------------------------------------------------------------
    def __init__(self, root_dirpath='.', doc_title=None):
        '''
        Constructor.
        
        Automatically initializes its attribute 'doc_text' which contains
        the whole HTML code related to the documentation.
        Saves this HTML code into file '<root_dirpath>_myDoc.html', or in
        file 'pyYadc.html' if root_dirpath is '.'.
        
        Args:
            root_dirpath: str
                The directory path of the software to be documented. Defaults
                to the current working directory.
            doc_title: str
                The title of this documentation.  May be None,  in which case
                no title is added to the document.
        '''
        self.doc_text = ""
        self._set_header( doc_title )
        self._set_body( root_dirpath )
        self._set_footer()
        self._save_documentation( root_dirpath )
    
    #-------------------------------------------------------------------------
    def _set_header(self, doc_title=None):
        '''
        Sets the header of this HTML documentation.
        
        Args:
            doc_title: str
                The title of this documentation. May be None, in which case
                no title is added to the document.
        '''
        self.doc_text = "{:s}{}{:s}{:s}{:s}".format( '<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n',
                                                     '  <title>' + str(doc_title) + '</title>\n' if doc_title else ''       ,
                                                     '  <style media="screen" type="text/css">\n'                           ,
                                                     myDoc_css_code                                                         ,
                                                     '  </style>\n</head>\n'                                                  )
  
     
    #-------------------------------------------------------------------------
    def _set_body(self, root_dirpath):
        '''
        Sets the body of this HTML documentation.
        '''
        self.doc_text += "<body>\n"
        
        # evaluates the html_package structure on disk and loops over packages
        for package_descr in DirectoryTree( root_dirpath ).packages_structure:
            self.doc_text += HtmlPackage( package_descr ).get_html_code()
            

    #-------------------------------------------------------------------------
    def _set_footer(self):
        '''
        Closes the description of this HTML documentation.
        '''
        self.doc_text += "</body>\n</html>\n"

    
    #-------------------------------------------------------------------------
    def _save_documentation(self, root_dirpath):
        '''
        Finally, saves the documentation HTML code into file.
        
        Raises:
            OSError, IOError:
                File could not be opened, created or written.
        '''
        try:
            my_root = root_dirpath or '.'
            my_package_name = os.path.basename( my_root )
            ##my_filepath = '{:s}/{:s}_myDoc.html'.format( my_root, root_dirpath if root_dirpath and root_dirpath != '.' else '' )
            my_filepath = '{:s}/{:s}doc.html'.format( my_root, my_package_name+'_' if my_package_name and my_package_name != '.' else '' )
            with open( my_filepath, 'w' ) as fp:
                fp.write( self.doc_text )
        except Exception as e:
            print( "Unable to save documentation into file '{}' because of error '{}'".format( my_filepath, str(e) ) )
            raise e

#=====   end of module   html_generator.py  =====#
