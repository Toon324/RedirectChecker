RedirectChecker
===============

Automatically checks redirects from a CSV file.


Requirements
===============

Python must be installed on the system. Either 2.7 or 3.4 will work.
www.python.org/downloads


#Changelog


v1.10 - Removed AutoIT dependency; Speed is greatly increased.

v1.00 - Initial release


Use
================

Run the script from CMD.

Enter in the absolute location of the .csv file to read from. This file should contain the original URL in the left collumn and the expected URL in the right collumn.

To run a test on all redirects, enter -1. Otherwise, enter the number of redirects you would like to test. This will always test starting from the top of the given list as element 0.

Failed tests (the final URL does not match the expected URL) will be written to <provided_file_name>_failed.txt in the same location as the provided file.

Passed tests (final URL matches expected URL) will be written to <provided_file_name>_passed.txt in the same location as the provided file.

The tests will always wait for a response from the URL via a HEAD request. If this request times out, or produces an error, the test is marked as failed.

A test of 1,500 URL's to a company site via a work network took approximately 4 minutes to complete.
