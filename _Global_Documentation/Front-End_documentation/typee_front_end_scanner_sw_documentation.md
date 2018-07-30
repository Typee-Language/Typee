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


This document describes the __Scanner__ part of the Front-End of the __Typee__
translator. We first explain the role of this __Scanner__. Then, we describe
all the modules that constitute this __Scanner__, as programmed in _Python_. 
The last section of this document presents the way detected errors are 
processed by the __Scanner__.


## 1. Role of the Scanner

### 1.1 Typee language grammar

__Typee__ grammar (or language) specification is documented in documents
prefixed with `typee_specs_LL1`. They are suffixed with file type `.grm`. They 
are versionned with `-v` and a number put just after `LL1` in their file name. 
The first version of the grammar specification gets no version numbering in 
its name. By July 2018, the last version of __Typee__ grammar specification is 
version v8.

The `.grm` suffix is used to get colored syntax with Notepad++ (sorry, for sole 
Windows users). The associated language rules for Notepad++ and their coloring 
are defined in file 
[`Notepad++XML-configs/grammars.xml`](../Notepad++XML-configs/grammars.xml). 
See  document [`notepad-readme.md`](../notepad-readme.md) directly available at 
the root of __Typee__ repository, to get an understanding of how to use this 
.xml file. It is very easy and Windows programmers are strongly recommended to 
use it and Notepad++.

Once you take a look to the __Typee__ grammar specification, you will get that 
it is an _LL(1)_ grammar. What is this, you might be asking. Just have a look 
to this formal (but clear) definition of LL(1) grammars just here:
[`http://www.csd.uwo.ca/~moreno/CS447/Lectures/Syntax.html/node14.html`](`http://www.csd.uwo.ca/~moreno/CS447/Lectures/Syntax.html/node14.html).
Such grammars have the immense double advantage to be __not ambiguous__ and
__not left-recursive__. They are then easy to define, easy to validate and
moreover are very intuitive to implement. Do not hesitate to search for more
information on the Web for LL(1) (and LL(_k_) grammars).

Since __Typee__ is defined with an LL(1) grammar, it is an LL(1) language.

So, then the Front-End __Scanner__ of the __Typee__ translator acts exactly as 
a compiler scanner would. It takes as input a __Typee__ module source code 
and provides as output a list of tokens for the usage of the Front-End 
__Parser__. For this, the __Scanner__ stage of the __Typee__ Front-End 
pipeline:
- scans a __Typee__ module source code;
- detects tokens in the source code;
- appends all of them to a single list for each scanned __Typee__ module;
- generates a high-level intermediate code for the input of the Front-End 
__Parser__.

Notice that this is the __first stage__ of the Front-End pipeline. It is the
__first step__ that is processed when translating __Typee__ source code in any
other available programming language (e.g. C++11, Java 8, Python 3.6, ...)

The manipulated data are of two kinds:
- as input, a __Typee__ source code;
- as output, a _list_ of Token Nodes, appended in the order of their scanning,
that is fully described in document
[```src/_Global_Documentation/typee_front_end_scanner_data_structure_documentation.md```](typee_front_end_scanner_data_structure_documentation.md).



## 2. _Python_ Modules Description

This section describes the software architecture of the __Typee__ Front-End
__Scanner__.

A first _Python_ module implements the __Scanner__ itself. Associated with 
this are imported modules that describe the data structures and their
manipulations.

__Notice__: scanners dedicated to LL(1) languages, which __Typee__ language 
is, are most often implemented as being _table driven_: _table of actions_
describes all actions to take place according to currently scanned character 
in the scanned source code. Such tables may be huge and are always sparsed. 
Their implementation is then difficult to read and errors and bugs are 
difficult to fix. Meanwhile, such implementations are very effective for low 
time processing.

As long as we are implementing a first version 0.0 of __Typee__ translator, 
we have decided to __not__ implement a _table-driven_ scanner. The alternative 
is then to implement a `while` loop with many `if` and `elif` branchings. This 
is not as time effective as a _table-driven_ implementation but:
- it is more memory-cost effective and
- it is far easier to read and to maintain.

Remember, the first implementation of the __Typee__ translator is considered 
as being a __proof of concept__ (a _POC_ ) and as such its implementation aims 
at being simple, easy to read, easy to maintain and provable (well, as much as 
it can be for this last feature).


### 2.1 _Python_ module src/FrontEnd/Scanner/fe_scanner.py

This __Scanner__ module implements the _tokenization_ of __Typee__ source 
code. It defines (as extracted from the _Python_ source code) this class:

```python
    class FEScanner:
        """
        This is the class of the Typhon Front-End Scanner.
        It is the very first stage of the front-end pipeline of  the  Typhon
        compiler.
        It scans Typhon source code and produces tokenized Intermediate Code
        that will be parsed by the Typhon Front-End Parser.
        """
```

The `while` loop implementing the scanning can be found in there.


#### 2.1.1 The Scanning Interface

The scanning of __Typee__ source code is done within memory. It is uploaded 
as a whole in memory and it is then scanned.

Method ```scan_memory()``` takes as input arguments a string, the one which 
contains the whole source code to be scanned, and maybe scan arguments that 
are currently unused but which are yet present for possible future use. It 
generates as its result a list of token nodes.

```python
    def scan_memory(self, src_code:str, **parse_args) -> FEIntermediateCode:
        '''
        Scans the source code,  according to some parsing arguments  passed  at
        command line, and returns a reference to the corresponding intermediate
        code.
        
        Args:
            src_code: str
                A string containing the source code to be scanned.
            parse_args: dict
                keyword arguments that contain the parsing arguments 
                as passed at the global command.  Please notice that
                this argument is present here for future use.
        
        Returns:
            A reference to the generated Front-End Intermediate Code.
        '''
```

Method `scan_file()` is also provided to ease the parsing of __Typee__
source code from module files. it takes as input argument the path to the 
module to be scanned and maybe scan arguments that are currently unused but 
which are yet present for possible future use. It generates as its result a 
list of token nodes.

```python
    def scan_file(self, filepath:str, **parse_args) -> FEIntermediateCode:
        '''
        Runs the Typhon scanner on a specified file.
        
        Args:
            filepath: str
                The path to the file to be scanned.
            parse_args: dict
                keyword arguments  that contain the parsing arguments as 
                passed at the global command line.
        
        Returns:
            A reference to the corresponding front-end intermediate code.
        
        Raises:
            IOError: source file not found or unavailable for reading.
        '''
```

        
#### 2.1.2 The internal _tokenization_

This is the core of the __Scanner__ module. __Typee__ source code is scanned
along the way and tokens are detected. These can be built-in instruction 
names (such as __for__, __while__, __if__ for instance), numbers, names (of 
functions, classes, methods or variables), operators (e.g. __=__, __==__, 
__>__, __>=__, etc.), single line or multiple lines strings or comments.

Private method `_tokenize()` checks for the next scanned character in the
__Typee__ source code and internally calls the corresponding private method.
For this purpose, tokens are classified among:
- \_SIMPLE_TOKEN
- \_COMPOUND_TOKEN
- \_ NAME_ALPHA_CHARS
- \_ NUM_CHARS
- \_ ENDLINE
- \_ SPACE
- and single or double quotes

Anything else is condisered to be \_UNEXPECTED and is not rejected but 
processed as an unexpected token. This is a sepcial type of Token Node which
is appended to the tokens series in the Intermediate Code list.

According to their detected classification, the scanned tokens are processed
by the related private method, as being called by the _tokenizer_.


#### 2.1.3 Tokens processing

In the _Python_ module 
[`src/FrontEnd/Scanner/fe_scanner.py`](../src/FrontEnd/Scanner/fe_scanner.py), 
next to method `tokenize()` is a list of private methods that are internally 
called and which are not part of the __Scanner__ interface. These are listed 
in alphabetical order from `_binary_number()` to `_string_quote()`. Each of 
them is specialized in simple tasks for the scanning of their related tokens.

Next to this list is another list of private methods, listed in alphabetical
order from `_arobase()` to `star()`. They are dedicated to those characters 
that are valid operators in __Typee__ and which may be completed with either 
other same character or with the sign `=`. For instance: `+`, `++` and `+=`.

Notice that operators that can be augmented with a `=` sign are called
__augmented operators__. A dedicated private method is available for their
processing, which contains factorized code: `_check_augmented_operator()`.


#### 2.1.4 Internal scanner processing

The next (and last) list of private methods in the __Scanner__ module lists in
alphabetical order all the methods that are used for the internal functionning 
of the _Scanner_.

These are from `_append_node()` to `_skip_space()`. Their roles are the 
skipping of characters, keywords, or new lines, the reading of next character 
in the scanned __Typee__ source code, the checking for characters or keywords, 
and of course, for the appending of newly scanned tokens into the list of 
scanned tokens.

Two properties are available also, next after this list:
- `_current` gives a direct access to the currently scanned character in
the scanned __Typee__ source code;
- `_eof` returns ```True``` as soon as the whole source code has been scanned. 


#### 2.1.5 Finally

The _Python_ module [`src/FrontEnd/Scanner/fe_scanner.py`](../src/FrontEnd/Scanner/fe_scanner.py) 
imports two other _Python_ modules.

The first one, 
[`src/FrontEnd/IntermediateCode/fe_icode_token_node.py`](src/FrontEnd/IntermediateCode/fe_icode_token_node.py),
describes the data structure and the manipulation of token nodes, i.e. those
nodes that are appended to the list of the tokenized internmediate code.

The second one, 
[`src/FrontEnd/IntermediateCode/fe_intermediate_code.py`](../src/FrontEnd/IntermediateCode/fe_intermediate_code.py),
describes the data structure of the intermediate code that is used interrnally 
in the __Typee__ Front-End operations.

We shortly describe those two imported modules in the next two sub-sections.


### 2.2 Tokens Specification

__Typee__ tokens are specified according to __Typee__ grammar specification. 
The successive versions of __Typee__ language (or grammar) specification can 
be found in dedicated directory 
[`Language-specifications/`](../Language-specifications) right at the root of
__Typee__ repository - i.e. at the same level than directory [`src`](..).


#### 2.2.2 Typee language tokens

So, from the LL(1) specification of the __Typee__ grammar, we easily 
evaluate all the tokens definitions of this language. For instance, the
operator `+` is a token, as well as operators `-`, `*`, `/`, etc. Keywords 
such as `abstract` or `with` are tokens, as well as usual instructions in 
programming languages are also: `for`, `if`, `while`, `else`, `try`, etc. 
Numbers, scalars, strings are also tokens, as are names (of variables, of 
classes, of functions, of methods, of attributes, etc.) Strings and comments, 
on a single line or on multiple lines, are tokens too. Finally, some specific 
characters are tokens also: parenthesis, brackets, braces, dots, new-lines, 
semi-colon, and even end-of-file.

All the defined tokens in __Typee__ LL(1) grammar are listed in the _Python_
module 
[`src/FrontEnd/IntermediateCode/fe_icode_tokens.py`](../src/FrontEnd/IntermediateCode/fe_icode_tokens.py).
In this module, we define two classes. The first one, `FEICodeTokens`, 
contains class constants which are the identifiers associated with each token. 
The second class, `FEICodeTokensData`, contains default data to be associated 
with __Typee__ tokens. This default data is set by default with instatiated 
tokens, to be further used when comparing tokens.


#### 2.2.3 Tokens identifiers implementation

The __Typee__ tokens identifiers are set in class `FEICodeTokens`. Do not get 
confused by the way this is implemented. Each constant gets, at  first sight, 
a same constant value: ```0```.

Moreover, a class attribute is defined next after the identifiers constants 
declarations. This is `_TOKEN_NAMES` and it is a _Python_ dictionary. In 
__Typee__ we would call this a __map__. It is an associated array which 
associates values to keys, just as would a dictionnary which associates 
definitions with words. Here again, do not get confused by the way it is 
implemented, since it is __not__ initialized yet on declaration.

Finally, a class method, `token_name()` is defined, which takes as input a 
token identifier and which returs as a result the token name associated with
this token identifier.

The way all of this stuff is initialized is inherent to _Python_ modules
parsing. Next after the definition of class `FEICodeTokens`, there are 
four lines of code. The first one initalizes a constant at the module level:

```python
    _OFFSET = 1000  # 1000 here is an arbitrary default value - do not change it...
```

The three next ones do __all__ the intialization of the above data in class
`FEICodeTokens`. They use _Python_ built-in goodies for this purpose:

```python
    for tk_id, tk_nm in enumerate( [ tk for tk in FEICodeTokens.__dict__ if tk[:3] == 'TK_' ] ):
        setattr( FEICodeTokens, tk_nm, tk_id + _OFFSET )
        FEICodeTokens._TOKEN_NAMES[ tk_id + _OFFSET ] = tk_nm
```

The thing to be noticed is that those lines are processed every time the
_Python_ module 
[`src/FrontEnd/IntermediateCode/fe_icode_tokens.py`](../src/FrontEnd/IntermediateCode/fe_icode_tokens.py)
is imported by another _Python_ module. This way, the constant value of each 
token identifier is automatically set and the adding of any new token, due to
any enhancement, modification or augmentation of __Typee__ language grammar is
then straightforward.

If a new token is added to the language specification, we just have to add a
constant class identifier by the end of their list, just before this line:

```python
    ##--- Add new tokens JUST BEFORE this line ---##
```

in the _Python_ module. Just verify that the token identifier has not already
been defined and assign it with 0. Things will then get automatically and 
correctly set without any other human operation.


#### 2.2.4 Tokens names automated associations with identifiers

In the same _Python_ module
[`src/FrontEnd/IntermediateCode/fe_icode_tokens.py`](../src/FrontEnd/IntermediateCode/fe_icode_tokens.py), 
a second class is implemented, `class FEICodeTokensData`.

This class defines a private attribute ``data`. This is a _Python_ dictionary 
(you know, what we would call a __map__ in __Typee__) . These private data 
associate a string with every __Typee__ token identifier.

Notice that this private data associates default string (or None if default 
strings are not applicable) to tokens identifiers values. Moreover, this data 
is generated at the time of the module import.

Class method `get()` returns the defaut associated string with the passed
token identifier.


#### 2.2.5 CAUTION - there is a Typee internal related tool

At any time _Python_ module
[`src/FrontEnd/IntermediateCode/fe_icode_tokens.py`](../src/FrontEnd/IntermediateCode/fe_icode_tokens.py) 
is modified, in any way it is, a specialized tool __has to be manually run__. 
This process is not yet automated, but should be when further developments 
will have taken place.

In directory [`src/local_tools`](../src/local_tools), few tools and templates 
are defined. Every time module 
[`src/FrontEnd/IntermediateCode/fe_icode_tokens.py`](../src/FrontEnd/IntermediateCode/fe_icode_tokens.py) 
is modified, the local tool script
[`src/local_tools/tool_generate_feicode_token_node_module.py`](../src/local_tools/tool_generate_feicode_token_node_module.py) 
__has to be run__ - either in console window with command line or from within 
developement framework (remember, Eclipse with PyDev plug-in is the recommended one).

This script generates _Python_ module 
[`src/FrontEnd/IntermediateCode/fe_icode_token_node.py`](../src/FrontEnd/IntermediateCode/fe_icode_token_node.py)
in a (semi-) automated way. We discuss this automatly generated module in 
next sub-section.


### 2.3 Token Node data structure

Token Nodes are the elementary data structures that is generated by the Front-
End __Scanner__. They describe each token evaluated from the __Typee__ source
code that has been scanned.

This data structure is described in _Python_ module file 
[`src/FrontEnd/IntermediateCode/fe_icode_token_node.py`](../src/FrontEnd/IntermediateCode/fe_icode_token_node.py)
by the next two classes:

```python
    class FEICodeTokenNode:
        """
        The class of nodes for the Front End Intermediate Code of the Typee Scanner.
        """    
```

and

```python
    class FEICodeTokenNodeProtection( FEICodeTokenNode ):
        """
        The class of nodes describing protection modes for the Front End 
        Intermediate Code Token Nodes of the Typee Scanner.
        """
```


#### 2.3.1 Token Nodes Attributes

Each Token Node basically owns four attributes:
- tk_ident: this is the Front-End internal identifier for the evaluated token;
- tk_data: the data associated with this token - mainly, the string that has
evaluated as this token;
- num_line: the line number in the scanned __Typee__ module where this token 
has been evaluated;
- num_coln: the column index in this line where the token has been evaluated.

Moreover, Protection Token Nodes have an additional attribute:
- tk_protection: an enumerated value corresponding to the evaluated protection
mode - i.e. 'public', 'protected' or 'hidden', the last one standing in
__Typee__ for 'private' as generaly used in other programming languages.

Notice that this attribute __cannot__ be checked for base class 
`FEICodeTokenNode` since this attribute is not defined in the base class. So, 
only check for it when you are sure to test on instances of class
`FEIcodeTokenNodeProtection`.


#### 2.3.2 Token Nodes Operators and Methods

Every Token Node can be compared for equality with any other Token Node. This
is implemented with operator wrapper method `__eq__()` as usual with _Python_ 
programming. Equality is said to be `True` when tokens identifiers 
(`tk_ident`) and tokens data (`tk_data`) compare the same.

Furthermore, each Token Node defines many properties to easily check of what 
kind they are. These properties are listed in class `FEICodeTokenNode`, in
alphabetical order from `is_ABSTRACT` to `is_WITH`. Those properties are set 
to `True` when the token identifier (`tk_ident`) equals the identifier of the 
checked kind of token.


#### 2.3.3 Token Nodes Classes for every kind of Token

Finally, in _Python_ module 
[`src/FrontEnd/IntermediateCode/fe_icode_token_node.py`](../src/FrontEnd/IntermediateCode/fe_icode_token_node.py), 
a class is defined for each of the tokens kinds. These classes are listed in 
alphabetical order, from `ICTokenNode_ABSTRACT` for token associated with 
__Typee__keyword __abstract__ to `ICTokenNode_WITH` for token associated with
__Typee__ keyword __with__.


#### 2.3.4 CAUTION - Token Nodes Classes description is AUTOMATED

This is very important to notice. The _Python_ module
[`src/FrontEnd/IntermediateCode/fe_icode_token_node.py`](../src/FrontEnd/IntermediateCode/fe_icode_token_node.py)
contains a specific mention just after the legal copyrigth and license text. 
Here is a copy of it:

```python
    #=============================================================================
    ## THIS FILE HAS BEEN AUTOMATICALLY GENERATED BY Typee FRAMEWORK.
    ## DO NOT MODIFY IT: ANY MODIFICATION WOULD BE LOST ON NEXT USE.
```

See sub-section 2.2.5 above for some more information.



### 2.4 Tokenized Intermediate Code data structure 

Currently, there is only __one__ definition of Front-End Intermediate Code
data structure. It is defined in _Python_ module
[`src/FrontEnd/IntermediateCode/fe_intermediate_code.py`](../src/FrontEnd/IntermediateCode/fe_intermediate_code.py).

In this _Python_ module, we define only one type, `FEIntermediateCode`, which 
is a wrapper to _Python_ built-in type ```list```. In _Python_, lists are 
_containers_ that can embed any kind of object type. This means that such a 
definition of Intermediate Code allows for the implementation in a single 
_Python_ instruction of a simple type of container embedding many different 
types of Token Nodes.

In the case of the Front-End __Scanner__, the contained token nodes are all of
class `FEIcodeTokenNode` or of its inheriting sub-class 
`FEICodeTokenNodeProtection` and this is the types of token nodes that the
evaluated Intermediate Code is returned by the Front-End __Scanner__ for input 
to the Front-End __Parser__.



## 3. Errors Processing Description

The __Typee__ __Scanner__ detects errors every time some token is badly
formed. For instance, something like _125abc_ is __neither__ a correct number 
__nor__ a valid identifier in __Typee__. A valid number would have been
_0x125abc_ and a valid identifier would habe been _\_125abc_.

So, every time token errors are detected by the Front-End __Scanner__, a 
specific Token Node is appended to the Intermediate Code list. This is a 
Token Node of type `ICTokenNode_UNEXPECTED`.

Unexpected Token Nodes are appended to the list of token nodes at the exact 
place where the erroneous token has been detected, with line number and column 
index set into the attributes of the node and most of the time with the 
corresponding erroneous string set in attribute `tk_data`.

This is the only processing of _tokenization_ errors that are held by the
Front-End __Scanner__. Such errors are passed to the Front-End __Parser__, via
the Intermediate Code list of Token Nodes, for the __Parser__ to be informed 
of some badly formed token.

The Front-End __Scanner__ does not print or log any error message. The 
printing or the logging of this kind of errors is delayed after the last stage 
of the Front-End __Parser__, once any other syntaxic or types errors have been 
detected. This way, all detected errors can be printed or logged in the order 
of the line numbers they are appearing within the translated __Typee__ 
module.



## Annex - This document revisions history

| Date  | Rev.  | Author(s)  | Comments  |
|---|---|---|---|
| 2018-07-22 | 0.0.1 | Kerm | Very first creation. Errors processing still to be documented |
| 2018-07-23 | 0.0.2 | Schmouk | Minor typo corrections, a few text addings. |
| 2018-07-23 | 0.0.3 | Kerm | Completed section 3. Errors Processing |
| 2018-07-23 | 1.0 | Kerm | This document is now considered as being validated |
| 2018-07-25 | 1.0.1 | Schmouk | Added links to documents (and this was a long journey over this document text), some complementary explanations; enhanced code specification (added Python spec to code); moved sub-section about __Typee__ grammar specification upward from tokens-related section to introduction section. |
| 2018-07-25 | 1.0.2 | Schmouk | Corrected a few mispelled links. |
|  |  |  |  |
