# 生成随机的10份测验试卷文件  问题是美国50个州的首府
import random

tmp={'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
     'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford',
     'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
     'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky':
     'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
     'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',  'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
     'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',  'New Hampshire': 'Concord',
     'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina':
     'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon':'Salem', 'Pennsylvania':
     'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
     'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
     'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming':'Cheyenne'}

# 针对每份试卷，随机问题和答案的顺序
for quiznum in range(10):
    # create quizfile and answerfile
    quizfile=open('capitals_quiz%s.txt' % str(quiznum+1),'w')
    answerfile=open('capitals_quiz_answer%s.txt' % str(quiznum+1),'w')
    # write header for quiz
    quizfile.write('Name:\n\nClass:\n\nDate:\n\n')
    quizfile.write((' '*20)+'State Capitals Quiz (%s)' % str(quiznum+1))
    quizfile.write('\n\n')
    # shuffle the order of states
    states=list(tmp.keys())
    random.shuffle(states)
    for questionnum in range(50):
        # get answer
        correct=tmp[states[questionnum]]
        wrong=list(tmp.values())
        # delete the correct answer
        del wrong[wrong.index(correct)]
        wrong=random.sample(wrong,3)
        answer=wrong+[correct]
        random.shuffle(answer)
        # write the question and option to quiz file
        quizfile.write("%s. What's the capital of %s?\n" % (questionnum+1,states[questionnum]))
        for i in range(4):
            quizfile.write('%s. %s\n' % ('ABCD'[i],answer[i]))
        quizfile.write('\n')
        # wirte the answer to answer file
        answerfile.write('%s. %s\n' % (questionnum+1,'ABCD'[answer.index(correct)]))
    quizfile.close()
    answerfile.close()
# 做出试卷和答案文件
