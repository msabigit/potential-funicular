------------------
  Transform SWF
------------------
The Transform SWF framework is a collection of classes for each of the data
structures and tags that make up the Flash File Format Specification from
Macromedia. The classes provide a completely object-oriented API to encode
and decode Flash (.swf) files. Transform SWF supports Flash MX 2004 (Flash 7).

The framework also contains classes that provide a higher level interface
supporting the addition of shapes, images, sounds, fonts and text from
external file formats.

The documentation that accompanied this release contains a description of the
each of the classes along with examples on how they may be used to decode,
process and encode Flash (.swf) files. Flagstone Software's web site,
www.flagstonesoftware.com also contains more detailed information and advanced
examples.

IMPORTANT: If you downloaded Transform then the framework only contains the
classes for reading and writing Flash files. All the classes used to perform 
testing and benchmarking are not included. If you want to do any development 
then you should check out all the files directly from the Subversion repository: 
https://svn.berlios.de/svnroot/repos/transform/trunk

-------------
  Licencing
-------------
Transform SWF is made available under the terms of the Berkeley Software
Distribution (BSD) license. This allow you complete freedom to use and
distribute the code in source and/or binary form as long as you respect
the original copyright. Please see the LiCENCE.txt file for exact terms.

-----------------
  Contributions
-----------------
Contributions by other authors are also available in the contrib directory.
Unless otherwise stated in the contribution's documentation, each is licensed
for use and redistribution under the terms of the Berkeley Software Distribution
(BSD) license.

----------------
  Requirements
----------------
To use Transform SWF you must have at least:

    Java 2 Standard Edition

--------------------------
  Building the Framework
--------------------------
The ANT build file, build.xml contains the following major targets:

    build   compile with optimisation all the classes in the
            transform and transform utilities and package them
            in transform.jar (examples and test classes are not
            included).

Minor targets provide more control over the compiling and packaging
of classes, allowing for example a JAR file to be created containing
the framework classes and the examples. Targets include:

    clean    remove all the compiled classes and jars.
    classes  compile the framework classes for production.
    jar      package all the compiled classes in a JAR.

-------------------------
  Testing the Framework
-------------------------
If you check out Transform from the repository then the source tree contains
code to test that the classes in the framework are encoding and decoding Flash
files correctly. The tests use JUnit 3.8.2 framework, which you can find out
more about at http://www.junit.org. Testing is designed to be performed within
an development environment, such as Eclipse, where the unit tests can be run
directly.

The package com.flagstone.transform.test contains tests for individual classes
as well as suites of tests for groups of classes. The class AllTests will run
the entire suite of tests available.

---------------------------
  Using Files For Testing
---------------------------
The directory test/data is designed to hold sets of files that can be used to
test the classes in the framework. The files augment the test patterns in the
unit tests. This is particularly important for more complex classes such as
images, fonts and sounds where the volume and/or variation in data can be
significant.

The directories are organized according to the type of file that is used in
testing:

test
  |
  +- data
  |   |
  |   +- swf
  |   +- ttf
  |   +- bmp
  |   +- png
  |
  +- results

The swf directory contain sample Flash files with a representative selection
of encoded data structures for a particular class. These files were extracted
from 'real-world' Flash files and so provide a useful sanity check for Flash
files that will be processed with the Transform framework.

These files have been assembled from a number of different sources. Different
sets of files such as fonts and images are subject to specific terms and
conditions however all can be distributed by Flagstone as part of this package.
Details of the terms and conditions are included in each directory.

The results directory are where the files generated during testing are written.
A separate sub-directory will be created for each class. Within this directory
sub-directories will be created for the files generated in each test.

A directory is also included for Flash Video, .flv files though none have been 
added to the repository to keep the project size down. Flash video files are 
widely available on the web and so adding files for testing is easy.

-----------------------
  Using the Framework
-----------------------
Add the JAR file to your classpath, e.g.:

Windows:  CLASSPATH=...;C:\Program Files\Flagstone\java\transform.jar
Unix:     CLASSPATH=...:/usr/local/java/transform.jar

To use the classes, place the following import statement in your code:

    com.flagstone.transform.*;

If you build the framework using the ANT target develop then the examples
can be used with the import statements:

    com.flagstone.transform.examples.*;

--------------------------
  Additional Information
--------------------------
For Further Information please contact:

Stuart MacKay

Flagstone Software Ltd.
92 High Street
Wick, Caithness KW1 4LY
Scotland

www.flagstonesoftware.com
