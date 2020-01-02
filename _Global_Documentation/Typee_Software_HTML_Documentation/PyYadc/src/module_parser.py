#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2016-2020 Philippe Schmouker, PyYadc project, https://github.com/schmouk/PyYadc

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
import ast
from os.path import join as os_path_join


#=============================================================================
class AssignDescr:
    """
    Description of ast.Assign nodes as being parsed.
    """
    #-------------------------------------------------------------------------
    def __init__(self, ast_node):
        '''
        Constructor.
        
        Once instantiated, this class offers access to attributes:
          - self.assign_def, of class ast.Assign.
        
        Args:
            ast_node: ast.FunctionDef
                A reference to the currently parsed node with ast. Within 
                current class, this is a ast.Assign instance.
        '''
        self.assign_node = ast_node

#=============================================================================
class ClassDescr:
    """
    Description of an ast.ClassDef node as being parsed.
    """
    #-------------------------------------------------------------------------
    def __init__(self, ast_node):
        '''
        Constructor.
        
        Once instantiated, this class offers access to attributes:

          - self.class_node, of class ast.ClassDef;
          - self.docstring, the associated doc string.
        
        Args:
            ast_node: ast.ClassDef
                A reference to the currently parsed node with ast.
                Within  current  class,  this  is  an ast.ClassDef 
                instance.
        '''
        self.class_node = ast_node
        self.docstring  = ast.get_docstring( ast_node, clean=False )


#=============================================================================
class FunctionDescr:
    """
    Description of an ast.FunctionDef node as being parsed.
    """
    #-------------------------------------------------------------------------
    def __init__(self, ast_node):
        '''
        Constructor.
        
        Once instantiated, this class offers access to attributes:
          - self.function_def, of class ast.FunctionDef;
          - self.docstring, the associated doc string.
        
        Args:
            ast_node: ast.FunctionDef
                A reference to the currently parsed node with ast. Within 
                current class, this is a ast.FunctionDef instance.
        '''
        self.function_node = ast_node
        self.docstring     = ast.get_docstring( ast_node, clean=False )


#=============================================================================
class ImportDescr:
    """
    Description of ast.Import and ast.ImportFrom nodes as being parsed.
    """
    #-------------------------------------------------------------------------
    def __init__(self, ast_node):
        '''
        Constructor.
        
        Once instantiated, this class offers access to attributes:
          - self.import_def, of class ast.Import or ast.ImportFrom.
        
        Args:
            ast_node: ast.FunctionDef
                A reference to the currently parsed node with ast. Within 
                current class, this is a ast.FunctionDef instance.
        '''
        self.import_node = ast_node


#=============================================================================
class ModuleDescr:
    """
    Description of a parsed Python module.
    """
    #-------------------------------------------------------------------------
    def __init__(self):
        '''Constructor.'''
        self.assigns_list   = list()
        self.classes_dict   = dict()
        self.functions_dict = dict()
        self.imports_list   = list()

    #-------------------------------------------------------------------------
    def add_new_assign(self, class_name, ast_node):
        '''
        Adds a new assignment descriptor either to the module description
        or to some class definition.
                
        Args:
            class_name: str
                The name of the currently parsed class, or None if this
                function definition is to be associated with a module.
            ast_node: ast.Assign
                A reference to the currently parsed node with ast.
        '''
        if class_name:
            self.classes_dict[class_name]['assigns_descrs'].append( AssignDescr(ast_node) )
        else:
            self.assigns_list.append( AssignDescr(ast_node) )
        pass
            
    #-------------------------------------------------------------------------
    def add_new_class(self, ast_node):
        '''
        Adds a new class descriptor to the module description.
                
        Args:
            ast_node: ast.ClassDef
                A reference to the currently parsed node with ast. Within 
                current class, this is an ast.ClassDef instance.
        '''
        self.classes_dict[ ast_node.name ] = { 'class_descr'     : ClassDescr( ast_node ),
                                               'functions_descrs': dict()                ,
                                               'assigns_descrs'  : list()                  }
        pass

    #-------------------------------------------------------------------------
    def add_new_function(self, class_name, ast_node):
        '''
        Adds a new function descriptor either to the module description
        or to some class definition.
                
        Args:
            class_name: str
                The name of the currently parsed class, or None if this
                function definition is to be associated with a module.
            ast_node: ast.FunctionDef
                A reference to the currently parsed node with ast.
        '''
        if class_name:
            self.classes_dict[class_name]['functions_descrs'][ast_node.name] = FunctionDescr( ast_node )
        else:
            self.functions_dict[ast_node.name] = FunctionDescr( ast_node )
        pass
        
    #-------------------------------------------------------------------------
    def add_new_import(self, ast_node):
        '''
        Adds a new 'import' or 'from ... import'  to the module description.
        
        Args:
            ast_node: ast.Import of ast.ImportFrom
                A reference to the currently parsed node with ast.
        '''
        self.imports_list.append( ImportDescr(ast_node) )
        pass
            

#=============================================================================
class ModuleParser( ast.NodeVisitor ):
    """
    Definition of the parsing of Python modules.
    """
    #-------------------------------------------------------------------------
    def __init__(self, package_path, module_name):
        '''
        Constructor.
        
        Args:
            package_path: str
                the path to the embedding package.
            module_name: str
                the name of this embedded module.
        '''
        super(ModuleParser, self).__init__()
   
        # gets the module Python content
        with open( os_path_join(package_path, module_name), 'r' ) as fp:
            self.module_content = fp.read()
        
        # evaluates corresponding lines
        self.module_lines = self.module_content.split( '\n' )
        
        # parses it
        self.module_node = ast.parse( self.module_content )
        self.docstring   = ast.get_docstring( self.module_node )
        
        # prepares internal descriptive structure
        self.module_descr = ModuleDescr()
        self.module_name  = module_name
        
        # and visits the ast tree
        self.visit( self.module_node )
        
    #-------------------------------------------------------------------------
    def visit_Assign(self, ast_node):
        '''
        Actions to be taken when parsing an assignment definition at the
        module level.
        
        Args:
            ast_node: ast.AST or any inheriting Node class
                A reference to the currently parsed not with ast.
        '''
        self.module_descr.add_new_assign( None, ast_node )

    #-------------------------------------------------------------------------
    def visit_ClassDef(self, ast_node):
        '''
        Actions to be taken when parsing a class definition.
        
        Args:
            ast_node: ast.ClassDef
                A reference to the currently parsed not with ast.
        '''
        #---------------------------------------------------------------------
        def my_internal_visit(class_name, node):
            if isinstance( node, ast.FunctionDef ):
                self.module_descr.add_new_function( class_name, node )
            elif isinstance( node, ast.Assign ):
                self.module_descr.add_new_assign( class_name, node )

        #---------------------------------------------------------------------
        my_class_name = ast_node.name
        self.module_descr.add_new_class( ast_node )
        
        for _field, value in ast.iter_fields(ast_node):
            if isinstance(value, list):
                for item in value:
                    my_internal_visit( my_class_name, item )
            
            elif isinstance( value, ast.FunctionDef ):
                my_internal_visit( my_class_name, value )
   
    #-------------------------------------------------------------------------
    def visit_FunctionDef(self, ast_node):
        '''
        Actions to be taken when parsing a function definition.
        
        Args:
            ast_node: ast.FucntionDef
                A reference to the currently parsed not with ast.
        '''
        self.module_descr.add_new_function( None, ast_node )
        #self.generic_visit( ast_node )

    #-------------------------------------------------------------------------
    def visit_If(self, ast_node):
        '''
        Checks for the 'if __name__ == "__main__"' instruction of scripts.
        Once detected, stops the down-tree parsing of this module.
        '''
        # well, we do not have to parse 'if' statements.
        # So, let's stop the tree visits right now!
        pass
   
    #-------------------------------------------------------------------------
    def visit_Import(self, ast_node):
        '''
        Actions to be taken when parsing an 'import' declaration.
        
        Args:
            ast_node: ast.Import
                A reference to the currently parsed not with ast.
        '''
        self.module_descr.add_new_import( ast_node )
   
    #-------------------------------------------------------------------------
    def visit_ImportFrom(self, ast_node):
        '''
        Actions to be taken when parsing an 'from ... import' declaration.
        
        Args:
            ast_node: ast.ImportFrom
                A reference to the currently parsed not with ast.
        '''
        self.module_descr.add_new_import( ast_node )
    
#=====   end of module   module_parser.py  =====#
