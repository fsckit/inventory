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
