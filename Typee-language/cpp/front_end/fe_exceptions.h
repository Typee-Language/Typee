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
#include <format>
#include <stdexcept>
#include <string>
#include <string_view>


//===========================================================================
/// \ingroup TypeeFrontEnd
/// \defgroup TypeeFrontEndExceptions Exceptions definitions for the Typee Front-End 
/// {
namespace ty_fe  //!< the Typee Front-End namespace
{
    //-----------------------------------------------------------------------
    /** \brief The base class for all Typee front-end exceptions. */
    class FEBaseException : public std::exception
    {
    public:
        /** \brief The default empty constructor.
        */
        inline FEBaseException() = default;

        /** \brief Valued constructor.
        * \param msg a reference to the message to display when exception is thrown.
        */
        inline FEBaseException(const std::string& msg)
            : _msg(msg)
        {}

        /** \brief The default destructor.
        */
        inline virtual ~FEBaseException() = default;
        
        /** \brief The message method called when exception is thrown.
        * \return a pointer to the text message to display.
        */
        inline const char* what() noexcept
        {
            return _msg.c_str();
        }

    private:
        std::string _msg{};  // a copy of the message argument passed at construction time (valued constructor)
    };


    //-----------------------------------------------------------------------
    /** \brief Data error on file stream reading. */
    class FEDataStreamErrorException : public FEBaseException
    {
    public:
        /** \brief The empty constructor.
        * Should be used on faulty memory streams.
        */
        inline FEDataStreamErrorException()
            : FEBaseException(_BASE_STR)
        {}

        /** \brief Valued constructor.
        * \param filepath the path string to the faulty file stream.
        */
        inline FEDataStreamErrorException(const std::string& filepath)
            : FEBaseException(
                std::vformat(
                    _BASE_STR + " from file '{}'",
                    std::make_format_args(filepath)
                )
              )
        {}

    private:
        static inline const std::string _BASE_STR{ "some data error occured while reading stream" };
    };


    //-----------------------------------------------------------------------
    /** \brief I/O Error on file. */
    class FEIOErrorException : public FEBaseException
    {
    public:
        /** \brief The empty constructor.
        * Should be used on faulty memory streams.
        */
        inline FEIOErrorException()
            : FEBaseException(_BASE_STR)
        {}

        /** \brief Valued constructor.
        * \param filepath the path string to the faulty file.
        */
        inline FEIOErrorException(const std::string& filepath)
            : FEBaseException(
                std::vformat(
                    _BASE_STR + " on file '{}'",
                    std::make_format_args(filepath)
                )
              )
        {}

    private:
        static inline const std::string _BASE_STR{ "some I/O error occured" };
    };


    //-----------------------------------------------------------------------
    /** \brief Memory allocation error. */
    class FEMemoryAllocationException : public FEBaseException
    {
    public:
        /** \brief The empty constructor.
        * Should be used on faulty memory streams.
        */
        inline FEMemoryAllocationException()
            : FEBaseException(_BASE_STR)
        {}

        /** \brief Valued constructor.
        * \param filepath the path string to the faulty file stream.
        */
        inline FEMemoryAllocationException(const std::size_t size)
            : _COMPL{ size > 1 ? "s" : "" }
            , FEBaseException(
                std::vformat(
                    _BASE_STR + " - unable to allocated {} byte{}",
                    std::make_format_args(size, _COMPL)
                )
              )
        {}

    private:
        static inline const std::string _BASE_STR{ "memory allocation failed" };
        const std::string _COMPL{};
    };


    //-----------------------------------------------------------------------
    /** \brief Unknown error on file stream reading. */
    class FEStreamErrorException : public FEBaseException
    {
    public:
        /** \brief The empty constructor.
        * Should be used on faulty memory streams.
        */
        inline FEStreamErrorException()
            : FEBaseException(_BASE_STR)
        {}

        /** \brief Valued constructor.
        * \param filepath the path string to the faulty file stream.
        */
        inline FEStreamErrorException(const std::string& filepath)
            : FEBaseException(
                std::vformat(
                    _BASE_STR + " from file '{}'",
                    std::make_format_args(filepath)
                )
            )
        {}

    private:
        static inline const std::string _BASE_STR{ "some unknown error occured while reading stream" };
    };


    //-----------------------------------------------------------------------
    /** \brief Too big code module from file. */
    class FETooBigModuleCodeException : public FEBaseException
    {
    public:
        /** The empty constructor.
        * Should be used on faulty modules already put in strings.
        */
        inline FETooBigModuleCodeException(const std::size_t module_size, const std::size_t max_size)
            : FEBaseException(
                std::vformat(
                    std::string("T code string") + _BASE_STR + " from file '{}'",
                    std::make_format_args(module_size, max_size)
                )
            )
        {}

        /** \brief Valued constructor.
        * \param module_path the path on disk to the module that is too big to load in memory space.
        */
        inline FETooBigModuleCodeException(const std::string& module_path, const std::size_t module_size, const std::size_t max_size)
            : FEBaseException(
                std::vformat(
                    std::string("T file module '{}'") + _BASE_STR + " from file '{}'",
                    std::make_format_args(module_path, module_size, max_size)
                )
            )
        {}

    private:
        inline static const std::string _BASE_STR{ " has a too big size (actually {} vs. max {})" };
    };


    //-----------------------------------------------------------------------
    /** \brief Too big code module from file. */
    class FEUnknownException : public FEBaseException
    {
    public:
        /** The empty constructor.
        */
        inline FEUnknownException()
            : FEBaseException(_BASE_STR)
        {}

        /** \brief Valued constructor.
        * \param text the text to be added to the default exception message.
        */
        inline FEUnknownException(const std::string& text)
            : FEBaseException(
                std::vformat(
                    _BASE_STR + " ({})",
                    std::make_format_args(text)
                )
            )
        {}

    private:
        inline static const std::string _BASE_STR{ "an unknown error occured in Typee Front-End" };
    };

}
/// }
