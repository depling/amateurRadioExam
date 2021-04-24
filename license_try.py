#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# license_try.py
"""
1. Read pre-processed text file of published questions and answers list;
2. Single out questions into data structure for exercise processing;
3. Present randomly selected questions with multiple choices;
4. Score right/wrong comparison of user selection;
5. Record session results and report.
"""
#  Copyright Doug Epling 2021
#  wmdoug.epling@gmail.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import re
import random

random.seed()

def runExam(afile):

    """
    Ask one question from each group in every subElement.  Record right/wrong
    answers for each question asked.  Call for results presentation.
    """
    global TESTLINES, ELEMENTGROUPNUMS, SUBELEMENTS, ELEMENTCRITERIA,\
        QUESTIONGROUPS, QUESTIONHEADERS, TESTSTRUCT

    TESTLINES = [line for line in open(afile)]
    # ELEMENTGROUPNUMS is set of strings representing numbers
    ELEMENTGROUPNUMS = {s[1:2] for s in TESTLINES if s[1:2].isdigit()}
    # SUBELEMENTS is list of major test areas
    SUBELEMENTS = [line[11:] for line in TESTLINES if\
                   re.match(r'SUBELEMENT ', line)]
     # ELEMENTCRITERIA is SUBELEMENTS broken into tuples w/
     # element number, description, number of questions for number of groups
    ELEMENTCRITERIA = [(line[:3], line[3:-30], line[line.rindex('['):])\
                       for line in SUBELEMENTS]
    # QUESTIONGROUPS is list of groups from every test area
    QUESTIONGROUPS = [line for line in TESTLINES if\
                      re.match(r'[T,G]{1}(\d){1}([A-Z]){1} ', line)]
    # testQUESTIONHEADERS is list of questions & answers
    QUESTIONHEADERS = [line for line in TESTLINES if\
                       re.match(r'[T,G]{1}(\d){1}([A-Z]){1}(\d){2}', line)] 
    TESTSTRUCT = {}

    exam = Exam()
    
    TESTSTRUCT = exam.getExam()

    for ikey in TESTSTRUCT.keys():

        for jkey in TESTSTRUCT[ikey].keys():

              for kkey in TESTSTRUCT[ikey][jkey].keys():

                  if isinstance(TESTSTRUCT[ikey][jkey][kkey], Question):

                      S = input(TESTSTRUCT[ikey][jkey][kkey].\
                                this_question +\
                                    '\nType your choice here: ')
                          
                      S.upper()  
                      S = S[:1]
                      
                      TESTSTRUCT[ikey][jkey][kkey].setQuestionResponse(S)
                      
                      break
   
    showResults(exam)


def showResults(exam):

    """
    Using the exam Class object along with its back-bone data structure
    containing the entire text of the exam file (TESTSTRUCT) this function
    tallies results and presents feedback to a user.
    """

    numRight = 0.0
    numWrong = 0.0

    for ikey in TESTSTRUCT.keys():

        for jkey in TESTSTRUCT[ikey].keys():

            for kkey in TESTSTRUCT[ikey][jkey].keys():

                if isinstance(TESTSTRUCT[ikey][jkey][kkey],Question):
                    #print(TESTSTRUCT[ikey][jkey][kkey])
                    print(TESTSTRUCT[ikey][jkey][kkey].this_question)
                    
                    if TESTSTRUCT[ikey][jkey][kkey].questionResponse[0] == 'R':
                        numRight += 1
                        print("Question answer {} is correct".\
                              format(TESTSTRUCT[ikey][jkey][kkey].\
                                     questionResponse[1]))
                        print('\n')
                    else:
                        numWrong += 1
                        print("Question answer {} is incorrect".\
                              format(TESTSTRUCT[ikey][jkey][kkey].\
                                     questionResponse[1]))
                        print('\n')
                            
                    break
                
    print('You scored {} right, and {} wrong for overall {:.2%} score.'.\
          format(str(numRight), str(numWrong),\
                 numRight/(numRight+numWrong)))


class Exam:

    """
    To create a mother-ship class, only to be called one time it is not intended
    to be propagated into instances.  Instead, it is mainly a container to
    process the public file into individual parts within a three tier
    dictionary data structure.  It works for both the Technician and the
    General License exams thanks to the forethought of folks who maintain
    those question pool documents.  The argument to this class, afile, is
    either the official Technician pool or General pool of questions.  These
    must be culled and trimmed during a manual preprocessing.
      RE:
      SUBELEMENT -> r'[T,G]{1}(\d){1}
      group -> r'[T,G]{1}(\d){1}([A-Z]){1}
      question --> r'[T,G]{1}(\d){1}([A-Z]){1}(\d){2}
    """
    def __init__(self):
        
        self.testStruct = self.createExam()
        
    def createExam(self):

        testStruct = {}.fromkeys(SUBELEMENTS, {})

        for ikey in testStruct.keys():
            testStruct[ikey] = {}.fromkeys([line for line in QUESTIONGROUPS if\
                                            line[:2] == ikey[:2]], {})
            for jkey in testStruct[ikey].keys():
                testStruct[ikey][jkey] = {}.fromkeys(\
                                                     [line for line in\
                                                     QUESTIONHEADERS if\
                                                          line[:3] == \
                                                              jkey[:3]], None)

                q = random.choice(list(testStruct[ikey][jkey].keys()))
                
                #  Question objects created here
                testStruct[ikey][jkey][q] = Question(q)

        return(testStruct)
    
    def getExam(self):
        
        return(self.testStruct)


class Question:

    """
    To create instance object for each test question chosen randomly from its
    group.  Each question is asked and answered and stored in leaves of the
    three tier exam.TESTSTRUCT.  The questionNum argument is defined with the 
    regular expression r'[T,G]{1}(\d){1}([A-Z]){1}(\d){2}, a 5 character string
    """

    def __init__(self, question):

        self.questionNum = question[:5]
        self.questionIndex = self.setIndex(self.questionNum)
        self.this_question = self.setQuestion(self.questionIndex)
        self.correctAnswer = TESTLINES[self.questionIndex][7:8]
        self.questionResponse = None  #R->right, W->wrong

    def setIndex(self, s):

        for i in range(len(TESTLINES)):
            if TESTLINES[i][:5] == s:

                return(i)

    def setQuestion(self, n):

        n += 1
        a_question = ''

        try:
            while not TESTLINES[n].startswith('~~') :
                a_question += TESTLINES[n]
                n += 1
                
            
            a_question = '\n'.join([self.getQuestionNum(), a_question])    
            return(a_question)

        except StopIteration:
            
            pass
        
    def getQuestionNum(self):
        
        return(self.questionNum)

    def getQuestion(self):

        return(self.this_question)

    def setQuestionResponse(self, S):

        if S == self.correctAnswer:
            self.questionResponse = ('R', S)

        else:
            self.questionResponse = ('W', S)

    def getResponse(self):

        return(self.questionResponse)


if __name__ == '__main__':
    import sys
    afile = sys.argv[1]
    runExam(afile)