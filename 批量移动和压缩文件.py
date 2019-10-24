# move files and zip files
import zipfile
import shutil
import re
import os
# create new directory
if not os.path.exists(r'.\quiz'):
    os.makedirs(r'.\quiz')
if not os.path.exists(r'.\answer'):
    os.makedirs(r'.\answer')
# create new zip file
quizzip=zipfile.ZipFile('quiz.zip','w')
answerzip=zipfile.ZipFile('answer.zip','w')

quizre=re.compile(r'.*quiz(\d)+.*')
answerre=re.compile(r'.*quiz_answer(\d)+.*')

# move and zip
for filename in os.listdir(r'.'):
    source = os.path.abspath(filename)
    quizfile=quizre.search(filename)
    if quizfile != None:
        dest=os.path.abspath(r'.\quiz')
        shutil.move(source,dest)
        print('%s move to %s' % (source,dest))
        newquizfile=os.path.join(dest,filename)
        quizzip.write(newquizfile)
        print('%s zipped to %s' % (filename, 'quiz.zip'))
    answerfile=answerre.search(filename)
    if answerfile != None:
        dest=os.path.abspath(r'.\answer')
        shutil.move(source, dest)
        print('%s move to %s' % (source, dest))
        newanswerfile=os.path.join(dest,filename)
        answerzip.write(newanswerfile)
        print('%s zipped to %s' % (filename, 'answer.zip'))

quizzip.close()
answerzip.close()

