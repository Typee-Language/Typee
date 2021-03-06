# Typee

A new generic object-oriented programming language.


## Want to Contribute?

If you wish to contribute, just contact main administrator 
[Schmouk](mailto:ph.schmouker@gmail.com) by e-mail and be patient. You will 
eventually get a response and will enthousiastically be added to the 
contributors list.
Current developments are in _Python 3.8_, based on _Anaconda 3_, with 
_Eclipse 2020-03_ framework and _PyDev_ plug-in. Windows is currently used also 
for these developments. So, if you get Linux expertise you're welcome!

Notice: Python 3.8 has been released by October 2019.


## What is Typee?

**Typee** is an Object Oriented Programming language. Its syntax is derived 
from other OOP language such as _C++11_, _Java 8.0_ and _Python 3.8_. Some 
goodies from other languages are used also (e.g. from _PHP_).


## Typee language characteristics

We list here only the main characteristics of **Typee**.

- Object Oriented Programming;
- typed variables and objects;
- classical scalar types;
- Templated on functions, methods and **operators** - as with templates in 
_C++_ and generics in _Java_ while with bonuses on operators;
- auto typing in specific cases - as with `auto` in _C++_ and as is by default 
in _Python_;
- 'for' and 'if' comprehensions - as in _Python_;
- built-in containers for objects - as in _Python_: `list`, `set`, `dict`, 
plus `array`;
- classical instructions plus bonuses - e.g. `otherwise` associated with `for` and 
`while` as in _Python_ or with `switch`;
- classical exception handling;
- classical operators plus a few bonuses - e.g. 0-shifting as built in _Java_;
- few undefined operators available for users specific definitions;
- unnamed functions - as in _Java_ or _Python_ lambdas;
- an `embed` instruction for the embedding of native code in _Python_, _C++_ or 
_Java_ for instance;
- and few other goodies you will enjoy to use.

While navigating in [Typee GitHub repository](https://github.com/Typee-Language/Typee) 
you will find numerous documentation on **Typee** grammar specification, the 
**Typee** translator software architecture (see short description below) or the 
whole software documentation - as generated in HTML by an open source 
application, _PyYadc_ (Yet another documentation compiler).

Please be aware that this project is under construction and that currently NO 
running version is available. Documentation as well as directories tree and 
their contents are highly subject to change, actually on a daily or at least 
on a weekly basis.

_Reminder_: if you wish to contribute, just contact main administrator 
[Schmouk](mailto:ph.schmouker@yahoo.fr) or directly 
[Typee](mailto:postmaster@typee.ovh) by e-mail and be patient. You will 
eventually get a response back and will enthousiastically be added to the 
contributors list. You will then be able to join some teams according to 
your aims and skills.


### Rationale

At first, this was a personnal project. It aimed at developping an upper layer 
to _Python_ with a true type verification. This had already been partially 
addressed by Google with their project 
[**PyType**](https://opensource.google.com/projects/pytype). The kind of 
annotations this project proposes is now widely accepted and inserted in new 
_Python_ code. _PyType_ is a static analyzer that infers and checks types for 
_Python_ code.

```
PyType is a static type inferencer and type checker for _Python_ code. It is 
capable of analyzing existing _Python_ code to determine what possible types 
could be used on APIs throughout the program.
```
(source: _Google_ project _PyType_)

Well. This is not exactly full type checking - while it is perfectly adapted to 
_Python_ programming for which no type declaration is needed before manipulating 
objects.

But we wanted to get a typed language to further translate it in _Python_ code, 
full static type checking having been done before automatically generating 
_Python_ modules then running the _Python_ interpreter on them.



### Typee: neither compiled nor interpreted but translated

Traditionnal OOP languages are either compiled (e.g. C++) or interpreted (e.g. 
_Python_ ). They even may be first compiled into an intermediate code which is 
then interpreted (e.g. Java and its Bytecode interpreted by a 
_Java Virtual Machine_ that has to be implemented on each of the different 
targeted devices).

**Typee** is neither compiled nor interpreted. It is rather translated into 
other OOP languages, such as _Python_ which chronologically is the first 
addressed OOP language from: _Python_, _C++_, _C#_ and _Java_. During the 
translation, type infering and checking is done not only for APIs as does 
_PyType_ but also on all the other parts of the code.

While this may seem to be valuable for untyped languages such as _Python_, it 
should appear to be not useful for other typed languages, of course.
Yes, but wait...


### Typee: one code for many implementations

Here is the core usefulness of **Typee**: once a program has been written in 
**Typee**, it can then easily be translated in any other available OOP 
language. At first, this will be a translator to _Python_. But as soon as other 
translators will be available, e.g. for _C++_ or _Java_, the same code will be 
available for translation in these languages also.

As long as related libraries are added to the package (for instance graphical 
ones or GPU parallel programming ones) and are programmed in **Typee** with 
dedicated code (i.e. native embedded code) for the targeted OOP language, it 
should be easy to program applications for Windows, Linux, iOS or Android with 
a single code programmed in **Typee**.

Here we are!


### Has this been done before?

Well, it might be that this has already been done before, yes.

[https://haxe.org](Haxe) is en excellent example of _transpilation_ from one formal generic language to many others. "_The **Haxe Foundation** was created to fund long term Haxe development and provide support to companies using Haxe._" as is said on their related Web site. This creation took place with many commercial partners, after many years of open-source development (which started by 2005).

Meanwhile, _Haxe_ is translated in many languages and for many platforms, with Web development as its first intention.

The Haxe compiler is specified with functionnal programming language OCaml, an [https://www.inria.fr/](Inria) extension of ML:

" _ML is a general-purpose functional programming language developed by Robin Milner and others in the early 1970s_ [first appeared in '73] _at the University of Edinburgh, whose syntax is inspired by ISWIM. It has roots in the Lisp language, and has been characterized as "LISP with types". Historically, ML stands for MetaLanguage: it was conceived to develop proof tactics in the LCF theorem prover (whose language, pplambda, a combination of the first-order predicate calculus and the simply-typed polymorphic lambda calculus, had ML as its metalanguage). It is known for its use of the Hindley–Milner type system, whose type inference algorithm can automatically assign the types of most expressions without requiring explicit type annotations. Additionally, the use of this algorithm ensures type safety—there is a formal proof that a well-typed ML program does not cause runtime type errors._ "
(source: [https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/ML_(programming_language).html](https://IPFS.io/ipfs) )


See also: [https://ocaml.org/](OCaml.org)

The description of the Haxe compiler is concise and ensures correctness of types checking. That's great.
_OCaml_ gets also a very good reputation about its computational optimization on time processing.

The global software architecture of **Typee**, while having been specified with no knowledge of the _Haxe_ one, is finally the same as the _Haxe_ compiler. As you will see below, _Haxe_ and **Typee** both specify a front-end and many back-ends. **Typee** seems then to be a well designed "compiler".

So, would the work have been already done?
Well, not exactly as we aim at doing it!

There are still a few concepts that are offered as built-in goodies in **Typee** that are not in _Haxe_. The main one is the **native code embedding** which helps generate efficient targeted code for some parts of it. Others are concepts that constitue **Typee** built-in libraries while they have been later added external libraries with _Haxe_.

Finally, nobody would re-program the _Haxe_ compiler in _Haxe_. Its (fully correct) _OCaml_ implementation being a functionnal one, this would need reprogrammation from scratch in an imperative language (i.e. _Haxe_). **Typee** first implementation being done in _Python 3.7_, it will be far easier to later reprogram it in **Typee** which, then, will be translated in far better time-efficient languages (e.g. C++).

Really so, Here We Are!


## Typee global architecture

**Typee** has been specified as would have been any compiler. Our bedside book 
for a long has been "Engineering a Compiler, 2nd Edition, Keith D.Cooper & 
Linda Torczon, Elsevier, 2012" and we encourage the reader to read this book.

We have choosen this book because it was newer than the famous Dragoon book 
"Compilers, principles, techniques, & tools, 2nd ed." from Alfred V. Aho, 
Monica S. Lam, Ravi Ethi and Jeffrey D. Ullman, Pearson-Addison Wesley, 2007, 
while this Dragoon book had been used to specify the _Python_ interpretor 
_CPython_.


### Global architecture of a compiler

A compiler is composed of a **front-end**, a **back-end** and an 
**optimizer**.


#### The Front-End

It contains a **scanner** that scans the code and generates a first level of 
intermediate code: the _tokenized_ code.

The generated tokenized code is provided to a **parser** that parses the 
tokens and generates a second level of intermediate code: the _IC_. The 
**parser** parses this code and checks it for syntax correctness. Syntax errors 
are emitted during this step of the compilation.

The generated _IC_ is finally passed to an **elaborator** that elaborates all 
the other checkings - such as types infering and checking, for instance. Not 
declared variables or objects, or types errors are emitted during this step of 
the compilation.


#### The Back-End

It generates the final binary code for the targeted processing unit. It gets 
as input the intermediate code _IC_ as generated by the **elaborator** of the 
**Front-End** once this _IC_ has been fully checked and validated. The 
**Back-End** output is a binary file that contains either executable code 
within a targeted _Operating System_ or binary code and linkage metadata to be 
later linked with other code.


#### The Optimizer

According to the targeted processing unit, the optimizer optimizes the 
finally generated binary code. According to the _IC_ generated by the 
**Front-End** it may also provide optimizations within the _IC_, e.g. by 
duplicating code of small functions rather than calling them (speed 
optimization) or by removing dead code as long as this can be statically 
detected (space optimization).


### Global architecture of Typee

Well, **Typee** is a translator not a compiler. So, we only implement the 
**Front-End** and the **Back-End** steps of a compiler.


#### Typee Front-End

As for any compiler, **Typee** gets a **scanner** for the tokenization of the 
code, a **parser** for syntax checking and an **elaborator** for undeclared 
variables detection, types infering and types checking.

It generates an _Intermediate Code_ and passes it to the _Back-End_ as long as 
all checks are ok.


#### Typee Back-End

The **Typee** _Back-End_ finalizes the translation to the targeted programming 
language. Remember, as a first step, _Python_ is the targeted language. _C++_ 
and _Java_ will come next.

According to this, the _Back-End_ of **Typee** contains as many generators as 
targeted languages, each of them generating the corresponding code to be 
either interpreted (_Python_) or compiled (_C++_, _Java_) with the 
corresponding interpreter / compiler.


#### Optimizer

**Typee** implements no _optimizer_. This step is left to the final 
interpreters and compilers that will do a definitively correct job.


#### Final step

The final step for the user is then to run the compiler or the interpretor of 
the targeted language. Of course, this step can be automated via scripting 
and **Typee** project aims at providing such scripts to ease the whole process.


## Development policy

Only develop under branch `dev`. Do not hesitate to create your own branches 
to commit then push your contributions, but start all of them from branch 
`dev`. Only an administrator may merge new releases of **Typee Translator** 
into branch `master`. Merges will be done only from branch `dev`.


## Visit us

at http://www.typee.ovh and https://typee-language.github.io/Typee/

or follow us at https://twitter.com/TypeeProgrammi1



## Last but not least

Let's thank the few (and known) hackers whose action, by August 2019, greatly 
helped us enhancing the correctness of this repository content. Nice, we feel 
far more secure now ;-) .


## That's it

Enjoy!
