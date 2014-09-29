RedirectChecker
===============

Automatically checks redirects from a CSV file.


Requirements
===============

Python must be installed on the system. Either 2.7 or 3.4 will work.
www.python.org/downloads

AutoIT must be installed.
https://www.autoitscript.com/site/autoit/downloads/
AutoIT will not run correctly in Python until you install the appropriate Python Extension for Windows: http://sourceforge.net/projects/pywin32/


Use
================

Run the script from CMD.

Enter in the absolute location of the .csv file to read from. This file should contain the original URL in the left collumn and the expected URL in the right collumn.

To run a test on all redirects, enter -1. Otherwise, enter the number of redirects you would like to test. This will always test starting from the top of the given list as element 0.

Failed tests (the final URL does not match the expected URL) will be written to <provided_file_name>_failed.txt in the same location as the provided file.

Passed tests (final URL matches expected URL) will be written to <provided_file_name>_passed.txt in the same location as the provided file.

Each URL will take 8.4 seconds to test.
