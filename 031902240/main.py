#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re


def write_to_ans(data_list, num, answer):  # 将一行中找到的敏感词写到文件中
    for item in data_list:
        answer.write("Line"+num+item+'\n')


def start_to_find(path1):  # 将敏感词读出并写入列表 
    with open(path1, 'rt', encoding='utf-8') as file:
        word_list = list()
        for line in file.readlines():
            if line is not None:
                word_list.append(line.strip('\n'))
    return word_list


"""
寻找敏感词 每读出一行都在单词列表内将单词循环进行匹配,使用正则表达式
首先直接寻找无变形的敏感词
其次使用正则表达式 首个字符与尾部字符做界限 找到匹配即认为有敏感词
"""


def serach_sensitive_word(path1, path2, path3):
    word_list = start_to_find(path1)
    total = 0
    with open(path2, 'rt', encoding='utf-8') as file, open(path3, 'wt', encoding='utf-8') as answer:
        answer.write('                                                           \n')
        line_num = 0
        for line in file:
            line_num = line_num + 1
            for item in word_list:
                data_list2 = re.findall(item, line)
                line = re.sub(item, "", line)
                data_list1 = re.findall(item[0]+".+?"+item[-1], line)
                if data_list1:
                    for case1 in data_list1:
                        total = total + 1
                        num_str = str(line_num)
                        answer.write("Line:"+num_str+" <"+item+"> "+case1+'\n')
                if data_list2:
                    for case2 in data_list2:
                        total = total + 1
                        num_str = str(line_num)
                        answer.write("Line:" + num_str + " <" + item + "> " + case2 + '\n')
        answer.seek(0)
        s1 = str(total)
        answer.write("Total: " + s1)


def main():
    path1 = input()
    path2 = input()
    path3 = input()
    serach_sensitive_word(path1, path2, path3)


if __name__ == '__main__':
    main()
