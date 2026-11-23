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

#include "tao/pegtl/pegtl_string.hpp"
#include "tao/pegtl/rules.hpp"

#include "../miscelaneous/miscelaneous.h"


namespace tlang_rules
{
    //===========================================================================
    struct Abstract_kw : TAO_PEGTL_KEYWORD("abstract") {};
    struct Abstract : pegtl::seq<Abstract_kw, pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct All_kw : TAO_PEGTL_KEYWORD("all") {};
    struct All : pegtl::seq<All_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct And_kw : TAO_PEGTL_KEYWORD("and") {};
    struct And : pegtl::seq<And_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Array_kw : TAO_PEGTL_KEYWORD("array") {};
    struct Array : pegtl::seq<Array_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct As_kw : TAO_PEGTL_KEYWORD("as") {};
    struct As : pegtl::seq<As_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Assert_kw : TAO_PEGTL_KEYWORD("assert") {};
    struct Assert : pegtl::seq<Assert_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct AutoType_kw : TAO_PEGTL_KEYWORD("?") {};
    struct AutoType : pegtl::seq<AutoType_kw, Spacing1> {};

    struct Break_kw : TAO_PEGTL_KEYWORD("break") {};
    struct Break : pegtl::seq<Break_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct But_kw : TAO_PEGTL_KEYWORD("but") {};
    struct But : pegtl::seq<But_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Case_kw : TAO_PEGTL_KEYWORD("case") {};
    struct Case : pegtl::seq<Case_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Cast_kw : TAO_PEGTL_KEYWORD("cast") {};
    struct Cast : pegtl::seq<Cast_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Class_kw : TAO_PEGTL_KEYWORD("class") {};
    struct Class : pegtl::seq<Class_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Const_kw : TAO_PEGTL_KEYWORD("const") {};
    struct Const : pegtl::seq<Const_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Continue_kw : TAO_PEGTL_KEYWORD("continue") {};
    struct Continue : pegtl::seq<Continue_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Delete_kw : TAO_PEGTL_KEYWORD("del") {};
    struct Delete : pegtl::seq<Delete_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Ellipsis_kw : TAO_PEGTL_KEYWORD("...") {};
    struct Ellipsis : pegtl::seq<Ellipsis_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Elseif_kw : pegtl::sor<TAO_PEGTL_KEYWORD("elseif"), TAO_PEGTL_KEYWORD("elsif"), TAO_PEGTL_KEYWORD("elif")> {};
    struct Elseif : pegtl::seq<Elseif_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Else_kw : TAO_PEGTL_KEYWORD("else") {};
    struct Else : pegtl::seq<Else_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Embed_kw : TAO_PEGTL_KEYWORD("embed") {};
    struct Embed : pegtl::seq<Embed_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Ensure_kw : TAO_PEGTL_KEYWORD("ensure") {};
    struct Ensure : pegtl::seq<Ensure_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Enum_kw : TAO_PEGTL_KEYWORD("enum") {};
    struct Enum : pegtl::seq<Enum_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Except_kw : TAO_PEGTL_KEYWORD("except") {};
    struct Except : pegtl::seq<Except_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Exception_kw : TAO_PEGTL_KEYWORD("exception") {};
    struct Exception : pegtl::seq<Exception_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Exclude_kw : TAO_PEGTL_KEYWORD("exclude") {};
    struct Exclude : pegtl::seq<Exclude_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Exit_kw : TAO_PEGTL_KEYWORD("exit") {};
    struct Exit : pegtl::seq<Exit_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct False_kw : pegtl::sor<TAO_PEGTL_KEYWORD("false"), TAO_PEGTL_KEYWORD("False")> {};
    struct False : pegtl::seq<False_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct File_kw : TAO_PEGTL_KEYWORD("file") {};
    struct File : pegtl::seq<File_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Final_kw : TAO_PEGTL_KEYWORD("final") {};
    struct Final : pegtl::seq<Final_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Finally_kw : TAO_PEGTL_KEYWORD("finally") {};
    struct Finally : pegtl::seq<Finally_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct For_kw : TAO_PEGTL_KEYWORD("for") {};
    struct For : pegtl::seq<For_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Forever_kw : TAO_PEGTL_KEYWORD("forever") {};
    struct Forever : pegtl::seq<Forever_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Forward_kw : pegtl::sor<TAO_PEGTL_KEYWORD("forward"), TAO_PEGTL_KEYWORD("fwd")> {};
    struct Forward : pegtl::seq<Forward_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct From_kw : TAO_PEGTL_KEYWORD("from") {};
    struct From : pegtl::seq<From_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Hidden_kw : TAO_PEGTL_KEYWORD("hidden") {};
    struct Hidden : pegtl::seq<Hidden_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct If_kw : TAO_PEGTL_KEYWORD("if") {};
    struct If : pegtl::seq<If_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Implements_kw : TAO_PEGTL_KEYWORD("implements") {};
    struct Implements : pegtl::seq<Implements_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Import_kw : TAO_PEGTL_KEYWORD("import") {};
    struct Import : pegtl::seq<Import_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct In_kw : TAO_PEGTL_KEYWORD("in") {};
    struct In : pegtl::seq<In_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Is_kw : TAO_PEGTL_KEYWORD("is") {};
    struct Is : pegtl::seq<Is_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Lambda_kw : TAO_PEGTL_KEYWORD("lambda") {};
    struct Lambda : pegtl::seq<Lambda_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct List_kw : TAO_PEGTL_KEYWORD("list") {};
    struct List : pegtl::seq<List_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Local_kw : TAO_PEGTL_KEYWORD("local") {};
    struct Local : pegtl::seq<Local_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Map_kw : TAO_PEGTL_KEYWORD("map") {};
    struct Map : pegtl::seq<Map_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Me_kw : TAO_PEGTL_KEYWORD("me") {};
    struct Me : pegtl::seq<Me_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct None_kw : pegtl::sor<TAO_PEGTL_KEYWORD("none"), TAO_PEGTL_KEYWORD("None"), TAO_PEGTL_KEYWORD("NONE")> {};
    struct None : pegtl::seq<None_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Nop_kw : pegtl::sor<TAO_PEGTL_KEYWORD("nop"), TAO_PEGTL_KEYWORD("pass")> {};
    struct Nop : pegtl::seq<Nop_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Not_kw : TAO_PEGTL_KEYWORD("not") {};
    struct Not : pegtl::seq<Not_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Operator_kw : TAO_PEGTL_KEYWORD("operator") {};
    struct Operator : pegtl::seq<Operator_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Or_kw : TAO_PEGTL_KEYWORD("or") {};
    struct Or : pegtl::seq<Or_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Otherwise_kw : TAO_PEGTL_KEYWORD("otherwise") {};
    struct Otherwise : pegtl::seq<Otherwise_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Print_kw : TAO_PEGTL_KEYWORD("print") {};
    struct Print : pegtl::seq<Print_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Private_kw : TAO_PEGTL_KEYWORD("private") {};
    struct Private : pegtl::seq<Private_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Property_kw : TAO_PEGTL_KEYWORD("property") {};
    struct Property : pegtl::seq<Property_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Protected_kw : TAO_PEGTL_KEYWORD("protected") {};
    struct Protected : pegtl::seq<Protected_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Public_kw : TAO_PEGTL_KEYWORD("public") {};
    struct Public : pegtl::seq<Public_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Raise_kw : TAO_PEGTL_KEYWORD("raise") {};
    struct Raise : pegtl::seq<Raise_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Repeat_kw : TAO_PEGTL_KEYWORD("repeat") {};
    struct Repeat : pegtl::seq<Repeat_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Require_kw : TAO_PEGTL_KEYWORD("require") {};
    struct Require : pegtl::seq<Require_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Return_kw : pegtl::sor<TAO_PEGTL_KEYWORD("return"), TAO_PEGTL_KEYWORD("ret")> {};
    struct Return : pegtl::seq<Return_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Set_kw : TAO_PEGTL_KEYWORD("set") {};
    struct Set : pegtl::seq<Set_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Static_kw : TAO_PEGTL_KEYWORD("static") {};
    struct Static : pegtl::seq<Static_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Switch_kw : TAO_PEGTL_KEYWORD("switch") {};
    struct Switch : pegtl::seq<Switch_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Todo_kw : pegtl::sor<TAO_PEGTL_KEYWORD("todo"), TAO_PEGTL_KEYWORD("TODO")> {};
    struct Todo : pegtl::seq<Todo_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct True_kw : pegtl::sor<TAO_PEGTL_KEYWORD("true"), TAO_PEGTL_KEYWORD("True")> {};
    struct True : pegtl::seq<True_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Try_kw : TAO_PEGTL_KEYWORD("try") {};
    struct Try : pegtl::seq<Try_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Type_kw : TAO_PEGTL_KEYWORD("type") {};
    struct Type : pegtl::seq<Type_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct Unnamed_kw : TAO_PEGTL_KEYWORD("unnamed") {};
    struct Unnamed : pegtl::seq<Unnamed_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Until_kw : TAO_PEGTL_KEYWORD("until") {};
    struct Until : pegtl::seq<Until_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct Volatile_kw : TAO_PEGTL_KEYWORD("volatile") {};
    struct Volatile : pegtl::seq<Volatile_kw, pegtl::not_at<NameNextChar>, Spacing1> {};

    struct When_kw : TAO_PEGTL_KEYWORD("when") {};
    struct When : pegtl::seq<When_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct While_kw : TAO_PEGTL_KEYWORD("while") {};
    struct While : pegtl::seq<While_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

    struct With_kw : TAO_PEGTL_KEYWORD("with") {};
    struct With : pegtl::seq<With_kw, pegtl::not_at<NameNextChar>, Spacing0> {};

}