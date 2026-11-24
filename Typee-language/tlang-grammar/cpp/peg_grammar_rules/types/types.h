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
#include "tao/pegtl/pegtl_string.hpp"
#include "tao/pegtl/rules.hpp"

#include "../tlang_grammar_rules.h"


namespace tlang_rules
{
    //=======================================================================
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


    //=======================================================================
    struct ArrayType : pegtl::seq<Array, ContainedType> {};


    struct AutoType : pegtl::seq<
                          AutoType,
                          pegtl::opt<
                              pegtl::seq<
                                  In,
                                  Spacing0,
                                  pegtl::one< '(' >,
                                  Spacing0,
                                  TypesList,
                                  pegtl::one< ')' >,
                                  Spacing0
                              >
                          >
                      > {};


    struct ContainedType :  pegtl::seq<
                                pegtl::one< '<' >,
                                Spacing0,
                                Type,
                                Spacing0,
                                pegtl::one< '>' >,
                                Spacing0
                            > {};


    struct ContainerType :  pegtl::sor<
                                ArrayType,
                                VectorType,
                                ListType,
                                MapType,
                                SetType
                            > {};


    struct FileType : pegtl::seq<File, ContainedType> {};


    struct FixedDimension : pegtl::seq<
                                pegtl::one< '[' >,
                                Spacing0,
                                Expression,         // Notice: expression must get an integer value
                                Spacing0,
                                pegtl::one< ']' >,
                                Spacing0
                            > {};


    struct FixedDimensions : pegtl::plus<FixedDimension> {};


    struct GenericContainerType : TAO_PEGTL_KEYWORD("_container_") {};


    struct GenericScalarType : pegtl::sor<
        pegtl::seq<TAO_PEGTL_KEYWORD("_int_")    , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
        pegtl::seq<TAO_PEGTL_KEYWORD("_uint_")   , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
        pegtl::seq<TAO_PEGTL_KEYWORD("_float_")  , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
        pegtl::seq<TAO_PEGTL_KEYWORD("_numeric_"), pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
        pegtl::seq<TAO_PEGTL_KEYWORD("_str_")    , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
        pegtl::seq<TAO_PEGTL_KEYWORD("_complex_"), pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
        pegtl::seq<TAO_PEGTL_KEYWORD("_scalar_") , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
    > {};


    struct ListType : pegtl::seq<List, pegtl::opt<ContainedType>> {};


    struct MapContainedTypes : pegtl::seq<
                                   pegtl::one< '<' >,
                                   Spacing0,
                                   Type,
                                   Spacing0,
                                   pegtl:one< ',' >,
                                   Spacing0,
                                   Type,
                                   Spacing0,
                                   pegtl::one< '>' >
                               > {};


    struct MapType : pegtl::seq<Map, MapContainedTypes> {};


    struct NotConstType : pegtl::sor<TemplatedType, SimpleType, None> {};


    struct ScalarType : pegtl::sor<
                            pegtl::seq<TAO_PEGTL_KEYWORD("bigint")    , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("bool")      , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("char16")    , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("char")      , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("complex32") , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("complex64") , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("complex128"), pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("float32")   , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("float64")   , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("float128")  , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("int8")      , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("int16")     , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("int32")     , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("int64")     , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("int128")    , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("slice")     , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("uint8")     , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("uint16")    , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("uint32")    , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("uint64")    , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            pegtl::seq<TAO_PEGTL_KEYWORD("uint128")   , pegtl::not_at<NameNextChar>, pegtl::not_at<NameNextChar>, Spacing0> {};
                            StringType
                        > {};


    struct ScalarTypeOrIdentifier : pegtl::sor<ScalarType, Identifier> {};


    struct SetType : pegtl::seq<Set, pegtl::opt<ContainedType>> {};


    struct SimpleType : pegtl::sor<
                            AutoType,
                            pegtl::seq<pegtl::one<'('>, Spacing0, TypesList, pegtl::one<')'>, Spacing0>,
                            ContainerType,
                            Enum,
                            FileType,
                            pegtl::seq<ScalarType, pegtl::opt<FixedDimensions>>
                        > {};


    struct StringType : pegtl::sor<
                            TAO_PEGTL_KEYWORD("str16"),
                            TAO_PEGTL_KEYWORD("str")
                        > {};


    struct TemplatedType  : pegtl::seq<
                                Identifier,
                                pegtl::opt<
                                    pegtl::one< '<' >,
                                    Spacing0,
                                    TypesAndExprsList,
                                    Spacing0,
                                    pegtl::one< '>' >
                                >,
                                pegtl::opt<FixedDimensions>
                            > {};


    struct Type   : pegtl::sor<
                        pegtm::seq<
                            pegtl::opt<Const>,
                            pegtl::sor<TemplatedType, SimpleType>
                        >,
                        None
                    > {};


    struct TypeCasting : pegtl::seq<
                             pegtl::one< '(' >,
                             pegtl::sor<ScalarType, Identifier>,  // Notice: identifier must be an alias to a scalar type
                             pegtl::one< ')' >,
                             Spacing0
                         > {};


    struct TypesAndExprsList  : pegtl::seq<
                                    pegtl::sor<Epression, Type>,
                                    Spacing0,
                                    pegtl::star<
                                        pegtl::one< ',' >,
                                        Spacing0,
                                        pegtl::sor(Expression, Type),
                                        Spacing0
                                    >
                                > {};
            


    struct TypesList  : pegtl::seq<
                            Type,
                            Spacing0,
                            pegtl::star<
                                pegtl::one< ',' >,
                                Spacing0,
                                Type,
                                Spacing0
                            >
                        > {};


    struct VectorType : pegtl::seq<
                            Vector,
                            pegtl::one< '<' >,
                            Spacing0,
                            Type,
                            Spacing0,
                            pegtl::one< '>' >,
                            Spacing0,
                            FixedDimension
                        > {};

}
