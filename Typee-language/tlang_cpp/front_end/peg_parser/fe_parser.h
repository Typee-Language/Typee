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
#include <filesystem>
#include <fstream>
#include <string>

#include "tao/pegtl.hpp"
namespace pegtl = TAO_PEGTL_NAMESPACE;

#include "../fe_exceptions.h"
#include "../fe_intermediate_code.h"


//===========================================================================
/// \addtogroup TypeeFrontEnd The Typee Language Front-End
/// \{
namespace ty_fe  //! the Typee Front-End namespace
{
    //=======================================================================
    /** \brief The Front-End parser of Typee-language "T".
    *
    * The external library PEGTL is used for the purpose of scanning and
    * parsing  Typee modules content according to the Typee language PEG
    * format specification. PEGTL groups these two first steps of modern
    * compilers into a single pass.
    *
    * Notice: As a first intention,  T code modules are loaded in memory 
    * space when parsed from file. This will avoid  parsing  very  large 
    * modules and will speed-up the parsing process.  Parsing from files
    * on disks will be provided in a next release.
    */
    class FEParser
    {
    public:
        //===   Constructors / Destructor   =================================
        //-------------------------------------------------------------------
        FEParser() = delete;  //!< Empty constructor is forbidden. Copy, Move and assignment operators are forbidden too.

        //-------------------------------------------------------------------
        /** \brief Constructor (1/2).
        * \param module_path a const reference to the filepath to the T code to be parsed.
        */
        FEParser(const std::string& module_path);

        //-------------------------------------------------------------------
        /** \brief Constructor (2/2).
        * \param module_fstream a reference to the ifstream to be parsed.
        */
        FEParser(std::ifstream& module_fstream);

        //-------------------------------------------------------------------
        virtual ~FEParser() = default;  //!< The default destructor.


        //===   Accessors / Mutators   ======================================
        //-------------------------------------------------------------------
        /** \brief Returns fail status of the parser.
        * \return true if parser has failed, or false otherwise.
        * \sa is_ok.
        */
        [[nodiscard]]
        inline constexpr bool failed() const noexcept
        {
            return !is_ok();
        }

        //-------------------------------------------------------------------
        /** \brief Returns a const reference to the internally created intermediate code structure.
        * \return a reference to the internal IC structure.
        */
        [[nodiscard]]
        inline constexpr FEIntermediateCode& get_ic() noexcept
        {
            return _ic;
        }

        //-------------------------------------------------------------------
        /** \brief Gets a reference to the last exception set for this parser.
        * \return a reference to the last set exception.
        * \see set_exception.
        */
        [[nodiscard]]
        inline const FEBaseException& get_last_exception() const noexcept
        {
            return _last_exception;
        }

        //-------------------------------------------------------------------
        /** \brief Returns the ok status of the parser.
        * \return true if parser is ok, or false otherwise.
        * \sa failed.
        */
        [[nodiscard]]
        inline constexpr bool is_ok() const noexcept
        {
            return _is_ok;
        }

        //-------------------------------------------------------------------
        /** \brief Sets an exception to be associated with the parser.
        * This exception may then be thrown by any caller. Before throwing
        * the 
        * \param except a reference to an exception instantiation associated
        *               with the parser operations.
        * \see get_last_exception.
        */
        inline void set_exception(const FEBaseException& except) noexcept
        {
            _last_exception = except;
            _is_ok = false;
        }


        //===   Operators   =================================================
        //-------------------------------------------------------------------
        /** \brief Casting operator to bool, returns the ok status of the parser.
        * \return true if the parser status is ok, or false otherwise.
        * \sa is_ok, failed.
        */
        [[nodiscard]]
        inline constexpr operator bool() const noexcept
        {
            return is_ok();
        }


        //===   Operations   ================================================
        //-------------------------------------------------------------------
        /** \brief The parsing operation of T modules from file.
        *
        * Operates the parsing operation of the T module content that has
        * been specified at construction time.  Generates an Intermediate
        * Code (IC) structure on the fly.
        * 
        * \return true if parsing was ok, or false otherwise.
        * 
        * NOTE: a  currently missing parameter is the reference to the IC
        * structure that will be initialized on the fly.
        */
        const bool parse();

        //-------------------------------------------------------------------
        /** \brief The parsing operation of T code from strings.
        *
        * Static method. Operates the parsing operation of T code from string.
        *
        * \param module_str a string containing T code to parse.
        * \return true if parsing was ok, or false otherwise.
        */
        static const bool parse(const std::string& module_str);

        //-------------------------------------------------------------------
        /** \brief The parsing operation of T code and IC generation applied to strings.
        *
        * Static method. Operates the parsing operation of T code from string.
        * Generates Internmediate Code.
        *
        * \param module_str a string containing T code to parse.
        * \param out_ic a reference to the Intermediate Code structure to be generated.
        * \return true if parsing was ok, or false otherwise.
        */
        static const bool parse(const std::string& module_str, FEIntermediateCode& out_ic);

        //-------------------------------------------------------------------
        /** \brief Throws the last set exception if the parser status is not ok.
        * Does not throw anything if the parser status is ok.
        */
        inline void throw_() const
        {
            if (failed())
                throw _last_exception;
        }


    private:
        FEBaseException    _last_exception{};   //!< the last exception associated with the parser. Only set if _is_ok is false.
        FEIntermediateCode _ic{};               //!< the intermediate code structure generated while parsing.
        std::string        _module_content{};   //!< the internal content of the module.
        bool               _is_ok{ true };      //!< the error status: true if 'ok', false otherwise.

        //-------------------------------------------------------------------
        /** \brief Loads the module content into memory space.
        * Sets last exception in case of any error while loading the
        * module content into memory.
        * \param module_fstream a reference to the module stream file.
        */
        void _load(std::ifstream& module_fstream);

    };

}  // end of namespace ty_fe

/// \}

