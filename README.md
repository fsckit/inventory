##Genericon Inventory Tracking
[![Build Status](https://secure.travis-ci.org/fsckit/inventory.png)](http://travis-ci.org/fsckit/inventory)

Brandon Waite  
Kevin Stangl  
Chelsea Poirier  
Doug Patti  

##Requirements

* [Python 2.6 or 2.7](http://www.python.org/getit/)
* [Git](http://git-scm.com/book/en/Getting-Started-Installing-Git)
* [pip](http://www.pip-installer.org/en/latest/installing.html)
* [virtualenv](http://www.virtualenv.org/en/latest/index.html)
* [psycopg2](http://www.initd.org/psycopg/download/)

##Setup for Development

Make sure you have the above requirements. Start my checking out the source
from Github in the folder of your choice.

    $ git clone https://github.com/fsckit/inventory

Enter the directory and run the initialization. This will install the required
packages via pip.

    $ cd inventory
    $ make init

Try running the server.

    $ make serve

Visit <http://localhost:8000/> to see if it works.

##Style Conventions

* Use spaces, never tabs
* 2 space indentation
* Classes should be written with capital CamelCase
* Constants should be ALL\_CAPS\_WITH\_UNDERSCORES
* Methods, variables, and decorators should be written
  lowercase\_with\_underscores
* No lines of code over 100 characters in width
* No comments over 80 characters in width
* Use "double quotes" for strings that will be printed out or contain
  interpolation
* Use 'single quotes' for symbol-like strings, such as dictionary keys
* Line endings should be Unix style (LF) and not Windows style (CRLF)
* File should end with a newline

##License

The MIT License

Copyright (c) 2012 Brandon Waite, Kevin Stangl, Chelsea Poirier, Doug Patti

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
