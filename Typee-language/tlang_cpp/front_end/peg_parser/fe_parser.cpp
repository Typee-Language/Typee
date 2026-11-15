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
#include <exception>
#include <fstream>
#include <ios>
#include <stdexcept>
#include <string>
#include <string_view>
#include <utility>

#include "tao/pegtl/ascii.hpp"
#include "tao/pegtl/config.hpp"
#include "tao/pegtl/parse.hpp"
#include "tao/pegtl/text_view_input.hpp"
namespace pegtl = TAO_PEGTL_NAMESPACE;

#include "../fe_exceptions.h"
#include "fe_parser.h"
#include "typee_language_grammar.h"


//===========================================================================
/** The Typee Front-End namespace */
namespace ty_fe
{
    //-------------------------------------------------------------------
    FEParser::FEParser(std::string module_path)
    {
        std::ifstream module_fstream(std::move(module_path));
        _load(module_fstream);
    }


    //-------------------------------------------------------------------
    FEParser::FEParser(std::ifstream& module_fstream)
    {
        _load(module_fstream);
    }


    //-------------------------------------------------------------------
    const bool FEParser::parse()
    {
        pegtl::text_view_input<tao::pegtl::ascii::scan::lf_crlf> parsed_str(
            std::string_view(_module_content.data(), _module_content.length())
        );  // PEGTL 4.0
        // PEGTL 3.2 version: pegtl::memory_input parsed_str(_module_content, "");
        return pegtl::parse< ty_grm::t_code_module >(parsed_str);
    }


    //-------------------------------------------------------------------
    const bool FEParser::parse(const std::string& module_str)
    {
        pegtl::text_view_input<tao::pegtl::ascii::scan::lf_crlf> parsed_str(
            std::string_view(module_str.data(), module_str.length())
        );  // PEGTL 4.0
        // PEGTL 3.2 version: pegtl::memory_input parsed_str(module_str, "");
        return pegtl::parse< ty_grm::t_code_module >(parsed_str);
    }


    //-------------------------------------------------------------------
    const bool FEParser::parse(const std::string& module_str, FEIntermediateCode& out_ic)
    {
        pegtl::text_view_input<tao::pegtl::ascii::scan::lf_crlf> parsed_str(
            std::string_view(module_str.data(), module_str.length())
        );  // PEGTL 4.0
        // PEGTL 3.2 version: pegtl::memory_input parsed_str(module_str, "");
        
        // CAUTION: next call is INCOMPLETE
        return pegtl::parse< ty_grm::t_code_module >(parsed_str);
    }


    //-------------------------------------------------------------------
    void FEParser::_load(std::ifstream& module_fstream)
    {
        if (module_fstream) [[likely]] {
            // things are currently ok for the file input stream
            std::streampos size{ 0 };
            try {
                module_fstream.seekg(0, std::ios_base::end);
                size = module_fstream.tellg();
                module_fstream.seekg(0, std::ios_base::beg);

                _module_content.resize(std::size_t(size));
                module_fstream.read(_module_content.data(), size);
            }
            catch (std::bad_alloc) {
                set_exception(FEMemoryAllocationException(size));
            }
            catch (std::length_error) {
                set_exception(FETooBigModuleCodeException(size, _module_content.max_size()));
            }
            catch (...) {
                set_exception(FEUnknownException("while loading in memory the content of a T module for its fast parsing"));
            }
        }

        // sets associated exception on maybe finally failure on stream
        // notice: may override the FEUnknownException that may have been set above
        if (module_fstream.fail())
            _last_exception = FEDataStreamErrorException();
        else if (module_fstream.bad())
            _last_exception = FEIOErrorException();
    }

}  // end of namespace ty_fe
