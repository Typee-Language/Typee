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
time, when the Front-End Parser is on specification_).



## 2. Data Structure Description

_<small intro>_


### 2.1 Input Data

In this sub-section, we describe the processed data structure as provided by 
the Front-End __Scanner__ for Input data to the Front-End Parser.


### 2.2 Output Data

In this sub-section, we describe the generated data structure as provided by 
the Front-End __Parser__ for Input data to the final pipeline stage of the 
Front-End, the __Elaborator__.


### 2.3 Internal Data

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
|  |  |  |  |
