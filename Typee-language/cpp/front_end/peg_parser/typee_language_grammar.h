#pragma once
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
#include "tao/pegtl.hpp"

namespace pegtl = TAO_PEGTL_NAMESPACE;


//===========================================================================
namespace ty_fe
{
namespace ty_grm  //!< the Typee language grammar namespace
{
    //=======================================================================
    // Forward declarations
    //--- tokens
    struct ENDMARKER;

    //--- rules
    struct statements_list;
    struct t_code_module;


    //=======================================================================
    // Tokens definitions
    struct ENDMARKER : pegtl::eof {};  //!< The end-of-file marker


    //=======================================================================
    // The Typee language rules definitions

    //---   TCodeModule   ---------------------------------------------------
    /** \brief The 'entry' rule of the Typee language grammar, specifying what are modules of T code. */
    struct t_code_module : pegtl::seq<statements_list, ENDMARKER> {};


    //---   StatementsList   ------------------------------------------------
    /** \brief Defines lists of T statements. */
    struct statements_list : pegtl::until<pegtl::eof, pegtl::any> {};  // Notice: this is a very temporary 'empty' definition!


}  // end of namespace ty_fe::grm 
}  // end of namespace ty_fe
