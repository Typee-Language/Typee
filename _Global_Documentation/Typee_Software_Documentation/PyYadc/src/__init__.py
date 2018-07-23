#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pyYadc stands for "Python - Yet Another Documentation Compiler".

This is an automated generator of HTML documentation.  It  provides  automatic 
formatting  of  documentation for Python packages.  Any available docstring is 
extracted and put as is near the documented items, i.e.:
  - modules (as contained in the package);
  - classes (as defined in each module);
  - functions (as defined in each module and in each
    class).

User is advised that when generating  documentation  for  Python 2  syntax,  a 
Python 2.x interpreter has  to be used while when generating documentation for 
Python 3 syntax, a Python 3.x interpreter should be used.

Usage:
The working directory is the directory which contains the Python package to be 
documented. Command is then:
$ python &lt;path_to_pyYadc_dir&gt;/pyYadc.py &lt;package_name&gt;

No options are currently available with this version 1.0.


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


from directory       import DirectoryDescr, DirectoryTree
from html_class      import HtmlClass
from html_function   import HtmlFunction
from html_generator  import HtmlGenerator
from html_module     import HtmlModule
from html_package    import HtmlPackage
from module_parser   import ModuleParser
from utils           import Utils