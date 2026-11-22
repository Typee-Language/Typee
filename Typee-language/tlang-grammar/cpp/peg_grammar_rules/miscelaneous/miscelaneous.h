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

namespace tlang_rules
{
    //===========================================================================
    struct AlphaChar;
    struct AlphaNumChar;
    struct Dot;
    struct DottedName;
    using  EndOfLine = pegtl::cr_lf_crlf;
    struct Identifier;
    struct Name;
    struct NameFirstChar;
    struct NameThenChar;
    struct SemiColon;
    using  Spacing = pegtl::space;
    struct Spacing0;
    struct Spacing1;
    struct Underscore;


    //===========================================================================
    struct AlphaChar : pegtl::ranges<'a', 'z', 'A', 'Z'> {};


    struct AlphaNumChar : pegtl::ranges<'a', 'z', '0', '9', 'A', 'Z'> {};


    struct Dot : pegtl::one<'.'> {};


    struct DottedName : pegtl::seq<
                            Name,
                            pegtl::plus<pegtl::seq<Dot, Spacing0, Name>>
                        > {};


    struct Identifier : pegtl::seq<  // Notice: the used rule definition here is the most effective one - see grammar specs doc
                            Name,
                            pegtl::star<pegtl::seq<Dot, Spacing0, Name>>
                        > {};


    struct Name : pegtl::seq<
                      pegtl::identifier,  // Notice: PEGTL v.4.0 specifies identifiers exactly as TLang PEG actually does
                      Spacing0
                  > {};
    /**
    // Should PEGTL specification of 'identifier' accept more chars than
    // TLang PEGTL does, next definition for rule 'Name' should be used.
    struct Name : pegtl::seq<
                      pegtl::sor<AlphaChar, Underscore>,
                      pegtl::star<pegtl::sor<AlphaNumChar, Underscore>>,
                      Spacing0
                  > {};
    */


    struct NameFirstChar : pegtl::sor<AlphaChar, pegtl::one<'_'>> {};


    struct NameNextChar : pegtl::sor<AlphaNumChar, pegtl::one<'_'>> {};


    struct SemiColon : pegtl::one<';'> {};


    struct Spacing0 : pegtl::star<Spacing> {};


    struct Spacing1 : pegtl::plus<Spacing> {};


    struct Underscore : pegtl::one<'_'> {};

}