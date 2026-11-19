#pragma once
/*
MIT License

Copyright (c) 2026 Philippe Schmouker, ph (dot) schmouker (at) gmail (dot) com

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
#include "tao/pegtl.hpp"
#include "tao/pegtl/config.hpp"
namespace pegtl = TAO_PEGTL_NAMESPACE;

#include "tao/pegtl/ascii.hpp"
#include "tao/pegtl/rules.hpp"


//===========================================================================
struct AlphaChar;
struct AlphaNumChar;
struct Dot;
struct DottedName;
struct EndOfLine;
struct Identifier;
struct Spacing;
struct Spacing0;
struct Spacing1;
struct Underscore;


//===========================================================================
struct AlphaChar :
    pegtl::ranges<'A', 'Z', 'a', 'z'> {};


struct AlphaNumChar :
    pegtl::ranges<'0', '9', 'A', 'Z', 'a', 'z'> {};


struct Dot :
    pegtl::one<'.'> {};


struct DottedName :
    pegtl::seq <
        Identifier,
        pegtl::star< pegtl::seq<Dot, Identifier> >,
        Spacing0
    > {};


struct EndOfLine :
    pegtl::sor<
        pegtl::eolf,  // i.e. "\r\n", "\n\r", '\n', '\r' or end-of-input
        pegtl::one<'\v', '\f'>
    > {};


struct Identifier :
    pegtl::seq<
        pegtl::sor<AlphaChar, Underscore>,
        pegtl::star<pegtl::sor<AlphaNumChar, Underscore>>,
        Spacing0
    > {};


struct Spacing :
    pegtl::sor<
        pegtl::one<' ', '\t'>,
        EndOfLine
    > {};

struct Spacing0 : pegtl::star<Spacing> {};
struct Spacing1 : pegtl::plus<Spacing> {};


struct Underscore :
    pegtl::one<'_'> {};
