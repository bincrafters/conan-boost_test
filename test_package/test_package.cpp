#include <boost/test/output_test_stream.hpp>

int main()
{
	boost::test_tools::output_test_stream output( "test.log", true );
}

