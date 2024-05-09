from html import page_source
import re

regex = r'''(<\w+( \w+(=[\"|'][^\"|']+[\"|'])?)* */? *>)([^<]+)'''
# tags = [{"tags":i[0].strip('<').split()[0], "attrs": [atrr.split('=')[0]:atrr.split('=')[-1].strip("'").strip("\"")} for atrr in i[0].replace(': ',':').strip('>').split()[1:]]]} for i in re.findall(regex,page_source)]]
tags = [{"tag": i[0].strip('<').split()[0], "attrs": {atrr.split('=')[0]: atrr.split('=')[-1].strip("'").strip("\"") for atrr in i[0].replace(': ', ':').strip('>').split()[1:]}, 'text': i[-1]} for i in re.findall(regex, page_source)]
for i in tags:
    if(i['tag'] == 'small' and i['attrs']['class'] == 'author'):
        print(i['text'].strip())