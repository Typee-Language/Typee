# Externals (libraries)
**Typee environment** and **Typee language** use external libraries.

These are downloaded in subdirectory `externals`.

They are listed here below, with a reminder of their associated licenses.

---
## PEGTL - Parsing Expressions Grammars Template Library
*The Parsing Expression Grammar Template Library (PEGTL) is a zero-dependency C++ header-only parser combinator library for creating parsers according to a Parsing Expression Grammar (PEG).* (extracted from GitHub repository.

#### Github repository: [https://github.com/taocpp/PEGTL](https://github.com/taocpp/PEGTL)

#### License: [Boost Software License, Version 1.0](https://www.boost.org/LICENSE_1_0.txt)


Initiated by Daniel Frey and Dr. Colin Hirsch, this fully templated library "*...is designed to be "lean and mean", the core library consists of approximately 6000 lines of code. Emphasis is on simplicity and efficiency, preferring a well-tuned simple approach over complicated optimisations.*

*The PEGTL is mostly concerned with parsing combinators and grammar rules, and with giving the user of the library (the possibility of) full control over all other aspects of a parsing run. Whether/which actions are taken, and whether/which data structures are created during a parsing run, is entirely up to the user.* ...

*Through the use of template programming and template specialisations it is possible to write a grammar once, and use it in multiple ways with different (semantic) actions in different (or the same) parsing runs.*

*With the PEG formalism, the separation into lexer and parser stages is usually dropped -- everything is done in a single grammar. The rules are expressed in C++ as template instantiations, and it is the compiler's task to optimise PEGTL grammars.*" (part of text extracted from [https://github.com/taocpp/PEGTL/README.md](https://github.com/taocpp/PEGTL/README.md)).

**Typee language** code uses this external library for the parsing of modules developed in language **T** and for the generation of the associated ASTs (*Abstract Syntaxic Trees*).
