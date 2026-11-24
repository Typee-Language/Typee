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


namespace tlang_rules
{
    //=====   Expressions Rules   ===========================================
    struct Expression;


    //=====   Keywords Rules   ==============================================
    struct Abstract_kw;
    struct Abstract;

    struct All_kw;
    struct All;

    struct And_kw;
    struct And;

    struct Array_kw;
    struct Array;

    struct As_kw;
    struct As;

    struct Assert_kw;
    struct Assert;

    struct AutoType_kw;
    struct AutoType;

    struct Break_kw;
    struct Break;

    struct But_kw;
    struct But;

    struct Case_kw;
    struct Case;

    struct Cast_kw;
    struct Cast;

    struct Class_kw;
    struct Class;

    struct Const_kw;
    struct Const;

    struct Continue_kw;
    struct Continue;

    struct Delete_kw;
    struct Delete;

    struct Ellipsis_kw;
    struct Ellipsis;

    struct Elseif_kw;
    struct Elseif;

    struct Else_kw;
    struct Else;

    struct Embed_kw;
    struct Embed;

    struct Ensure_kw;
    struct Ensure;

    struct Enum_kw;
    struct Enum;

    struct Except_kw;
    struct Except;

    struct Exception_kw;
    struct Exception;

    struct Exclude_kw;
    struct Exclude;

    struct Exit_kw;
    struct Exit;

    struct False_kw;
    struct False;

    struct File_kw;
    struct File;

    struct Final_kw;
    struct Final;

    struct Finally_kw;
    struct Finally;

    struct For_kw;
    struct For;

    struct Forever_kw;
    struct Forever;

    struct Forward_kw;
    struct Forward;

    struct From_kw;
    struct From;

    struct Hidden_kw;
    struct Hidden;

    struct If_kw;
    struct If;

    struct Implements_kw;
    struct Implements;

    struct Import_kw;
    struct Import;

    struct In_kw;
    struct In;

    struct Is_kw;
    struct Is;

    struct Lambda_kw;
    struct Lambda;

    struct List_kw;
    struct List;

    struct Local_kw;
    struct Local;

    struct Map_kw;
    struct Map;

    struct Me_kw;
    struct Me;

    struct None_kw;
    struct None;

    struct Nop_kw;
    struct Nop;

    struct Not_kw;
    struct Not;

    struct Operator_kw;
    struct Operator;

    struct Or_kw;
    struct Or;

    struct Otherwise_kw;
    struct Otherwise;

    struct Print_kw;
    struct Print;

    struct Private_kw;
    struct Private;

    struct Property_kw;
    struct Property;

    struct Protected_kw;
    struct Protected;

    struct Public_kw;
    struct Public;

    struct Raise_kw;
    struct Raise;

    struct Repeat_kw;
    struct Repeat;

    struct Require_kw;
    struct Require;

    struct Return_kw;
    struct Return;

    struct Set_kw;
    struct Set;

    struct Static_kw;
    struct Static;

    struct Switch_kw;
    struct Switch;

    struct Todo_kw;
    struct Todo;

    struct True_kw;
    struct True;

    struct Try_kw;
    struct Try;

    struct Type_kw;
    struct Type;

    struct Unnamed_kw;
    struct Unnamed;

    struct Until_kw;
    struct Until;

    struct Volatile_kw;
    struct Volatile;

    struct When_kw;
    struct When;

    struct While_kw;
    struct While;

    struct With_kw;
    struct With;


    //======   Miscelaneous Rules   =========================================
    struct AlphaChar;
    struct AlphaNumChar;
    struct Dot;
    struct DottedName;
    struct EndOfLine;
    struct Identifier;
    struct Name;
    struct NameFirstChar;
    struct NameNextChar;
    struct SemiColon;
    struct Spacing;
    struct Spacing0;
    struct Spacing1;
    struct Underscore;


    //=====   Types Rules   =================================================
    struct ArrayType;
    struct AutoType;
    struct ContainedType;
    struct ContainerType;
    struct FileType;
    struct FixedDimension;
    struct FixedDimensions;
    struct GenericContainerType;
    struct GenericScalarType;
    struct ListType;
    struct MapContainedTypes;
    struct MapType;
    struct NotConstType;
    struct ScalarType;
    struct ScalarTypeOrIdentifier;
    struct SetType;
    struct SimpleType;
    struct StringType;
    struct TemplatedType;
    struct Type;
    struct TypeCasting;
    struct TypesAndExprsList;
    struct TypesList;
    struct VectorType;

}


//=====   Mandatory includes    =============================================
#include "miscelaneous/miscelaneous.h"
