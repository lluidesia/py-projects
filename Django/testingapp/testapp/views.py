
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
import pandas as pd

from random import shuffle


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class ResultPageView(TemplateView):
    def get(self, request, **kwargs):
        answer_user = request.GET['answer']
        answer_right = request.GET['answer_r']

        text_legend = "Вітання!!"
        text = "Ви супер пайтон програміст!!"
        text_button = "Ура!"
        snake = "https://img.clipartxtras.com/d814c670ec5e2eb84f04fb44777a6f87_free-python-clipart-python-snake-clipart_218-217.jpeg"
        if answer_user!=answer_right:
            text_legend = "Невдача!!"
            text = "Спробуйте ще раз..."
            text_button = "Пройти ще раз!"
            snake = "https://img.clipartxtras.com/676d82a73a98203c039769c6b61545bb_python-clipart-download-python-clipart-python-snake-clipart_240-195.jpeg"

        return render(request, 'result.html', {'text_legend':text_legend, 'text':text, 'text_button':text_button,'snake':snake})


class TestPageView(TemplateView):
    def get(self, request, **kwargs):
        text_1 = request.GET['TEXT_1']
        if text_1=='':
            text_1 = 'Анонім'

        user_test = Test('files/Questions.csv')
        test_question = user_test.question()

        test_data = {'aaa': text_1, 'question': test_question[0][0], 'val1':test_question[0][1],'val2':test_question[0][2],'val3': test_question[0][3],'answer_r': test_question[0][4]}
        return render(request, 'test.html', test_data)


class Test(object):
    def __init__(self, questions):
        self.questions = pd.read_csv(questions)
        self.n = 1

    def random_question(self):
        num_list = [i for i in range(len(self.questions))]
        shuffle(num_list)
        num_list = num_list[0:self.n]

        return num_list

    def question(self):
        test = self.questions.values[self.random_question()]
        return test

