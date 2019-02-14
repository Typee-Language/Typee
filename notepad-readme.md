#  Notepad++ recommendations

The directory `Typee/Notepad++XML-configs` contains three `.xml` files:
- desktop.ini
- grammars.xml
- typhon.xml

The first file contains configuration for the display of this repository.

The two last files contain descriptions of language and syntax coloring specification 
for:
- `.grm` files, i.e. files contining grammars specification of programming 
languages, and
- `.ty` and `.typee` modules containing Typee code.

Windows users who would like to use Notepad++ for its syntax coloring 
capabilities are encouraged to put those three `.xml` files directly at the 
root directory of their Notepad++ installation. Any `.grm`, `.ty` or 
`.typee` file will then be automatically coloured.

Notably, the .grm specification file of __Typee__ (see directory `Specs`) will
open and will be coloured in Notepad++.

Any __Typee__ module you would program will also automatically get syntax 
colorisation as long as it is suffixed with either `.ty`or `.typee` (which are
the recommended suffixes for __Typee__ modules).