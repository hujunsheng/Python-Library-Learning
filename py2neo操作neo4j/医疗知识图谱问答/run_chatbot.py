"""
# -*- coding: utf-8 -*-
# @File    : run_chatbot.py
# @Time    : 2020/11/25 10:07 上午
# @Author  : xiaolu
# @Email   : luxiaonlp@163.com
# @Software: PyCharm
"""
from data_process.question_classifier import QuestionClassifier
from data_process.question_parser import QuestionPaser
from data_process.answer_search import AnswerSearcher


class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = "您好, 我是小路医药智能助理,希望可以帮到您。如果没答上来，可联系120。祝您身体棒棒的!!!"
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


if __name__ == '__main__':
    handler = ChatBotGraph()
    while True:
        question = input("用户:")
        answer = handler.chat_main(question)
        print("小路:", answer)
