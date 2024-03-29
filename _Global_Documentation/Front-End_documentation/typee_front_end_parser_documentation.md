# Typee Front-End Parser Documentation

This document is part of the Open Source project **Typee**. As such, it is
delivered under the MIT license:
```
Copyright (c) 2018-2021 Philippe Schmouker, Typee project, http://www.typee.ovh

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


This document describes the **Parser** part of the Front-End of the **Typee**
translator. We first explain the role of this **Parser**. Then, we describe
the whole data structure: input, output and internal ones. In a third section,
we describe all the modules that constitute this **Parser**, as programmed in
_Python_. The last section of this document presents the way detected errors 
are processed by the **Parser**.


## 1. Role of the Parser

![Front-End and Parser figure](../Picts/front-end-parser.png)

The Front-End **Parser** of the **Typee** translator acts exactly as a 
compiler parser would. It takes as input a list of tokens provided by the 
Front-End **Scanner** and parses this list of tokens to:
- detect syntaxic errors;
- generate a high-level intermediate code (I.C.) for the input of the 
Front-End **Elaborator**.

The generated I.C. is named _syntaxic intermediate code_.


### 1.1 Syntax analysis

The Parser runs through the linear _tokenized intermediate code_ generated by 
the Front-End **Scanner** and checks for the validity of this code according 
to the **Typee** grammar rules.

We explain in section 3 how the syntax of the _tokenized intermediate code_ is 
validated. But for now, let's just say that it compares the read token with 
the expected one according to the grammar rule that is currently applied. 
Notice: the _tokenized intermediate code_ is an exact, internal, 
representation of the source code that is parsed.


## 1.2 Generation of the _syntaxic intermediate code_

While running through the _tokenized intermediate code_ and verifying its 
correctness against **Typee** grammar rules, the **Parser** also generates a 
specific intermediate code, the _syntaxic intermediate code_, that will then 
be transmitted to the Front-End **Elabrator**.

The description of the _syntaxic intermediate code_ is provided in section 2.



## 2. Data Structure Description

The next two sub-sections below describe the data structures manipulated by
the Front-End **Parser** of the **Typee** translator.


### 2.1 Input Data Description

In this sub-section, we describe the processed data structure as generated by 
the Front-End **Scanner**.


#### 2.1.1 Tokens are issued from the **Scanner**

Remember, the **Scanner** scans a **Typee** source code module and provides a 
list of successive corresponding tokens. For instance, each time the
**Scanner** detects a ";" (i.e. end of instruction) in the source code, it
appends a related token data structure at the end of the list of previously 
generated tokens.

A description of all **Typee** valid tokens identifiers is available in file
[`src/FrontEnd/IntermediateCode/fe_icode_tokens.py`](../../src/FrontEnd/IntermediateCode/fe_icode_tokens.py) 
where a class is defined to be used as a namespace: `class FEICodeTokens`.


#### 2.1.2 Tokens and the _tokenized intermediate code_

Take a look to the Front-End 
[**Scanner** description document](typee_front_end_scanner_sw_documentation.md) 
to see how tokens are constructed by the **Scanner** when evaluated, and how 
all the associated mechanisms interact together. In this document are 
described the way new tokens can be specified and added to the **Typee** 
translator when **Typee** grammatical syntax evolves.

Ok, from these token identifiers, the **Scanner** generates _Intermediate Code 
Nodes_ that are appended one after the other by the **Scanner** into a **list 
of token nodes**, in the exact order of the tokens creation. This list is the 
_tokenized intermediate code_ that is generated by the **Scanner** and that is 
provided as input to the **Parser**.


#### 2.1.3 Implementation of Tokens - Python classes

##### class FEICodeTokenNode

Those token nodes are described by class `FEICodeTokenNode`. They own four 
data attributes:
- `tk_ident` is the identifier of the related token;
- `tk_data` is the data asociated with the token (most often, this is the
string as read by the scanned **Typee** module);
- `tk_num_line` is the line number in the module where this token has been
evaluated, as long as this information is available at Node creation time;
- `tk_num_coln` is the column number in the module line where this token 
has been evaluated, as long as this information is available at Node creation 
time.

The equality operator is redefined in this class (see _Python_ function 
`**eq**()`) as well as are properties to qualify the token (for instance, 
property `is_WHILE` is True when the token evaluates as instruction "while" 
in the scanned **Typee** module.

##### class FEICodeTokenNodeProtection

If you take a look to source file 
[`src/FrontEnd/IntermediateCode/fe_icode_token_node.py`](../../src/FrontEnd/IntermediateCode/fe_icode_token_node.py), 
you will see the definition of sub-class `class FEICodeTokenNodeProtection` 
which is dedicated to access protection tokens (i.e. `public`, `protected` and 
`hidden` - the last one standing in **Typee** for `private` in many other 
object oriented languages.

This sub-class gets an additional specific attribute, `tk_protection`. This 
one describes the access protection associated with those specific tokens. 
Trust us, there is a really good reason for this attribute to be added there.

##### All other classes - token ID related

Finally, in source file
[```src/FrontEnd/IntermediateCode/fe_icode_token_node.py```](../../src/FrontEnd/IntermediateCode/fe_icode_token_node.py),
one dedicated class is specified for each token type. They inherit either from 
class `FEICodeTokenNode` or from class `FEICodeTokenNodeProtection`. For 
instance:
- `class ICTokenNode_ABSTRACT` is the class for all token nodes associated
with token "abstract";
- `ICTokenNode_ALL` is the class for all tokens nodes associated with token 
"all";
- ...
- `ICTokenNode_WITH` is the class for all tokens nodes associated with token 
"with".


#### 2.1.4 Caution - file `fe_icode_token_node.py` gets automated generation

Please notice, as stated elsewhere, that file
[`src/FrontEnd/IntermediateCode/fe_icode_token_node.py`](../../src/FrontEnd/IntermediateCode/fe_icode_token_node.py) 
is generated with the help of a dedicated tool and that, as such, it should 
not be modified by hand. Hand-made modifications would be lost on the next run 
of this dedicated tool. Any modification to be implemented in this _Python_ 
module **has to be done** right in the code of the dedicated tool. For more 
information, have a look to document 
[`src/_Global_Documentation/typee_front_end_scanner_sw_documentation.md`](typee_front_end_scanner_sw_documentation.md).



### 2.2 Output Data Description

In this sub-section, we describe the data structure generated by the Front-End 
**Parser** and transferred for input data to the final pipeline stage of the 
Front-End: the **Elaborator**.


#### 2.2.1 _Syntaxic Intermediate Code_ structure

The _SIC_ (for _syntaxic intermediate code_, sic!) is structured as a tree. In 
algorithm programming, a tree gets a root which links to children nodes via 
branches. Each node may link also to other nodes, in which case they are 
internal nodes, or may be an ending node, branching to no other child node, in 
which case it is named a leaf.


##### Tokens and Statements

The _tokenized intermediate code_ is a linear list of token nodes - see above 
section. The **Parser** parses this I.C. and checks for the correctness of the 
succession of tokens, according to the grammar rules that define **Typee** 
language. So, as we explain it below (in next section 3.), the **Parser** can 
get when it is starting to parse a new statement.

The root rule of **Typee** language reads this way:
```
<code file> ::= <statements list> <ENDOFFILE>

```
with `<statements list>` specified as:
```
<statements list> ::= <empty statement> <statements list>
                   |  <compound statement> <statements list>
                   |  <simple statement> <statements list>
                   |  <statements block> <statements list>
                   |  EPS
```
and with `<statements block>` recursively specified  as:
```
<statements block> ::= '{' <statements list> '}' | ...
```

Each time the **Parser** starts parsing grammar rule `<statements list>`, it 
appends a new **_statement node**_to the _syntaxic tree_, (i.e. the tree that 
contains the _syntaxic intermediate code_). The structure of a **_statement 
node**_ is described in next subsection.



#### 2.2.2 Syntaxic Nodes structure



## 3. Parser Processing Description

_<small intro>_


### 3.1 ...


### 3.X Errors Processing Description






## 4. _Python_ Modules Description

_<small intro>_




## Annex - This document revisions history

| Date  | Rev.  | Author(s)  | Comments  |
|---|---|---|---|
| 2018-07-19 | 0.0.1  | Schmouk | Very first creation |
| 2018-07-20 | 0.0.2 | Schmouk | Numbered sections and sub-sections; added copyright and license texts; written section "1. Role of..."; augmented few sub-sections |
| 2018-07-21 | 0.0.3 | Schmouk | Completed sub-section 2.1 "Input Data Description" |
| 2018-08-15 | 0.0.4 | Schmouk | Corrected section 1.; corrected and augmented section 2.1; inverted sections 3. and 4. |
|  |  |  |  |
