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

#-------------------------------------------------------------------------
'''This is the CSS3 code associated with pyYadc documentation files.'''
myDoc_css_code = '''<!-- pyYadc CSS description -->
body {
    font-family: calibri, arial, helvetica, tahoma, sans-serif;
}

pre {
    font-size: 0.75em;  //0.85em;  //0.95em;
    color    : #141528;
    font-family: "Courier New";
}

.dir_struct {
    border-color : #000000;
    border-radius: 8px 8px 0px 0px;
    border-style : solid;
    border-width : 2px;
}

.package_container {
    font-family  : calibri, arial, helvetica, tahoma, "Courier New", sans-serif;
    border-color : #A4091D;
    border-radius: 10px 10px 0px 0px;
    border-style : solid;
    border-width : 6px;
    margin       : 6px;
    margin-bottom: 60px;
    padding      : 5px;
}

.package_def {
    font-family: calibri, arial, helvetica, tahoma, "Courier New", sans-serif;
    font-size  : 1.30em; //1.45em;
    color      : #A4091D;
    padding    : 1px 8px 4px 4px;
    background-color: #F2F2F2; //#FFF2F2;
    border-color : #ED5656;
    border-width : 3px 0px 0px 0px;
    border-style : solid;
}

.package_end {
    font-family: calibri, arial, helvetica, tahoma, "Courier New", sans-serif;
    font-size  : 0.90em; //1.0em;
    color      : #A4091D;
}

a .package_def {
    color: #A4091D;
}

a .package_end {
    color: #A4091D;
}

.packages-list {
    color        : #141528;
    font-size    : 1.0em; //1.10em;
    border-color : #A4091D;
    border-radius: 5px 5px 0px 0px;
    border-style : solid;
    border-width : 2px;
    margin       : 6px;
    margin-bottom: 20px;
    padding      : 5px;
}

.packages-names {
    color        : #141528;
    font-size    : 1.0em; //1.10em;
    margin       : 6px 6px 35px 20px;
    margin-bottom: 20px;
    padding      : 5px 5px 5px 15px;
    line-height  : 165%;
}

.module_container {
    border-color : #13269C;
    border-radius: 6px 6px 0px 0px;
    border-style : solid;
    border-width : 3px;
    //box-shadow   : 4px 4px 3px;
    padding      : 5px;
    margin-bottom: 40px;
    color: #091DF4;
}

.module_def {
    font-family: calibri, arial, helvetica, tahoma, "Courier New", sans-serif;
    font-size  : 1.12em; //1.25em;
    color      : #13269C;
    padding    : 4px 16px 4px 8px;
    background-color: #F2F2F2; //#CCF1FF;
    border-color : #8697FF;
    border-width : 3px 0px 0px 0px;
    border-style : solid;
}

.module_end {
    font-family: calibri, arial, helvetica, tahoma, "Courier New", sans-serif;
    font-size  : 0.90em; //1.0em;
    color      : #13269C;
    font-weight: bold;
}

.modules-list {
    color        : #141528;
    font-size    : 0.97em; //1.08em;
    border-color : #141528;
    border-radius: 5px 5px 0px 0px;
    border-style : solid;
    border-width : 2px;
    //margin       : 6px;
    margin-bottom: 40px;
    padding      : 5px;
}

.modules-data-list {
    color        : #141528;
    font-size    : 0.75em; //1.08em;
}

.modules-names {
    color        : #141528;
    font-size    : 0.97em; //1.08em;
    margin       : 6px 6px 20px 20px;
    padding      : 5px 5px 5px 15px;
    line-height  : 165%;
}

.modules-comments {
    color        : #141528;
    font-size    : 0.97em; //1.08em;
    margin       : 6px 6px 20px 20px;
    padding      : 5px 5px 5px 15px;
}

.imports-list {
    color        : #141528;
    font-size    : 1.05em; //0.95em; //1.04em;
    border-color : #141528;
    border-radius: 4px 4px 0px 0px;
    border-style : solid;
    border-width : 1px;
    margin       : 6px;
    margin-bottom: 8px;
    padding      : 4px;
}

.imports-def {
    color        : #141528;
    font-size    : 1.00em; //0.97em; //1.08em;
    font-style   : bold;
    background-color: #F2F2F2;
    padding      : 2px 2px 2px 6px;
    border-color : #A9A9A9;
    border-width : 3px 0px 0px 0px;
    border-style : solid;
}

.class_container {
    border-color : #091DF4;
    border-radius: 5px 5px 0px 0px;
    border-style : solid;
    border-width : 2px;
    padding      : 4px;
    margin       : 6px;
    margin-bottom: 16px;
}

.class_def {
    font-family: calibri, arial, helvetica, tahoma, "Courier New", sans-serif;
    font-size  : 1.05em; //1.15em;
    padding    : 4px 16px 4px 8px;
    margin-left: 4px;
    background-color: #F2F2F2;
    border-color    : #AEAEFC;
    border-width    : 3px 0px 0px 0px;
    border-style : solid;
}

.class_end {
    font-family: calibri, arial, helvetica, tahoma, "Courier New", sans-serif;
    font-size  : 0.90em; //1.0em;
    color      : blue;  //#13269C;
    font-weight: bold;
}

.classes_list {
    color        : #141528;
    font-size    : 1.05em; //1.15em;
    border-color : #141528;
    border-radius: 4px 4px 0px 0px;
    border-style : solid;
    border-width : 1px;
    margin       : 6px;
    margin-bottom: 8px;
    padding      : 4px;
}

.class_decorators {
    font-family: calibri, arial, helvetica, tahoma, "Courier New", sans-serif;
    font-size  : 0.90em; //1.10em;
    background-color: #F2F2F2;
}

.function_div {
    font-family     : calibri, arial, helvetica, tahoma, sans-serif;
    font-size       : 0.95em; //1.05em;
    padding         : 4px 16px 4px 8px;
    margin-left     : 12px;
    margin-right    : 12px;
    background-color: #F2F2F2;
    border-color    : #AEAEFC;
    border-width    : 1px 0px 0px 0px;
    border-style    : solid;
}

.function_def {
    font-family     : calibri, arial, helvetica, tahoma, sans-serif;
    font-size       : 0.95em; //1.05em;
    padding         : 4px 8px 4px 40px;
    text-indent     : -32px;
    //padding-left    : 32px;
    margin-left     : 12px;
    margin-right    : 12px;
    background-color: #F2F2F2;
    border-color    : #AEAEFC;
    border-width    : 1px 0px 0px 0px;
    border-style    : solid;
}

.function_decorators {
    //font-family: calibri, arial, helvetica, tahoma, sans-serif;
    font-size  : 0.85em; //1.00em;
}

.navy {
    color: navy;
}
.MediumBlue {
    color: MediumBlue;
}
.blue {
    color: blue;
}
.keyword {
    color: blue; // #13269C;
    //font-style: italic;
    font-weight: bold;
}
.module-color {
    color: #13269C;
}

.class-color {
    color : #13269C;
}

'''

#=====   end of module  css_code.py   =====#
