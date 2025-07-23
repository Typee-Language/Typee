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
#include <filesystem>
#include <ios>
#include <utility>

#include "tao/pegtl.hpp"
namespace pegtl = TAO_PEGTL_NAMESPACE;

#include "fe_parser.h"
#include "typee_language_grammar.h"


//===========================================================================
/// \defgroup TypeeFrontEnd The Typee Language Front-End
/// {
namespace ty_fe  //!< the Typee Front-End namespace
{
    //-------------------------------------------------------------------
    /** Constructor (1/2). */
    FEParser::FEParser(const std::string& module_path)
    {
        std::ifstream module_fstream(module_path);
        _load(module_fstream);
    }


    //-------------------------------------------------------------------
    /** Constructor (2/2). */
    FEParser::FEParser(std::ifstream& module_fstream)
    {
        _load(module_fstream);
    }


    //-------------------------------------------------------------------
    /** \brief The parsing operation.
    *
    * Operates the parsing operation of the T module content that has been
    * specified at construction time.  Generates an Intermediate Structure
    * on the fly.
    *
    * \return true if parsing was ok, or false otherwise.
    *
    * NOTE:  currently missing parameter is a reference to an IC structure
    * to be initialized on the fly.
    */
    const bool FEParser::parse()
    {
        pegtl::memory_input parsed_str(_module_content, "");
        return pegtl::parse< ty_grm::t_code_module >(parsed_str);
    }


    //-------------------------------------------------------------------
    /** \brief The parsing operation of T code from strings.
    *
    * Static method. Operates the parsing operation of T code from string.
    *
    * \return true if parsing was ok, or false otherwise.
    *
    * NOTE: a  currently missing parameter is the reference to the IC
    * structure that will be initialized on the fly.
    */
    const bool FEParser::parse(const std::string& module_str)
    {
        pegtl::memory_input parsed_str(module_str, "");
        return pegtl::parse< ty_grm::t_code_module >(parsed_str);
    }


    //-------------------------------------------------------------------
    /** \brief Loads the module content into memory space.
    * Sets last exception in case of any error while loading the
    * module content into memory.
    * \param module_fstream a reference to the module stream file.
    */
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

/// }
