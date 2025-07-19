# Typee

A new generic object-oriented programming language and a programming environment.


## What is Typee?

**Typee** is a programming framework which embeds a **Typee environment** as well as a programming language, the **Typee language** (also named **T** language).

The **Typee language** is an Object Oriented Programming language. Its syntax is derived from other OOP language such as *c++*, *Java* and *Python 3*. Some goodies from other languages are used also (e.g. from *PHP*).  
The programming **Typee environment** helps translating Typee language source code into other programming languages source code: this is the ***transpilation*** process.


## Some chronology

This project started by mid of 2018. The **Typee language** grammar had first been specified in an *LL1* form and by those times the **Typee environment** was implemented with Python (3.7, then 3.8). Work was done on hobby time and happenned to be put for a while in stand-by mode by mid of 2021.

By end of July 2025, work on this project restarted, still on hobby time. Development policy has evolved (see later in this document). The grammar of **Typee language** is now specified according to **Parsing Expressions Grammar** (**PEG**) as the Python grammar has been specified since its version 3.9.  
Furthermore, the **Typee environment** is now coded using c++23 (or at least c++20 when it happens that c++23 features are not yet available with c++ compilers).

About **PEG**, Bryan Ford formalized this concept and published it in a famous paper by January 2004: ["*Parsing Expression Grammars: A Recognition Based Syntactic Foundation*"](https://bford.info/pub/lang/peg.pdf), *PDF format*, in proceedings of the 31st ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages, pp. 111–122.  
[doi:10.1145/964001.964011](https://doi.org/10.1145%2F964001.964011).  
ISBN 1-58113-729-X.  
The curious reader will take benefit of reading this paper.


## Typee language characteristics

We list here only the main characteristics of **Typee language**, i.e. **T**.

- Object Oriented Programming;
- with the initial aim at neither being compiled nor being interpreted but **transpiled** into other targeted programming languages source code;
- typed variables and objects;
- classical scalar types;
- Templated on functions, methods and **operators** - as with templates in 
*C++* and generics in *Java* while with bonuses on operators;
- auto typing in specific cases - as with `auto` in *C++* and as is by default in *Python*;
- 'for' and 'if' comprehensions - as in *Python*;
- built-in containers for objects - as in *Python*: `list`, `set`, `dict`, 
plus `array`;
- classical instructions plus bonuses - e.g. `otherwise` associated with `for` and `while` as in *Python* or with `switch`;
- classical exception handling;
- classical operators plus a few bonuses - e.g. 0-shifting as built in *Java*;
- few undefined operators available for users specific definitions;
- unnamed functions - as in *Java* or *Python* lambdas;
- an `embed` instruction for the embedding of native code in *Python*, *C++* or *Java* for instance;
- and few other goodies you will enjoy to use.

While navigating in [Typee GitHub repository](https://github.com/Typee-Language/Typee) you will find numerous documentation on **Typee** grammar specification, the **Typee** translator software architecture (see short description below) or the whole software documentation - as generated in HTML by an open source application, *PyYadc* (Yet another documentation compiler). Notice: related work is currently in progress.

Please be aware that this project is under construction and that currently NO released, running, version is available. Documentation as well as directories tree and their contents are highly subject to change, actually on a daily or at least on a weekly basis.


### Typee language: neither compiled nor interpreted but translated

Traditionnal OOP languages are either compiled (e.g. *C++*) or interpreted (e.g. *Python* ). They even may be first compiled into an intermediate code which is then interpreted (e.g. *Java* and its Bytecode interpreted by a *Java Virtual Machine* that has to be implemented on each of the different targeted devices).

**Typee language** aims at neither beign compiled nor beign interpreted. It rather aims at being translated into other OOP languages source code, such as *Python*, *c++*, *C#* or *Kotlin* (i.e. *Java*-like for Android)). During the translation, type infering and checking is done. This is of great help for producing type-checked code for untyped programming languages.

While this may seem to be valuable for untyped languages such as *Python*, it should appear to be not that useful for other typed languages, of course.

Yes, but wait...


### Typee: one code for many implementations

Here is the core usefulness of **Typee environment**: once a program has been written in **Typee language**, it can then be easily translated in many other programming languages - as long as related transpilers are available. Source code in **Typee language** is then tranlated into targeted language source code, these being OOP languages or not.

As long as related libraries are added to the **Typee environment** (for instance graphical ones or GPU parallel programming ones) and as long as they are programmed in **Typee language** for the targeted OOP language (maybe with dedicated code, i.e. native embedded code), it will be easy to code applications for Windows, Linux, iOS or Android with a single code programmed in **Typee language**.

Here we are!


### Has this been done before?

Well, it might be that this has already been done before, yes.

[https://haxe.org](Haxe) is en excellent example of *transpilation* from one formal generic language to many others. "*The **Haxe Foundation** was created to fund long term Haxe development and provide support to companies using Haxe.*" as is said on their Web site. This creation took place with many commercial partners, after many years of open-source development (which started by 2005).

Meanwhile, *Haxe* code is translated into many languages and for many platforms, with Web development as its first aim.

The *Haxe* compiler is specified with functionnal programming language OCaml, an [https://www.inria.fr/](Inria) extension of ML:

" *ML is a general-purpose functional programming language developed by Robin Milner and others in the early 1970s* [first appeared in '73] *at the University of Edinburgh, whose syntax is inspired by ISWIM. It has roots in the Lisp language, and has been characterized as "LISP with types". Historically, ML stands for MetaLanguage: it was conceived to develop proof tactics in the LCF theorem prover (whose language, pplambda, a combination of the first-order predicate calculus and the simply-typed polymorphic lambda calculus, had ML as its metalanguage). It is known for its use of the Hindley–Milner type system, whose type inference algorithm can automatically assign the types of most expressions without requiring explicit type annotations. Additionally, the use of this algorithm ensures type safety—there is a formal proof that a well-typed ML program does not cause runtime type errors.* "  
Source: [https://IPFS.io/ipfs](https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/ML_(programming_language).html)  
See also: [https://ocaml.org/](OCaml.org)

The description of the Haxe compiler is concise and ensures correctness of types checking. That's great. *OCaml* gets also a very good reputation about its computational optimization on time processing.

The global software architecture of **Typee environment**, while having been specified with no knowledge of the *Haxe* one, is finally similar to the *Haxe* compiler. As you will see below, *Haxe* and **Typee** both specify a front-end and many back-ends. As such, **Typee environment** "seems" then to embed a well designed "compiler".

So, would the work have been already done?
Well, not exactly as we aim to do it!

There are still a few concepts that are offered as built-in goodies in **Typee language** that are not in *Haxe*. The main one is the **native code embedding** which helps generate efficient targeted code for some parts of it. Other ones are concepts that constitute the built-in libraries of **Typee environment**: many libraries have been later added as external libraries with *Haxe*.

Finally, nobody would re-program the *Haxe* compiler in *Haxe*. Its (fully correct) *OCaml* implementation being a functionnal one, this would need reprogrammation from scratch in an imperative language (as is *Haxe*).  **Typee** implementation being done in a generic OOP language, it will be far easier to later reprogram it in **Typee language** which, then, could be translated in far better time-efficient languages (e.g. C++).

Really so, Here We Are!


## Typee global architecture

**Typee** has been specified as would have been any compiler. Our bedside book for a long has been "Engineering a Compiler, 2nd Edition, Keith D.Cooper & Linda Torczon, Elsevier, 2012" and we encourage the reader to read this book.

We have choosen this book because it was newer than the famous Dragoon book "Compilers, principles, techniques, & tools, 2nd ed." from Alfred V. Aho, Monica S. Lam, Ravi Ethi and Jeffrey D. Ullman, Pearson-Addison Wesley, 2007, that had been used to specify the *Python* interpreter 
*CPython*.


### Global architecture of a compiler

A compiler is composed of a **front-end**, a **back-end** and an 
**optimizer**.


#### The Front-End

The **front-end** of a compiler contains a **scanner** that scans the code and generates a first level of intermediate code: the *tokenized* code.

The generated tokenized code is provided to a **parser** that parses the 
tokens and generates a second level of intermediate code: the *IC*. The
**parser** parses this intermediate code and checks it against syntax correctness. Syntax errors are emitted during this step of the compilation.

The generated *IC* is finally passed to an **elaborator** that elaborates all the other checkings - such as types infering and checking for instance. Not declared variables or objects, or types errors are emitted during this step of the compilation.


#### The Back-End

The **back-end** of a compiler generates the final binary code for the targeted processing unit.

It gets as its input the intermediate code *IC* as generated by the **elaborator** of the **Front-End** once this *IC* has been fully checked and validated.

The **Back-End** output is a binary file that contains either executable code within a targeted *Operating System* or binary code and linkage metadata to be later linked with other code.


#### The Optimizer

According to the targeted processing unit, the **optimizer** optimizes the 
finally generated binary code. According to the *IC* generated by the
**Front-End** it may also provide optimizations within the *IC*, for instance by duplicating code of small functions rather than calling them (speed optimization) or by removing dead code as long as this can be statically detected (memory space optimization).


### Global architecture of Typee transpiler

So, the **Typee environment** embeds *transpilers*, not a compiler. So, we only implement a single **Front-End** that takes **T** code as its input and multiple **Back-Ends**, each one related to a single targeted programming language and a single of their standards.


#### Typee Front-End

As for any compiler, **Typee front-end** gets a **scanner** for the tokenization of the **T** code, a **parser** for syntax checking and an **elaborator** for undeclared variables detection, types infering and types checking.

It generates an *Intermediate Code* and passes it to the *Back-Ends* as long as all checkings are ok.


#### Typee Back-End

The **Typee Back-End** finalizes the translation into the targeted programming languages, for the targeted of their standards and for targeted platforms if pertinent.

According to this, the *Back-End* of **Typee** contains as many generators as targeted languages and related standards, each of them generating the corresponding code to be either interpreted (e.g. *Python*) or compiled (e.g. *C++* or *Java*) with the related interpreter / compiler.


#### Optimizer

**Typee environment** implements no *optimizer*. This step is left to the final interpreters and compilers that will do a definitively correct job.


#### Final step

The final step for the user is then to run the compiler or the interpretor of the targeted languages. Of course, this step can be automated via scripting and **Typee environment** aims at providing such scripts to ease the whole process.


## Development policy

In the initial and earliest configuration of **typee environment** any developemnt had to be done in speciic branches created from branch `dev`. Only an administrator could merge new releases of **Typee Translator** into branch `master`.

A new policy is now in action. Only administrators can still merge new releases of **Typee environment** into branch `master`, but developments are now done into release branches, each one created under branch `master`. The naming of release branches is in the form "release-*x*-*y*" where *x* is the major version and *y* the minor version of the release. A patch version may be finally added to the release tag, at release time.



## Visit us

at http://www.typee.ovh,  
at https://github.com/Typee-Language/Typee/ and  
at https://typee-language.github.io/Typee/



## Last but not least

Let's thank the few (and known) hackers whose action, by August 2019, greatly helped us enhancing the correctness of this repository content. Really nice: we feel far more secure now ;-) .


## That's it

Enjoy!
