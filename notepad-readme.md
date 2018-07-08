#  Notepad++ recommendations

The directory `XML-configs` contains three `.xml` files:
- grammars.xml
- langs.model.xml
- typhon.xml

These files contain descriptions of language and syntax coloring specification 
for:
- `.grm` files, i.e. files contining grammars specification of programming 
languages, and
- `.ty` and `.typhon` modules containing Typhon code.

Windows users who would like to use Notepad++ for its syntax coloring 
capabilities are encouraged to put those three `.xml` files directly at the 
root directory of their Notepad++ installation. Any `.grm`, `.ty` or 
`.typhon` file will then be automatically coloured.

Notably, the .grm specification file of __Typhon__ (see directory `Specs`) will
open and will be coloured in Notepad++.

Any __Typhon__ module you would program will also automatically get syntax 
colorisation as long as it is suffixed with either `.ty`or `.typhon` (which are
the recommended suffixes for __Python__ modules).
