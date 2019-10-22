# 电话号码和邮件提取程序
import re
import pyperclip

# phone regex
phoneRegex=re.compile(r'''(
((\d{3})|\(\d{3}\))?              #area code
(\s|-|\.)?                        #separator
(\d{3})                           #first digits
(\s|-|\.)                         #separator
(\d{4})                           #last digits
(\s*(ext|x|ext\.)\s*(\d{2,5}))?   #extension 
)''',re.VERBOSE)
# email regex
emailRegex=re.compile(r'''(
[a-zA-Z0-9._%+-]+                 #user name
@
[a-zA-Z0-9.-]+                    #@domain name
\.
[a-zA-Z]{2,4}                     #dot anything
)''',re.VERBOSE)

# match
text=str(pyperclip.paste())
matches=[]
for i in phoneRegex.findall(text):
    matches.append(i[0])
for i in emailRegex.findall(text):
    matches.append(i)

print(matches)
# copy to clipboard
if len(matches)>0:
    ans='\n'.join(matches)
    pyperclip.copy(ans)
    print("copied to clipboard :")
    print(ans)
else:
    print('no phone numbers or email found !')

# 中国农业大学 版权所有 ©2017  010-123-4567 校登记号：NW—0201 文保网安备案号:1101080025 京ICP备05004632号-1 联系我们:wlzx@cau.edu.cn jerry_xmz@163.com 电话123-4567
# (010)-123-4567 ext. 26

# 练习：强口令检测
def passwd_check(pwd):
    if len(pwd)<8:
        return False
    else:
        regex1=re.compile(r'.*[a-z].*')
        regex2 = re.compile(r'.*[A-Z].*')
        regex3 = re.compile(r'.*[0-9].*')
        if len(regex1.findall(pwd))>0 and len(regex2.findall(pwd))>0 and len(regex3.findall(pwd))>0:

            return  True
        else:
            return False
