# Front-End Scanner: Tests Documentation

This document is part of the Open Source project __Typee__. As such, it is
delivered under the MIT license:
```
Copyright (c) 2018-2019 Philippe Schmouker, Typee project, http://www.typee.ovh

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

Currently, those tests are not automated. It is the responsability of the
coder to manually run the scripts that check for the correctness of the
tokenization of __Typee__ or __Typee__-like source files by the Front-End 
scanner.

Should any arror be detected, it is also the responsability of the coder to
fix the bugs she introduced before committing her code.

Please do not modify the content of directory src/ Tests/Scanner_Tokens/Data/
unless you are sure of what you are doing. See at end of this documentation to
get details.



## Testing scripts

They can be found in directory src/Tests/Scanner_Tokens.
- `tokens_test_base.py` contains the base class that is used by every test 
script. No one should either use or modify its content.
- `script_compound_tokens_test.py` tests for "compound" tokens. These are the 
tokens that contain multiple characters with either their first character may also
be a token by itself - e.g. "==" and "=" or "<=" and "<" or... not.
- `script_names_and_nums_tokens_test` tests legal and illegal identifiers and
numbers;
- `script_simple_tokens_test.py` tests tokens that only get one character and
are not the beginning of a compuond token.


### To run the scripts

With framework __Eclipse__, run those three scripts and check the code you may
have added in the parser if any error occurs.

With console, just run your Python interpreter for each of those scripts,
for isntance:

```
$ python script_compound_tokens_test.py
```


### Notice

Please notice that thos scripts are quite simple, because they don't test much
things. This is a reason why you should not bother too much if you get many
errors. Just try to correct the very first encountered one. Most of the times,
the next ones were only due to the very first detected error.



## The way scripts are working

The testing procedure is quite simple for checking tokens.

Take a look at directory `src/Tests/Scanner_Tokens/Data/`. For each of the 
testing scripts there exist two files. Let's take an example just to
easily explain (and understand).

The Typee module `tokenization_simple_tokens.ty` contains __Typee__ code with
every simple tokens (e.g. "[", "]" even if they are put in side by side, "#",
etc.) This module DOES NOT correspond to any valid syntax for __Typee__. It
only contains __Typee__ tokens that are to-be-checked against __Typee__
Front-End scannerization.

Associated with this __Typee__-like module you will find a _Python_ module
named `tokenization_simple_solution.py`. This module only defines a list named
`soluce` which gets the successive _Intermediate Code_ nodes that SHOULD be
created by the Front End Scanner when things get right. This module is imported
by the related testing script `script_simple_tokens_test.py` and the final
result of the Front-End Scanner pass is then compared with this `soluce`.


## Adding new tokens to those testing scripts.

When a new version of __Typee__ grammar is released, there may be new tokens
added to its specifications. Those new tokens have to :
1. be added as-is int the related `Data/tokenization_xxx_tokens.ty` with `xxx`
in (`simple_tokens`, `names_and_nums`, `compound_tokens`);
2. get their related ICNode inserted in the right place in the list `soluce`
within the related _Python_ module `Data/tokenization_xxx_solution.py`.

Be very cautious there. Just put the expected ICNode with the correct name, the
correct content and at the correct place in the soluce.


## That's it

And before adding any new rule to __Typee__ grammar specification, just
provide a TExP - Typpe EXtension Proposal.
Unfortunately, by those days, there is no yet defined formal way to create
TExP. Surely soon to come on http://www.typee.ovh web site!



## Annex - This document revisions history

| Date  | Rev.  | Author(s)  | Comments  |
|---|---|---|---|
| 2018-07-13 | 0.0.1 | Schmouk | Very first creation |
| 2018-07-13 | 0.0.2 | Schmouk | One very minor typo correction |
| 2018-07-20 | 0.0.3 | Schmouk | Added copyright, license text and this history |
|  |  |  |  |


