# amateurRadioExam
Python script for learning FCC requirements for Amateur Radio license.

# Amateur Radio Practice License Exam

The Python script file in this project folder is designed to emulate the examinations for FCC amateur radio licenses.  It is a command line application that asks questions from a pre-processed text file.  Multiple choice questions are asked according to testing format and chosen at random from the entire pool of questions.  When questions have been asked and answered according to requirements for an actual exam sitting, the exam is scored and feedback is provided.

The official public files represented with the pre-processed files included are:

**FCC Exam Element 2 Question Pool for Technician Class Effective 7/01/2018-6/30/2022**

**2019-2023 General Class FCC Element 3 Syllabus - Effective July 1, 2019**

To run the trial exam, open a terminal in this project directory.  Assuming there is a functional Python interpreter on the machine, the usage on the command line is:  
`$>python license_try.py <file>`   
where file is either the Tech level text or the Basic level text.

# todo

  * script runs as is on Linux, but will require some tweeks for other platforms;
  * the two data files are also formatted for Unix line endings and UTF-8;
  * GUI would be nice;
  * configuration options such as file records of test attempts, etc.;
  * control options such as multiple runs without repeated questions;

*Thanks to the testing authors and maintainers at [http://www.ncvec.org/](URL) who provide cogent and consistent documentaiton*
