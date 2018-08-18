#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2018 Philippe Schmouker, Typee project, http://www.typee.ovh

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
"""

#=============================================================================
# no import.


#=============================================================================
class FESyntaxErrors:
    """
    Description of errors strings (in English) while parsing Typee modules
    for the Typee Front-End.
    
    This class is used as a namespace for error strings.
    """    
    #-------------------------------------------------------------------------
    ABSTRACT_DEF                = 'missing type identifier after keyword "abstract"',
    ACCESS_DECL_DEF             = 'missing declaration or definition after access-qualifier clause',
    ACCESS_END                  = 'missing : at end of access-qualifier clause',
    ACCESS_QUALIFIER            = 'missing or badly formed access qualifier after : in access-qualifier clause',
    ARITHM_EXPR                 = 'missing or badly formed term in arithmetic expression',
    ARRAY_CONTAINED_TYPE        = 'missing contained type while defining an array',
    AS_IDENT                    = 'missing or badly formed identifier after keyword "as" in alias or import clause',
    ASSERT_COMMA_EXPR           = 'missing or badly formed expression after "," in assert clause',
    ASSERT_EXPR                 = 'missing or badly formed conditional expression after keyword "assert"',
    ASSIGN_EXPR                 = 'missing or badly formed expression after assignment operator',
    ASSIGN_FUNC_CALL            = 'missing or badly formed assignment or function parameters',
    ASSIGN_OPERATOR             = 'missing assignment operator',
    ATOM_DOTTED_NAME            = 'missing identifier after dot in dotted name',
    AUTO_IN_PARCL               = 'missing ) at end of auto-type clause, leads to unpaired (',
    AUTO_IN_PAROP               = 'missing ( after keyword "in" in auto-type clause',
    AUTO_IN_TYPES_LIST          = 'missing or badly formed list of types after keyword "in" in auto-type clause',
    
    BITAND_EXPR                 = 'missing or badly formed expression after bitwise operator "&"',
    BITOR_EXPR                  = 'missing or badly formed expression after bitwise operator "|"',
    BITXOR_EXPR                 = 'missing or badly formed expression after bitwise operator "^"',
    BODY_END                    = 'missing } at end of instructions block, leads to unpaired {',
    BRACKET_ENDING              = 'missing ] at end of bracket-form clause, leads to unpaired ]',
    BRACKET_FORM_EXPR           = 'missing expression in bracket form clause',
    BRACKET_FORM_LIST_OR_MAP    = 'missing list of map clause after expression in bracket form clause',
    
    CALL_OP                     = 'missing ) at end of call operator definition, leads to unpaired (',
    CASE_BODY                   = 'missing instruction or instructions block after case clause',
    CASE_EXPR                   = 'missing or badly formed expression after keyword case',
    CASTED_TYPE                 = 'missing type identifier after cast clause',
    CASTING_EXPR                = 'missing or badly formed expression in scalar type casting clause',
    CASTING_PARCL               = 'missing ) at end of scalar type casting clause, leads to unpaired (',
    CASTING_PAROP               = 'missing ( in scalar type casting clause',
    CLASS_BODY                  = 'missing class definition after class clause',
    CLASS_NAME                  = 'missing class name after keyword class',
    COMP_EXPR                   = 'missing or badly formed expression after comparison operator',
    CONST_TYPE                  = 'missing or badly formed type identifier after keyword "const"',
    CONTAINED_TYPE              = 'missing type specification after < in contained type definition',
    CONTAINER_END               = 'missing > at end of contained type definition',
    
    DECL_ASSIGN_EXPR            = 'missing or badly formed expression after = in declaration instruction',
    DECL_COMMA_IDENT            = 'missing or badly formed variable identifier after , in list of variables declaration',
    DECL_DEF_IDENT_OP           = 'missing or badly formed identifier or keyword "operator" in declaration/definition clause',
    DECL_DEF_TYPE               = 'missing or badly formed type name or constructor name',
    DECL_IDENT                  = 'missing or badly formed identifier after , in declaration instruction',
    DECR_IDENT                  = 'missing variable name after operator "--"',
    DEL_IDENT                   = 'missing or badly formed identifier in del instruction',
    DIMENSION_CONST             = 'missing or badly formed identifier of const value in dimension specification',
    DIMENSION_END               = 'missing ] at end of dimension specification, leads to unpaired [',
    DIMENSION_FLOAT             = 'float value used in dimension specification, only const integer values or identifiers are allowed',
    DOTTED_AS                   = 'missing or badly formed identifier after , in alias clause list',
    DOTTED_IDENT                = 'missing or badly formed identifier after . in dotted name',
    
    ELIF_BODY                   = 'missing instruction or block of instructions after else-if clause',
    ELIF_COND                   = 'missing condition expression in else-if clause',
    ELIF_CONDITION_BEGIN        = 'missing ( after keyword and before condition expression in else-if clause',
    ELIF_CONDITION_END          = 'missing ) at end of condition expression in else-if clause, leads to unpaired (',
    ELLIPSIS_IDENT              = 'missing or badly formed identifier after ... in ellipsis clause',
    ELSE_BODY                   = 'missing instruction or block of instructions after keyword "else"',
    EMBEDDED_CODE_END           = 'missing }} at end of external-language embed instruction, leads to unpaired {{ and finally reached end-of-file',
    EMBEDDED_LANGUAGE           = 'missing or unrecognized language identifier in external-language embed clause',
    EMBEDDED_LANGUAGE_CODE      = 'missing either file path specification or external-language block of instructions',
    END_OF_FILE                 = 'missing end-of-file marker by end of code file',
    ENSURE_COMMA_EXPR           = 'missing or badly formed expression after , in ensure clause',
    ENSURE_EXPR                 = 'missing or badly formed conditional expression after keyword "ensure"',
    EXCEPT_EXPR_BEGIN           = 'missing ( after keyword "except" in try-except instruction',
    EXCEPT_EXPR_END             = 'missing ) at end of except clause in try-except instruction, leads to unpaired (',
    EXPR_FOR_COMPREHENSION      = 'missing keyword for after expression in comprehension clause',
    
    FINAL_DEF                   = 'missing type identifier after keyword "final"',
    FOR_BODY                    = 'missing instruction or block of instructions after for clause in for instruction',
    FOR_COMPR_CONDITION         = 'missing or badly formed condition after keyword "if" in for-comprehension clause',
    FOR_COMPR_IN                = 'missing keyword "in" after identifier(s) in for-comprehension clause',
    FOR_COMPR_TARGETS           = 'missing or badly formed identifier after keyword "for" in for-comprehension clause',
    FOR_ELSE_BODY               = 'missing instruction or block of instructions after keyword "else" in for instruction',
    FOR_EXPR                    = 'missing expression(s) after keyword "in" in for instruction',
    FOR_IN                      = 'missing keyword "in" after identifier(s) in for instruction',
    FOR_PARCL                   = 'missing ) at end of for clause in for clause, leads to unpaired (',
    FOR_PAROP                   = 'missing ( after keyword "for" in for clause',
    FOR_TARGETS                 = 'missing identifier or list of identifiers after ( in for instruction',
    FOREVER_BODY                = 'missing instruction or block of instructions after forever clause in forever instruction',
    FOREVER_PARCL               = 'missing ) at end of forever clause, leads to unpaired (',
    FOREVER_PAROP               = 'missing ( after keyword "forever"',
    FROM_IDENT_IMPORT           = 'missing or badly formed module identifier after keyword "from" in from-import instruction',
    FROM_IMPORT                 = 'missing keyword "import" after module identifier in from-import instruction',
    FROM_IMPORT_IDENT           = 'missing expected keyword "all" or expected ( or expected identifier after keyword "import" in from-import instruction',
    FROM_IMPORT_LIST            = 'missing or badly formed identifier within list of imports in from-import instruction',
    FUNCTION_ARGS               = 'missing or badly formed arguments list in function or method definition',
    FUNCTION_ARGS_BEGIN         = 'missing ( after function name in function call instruction',
    FUNCTION_ARGS_END           = 'missing ) at end arguments list in the declaration of a function, leads to unpaired (',
    FUNCTION_ARGS_LIST          = 'missing argument after , in arguments list of a function or a method call',
    FUNCTION_ARGS_PAROP         = 'missing ( after function name in function definition',
    FUNCTION_BODY               = 'missing instruction or block of instructions in function or method definition',
    FUNCTION_CALL               = 'missing arguments list (may be empty) after function or method name',
    FUNCTION_CALL_BEGIN         = 'missing ( after function or method name',
    FUNCTION_CALL_END           = 'missing ) at end of function or method call, leads to unpaired (',
    
    IF_BODY                     = 'missing instruction or block of instructions after if clause in if instruction',
    IF_COMPR_COND               = 'missing condition of unnamed function definition after keyword "if" in if-comprehension clause',
    IF_COND                     = 'missing condition expression after keyword "if" in inlined if clause or in if instruction',
    IF_CONDITION_BEGIN          = 'missing ( after keyword "if" in if clause',
    IF_CONDITION_END            = 'missing ) after condition in if clause, leads to unpaired (',
    IF_ELSE                     = 'missing keyword "else" in inlined if clause',
    IF_ELSE_EXPR                = 'missing expression after keyword "else" in inlined if clause',
    IMPORT_IDENT                = 'missing or badly formed identifier after , in list of identifiers in import-as instruction',
    IMPORT_MODULE               = 'missing or badly formed module identifier in import instruction',
    INCR_IDENT                  = 'missing variable name after operator "++"',
    INHERITANCE_CLASS           = 'missing or badly formed class name in class inheritance specification',
    INSTANCE_OF                 = 'missing or badly formed class name after operator "->"',
    
    LIST_COMMA_EXPR             = 'missing or badly formed expression after , in list of expressions',
    LIST_COMMA_IDENT            = 'missing or badly formed identifier after , in list of expressions',
    LIST_END                    = 'missing ] at end of list specification, leads to unpaired [',
    LIST_EXPR                   = 'missing or badly formed expression after [ in list specification',
    
    MAP_EXPR                    = 'missing or badly formed expression after : in map-form clause or map item specification',
    MAP_ITEM_SEP                = 'missing : after expression in map item specification',
    MAP_LIST_COMPR              = 'missing "," or missing/badly-formed for-comprehension in map form',
    MAP_LIST_ITEM               = 'missing or badly formed map item after , within list of items in map specification',
    METHOD_OPERATOR             = 'missing or badly formed operator identifier or method name after type specification',
    
    NOT_COND                    = 'missing or badly formed condition expression after keyword "not"',
    NOT_IN                      = 'missing keyword "in" after keyword "not"',
    
    OP_IDENT_DECL_DEF           = 'missing keyword operator in definition instruction or badly formed identifier in declaration instruction',
    OPERATOR_ARGS               = 'missing or badly formed arguments specification in operator definition',
    OPERATOR_BODY               = 'missing instruction or block of instructions in operator definition',
    OPERATOR_OP                 = 'missing or badly formed operator identifier in operator definition',
    OR_EXPR                     = 'missing or badly formed numerical expression after bitwise operator |',
    OR_TEST                     = 'missing or badly formed comparison expression after keyword "or"',
    
    PARENTH_EXPR                = 'missing or badly formed expression in parenthesis-form clause',
    POWER_EXPR                  = 'missing or badly formed expression after power operator',
    
    RAISE_EXPR                  = 'missing or badly formed expression after keyword "raise" in raise instruction',
    RAISE_FROM_EXPR             = 'missing or badly formed expression after keyword "from" in raise instruction',
    REF_IDENT                   = 'missing or badly formed object identifier after "@" in reference clause',
    REPEAT_BODY                 = 'missing instruction or block of instructions after keyword "repeat" in repeat-until instruction',
    REPEAT_UNTIL                = 'missing keyword "until" after instruction(s) in repeat-until instruction',
    REQUIRE_COMMA_EXPR          = 'missing or badly formed expression after , in require instruction',
    REQUIRE_EXPR                = 'missing or badly formed conditional expression after keyword "require"',
    
    SHIFT_EXPR                  = 'missing or badly formed arithmetic expression after bitwise shift operator',
    SCALAR_TYPE                 = 'missing or badly formed scalar type identifier',
    SLICE_END                   = 'missing ] or ) at end of slice (i.e. interval) specification, leads to unpaired [',
    STATEMENT_END               = 'missing ; at end of instruction',
    STATIC_DECL_DEF             = 'missing or badly formed declaration or definition after keywsord static',
    STRING_FUNC_ARGS            = 'missing or badly formed list of arguments after function name to be applied to a string',
    STRING_FUNC_IDENT           = 'missing or badly formed function name after "." to be applied to a string',
    SUBSCR_SLICE_EXPR           = 'missing or badly formed expression in subscription or slicing specification',
    SUBCSR_SLICE_END            = 'missing ] at end of subscription or slicing specification, leads to unpaired [',
    SWITCH_BODY_BEGIN           = 'missing { after switch clause and before block of case clauses in switch instruction',
    SWITCH_BODY_END             = 'missing } at end of case clauses in switch instruction, leads to unpaired {',
    SWITCH_ELSE_BODY            = 'missing instruction or instructions block after keyword "else" of switch statement',
    SWITCH_EXPR                 = 'missing or badly formed expression after ( in switch instruction',
    SWITCH_EXPR_BEGIN           = 'missing ( after keyword "switch" in switch instruction',
    SWITCH_EXPR_END             = 'missing ) at end of switch clause in switch instruction, leads to unpaired (',
    
    TARGET_IDENT                = 'missing or badly formed identifier',
    TARGET_TYPE                 = 'missing or badly formed typed identifier after "," in list of types identifiers',
    TEMPLATE_COMMA_COND         = 'missing or badly formed condition or identifier after "," in template arguments specification',
##    TEMPLATE_CONST_ASSIGN       = 'missing = within constant value specification in template arguments definition',
    TEMPLATE_CONST_EXPR         = 'missing or badly formed scalar expression within constant value specification in template arguments definition',
    TEMPLATE_CONST_IDENT        = 'missing or badly formed identifier as a constant value in template arguments definition',
##    TEMPLATE_CONST_KW           = 'badly formed identifier or missing keyword "const" in template arguments definition',
##    TEMPLATE_CONST_TYPE         = 'missing or badly formed scalar type identifier after keyword "const" in template arguments definition',
    TEMPLATE_DEF_CONST_TYPE     = 'missing or badly formed type identifier after keyword "const" in template definition',
    TEMPLATE_DEF_IDENT_CONST    = 'missing or badly formed identifier name or keyword "const" in template definition',
    TEMPLATE_ENDING             = 'missing > at end of template clause, leads to unpaired <',
    TEMPLATE_COND               = 'missing or badly formed condition in template arguments specification',
    TEMPLATE_SPECIFICATION      = 'missing or badly formed expression or identifier in template arguments specification',
    TEMPLATE_TYPES_LIST         = 'missing or badly formed expression or type identifier within types-and-expressions list in template specification',
    TRY_AS_IDENT                = 'missing or badly formed identifier after keyword "as" in except clause',
    TRY_BODY                    = 'missing instruction or instructions block after keyword "try"',
    TRY_ELSE_BODY               = 'missing instruction or instructions block after keyword "else" in try-except instruction',
    TRY_EXCEPT_BODY             = 'missing instruction or instructions block after except clause in try-except instruction',
    TRY_FINALLY_BODY            = 'missing instruction or instructions block after keyword "finally" in try-except instruction',
    TYPE_ALIAS                  = 'missing or badly formed type identifier after keyword "type" in type alias instruction',
    TYPE_AS                     = 'missing keyword "as" after type identifier in type alias instruction',
    TYPE_AS_IDENT               = 'missing or badly formed identifier after keyword "as" in type alias instruction',
    TYPES_LIST                  = 'missing or badly formed list of type identifiers after (',
    TYPES_LIST_END              = 'missing ) at end of type identifiers list, leads to unpaired (',
    TYPE_LIST_IDENT             = 'missing or badly formed identifier in list of typed arguments',
    TYPES_LIST_TYPE             = 'missing or badly formed type identifier in list of types',
    TYPED_TARGET_IDENT          = 'missing or badly formed identifier or typed identifier within list of targets in for-comprehension clause or for instruction clause',
    
    UNNAMED_ARGS                = 'missing or badly formed list of arguments in unnamed function definition',
    UNNAMED_BODY                = 'missing instruction or instructions blocks in unnamed function definition',
    UNNAMED_TYPE                = 'missing or badly formed type identifier after "unnamed" in unnamed function definition',
    UNPAIRED_PAROP              = 'missing ), leads to unpaired (',
    UNTIL_BEGIN                 = 'missing ( after keyword "until" in repeat-until instruction',
    UNTIL_END                   = 'missing ) after keyword "until" in repeat-until instruction, leads to unpaired (',
    UNTIL_EXPR                  = 'missing or badly formed conditional expression after ( in until clause',
    UNTIL_STATEMENT_END         = 'missing ; at end of repeat-until instruction',
    
    VAR_NAME                    = 'missing variable identifier after keyword "volatile"',
    VAR_TYPE                    = 'missing type identifier in declaration or definition instruction',
    VOLATILE_MEM_KW             = 'missing @ before memory address in volatile variable declaration',
    VOLATILE_MEM_ADDR           = 'missing or badly formed integer value for memory address after @ in volatile variable declaration',
    VOLATILE_TYPE               = 'missing or badly formed type identifier after keyword "volatile"',
    
    WHILE_BODY                  = 'missing instruction or instructions block after while clause in while instruction',
    WHILE_COND                  = 'missing or badly formed conditional expression after ( in while clause',
    WHILE_COND_BEGIN            = 'missing ( after keyword "while"',
    WHILE_COND_END              = 'missing ) at end of conditional expression in while clause, leads to unpaired (',
    WHILE_ELSE_BODY             = 'missing instruction or instructions block after keyword "else" in while instruction',
    WITH_AS_IDENT               = 'missing or badly formed identifier after keyword "as" in with clause',
    WITH_BODY                   = 'missing instruction or instructions block after with clause in with instruction',
    WITH_EXPR                   = 'missing or badly formed expression after keyword "with"',
    WITH_LIST_COMMA             = 'missing or badly formed with-as clause in list of with-as clauses'  ## notice: we already know that this kind of error will never be detected as such

#=====   end of   FrontEnd.Errors.fe_syntax_errors   =====#
        