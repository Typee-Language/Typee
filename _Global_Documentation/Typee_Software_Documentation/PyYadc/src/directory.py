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
import os


#=============================================================================
class DirectoryDescr:
    """
    Descriptors of directories contain:
        - the name of or the path to this directory
        - the list of sub-directories
        - the list of contained files (without '.' and '..')
    """
    #-------------------------------------------------------------------------
    def __init__(self, main_root, root, dirs, files):
        '''
        Constructor.
        
        Args:
            main_root: str or bytes
                A string or a bytes containing the name of the full path to
                the overall root directory that is currently scanned.
            root: str or bytes
                A string or a bytes containing the name or the full path to
                this directory.
            dirs: list of (str or bytes)
                A reference to a list containing all sub-directories of this
                directory.
            files: list of (str or bytes)
                A reference to a list containing all files present  in  this
                directory.
        '''
        self.main_root = main_root
        self.root      = root
        self.dirs      = dirs
        self.files     = files

    #-------------------------------------------------------------------------
    def is_package(self):
        '''
        Returns:
            True if this directory is a Python html_package, and False else.
        '''
        if '__init__.py' in self.files:
            # checks for the 'package' status of parent directories
            my_base_dirs = self.root.split( self.main_root )[1].strip( os.sep ).split( os.sep )
            
            try:
                my_path = self.main_root
                for dir_ in my_base_dirs[:-1]:
                    my_path = os.path.join( my_path, dir_ )
                    if '__init__.py' not in os.listdir( my_path ):
                        return False
            
                return True
            
            except:
                # we are at the very first level of the directory tree
                return '__init__.py' in self.files

        else:
            return False
    

#=============================================================================
class DirectoryTree:
    """
    Description of a whole directories tree.
    """
    #-------------------------------------------------------------------------
    def __init__(self, root_dirpath='.'):
        '''
        Constructor.
        
        Args:
            root_dirparth: str
                The root directory path to be walked through.
                Defaults to '.' .
            
        Raises:
            TypeError:
                Type of root_dirpath is not string or byte.
            OSError, IOError:
                Some I/O error occurred,  maybe because  root
                directory was not found or for any OS reason.
        '''
        self.root_dirpath       = root_dirpath
        self.dir_structure      = self.__get_directories_structure( root_dirpath )
        self.packages_structure = self.get_packages_and_modules()

    #-------------------------------------------------------------------------
    def get_packages_and_modules(self, root_dirpath=None):
        '''
        Evaluates the directory structure.
        
        Args:
            root_dirparth: str
                The root directory path to be walked  through.
                If None, the root_dirpath used at construction
                time is used. Defaults to None.
        
        Returns:
            A  list  of  directories  descriptors  with   only
            packages and modules.
            
        Raises:
            TypeError:
                Type of root_dirpath is not str or byte.
            OSError, IOError:
                Some I/O error occurred,  maybe  because  root
                directory was not found or for any OS reason.
        '''
        my_list = []

        #---------------------------------------------------------------------
        def my_evaluate_package_and_module( dir_descr ):
            if dir_descr.is_package():
                my_packages = [ pathname for pathname in dir_descr.dirs if DirectoryDescr(self.root_dirpath,
                                                                                          dir_descr.root,
                                                                                          None,
                                                                                          os.listdir(dir_descr.root + '/' + pathname)).is_package() ]
                my_modules  = [f for f in dir_descr.files if f.endswith('.py')]
                my_list.append( DirectoryDescr(self.root_dirpath, dir_descr.root, my_packages, my_modules) )

        #---------------------------------------------------------------------
        if root_dirpath:
            for root, dirs, files in os.walk(root_dirpath):
                my_evaluate_package_and_module( DirectoryDescr(self.root_dirpath, root, dirs, files) )
        else:
            for dir_descr in self.dir_structure:
                my_evaluate_package_and_module( dir_descr )
            
        return my_list
    
    #-------------------------------------------------------------------------
    def __get_directories_structure(self, root_dirpath='.'):
        '''
        Evaluates the whole directory structure.
        
        Args:
            root_dirpath: str
                The root directory path to be walked through.
                Defaults to current working directory.
        
        Returns:
            A list of directories  descriptors  -  see  class
            DirectoryDescr in this same module.
            
        Raises:
            TypeError:
                Type of root_dirpath is not str or byte.
            OSError, IOError:
                Some I/O error occurred,  maybe because  root
                directory was not found or for any OS reason.
        '''
        return [ DirectoryDescr( self.root_dirpath, root, dirs, files ) for root, dirs, files in os.walk(root_dirpath) ]
    
#=====   end of module  directory.py  =====#
