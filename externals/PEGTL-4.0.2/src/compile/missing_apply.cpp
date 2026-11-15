// Copyright (c) 2026 Dr. Colin Hirsch and Daniel Frey
// Distributed under the Boost Software License, Version 1.0.
// (See accompanying file LICENSE_1_0.txt or copy at https://www.boost.org/LICENSE_1_0.txt)

#include "test.hpp"

#include <tao/pegtl.hpp>

namespace pegtl = TAO_PEGTL_NAMESPACE;

struct action_rule : pegtl::one< 'a' >
{};

struct grammar : pegtl::must< action_rule, pegtl::eof >
{};

template< typename Rule >
struct action
   : pegtl::nothing< Rule >
{};

template<>
struct action< action_rule >
{
#if TAO_PEGTL_COMPILE_ACCEPT
   static void apply0()
   {}
#endif
};

int main()
{
#if TAO_PEGTL_COMPILE_REJECT
   // include/tao/pegtl/match.hpp
   // static_assert( !enable_action || !validate_nothing || is_nothing || is_maybe_nothing || has_apply || has_apply0, "Either apply() or apply0() must be defined in action!" );
#endif
   return pegtl::parse< grammar, action >( pegtl::text_view_input< pegtl::scan::lf >( "a" ) ) ? 0 : 1;
}
