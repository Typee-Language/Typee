# Programming Languages Translation - a State of the Art

This is a short __State of the Art__ document related to _Programming 
Languages Translation_.


# 1. Introduction

If one try to get the history of research work on programming languages 
tanslation, she will eventually go back to the early 60's. About sixty years 
ago... By those days, researchers were working on programming languages and 
their related compilers, about some formal way to define these languages then 
to implement their compilers.

So, we will first refer to those works that lead to the definition of 
metalanguages, metacompilers and metaprogramming. Since that, many papers and 
patents have been published and registererd. We list a part of them at Annex A 
(Bibliography and Patents) and we discuss those texts in next sections. We 
will then focus on the translation of source code into another source code, 
most work of this having been done in the 90's and up to 2010. Those 20 years 
have been relatively active about translation of programming source codes from 
one programming language to another one.


# 2. Metalanguage, Metaprogramming and Metacompilers

### 2.1 Signification of _meta_

In computering engineering (or in computering science), we are used to use the 
term __meta__ to specify either something that relates to itself or something 
that relates to its own category - for instance, __metadata__ are data that 
refer to or that describe other data.

But __meta__ may also be used for indicating some higher level of abstraction. 
For instance, in object oriented programming a __metaclass__ is a higher level 
of definition of a class. A metaclass is a class for which instances are 
classes.

Let's talk now about __metalanguage__, __metaprogramming__ and 
__metacompilers__.


### 2.2 Metalanguage

As for a metaclass about classes, a metalanguage is a higher level of 
abstraction that helps specifying the properties of other languages. In 1959, 
John W. Backus specified a formal metalanguage[1] that he previously used to 
describe the syntax of some new language, IAL, later renamed ALGOL 58. This 
metalanguage took the name __BNF__ for _Backus normal form_. Peter Naur having 
contributed to the specification of ALGOL 60, the next version of programming 
language ALGOL, Donald E.Knuth later proposed to rename __BNF__ to 
___Backus-Naur Form___, since BNF was not a true normal form and since Peter 
Naur had proposed some useful changes to the metalanguage descrition. This 
last name, Backus-Naur Form, is still used today for BNF.

As a _metalanguage_, __BNF__ describes only the syntax of a language not its 
semantic. BNF is then said to be a _weak_ metalanguage. 


### 2.3 Metaprogramming

__Metaprogramming__ consists in writing a computer program that processes 
other programs as its data. The _metaprogram_ can so read, analyse, transform 
or generate other programs by its own. It can also modify itself at run-time. 

Meanwhile, this concept aims at doing processing at compile-time rather than 
at run-time. It should lead to better time performance since those 
computations are done once, at compile-time, rather than each time at 
run-time.

The metaprogram is written in a metalanguage. It processes programs that are 
written in what is named an _object language_. You may now get the idea that 
a programming language could be its own metalanguage, i.e. the object language 
is the programming language itself. This ability is named _reflexivity_.

So, what's metacompiling?


### 2.4 Metacompilers

Ok, a compiler compiles a programming language into binary code, targeting a 
specified processor, most often for a targeted environment (e.g. an Operating 
System).

A __metacompiler__ is a software application that constructs compilers, 
interpreters or translators for other programming languages. It is a 
metaprogram that is either written in its own metalanguage or written in an 
existing programming language.
- It takes as input a metaprogram;
- It provides as output an executable object program.

The input metaprogram of a metacompiler is coded with a specialized 
metalanguage. We mean, as of a Java compiler that compiles programs written 
in Java, a metacompiler compiles programs written in a metalanguage.


### 2.5 What's up now?

So, what's up with all of this? Once John W. Backus (1924-2007) had specified 
__BNF__ as a metalanguage to describe programming languages, and to specify 
ALGOL 58, people started to use it for other projects.

In 1962, Robert S. Ledley and James B. Wilson proposed a method for the 
automated translation of programming language through syntactical analysis[2].

We may say that the first true works on metacompilers started in 1963, when 
Howard Metcalfe designed a compiler-writing interpreter[3] using the method 
proposed in [2] the year before. He was working in a group that was involved 
in _syntax driven compilers_. Remember, BNF is well suited for syntax rules
definition.

Up to '65, defined languages seemed to be of the from LL(_k_). Languages 
defined with a BNF are context-free languages that are read from left to right 
and for wich derivation of rules executed on the left of the rules. These are 
grammars that are easy to read for humans, that are easy to program and to 
debug also. often, _k_ values to __1__ and states the number of non-read 
symbols that need to be anticipated to evaluate the rule to be derived. In 
1965, Donald E. Knuth proposed in [4] a new approach for deriving rules. In 
this paper, he defined LR(_k_) grammars and proposed algorithms to decide if 
a language programming grammar satisfies le LR(_k_) conditions. __LR__ stands 
for Left-to-write read languages and Right derivation of rules, with _k_ again 
the number of non-read symbols needed to evaluate the derivation. 
Right-derivation means that the evaluation of applied rules starts from the 
leaves of the grammar, up to the root.


### 2.6 Conclusion

From there, many programming languages (as well the very well known and 
largely used ones as the many more confidential ones) have been specified with 
the __BNF__ concept. The related compilers and interpeters have been designed 
according to the nature of the programming languages they were implementing: 
LL(_k_) or LR(_k_). For instance, Python syntax is presented in its online 
documentation with an LL(1) grammar and as such it is an LL(1) language. The 
main advantages of defining programming languages this way is that those 
languages are __context-free__ and __unambiguous__.

In the meantime, it seems that the only translating that was expected from the 
compilers or from the interpreters was the translating of source codes into 
binary code for a targeted processor, to run it either after compile-time 
or at run-time while interpreted on-the-fly.

The first works we have found published on programming languages translation 
from one to another appeared... about 30 years later. Patents related to this 
topic have been registrered by 1994 [10], while a paper published in 1995 
first suggested the mixing of programming languages [5]. Let's go through some 
of these works.


# 3. Translating a Programming Language into another Programming Language



# Annex A - Bibliography and Patents

### A.1 Bibliography

| Ref. | Paper citation |
|:---:|---|
| [1] | _The Syntax and Semantics of the Proposed International Algebraic Language of the Zurich ACM-GAMM Conference_. J. W. Backus. Proceedings of the International Conference on Information Processing, UNESCO, 1959, pp.125-132. [http://www.softwarepreservation.org/projects/ALGOL/paper/Backus-Syntax_and_Semantics_of_Proposed_IAL.pdf](http://www.softwarepreservation.org/projects/ALGOL/paper/Backus-Syntax_and_Semantics_of_Proposed_IAL.pdf) |
| [2] | _Automatic-programming-language translation through syntactical analysis_. Robert S. Ledley and James B. Wilson. 1962. Commun. ACM 5, 3 (March 1962), 145-155. DOI=http://dx.doi.org/10.1145/366862.366872 |
| [3] | _A Parameterized Compiler Based on Mechanical Linguistics_. Howard Metcalfe. Planning Research Corporation R-311, March 1, 1963, also in Annual Review in Automatic Programming, Vol. 4 |
| [4] | _On the translation of languages from left to right_. Donald E.Knuth. Information and Control Volume 8, Issue 6, December 1965, Pages 607-639 |
| [5] | _Mixed Languages Programming_. Burkhard D. Burow. in Computing in High Energy Physics '95, pp. 610-614 (1996) |


### A.2 Patent

| Ref. | Patent citation |
|:---:|---|
| [10] | _Method and apparatus for translating source code from one high-level computer language to another_. Kristy A. Andrews, Paul Del Vigna, Mark E. Molloy. US5768564A and US6031993A. 1994-10-07. |



## Annex B - This document revisions history

| Date  | Rev.  | Author(s)  | Comments  |
|:---:|:---:|---|---|
| 2018-08-17 | 0.0.1  | Schmouk | Created from scratch; Instered first version of bibliography (just links to) |
| 2018-08-18 | 0.0.2 | PhHays | Completed sections 1. and 2.; Put bibliography on correct form |
|  |  |  |  |
