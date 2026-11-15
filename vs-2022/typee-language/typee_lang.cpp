/*
MIT License

Copyright (c) 2025 Philippe Schmouker, ph (dot) schmouker (at) gmail (dot) com

This file is part the Typee framework - dedicated to Typee language.

Permission is hereby granted,  free of charge,  to any person obtaining a copy
of this software and associated documentation files (the "Software"),  to deal
in the Software without restriction,  including without limitation the  rights
to use,  copy,  modify,  merge,  publish,  distribute, sublicense, and/or sell
copies of the Software,  and  to  permit  persons  to  whom  the  Software  is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS",  WITHOUT WARRANTY OF ANY  KIND,  EXPRESS  OR
IMPLIED,  INCLUDING  BUT  NOT  LIMITED  TO  THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT  SHALL  THE
AUTHORS  OR  COPYRIGHT  HOLDERS  BE  LIABLE  FOR  ANY CLAIM,  DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM,
OUT  OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/


//===========================================================================
#include "typee_lang.h"


// for local tests purposes
#include <cassert>
#include <filesystem>
#include <string>

#include "front_end/peg_parser/fe_parser.h"


//===========================================================================
/** \brief Currently, for compilation purpose only
*/
int main()
{
    // ok, let'suse this for very first tests
    {
        assert(ty_fe::FEParser::parse(""));
    }
    {
        assert(ty_fe::FEParser::parse("..."));
    }
    {
        ty_fe::FEParser test_parser("E:/GitHub/Typee/Typee-language/python/Libs/SysTime/systime.ty");
        assert(test_parser);
        assert(test_parser.parse());
    }

    // currently left so simple
    return 0;
}
