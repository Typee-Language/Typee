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

#include <algorithm>
#include <cctype>
#include <format>
#include <ranges>
#include <string>
#include <vector>

#include "peg_grammar_rules/miscelaneous/miscelaneous.h"  // Notice: have a look to the included paths in the project definition
#include "tlang_cpp/front_end/peg_parser/fe_parser.h"     // Notice: have a look to the included paths in the project definition

using namespace tlang_rules;


//===========================================================================
namespace miscelaneous_rules
{
    //=========================================================
    // Miscelaneous Rules GTest Fixture
    class MiscelaneousFixtureTest : public testing::Test
    {
    private:
        static const int MAX_CHAR_VALUE{ 127 };  // We'll deal with sole ASCII characters, and not with char '\0'.

    protected:
        MiscelaneousFixtureTest()
            : testing::Test()
        {
            std::ranges::copy(std::ranges::views::iota(1, MAX_CHAR_VALUE+1), ascii_chars);
        }

        virtual ~MiscelaneousFixtureTest()
        {}

        const bool is_identifier(const char c1, const char c2, const char c3) const noexcept
        {
            return (std::isalnum(c2) || c2 == '_') &&
                (std::isalnum(c3) || c3 == '_') &&
                (std::isalpha(c1) || c1 == '_');
        }


        char ascii_chars[MAX_CHAR_VALUE];
        ty_fe::FEParser fe_parser{ "" };
    };


    //=====   AlphaChar   =====================================
    TEST_F(MiscelaneousFixtureTest, TestAlphaCharRule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };
            ASSERT_EQ(fe_parser.parse<AlphaChar>(test_code), static_cast<bool>(std::isalpha(c)))
                << std::format("tested code '{}' finally is not analpha char", c);
        }

        ASSERT_FALSE(fe_parser.parse<AlphaChar>(""))
            << "end-of-file character finally is an alpha char?!?";
    }


    //=====   AlphaNumChar   ==================================
    TEST_F(MiscelaneousFixtureTest, TestAlphaNumRule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };
            ASSERT_EQ(fe_parser.parse<AlphaNumChar>(test_code), static_cast<bool>(std::isalnum(c)))
                << std::format("tested code '{}' finally is not an alphanum char", c);
        }

        ASSERT_FALSE(fe_parser.parse<AlphaNumChar>(""))
            << "end-of-file character finally is an alphanum char?!?";
    }


    //=====   Dot   ===========================================
    TEST_F(MiscelaneousFixtureTest, TestDotRule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };
            ASSERT_EQ(fe_parser.parse<Dot>(test_code), c == '.')
                << std::format("tested code '{}' finally is not a dot", c);
        }

        ASSERT_FALSE(fe_parser.parse<Dot>(""))
            << "end-of-file character finally is a dot?!?";
    }


    //=====   DottedName   ====================================
    TEST_F(MiscelaneousFixtureTest, TestDottedNameRule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };

            if (std::isalpha(c) || c == '_') {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    if (c2 == '.') {
                        for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                            std::string test_code3{ test_code + c2 + c3 };
                            if (std::isalpha(c3) || c3 == '_') {
                                for (const char c4 : MiscelaneousFixtureTest::ascii_chars) {
                                    test_code3 += c4;
                                    ASSERT_TRUE(fe_parser.parse<DottedName>(test_code3))
                                        << std::format(
                                                "tested code '{}' (0x{:02x}{:02x}{:02x}{:02x}) should be recognized as a dotted name",
                                                test_code3, c, c2, c3, c4
                                           );
                                }
                            }
                            else {
                                ASSERT_FALSE(fe_parser.parse<DottedName>(test_code3))
                                    << std::format(
                                           "tested code '{}' (0x{:02x}{:02x}{:02x}) should not be recognized as a dotted name",
                                           test_code3, c, c2, c3
                                       );
                            }
                        }
                    }
                    else {
                        // Notice: c1 is a valid char for an identifier, so whatever are chars c2 and c3
                        // the PEG rule will always evalaute to true (maybe by stopping the evaluation 
                        // on c1 -> an error will be later raised then on the dot while parsing the 
                        // related module code.
                        for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                            std::string test_code3{ test_code + c2 + c3 };
                            ASSERT_FALSE(fe_parser.parse<DottedName>(test_code3))
                                << std::format(
                                       "tested code '{}' (0x{:02x}{:02x}{:02x}) should be recognized as a dotted name",
                                       test_code3, c, c2, c3
                                   );
                        }
                    }
                }
            }
            else {
                ASSERT_FALSE(fe_parser.parse<DottedName>(test_code))
                    << std::format(
                           "test code '{}' (0x{:02x}) finally is recognized as a dotted name while it should not",
                           test_code, c
                       );
            }
        }

        ASSERT_FALSE(fe_parser.parse<Identifier>(""))
            << "end-of-file character finally is an identifier?!?";
    }


    //=====   EndOfLine   =====================================
    TEST_F(MiscelaneousFixtureTest, TestEndOfLineRule)
    {
        const std::vector<std::string> end_of_lines{ "\n", "\r" };
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };
            const bool is_ok{ std::ranges::find(end_of_lines, test_code) != end_of_lines.end() };

            ASSERT_EQ(fe_parser.parse<EndOfLine>(test_code), is_ok)
                << std::format(
                    "tested code '{}' (0x{:02x}) finally is not a valid end-of-line",
                    test_code, int(test_code[0])
                   );
        }

        std::string test_code{};
        const std::vector<std::string> end_of_lines_str{ "\n", "\r", "\r\n" };
        for (const char c1 : MiscelaneousFixtureTest::ascii_chars) {
            switch (c1) {
            case '\n':
                test_code = c1;
                ASSERT_TRUE(fe_parser.parse<EndOfLine>(test_code))
                    << std::format(
                        "tested code '{}' (0x{:02x}) finally is not a valid end-of-line",
                        test_code, int(test_code[0])
                       );
                break;

            case '\r':
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    test_code = c1;
                    if (c2 == '\n')
                        test_code += c2;
                    bool is_ok{ false };
                    for (const auto& eol : end_of_lines_str) {
                        const int comp{ test_code.compare(eol) };
                        if (comp == 0) {
                            is_ok = true;
                            break;
                        }
                    }
                    ASSERT_EQ(fe_parser.parse<EndOfLine>(test_code), is_ok)
                        << std::format(
                            "tested code '{}' (0x{:02x},0x{:02x}) finally is not a valid end-of-line",
                            test_code, int(test_code[0]), int(test_code[1])
                           );
                }
                break;

            default:
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    test_code = c1;
                    test_code += c2;
                    ASSERT_FALSE(fe_parser.parse<EndOfLine>(test_code))
                        << std::format(
                            "tested code '{}' (0x{:02x}) finally is not a valid end-of-line",
                            test_code, int(test_code[0])
                           );
                }
                break;
            }
        }

        ASSERT_FALSE(fe_parser.parse<EndOfLine>(""))
            << "end-of-file character finally is a dot?!?";
    }


    //=====   Identifier   ====================================
    TEST_F(MiscelaneousFixtureTest, TestIdentifierRule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };

            if (std::isalpha(c) || c == '_') {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                        // Notice: when c2 and/or c3 are spaces, the end of the Identifier rule is automatically tested (i.e. Spacing rule)
                        std::string test_code3{ test_code + c2 + c3 };
                        if (is_identifier(c, c2, c3)) {  // Notice: defined in the fixture
                            ASSERT_TRUE(fe_parser.parse<Identifier>(test_code3))
                                << std::format(
                                    "tested code '{}' (0x{:02x}{:02x}{:02x}) should be recognized as an identifier",
                                    test_code3, c, c2, c3
                                );
                        }
                        else {
                            ASSERT_TRUE(fe_parser.parse<Identifier>(test_code3))
                                << std::format(
                                    "tested code '{}' (0x{:02x}{:02x}{:02x}) should be recognized as an identifier on first chars",
                                    test_code3, c, c2, c3
                                );
                        }
                    }
                }
            }
            else {
                ASSERT_FALSE(fe_parser.parse<Identifier>(test_code))
                    << std::format(
                        "test code '{}' (0x{:02x}) finally is recognized as an identifer while it should not",
                        test_code, c
                    );
            }
        }

        ASSERT_FALSE(fe_parser.parse<Identifier>(""))
            << "end-of-file character finally is an identifier?!?";
    }


    //=====   Name   ==========================================
    TEST_F(MiscelaneousFixtureTest, TestNameRule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };

            if (std::isalpha(c) || c == '_') {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                        // Notice: when c2 and/or c3 are spaces, the end of the Name rule is automatically tested (i.e. Spacing rule)
                        std::string test_code3{ test_code + c2 + c3 };
                        if (is_identifier(c, c2, c3)) {  // Notice: defined in the fixture
                            ASSERT_TRUE(fe_parser.parse<Name>(test_code3))
                                << std::format(
                                    "tested code '{}' (0x{:02x}{:02x}{:02x}) should be recognized as a name",
                                    test_code3, c, c2, c3
                                   );
                        }
                        else {
                            ASSERT_TRUE(fe_parser.parse<Name>(test_code3))
                                << std::format(
                                    "tested code '{}' (0x{:02x}{:02x}{:02x}) should be recognized as a name on first chars",
                                    test_code3, c, c2, c3
                                   );
                        }
                    }
                }
            }
            else {
                ASSERT_FALSE(fe_parser.parse<Name>(test_code))
                    << std::format(
                        "test code '{}' (0x{:02x}) finally is recognized as a name while it should not",
                        test_code, c
                       );
            }
        }

        ASSERT_FALSE(fe_parser.parse<Name>(""))
            << "end-of-file character finally is a name?!?";
    }


    //=====   SemiColon   =====================================
    TEST_F(MiscelaneousFixtureTest, TestSemiColon)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };
            if (c == ';')
                ASSERT_TRUE(fe_parser.parse<SemiColon>(test_code))
                    << std::format("tested code '{}' should not be considered as a semicolon", c);
            else
                ASSERT_FALSE(fe_parser.parse<SemiColon>(test_code))
                    << std::format("tested code '{}' should be considered as a semicolon", c);
        }

        ASSERT_FALSE(fe_parser.parse<SemiColon>(""))
            << "end-of-file character finally is a semicolon?!?";
    }


    //=====   Spacing   =======================================
    TEST_F(MiscelaneousFixtureTest, TestSpacingRule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };
            ASSERT_EQ(fe_parser.parse<Spacing>(test_code), static_cast<bool>(std::isspace(c)))
                << std::format("tested code '{}' finally is not a spacing char", c);
        }

        ASSERT_FALSE(fe_parser.parse<Spacing>(""))
            << "end-of-file character finally is an alpha char?!?";
    }


    //=====   Spacing0   ======================================
    TEST_F(MiscelaneousFixtureTest, TestSpacing0Rule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };
            ASSERT_TRUE(fe_parser.parse<Spacing0>(test_code))  // Notice: this is ALWAYS true
                << std::format(
                    "tested code '{}' (0x{:02x}) finally is not an optional spacing char",
                    test_code, c
                   );

            if (std::isspace(c)) {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                        std::string test_code3{ test_code + c2 + c3 };
                        ASSERT_TRUE(fe_parser.parse<Spacing0>(test_code3))  // Notice: this is ALWAYS true
                            << std::format(
                                "tested code '{}' finally is not an optional multiple spacing char",
                                test_code3
                               );
                    }
                }
            }
            else {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                        std::string test_code3{ test_code + c2 + c3 };
                        ASSERT_TRUE(fe_parser.parse<Spacing0>(test_code3))  // Notice: this is ALWAYS true
                            << std::format(
                                "tested code '{}' (0x{:02x}{:02x}{:02x}) finally is an optional multiple spacing char?!?",
                                test_code3, c, c2, c3
                               );
                    }
                }
            }
        }

        ASSERT_TRUE(fe_parser.parse<Spacing0>(""))  // Notice: this is ALWAYS true
            << "end-of-file character finally is an optional spacing char";
    }


    //=====   Spacing1   ======================================
    TEST_F(MiscelaneousFixtureTest, TestSpacing1Rule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };
            ASSERT_EQ(fe_parser.parse<Spacing1>(test_code), static_cast<bool>(std::isspace(c)))
                << std::format("tested code '{}' finally is not an optional spacing char", test_code);
        }

        for (const char c1 : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c1 };

            if (std::isspace(c1)) {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                        std::string test_code3{ test_code + c2 + c3 };
                        ASSERT_TRUE(fe_parser.parse<Spacing1>(test_code3))
                            << std::format(
                                "tested code '{}' (0x{:02x}{:02x}{:02x}) finally is not a multiple spacing char",
                                test_code3, c1, c2, c3
                               );
                    }
                }
            }
            else {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                        std::string test_code3{ test_code + c2 + c3 };
                        ASSERT_FALSE(fe_parser.parse<Spacing1>(test_code3))
                            << std::format(
                                "tested code '{}' (0x{:02x}{:02x}{:02x}) finally is a multiple spacing char",
                                test_code3, c1, c2, c3
                               );
                    }
                }
            }
        }

        ASSERT_FALSE(fe_parser.parse<Spacing1>(""))
            << "end-of-file character finally is a spacing char?!?";
    }


    //=====   Underscore   ====================================
    TEST_F(MiscelaneousFixtureTest, TestUnderscoreRule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };
            ASSERT_EQ(fe_parser.parse<Underscore>(test_code), c == '_')
                << std::format("tested code '{}' finally is not an underscore char '_'", test_code);
        }
    }

}