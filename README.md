# amateurRadioExam
Python script for learning FCC requirements for Amateur Radio license.

# Amateur Radio Practice License Exam

The Python script file in this project folder is designed to emulate the examinations for FCC amateur radio licenses.  It is a command line application that asks questions from a pre-processed text file.  Multiple choice questions are asked according to testing format and chosen at random from the entire pool of questions.  When questions have been asked and answered according to requirements for an actual exam sitting, the exam is scored and feedback is provided.

The official public files represented with the pre-processed files included are:

**FCC Exam Element 2 Question Pool for Technician Class Effective 7/01/2018-6/30/2022**

**2019-2023 General Class FCC Element 3 Syllabus - Effective July 1, 2019**

Those are available online, and not included herein.

The preprocessed data files are included in versions for Unix and Win32, UTF-8, for the users convenience.  Preprocessing entailed removing the 'errata' section at the beginning, replacing a few non-printing text characters, and removing some extraneous empty lines at the EOF.  
To run the trial exam, open a terminal in this project directory.  Assuming there is a functional Python interpreter on the machine, the usage on the command line is:  
`$>python license_try.py <file>` where file is either the Tech level text or the Basic level text.

NOTE:  The file parameter must specify whether you want the Unix version or the Win32 version as specified in the file name.

# todo

  * GUI would be nice;
  * expand feedback on right/wrong answers to include reference when available;
  * configuration options such as file records of test attempts, etc.;
  * control options such as multiple runs without repeated questions;

*Thanks to the testing authors and maintainers at [http://www.ncvec.org/](URL) who provide cogent and consistent documentaiton*
