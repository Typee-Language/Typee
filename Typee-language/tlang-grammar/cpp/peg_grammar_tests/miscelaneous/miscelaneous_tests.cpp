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

        char ascii_chars[MAX_CHAR_VALUE];
        ty_fe::FEParser fe_parser{ "" };
    };


    //=====   AlphaChar   =====================================
    TEST_F(MiscelaneousFixtureTest, TestAlphaCharRuleTest)
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


    //=====   EndOfLine   =====================================
    TEST_F(MiscelaneousFixtureTest, TestEndOfLineRule)
    {
        const std::vector<std::string> end_of_lines{ "\n", "\r" };
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };
            const bool is_ok{ std::ranges::find(end_of_lines, test_code) != end_of_lines.end() };

            ASSERT_EQ(fe_parser.parse<EndOfLine>(test_code), is_ok)
                << std::format("tested code '{}' (0x{:02x}) finally is not a valid end-of-line", test_code, int(test_code[0]));
        }

        std::string test_code{};
        const std::vector<std::string> end_of_lines_str{ "\n", "\r", "\r\n" };
        for (const char c1 : MiscelaneousFixtureTest::ascii_chars) {
            switch (c1) {
            case '\n':
                test_code = c1;
                ASSERT_TRUE(fe_parser.parse<EndOfLine>(test_code))
                    << std::format("tested code '{}' (0x{:02x}) finally is not a valid end-of-line", test_code, int(test_code[0]));
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
                        << std::format("tested code '{}' (0x{:02x},0x{:02x}) finally is not a valid end-of-line", test_code, int(test_code[0]), int(test_code[1]));
                }
                break;

            default:
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    test_code = c1;
                    test_code += c2;
                    ASSERT_FALSE(fe_parser.parse<EndOfLine>(test_code))
                        << std::format("tested code '{}' (0x{:02x}) finally is not a valid end-of-line", test_code, int(test_code[0]));
                }
                break;
            }
        }

        ASSERT_FALSE(fe_parser.parse<EndOfLine>(""))
            << "end-of-file character finally is a dot?!?";
    }


    //=====   Identifier   ====================================
    /*
    struct Identifier :
        pegtl::seq<
            pegtl::sor<AlphaChar, Underscore>,
            pegtl::star<pegtl::sor<AlphaNumChar, Underscore>>,
            Spacing0
        > {};
    */
    TEST_F(MiscelaneousFixtureTest, TestIdentifierRule)
    {
        for (const char c : MiscelaneousFixtureTest::ascii_chars) {
            std::string test_code{ c };

            if (std::isalpha(c) || c == '_') {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                        std::string test_code3{ test_code + c2 + c3 };
                        ASSERT_TRUE(fe_parser.parse<Spacing0>(test_code3))  // Notice: this is ALWAYS true
                            << std::format("tested code '{}' (0x{:02x}{:02x}{:02x}) finally is an optional multiple spacing char?!?", test_code3, c, c2, c3);
                    }
                }
            }
            else {
                ASSERT_FALSE(fe_parser.parse<Identifier>(test_code))
                    << std::format("test code '{}' (0x{:02x}) finally is an identifer", test_code, c);
            }
        }
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
                << std::format("tested code '{}' (0x{:02x}) finally is not an optional spacing char", test_code, c);

            if (std::isspace(c)) {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                        std::string test_code3{ test_code + c2 + c3 };
                        ASSERT_TRUE(fe_parser.parse<Spacing0>(test_code3))  // Notice: this is ALWAYS true
                            << std::format("tested code '{}' finally is not an optional multiple spacing char", test_code3);
                    }
                }
            }
            else {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                        std::string test_code3{ test_code + c2 + c3 };
                        ASSERT_TRUE(fe_parser.parse<Spacing0>(test_code3))  // Notice: this is ALWAYS true
                            << std::format("tested code '{}' (0x{:02x}{:02x}{:02x}) finally is an optional multiple spacing char?!?", test_code3, c, c2, c3);
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
                            << std::format("tested code '{}' (0x{:02x}{:02x}{:02x}) finally is not a multiple spacing char", test_code3, c1, c2, c3);
                    }
                }
            }
            else {
                for (const char c2 : MiscelaneousFixtureTest::ascii_chars) {
                    for (const char c3 : MiscelaneousFixtureTest::ascii_chars) {
                        std::string test_code3{ test_code + c2 + c3 };
                        ASSERT_FALSE(fe_parser.parse<Spacing1>(test_code3))
                            << std::format("tested code '{}' (0x{:02x}{:02x}{:02x}) finally is a multiple spacing char", test_code3, c1, c2, c3);
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