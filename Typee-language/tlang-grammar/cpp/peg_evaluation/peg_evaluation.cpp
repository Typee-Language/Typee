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
#include <iostream>
#include <string>
#include <utility>

#include "peg_evaluation.h"

#include "miscelaneous/miscelaneous.h"
#include "miscelaneous/miscelaneous_evaluation.h"

#include "../tlang_cpp/front_end/fe_exceptions.h"
#include "../tlang_cpp/front_end/peg_parser/fe_parser.h"


//===========================================================================
int main()
{
    bool evaluation_ok{ true };

    evaluation_ok = evaluation_ok && EvaluateMiscelaneous().evaluate();

    std::cout << std::endl << (evaluation_ok ? "ALL OK" : "Detected Errors") << std::endl << std::endl;
}


//===========================================================================
//---------------------------------------------------------------------------
EvaluationBase::EvaluationBase(std::string tested_module_name)
    : _module_name(std::move(tested_module_name))
{}

//---------------------------------------------------------------------------
const bool EvaluationBase::evaluate(std::string tested_t_code) noexcept
{
    std::cout << _module_name << "... "; std::cout.flush();

    _evaluation_ok = _evaluate(std::move(tested_t_code));

    std::cout << (_evaluation_ok ? "Ok" : "ERR") << std::endl;
    return _evaluation_ok;
}
