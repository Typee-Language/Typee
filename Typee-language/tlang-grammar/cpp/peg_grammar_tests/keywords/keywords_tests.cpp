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
#pragma warning(disable:4099)   // Notice: to avoid this type of Linker warning with VS2026
#include "gtest/gtest.h"

#include <format>
#include <string>
#include <vector>

#include "peg_grammar_rules/keywords/keywords.h"  // Notice: have a look to the included paths in the project definition
#include "tlang_cpp/front_end/peg_parser/fe_parser.h"     // Notice: have a look to the included paths in the project definition

using namespace tlang_rules;


//===========================================================================
namespace keywords_rules
{

    //=========================================================
    // Keywords Rules GTest Fixture
    class KeywordsFixtureTest : public testing::Test
    {
    protected:
        KeywordsFixtureTest()
            : testing::Test()
        {}

        virtual ~KeywordsFixtureTest()
        {}

        ty_fe::FEParser fe_parser{ "" };
        std::string spaces{ " \n\r\t\v\f" };
    };


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestAbstractRule)
    {
        const std::vector<std::string> expected_keywords{ "abstract" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Abstract>(kw));

            ASSERT_FALSE(fe_parser.parse<Abstract>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Abstract>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Abstract>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Abstract>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Abstract>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'abstract' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Abstract>(""))
            << "end-of-file character finally is understood as the 'abstract' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestAllRule)
    {
        const std::vector<std::string> expected_keywords{ "all" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<All>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<All>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<All>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<All>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<All>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<All>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'all' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<All>(""))
            << "end-of-file character finally is understood as the 'all' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestAndRule)
    {
        const std::vector<std::string> expected_keywords{ "and" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<And>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<And>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<And>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<And>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<And>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<And>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'and' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<And>(""))
            << "end-of-file character finally is understood as the 'and' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestArrayRule)
    {
        const std::vector<std::string> expected_keywords{ "array" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Array>(kw));

            ASSERT_FALSE(fe_parser.parse<Array>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Array>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Array>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Array>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Array>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'array' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Array>(""))
            << "end-of-file character finally is understood as the 'array' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestAsRule)
    {
        const std::vector<std::string> expected_keywords{ "as" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<As>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<As>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<As>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<As>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<As>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<As>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'as' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<As>(""))
            << "end-of-file character finally is understood as the 'as' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestAssertRule)
    {
        const std::vector<std::string> expected_keywords{ "assert" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Assert>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Assert>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Assert>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Assert>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Assert>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Assert>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'assert' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Assert>(""))
            << "end-of-file character finally is understood as the 'assert' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestBreakRule)
    {
        const std::vector<std::string> expected_keywords{ "break" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Break>(kw));

            ASSERT_FALSE(fe_parser.parse<Break>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Break>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Break>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Break>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Break>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'break' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Break>(""))
            << "end-of-file character finally is understood as the 'break' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestButRule)
    {
        const std::vector<std::string> expected_keywords{ "but" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<But>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<But>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<But>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<But>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<But>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<But>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'but' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<But>(""))
            << "end-of-file character finally is understood as the 'but' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestCaseRule)
    {
        const std::vector<std::string> expected_keywords{ "case" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Case>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Case>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Case>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Case>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Case>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Case>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'case' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Case>(""))
            << "end-of-file character finally is understood as the 'case' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestCastRule)
    {
        const std::vector<std::string> expected_keywords{ "cast" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Cast>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Cast>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Cast>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Cast>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Cast>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Cast>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'cast' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Cast>(""))
            << "end-of-file character finally is understood as the 'cast' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestClassRule)
    {
        const std::vector<std::string> expected_keywords{ "class" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Class>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Class>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Class>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Class>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Class>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Class>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'class' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Class>(""))
            << "end-of-file character finally is understood as the 'class' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestConstRule)
    {
        const std::vector<std::string> expected_keywords{ "const" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Const>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Const>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Const>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Const>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Const>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Const>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'const' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Const>(""))
            << "end-of-file character finally is understood as the 'const' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestContinueRule)
    {
        const std::vector<std::string> expected_keywords{ "continue" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Continue>(kw));

            ASSERT_FALSE(fe_parser.parse<Continue>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Continue>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Continue>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Continue>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Continue>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'continue' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Continue>(""))
            << "end-of-file character finally is understood as the 'continue' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestDeleteRule)
    {
        const std::vector<std::string> expected_keywords{ "del" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Delete>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Delete>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Delete>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Delete>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Delete>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Delete>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'del' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Delete>(""))
            << "end-of-file character finally is understood as the 'del' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestEllipsisRule)
    {
        const std::vector<std::string> expected_keywords{ "..." };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Ellipsis>(kw));

            ASSERT_FALSE(fe_parser.parse<Ellipsis>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Ellipsis>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Ellipsis>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Ellipsis>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Ellipsis>(kw + '0'))
                << std::format("tested word '{}' finally checks the '...' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Ellipsis>(""))
            << "end-of-file character finally is understood as the '...' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestElseRule)
    {
        const std::vector<std::string> expected_keywords{ "else" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Else>(kw));

            ASSERT_FALSE(fe_parser.parse<Else>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Else>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Else>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Else>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Else>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'else' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Else>(""))
            << "end-of-file character finally is understood as the 'else' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestElseifRule)
    {
        const std::vector<std::string> expected_keywords{ "elseif", "elsif", "elif" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Elseif>(kw));

            ASSERT_FALSE(fe_parser.parse<Elseif>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Elseif>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Elseif>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Elseif>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Elseif>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'elseif' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Elseif>(""))
            << "end-of-file character finally is understood as the 'elseif' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestEmbedRule)
    {
        const std::vector<std::string> expected_keywords{ "embed" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Embed>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Embed>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Embed>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Embed>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Embed>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Embed>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'embed' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Embed>(""))
            << "end-of-file character finally is understood as the 'embed' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestEnsureRule)
    {
        const std::vector<std::string> expected_keywords{ "ensure" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Ensure>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Ensure>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Ensure>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Ensure>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Ensure>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Ensure>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'ensure' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Ensure>(""))
            << "end-of-file character finally is understood as the 'ensure' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestEnumRule)
    {
        const std::vector<std::string> expected_keywords{ "enum" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Enum>(kw));

            ASSERT_FALSE(fe_parser.parse<Enum>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Enum>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Enum>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Enum>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Enum>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'enum' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Enum>(""))
            << "end-of-file character finally is understood as the 'enum' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestExceptRule)
    {
        const std::vector<std::string> expected_keywords{ "except" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Except>(kw));

            ASSERT_FALSE(fe_parser.parse<Except>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Except>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Except>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Except>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Except>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'except' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Except>(""))
            << "end-of-file character finally is understood as the 'except' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestExceptionRule)
    {
        const std::vector<std::string> expected_keywords{ "exception" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Exception>(kw));

            ASSERT_FALSE(fe_parser.parse<Exception>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Exception>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Exception>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Exception>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Exception>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'exception' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Exception>(""))
            << "end-of-file character finally is understood as the 'exception' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestExcludeRule)
    {
        const std::vector<std::string> expected_keywords{ "exclude" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Exclude>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Exclude>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Exclude>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Exclude>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Exclude>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Exclude>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'exclude' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Exclude>(""))
            << "end-of-file character finally is understood as the 'exclude' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestExitRule)
    {
        const std::vector<std::string> expected_keywords{ "exit" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Exit>(kw));

            ASSERT_FALSE(fe_parser.parse<Exit>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Exit>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Exit>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Exit>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Exit>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'exit' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Exit>(""))
            << "end-of-file character finally is understood as the 'exit' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestFalseRule)
    {
        const std::vector<std::string> expected_keywords{ "false", "False" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<False>(kw));

            ASSERT_FALSE(fe_parser.parse<False>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<False>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<False>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<False>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<False>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'false' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<False>(""))
            << "end-of-file character finally is understood as the 'false' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestFileRule)
    {
        const std::vector<std::string> expected_keywords{ "file" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<File>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<File>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<File>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<File>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<File>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<File>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'file' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<File>(""))
            << "end-of-file character finally is understood as the 'file' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestFinalRule)
    {
        const std::vector<std::string> expected_keywords{ "final" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Final>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Final>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Final>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Final>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Final>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Final>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'final' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Final>(""))
            << "end-of-file character finally is understood as the 'final' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestFinallyRule)
    {
        const std::vector<std::string> expected_keywords{ "finally" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Finally>(kw));

            ASSERT_FALSE(fe_parser.parse<Finally>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Finally>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Finally>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Finally>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Finally>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'finally' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Finally>(""))
            << "end-of-file character finally is understood as the 'finally' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestForRule)
    {
        const std::vector<std::string> expected_keywords{ "for" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<For>(kw));

            ASSERT_FALSE(fe_parser.parse<For>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<For>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<For>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<For>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<For>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'for' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<For>(""))
            << "end-of-file character finally is understood as the 'for' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestForeverRule)
    {
        const std::vector<std::string> expected_keywords{ "forever" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Forever>(kw));

            ASSERT_FALSE(fe_parser.parse<Forever>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Forever>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Forever>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Forever>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Forever>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'forever' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Forever>(""))
            << "end-of-file character finally is understood as the 'forever' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestForwardRule)
    {
        const std::vector<std::string> expected_keywords{ "forward", "fwd" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Forward>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Forward>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Forward>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Forward>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Forward>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Forward>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'forward' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Forward>(""))
            << "end-of-file character finally is understood as the 'forward' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestFromRule)
    {
        const std::vector<std::string> expected_keywords{ "from" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<From>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<From>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<From>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<From>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<From>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<From>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'from' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<From>(""))
            << "end-of-file character finally is understood as the 'from' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestHiddenRule)
    {
        const std::vector<std::string> expected_keywords{ "hidden" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Hidden>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Hidden>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Hidden>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Hidden>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Hidden>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Hidden>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'hidden' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Hidden>(""))
            << "end-of-file character finally is understood as the 'hidden' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestIfRule)
    {
        const std::vector<std::string> expected_keywords{ "if" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<If>(kw));

            ASSERT_FALSE(fe_parser.parse<If>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<If>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<If>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<If>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<If>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'if' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<If>(""))
            << "end-of-file character finally is understood as the 'if' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestImplementsRule)
    {
        const std::vector<std::string> expected_keywords{ "implements" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Implements>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Implements>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Implements>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Implements>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Implements>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Implements>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'implements' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Implements>(""))
            << "end-of-file character finally is understood as the 'implements' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestImportRule)
    {
        const std::vector<std::string> expected_keywords{ "import" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Import>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Import>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Import>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Import>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Import>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Import>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'import' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Import>(""))
            << "end-of-file character finally is understood as the 'import' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestInRule)
    {
        const std::vector<std::string> expected_keywords{ "in" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<In>(kw));

            ASSERT_FALSE(fe_parser.parse<In>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<In>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<In>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<In>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<In>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'in' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<In>(""))
            << "end-of-file character finally is understood as the 'in' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestIsRule)
    {
        const std::vector<std::string> expected_keywords{ "is" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Is>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Is>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Is>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Is>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Is>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Is>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'is' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Is>(""))
            << "end-of-file character finally is understood as the 'is' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestLambdaRule)
    {
        const std::vector<std::string> expected_keywords{ "lambda" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Lambda>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Lambda>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Lambda>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Lambda>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Lambda>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Lambda>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'lambda' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Lambda>(""))
            << "end-of-file character finally is understood as the 'lambda' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestListRule)
    {
        const std::vector<std::string> expected_keywords{ "list" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<List>(kw));

            ASSERT_FALSE(fe_parser.parse<List>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<List>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<List>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<List>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<List>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'list' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<List>(""))
            << "end-of-file character finally is understood as the 'list' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestLocalRule)
    {
        const std::vector<std::string> expected_keywords{ "local" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Local>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Local>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Local>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Local>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Local>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Local>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'local' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Local>(""))
            << "end-of-file character finally is understood as the 'local' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestMapRule)
    {
        const std::vector<std::string> expected_keywords{ "map" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Map>(kw));

            ASSERT_FALSE(fe_parser.parse<Map>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Map>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Map>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Map>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Map>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'map' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Map>(""))
            << "end-of-file character finally is understood as the 'map' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestMeRule)
    {
        const std::vector<std::string> expected_keywords{ "me" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Me>(kw));

            ASSERT_FALSE(fe_parser.parse<Me>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Me>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Me>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Me>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Me>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'me' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Me>(""))
            << "end-of-file character finally is understood as the 'me' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestNoneRule)
    {
        const std::vector<std::string> expected_keywords{ "none", "None", "NONE" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<None>(kw));

            ASSERT_FALSE(fe_parser.parse<None>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<None>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<None>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<None>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<None>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'none' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<None>(""))
            << "end-of-file character finally is understood as the 'none' keyword?!?";
    }


    //=========================================================

    TEST_F(KeywordsFixtureTest, TestNopRule)
    {
        const std::vector<std::string> expected_keywords{ "nop", "pass" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Nop>(kw));

            ASSERT_FALSE(fe_parser.parse<Nop>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Nop>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Nop>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Nop>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Nop>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'nop' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Nop>(""))
            << "end-of-file character finally is understood as the 'nop' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestNotRule)
    {
        const std::vector<std::string> expected_keywords{ "not" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Not>(kw));

            ASSERT_FALSE(fe_parser.parse<Not>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Not>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Not>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Not>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Not>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'not' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Not>(""))
            << "end-of-file character finally is understood as the 'not' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestOperatorRule)
    {
        const std::vector<std::string> expected_keywords{ "operator" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Operator>(kw));

            ASSERT_FALSE(fe_parser.parse<Operator>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Operator>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Operator>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Operator>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Operator>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'operator' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Operator>(""))
            << "end-of-file character finally is understood as the 'operator' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestOrRule)
    {
        const std::vector<std::string> expected_keywords{ "or" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Or>(kw));

            ASSERT_FALSE(fe_parser.parse<Or>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Or>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Or>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Or>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Or>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'or' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Or>(""))
            << "end-of-file character finally is understood as the 'or' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestOtherwiseRule)
    {
        const std::vector<std::string> expected_keywords{ "otherwise" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Otherwise>(kw));

            ASSERT_FALSE(fe_parser.parse<Otherwise>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Otherwise>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Otherwise>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Otherwise>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Otherwise>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'otherwise' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Otherwise>(""))
            << "end-of-file character finally is understood as the 'otherwise' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestPrintRule)
    {
        const std::vector<std::string> expected_keywords{ "print" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Print>(kw));

            ASSERT_FALSE(fe_parser.parse<Print>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Print>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Print>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Print>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Print>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'print' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Print>(""))
            << "end-of-file character finally is understood as the 'print' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestPrivateRule)
    {
        const std::vector<std::string> expected_keywords{ "private" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Private>(kw));

            ASSERT_FALSE(fe_parser.parse<Private>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Private>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Private>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Private>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Private>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'private' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Private>(""))
            << "end-of-file character finally is understood as the 'private' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestPropertyRule)
    {
        const std::vector<std::string> expected_keywords{ "property" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Property>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Property>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Property>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Property>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Property>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Property>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'property' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Property>(""))
            << "end-of-file character finally is understood as the 'property' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestProtectedRule)
    {
        const std::vector<std::string> expected_keywords{ "protected" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Protected>(kw));

            ASSERT_FALSE(fe_parser.parse<Protected>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Protected>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Protected>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Protected>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Protected>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'protected' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Protected>(""))
            << "end-of-file character finally is understood as the 'protected' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestPublicRule)
    {
        const std::vector<std::string> expected_keywords{ "public" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Public>(kw));

            ASSERT_FALSE(fe_parser.parse<Public>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Public>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Public>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Public>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Public>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'public' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Public>(""))
            << "end-of-file character finally is understood as the 'public' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestRaiseRule)
    {
        const std::vector<std::string> expected_keywords{ "raise" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Raise>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Raise>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Raise>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Raise>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Raise>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Raise>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'raise' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Raise>(""))
            << "end-of-file character finally is understood as the 'raise' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestRepeatRule)
    {
        const std::vector<std::string> expected_keywords{ "repeat" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Repeat>(kw));

            ASSERT_FALSE(fe_parser.parse<Repeat>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Repeat>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Repeat>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Repeat>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Repeat>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'repeat' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Repeat>(""))
            << "end-of-file character finally is understood as the 'repeat' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestRequireRule)
    {
        const std::vector<std::string> expected_keywords{ "require" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Require>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Require>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Require>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Require>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Require>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Require>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'require' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Require>(""))
            << "end-of-file character finally is understood as the 'require' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestReturnRule)
    {
        const std::vector<std::string> expected_keywords{ "return", "ret" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Return>(kw));

            ASSERT_FALSE(fe_parser.parse<Return>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Return>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Return>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Return>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Return>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'return' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Return>(""))
            << "end-of-file character finally is understood as the 'return' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestSetRule)
    {
        const std::vector<std::string> expected_keywords{ "set" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Set>(kw));

            ASSERT_FALSE(fe_parser.parse<Set>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Set>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Set>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Set>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Set>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'set' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Set>(""))
            << "end-of-file character finally is understood as the 'set' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestStaticRule)
    {
        const std::vector<std::string> expected_keywords{ "static" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Static>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Static>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Static>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Static>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Static>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Static>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'static' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Static>(""))
            << "end-of-file character finally is understood as the 'static' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestSwitchRule)
    {
        const std::vector<std::string> expected_keywords{ "switch" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Switch>(kw));

            ASSERT_FALSE(fe_parser.parse<Switch>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Switch>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Switch>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Switch>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Switch>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'switch' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Switch>(""))
            << "end-of-file character finally is understood as the 'switch' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestTodoRule)
    {
        const std::vector<std::string> expected_keywords{ "todo" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Todo>(kw));

            ASSERT_FALSE(fe_parser.parse<Todo>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Todo>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Todo>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Todo>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Todo>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'todo' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Todo>(""))
            << "end-of-file character finally is understood as the 'todo' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestTrueRule)
    {
        const std::vector<std::string> expected_keywords{ "true", "True" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<True>(kw));

            ASSERT_FALSE(fe_parser.parse<True>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<True>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<True>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<True>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<True>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'true' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<True>(""))
            << "end-of-file character finally is understood as the 'true' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestTryRule)
    {
        const std::vector<std::string> expected_keywords{ "try" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Try>(kw));

            ASSERT_FALSE(fe_parser.parse<Try>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Try>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Try>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Try>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Try>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'try' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Try>(""))
            << "end-of-file character finally is understood as the 'try' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestTypeRule)
    {
        const std::vector<std::string> expected_keywords{ "type" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Type>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Type>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Type>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Type>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Type>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Type>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'type' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Type>(""))
            << "end-of-file character finally is understood as the 'type' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestUnnamedRule)
    {
        const std::vector<std::string> expected_keywords{ "unnamed" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Unnamed>(kw));

            ASSERT_FALSE(fe_parser.parse<Unnamed>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Unnamed>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Unnamed>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Unnamed>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Unnamed>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'unnamed' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Unnamed>(""))
            << "end-of-file character finally is understood as the 'unnamed' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestUntilRule)
    {
        const std::vector<std::string> expected_keywords{ "until" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<Until>(kw));

            ASSERT_FALSE(fe_parser.parse<Until>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Until>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Until>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Until>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Until>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'until' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Until>(""))
            << "end-of-file character finally is understood as the 'until' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestVolatileRule)
    {
        const std::vector<std::string> expected_keywords{ "volatile" };

        for (const auto& kw : expected_keywords) {
            ASSERT_FALSE(fe_parser.parse<Volatile>(kw));  // Notice: at least one space char is mandatory after this keyword

            ASSERT_FALSE(fe_parser.parse<Volatile>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<Volatile>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<Volatile>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<Volatile>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<Volatile>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'volatile' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<Volatile>(""))
            << "end-of-file character finally is understood as the 'volatile' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestWhenRule)
    {
        const std::vector<std::string> expected_keywords{ "when" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<When>(kw));

            ASSERT_FALSE(fe_parser.parse<When>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<When>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<When>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<When>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<When>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'when' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<When>(""))
            << "end-of-file character finally is understood as the 'when' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestWhileRule)
    {
        const std::vector<std::string> expected_keywords{ "while" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<While>(kw));

            ASSERT_FALSE(fe_parser.parse<While>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<While>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<While>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<While>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<While>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'while' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<While>(""))
            << "end-of-file character finally is understood as the 'while' keyword?!?";
    }


    //=========================================================
    TEST_F(KeywordsFixtureTest, TestWithRule)
    {
        const std::vector<std::string> expected_keywords{ "with" };

        for (const auto& kw : expected_keywords) {
            ASSERT_TRUE(fe_parser.parse<With>(kw));

            ASSERT_FALSE(fe_parser.parse<With>(std::string(" ") + kw));
            ASSERT_FALSE(fe_parser.parse<With>(std::string("z") + kw));

            for (char c1 : spaces)
                ASSERT_TRUE(fe_parser.parse<With>(kw + c1));

            for (char c1 : spaces)
                for (char c2 : spaces)
                    ASSERT_TRUE(fe_parser.parse<With>(kw + c1 + c2));

            ASSERT_FALSE(fe_parser.parse<With>(kw + '0'))
                << std::format("tested word '{}' finally checks the 'with' keyword?!?", kw + '0');
        }

        ASSERT_FALSE(fe_parser.parse<With>(""))
            << "end-of-file character finally is understood as the 'with' keyword?!?";
    }
}
