# Typee Front-End Parser Documentation

This document is part of the Open Source project __Typee__. As such, it is
delivered under the MIT license:
```
Copyright (c) 2018 Philippe Schmouker, Typee project, http://www.typee.ovh

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
```


This document describes the __Parser__ part of the Front-End of the __Typee__
translator. We first explain the role of this __Parser__. Then, we describe
the whole data structure: input, output and internal ones. In a third section,
we describe all the modules that constitute this __Parser__, as programmed in
_Python_. The last section of this document presents the way detected errors 
are processed by the __Parser__.


## 1. Role of the Parser

The Front-End __Parser__ of the __Typee__ translator acts exactly as a 
compiler parser would. It takes as input a list of tokens provided by the 
Front-End __Scanner__ and parses this list of tokens to:
- detect syntaxic errors;
- evaluate types of variables and expressions;
- check types inconsistencies or errors;
- generate a high-level intermediate code for the input of the Front-End 
__Elaborator__.

All of these tasks are combined into a multi-steps process:
1. a first step analyzes the tokens list to check the syntaxic correction of
the currently parsed __Typee__ module;
2. a second step evaluates types of expressions and variables;
3. a third step checks for the consistency and the correctness of types
usage along the parsed module;
4. a final, fourth step, preparesz the final intermediate code to pass it as
input to the __Elaborator__ of the __Typee__ Front-End.

(_Notice to contributors: the above description is subject to changes over
time, when the Front-End Parser is under specification_).



## 2. Data Structure Description

The next three sub-sections below describe the data structures manipulated by
the Front-End __Parser__ of the __Typee__ translator.


### 2.1 Input Data Description

In this sub-section, we describe the processed data structure as provided by 
the Front-End __Scanner__ for Input data to the Front-End Parser.

Remember: the __Scanner__ scans a __Typee__ source code module and provides a 
list of successive corresponding tokens. For instance, each time the
__Scanner__ detects a ";" (i.e. end of instruction) in the source code, it
appends a related token data structure at the end of the list of previously 
generated tokens.

A description of all __Typee__ valid tokens identifiers is available in file
```src/FrontEnd/IntermediateCode/fe_icode_tokens.py``` where a class is
defined to be used as a namespace: ```class FEICodeTokens```.

Take a look to the Front-End __Scanner__ description document to see how 
tokens are constructed by the __Scanner__ when evaluated, and how all the 
associated mechanisms interact together. There are described the way new 
tokens can be specified and added to the __Typee__ translator when 
__Typee__ grammatical syntax evolves.

Ok, from these token identifiers, the __Scanner__ generates 
_Intermediate Code Nodes_ that are appended one after the other by the 
__Scanner__ into a __list of token nodes__, in the exact order of the tokens 
creation.

Those nodes are described by ```class FEICodeTokenNode```. They own four data
attributes:
- ```tk_ident``` is the identifier of the related token;
- ```tk_data``` is the data asociated with the token (most often, this is the
string as read in the scanned __Typee__ module);
- ```tk_num_line``` is the line number in the module where this token has been
evaluated, as long as this information is available at Node creation time;
- ```tk_num_coln``` is the column number in the module line where this token 
has been evaluated, as long as this information is available at Node creation 
time.

The equality operator is redefined in this class (see function ```__eq__()```)
as well as are properties to qualify the token (for instance, property 
```is_WHILE``` is True when the token evaluates as instruction "while" in the 
scanned __Typee__ module.

If you take a look to source file 
```src/FrontEnd/IntermediateCode/fe_icode_token_node.py```, you will see the
definition of a sub-class: ```class FEICodeTokenNodeProtection``` which is
dedicated to access protection tokens (i.e. ```public```, ```protected``` and
```hidden``` - the last one standing in __Typee__ for _private_ in many other
object oriented languages.

This sub-class gets an additional specific attribute, ```tk_protection```. 
This one describes the access protection associated with those specific 
tokens. Trust us, there is a really good reason for this attribute to be added 
there.

Finally, in source file
```src/FrontEnd/IntermediateCode/fe_icode_token_node.py```, one dedicated
class is specified for each token type. They inherit either from class 
```FEICodeTokenNode``` or from class ```FEICodeTokenNodeProtection```. For 
instance:
- ```class ICTokenNode_ABSTRACT``` is the class for all token nodes associated
with token "abstract";
- ```ICTokenNode_ALL``` is the class for all tokens nodes associated with
token "all";
- ...
- ```ICTokenNode_WITH``` is the class for all tokens nodes associated with
token... "with".

Please notice, as stated elsewhere, that file
```src/FrontEnd/IntermediateCode/fe_icode_token_node.py``` is generated with 
the help of a dedicated tool and that, as such, it should not be modified by 
hand since modifications would be lost on the next run of this dedicated tool. 
Any modification to be implemented in this _Python_ module __has to be done__ 
right in the code of the dedicated tool. For more information, have a look to
document 
```src/_Global_Documentation/typee_front_end_scanner_documentation.md```.



### 2.2 Output Data Description

In this sub-section, we describe the generated data structure as provided by 
the Front-End __Parser__ for Input data to the final pipeline stage of the 
Front-End, the __Elaborator__.


### 2.3 Internal Data Description

In this sub-section, we describe all the internal data structures used by the
Front-End __Parser__ for its internal processing along its internal pipeline.




## 3. _Python_ Modules Description

_<small intro>_


### 3.1 First step - Syntaxic Errors Checking


### 3.2 Second step - Types Evaluation


### 3.3 Third step - Types Usage Correctness Checking


### 3.4 Fourth Step - Final Intermediate Code Generation




## 4. Errors Processing Description

_<small intro>_




## Annex - This document revisions history

| Date  | Rev.  | Author(s)  | Comments  |
|---|---|---|---|
| 2018-07-19 | 0.0.1  | Schmouk  | Very first creation |
| 2018-07-20 | 0.0.2 | Schmouk | Numbered sections and sub-sections; added copyright and license texts; written section "1. Role of..."; augmented few sub-sections |
| 2018-07-21 | 0.0.3 | Schmouk | Completed sub-section 2.1 "Input Data Description" |
|  |  |  |  |
