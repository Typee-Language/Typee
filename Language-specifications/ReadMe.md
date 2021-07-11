# Typee Language Specifications

All successive versions of the specification of Typee language grammar are 
put here.


## Versionning

### Since 2021

The Typee language grammar is specified according to the formal, unambiguous 
and easy to read PEG format (stands for *Processing Expression Grammar*).

Processing Expression Grammars have been first specified by Bryan Ford (MIT)
by 2004 in his famous paper "Parsing Expression Grammars: A Recognition-Based 
Syntactic Foundation". This article has been published at the POPL’04 
conference that had been  held by January 14–16, 2004 at Venice, Italy. Its a 
copyrighted document of ACM with number 1-58113-729-X/04/0001 and it can be 
easily found on the Net.

So, now on, all versions of Typee grammar specifications are numbered and 
named as `typee_sppecs_PEG_v<XX>.grm`, where `<XX>` belongs in 
interval 01 up to 99.


### Before 2021

Notice that Typee language wass specified with a formal, unambiguous, LL(1) 
grammar.

The very first version of these specifications is not numbered. See file 
`typee_specs_LL1.grm`.

Next versions are all numbered: `...-v2.grm`, `...-v3.grm`, ..., 
`...-v9.grm` and currently `...-v10.grm` as the very last version of 
document.

You'll notice that version `v4` is missing. Unfortunately, it has been lost 
before being stored here.

Since version `v8`, a second version of the specifications is 
provided: from `...-v8-EBNF.grm` to `...-v10-EBNF.grm`. 



## Specification format

### Since 2021

The used syntax to describe the grammar rules is the original PEG one. So, 
we use notations `<-` and `/` for instance, while newer papers use `::=` 
or `|` instead as it is usual in CFGs (*Context Free Grammars*, which what 
LL(1) grammars are).

Notice that we use notation '##' as the starting point for comments, while
Bryan Floyd was using '#' in his original paper. This is a commodity we use 
to get colored syntax in Notepad++. Notioce also that Comments are one line 
comments only in the very first description of PEG grammars. The PEG
specification of **Typee** conforms to this.

We strongly encourage the reader to get access to the initial article from 
Bryan Ford. Section 2 of this paper fully explains the syntax of PEGrammars:
"*Parsing Expression Grammars: A Recognition-Based Syntactic Foundation*",
ACM 1-58113-729-X/04/0001, POPL’04, January 14–16, 2004, Venice, Italy. It
can easily be accessed on Internet with these references. We shall not copy 
here anything from it without permission.


### Before 2021

#### Formal classical description - LL(1)

The used syntax to describe the grammar rules is very classical.
Rules are named between angle brackets: `<rule name>`. Those names may 
be appended with single quote(s), to functionnaly group together different
strongly related rules.

The derivation rules of a grammar rule are specified after the rule name, 
separated from this name by operator `::=`.

Literals are specified between single as well as double quotes: `'for'`,
`"'"`. Escaped chars in literals are preceded by an anti-slash: `'\''` is 
equivalent to `"'"`, `'\n'` stands for newline, `'\\'` stands for single 
anti-slash.

When defining literals, sets of characters are defined between brackets: 
`[' ', '\n', '\f', '\r', '\t']` specifies the set of all spacing characters.

When defining literals, the ellipsis define an interval of characters 
specified by the starting and the ending character: 

    <hexadecimal digit> ::= ['0'...'9', 'a'...'f', 'A'...'F']`

When defining literals, characters may be specified by their unicode code:
`u0x0041` stands for character 'A'.

When defining literals, groups of characters may be excluded from an interval 
of characters with operator `-`:

    <any non newline char> ::= u0x0000...u0xFFFF - ['\n', '\r', '\f']

The vertical bar `|` is used to specify options between derivations rules:

    <boolean> ::= <TRUE>  | <FALSE>
    <TRUE>    ::= 'true'  | 'True'
    <FALSE>   ::= 'false' | 'False'

This "option" vertical bar separates groups of rules. There is no need to 
group together successive rule names between parenthesis. Next specifications 
are unambiguous:

    <single string>  ::= "'" <single string'> "'"
                      |  '"' <single string"> '"'

    <single string'> ::= <any escaped char> <single string'>
                      |  <any string quote char> <single string'>
                      |  EPS

    <single string"> ::= <any escaped char> <single string">
                      |  <any string doublequote char> <single string">
                      |  EPS

Finally, keyword `EPS` specifies the empty (epsilon) rule. It specifies that 
this rule may be not derived. In the above rules, it states that empty strings 
formed as `''` or `""` are legal in Typee.


#### Extended Backus-Naur Form (EBNF) description

This is a simplified and more easy to read format for grammar rules 
specifications. We have been providing them since version `v8` of Typee 
language grammar specification. Please notice that we still use the 
classical format description of Typee grammar to implement the Front-End 
Scanner and Parser modules.

The EBNF format accepts every classical description rules as listed in above 
section. It adds factoring separators which help reduce the number of 
derivation rules to specify a grammar rule.


Parenthesis `( )` are used to group grammar rules together:

    <identifier>  ::= ( <alpha char> | '_' ) <identifier'>
    <identifier'> ::= ( <alpha num char> | '_' ) <identifier'>

Here, an identifier is specified as starting with either an alphabetical 
character, i.e. any character from group `['A'...'Z', 'a'...'z']`, or with an
underscore, i.e. `'_'`, preceding any series of alphanumerical character and 
undercores, i.e. any character from group `['0'...'9', 'A'...'Z', 'a'...'z', '_']`.

Parenthesis are also used jointly with an ending character star `'*'`. There, 
they mean that the derivations rules that they group together may be derived 
from 0 to many times (with no limitations):

    <identifier> ::= ( <alpha char> | '_' ) ( <alpha num char> | '_' )*

You can get here that this kind of factorization helps easing the reading of 
grammars specifications as well as it helps reducing their specifications 
sizes.


Brackets `[ ]` are used to specify that some group of derivation rules may be 
derived at most once - which means that they may also not be derived. This 
helps avoiding the use of keyword `EPS`:

    <octal number> ::= '0' <octal char> ( ['_'] <octal char> )*
    <octal char>   ::= '0'...'7' 

Here, octal numbers are specified as starting with character `'0'`, containing 
then suites of any number of octal characters, i.e. characters from interval 
`['0'...'7']`, maybe separated with single underscores. It specifies that in 
Typee, `00` or `01_23_45_67` are legal octal numbers while `0123__4567` is not.



## Syntax Coloring

When reading a `.grm` file on Windows, we recommend you to use Notepad++. We 
have created a dedicated profile file accessible here:
[grammars.xml](../Notepad%2B%2BXML-configs/), 
that you just have to put in the same directory as executable file 
`notepad++.exe` on your computer. You will then enjoy syntax coloring when 
opening `.grm` files with Notepad++ (but with a few limitations when reading 
EBNF versions of those files - "no one is perfect").
