from django.shortcuts import render
from searchengine_whoosh.whoosh_ex import indexing
from searchengine_whoosh.whoosh_ex import search_engine
from django.core.paginator import Paginator
import pandas as pd
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import *

indexing()

def index(request) :#request =
    return render(request, 'search_page/index.html')

def search_result(request) :
    page = request.GET.get('page')
    print(page)
    print("뭘까" + str(request))
    if page == None :

        user_input_str = request.GET.get('search_input')#검색어를 받음
        print(user_input_str)
        user_output_str = search_engine(user_input_str)
        a = int(1)
        # if user_output_str == []:
        #
        #     return render(request, 'my_to_do_app/search_result.html', {'user_output_str_in_html': user_output_str })
        # else:
        #     for i in user_output_str:
        #         i.append(a)
        #         a += 1
        #         # print(user_output_str)
        #
        paginator = Paginator(user_output_str, 10)
        page = paginator.get_page(page)

        return render(request, 'search_page/search_result.html', {'user_output_str_in_html': page ,
                                                                   'all_things' : user_output_str ,
                                                                   "search_input": user_input_str})
    else :
        next_page= request.GET.get(page)
        user_input_str = request.GET.get('search_input')
        user_output_str = search_engine(user_input_str)
        # next_page_2 = request.GET.get()
        print('넘어갔습니다')
        print(request)
        print(next_page)
        paginator = Paginator(user_output_str, 10)
        page = paginator.get_page(page)
        # print(next_page_2)
        return render(request, 'search_page/search_result.html', {'user_output_str_in_html': page , 'all_things' : user_output_str ,"search_input": user_input_str})


def detail(request):
    print("뭘까요" + str(request))
    # print(request)
    detail_input = request.GET.get('key')
    print(detail_input)
    detail_output = search_engine(detail_input)

    return render(request, 'search_page/detail.html', {'detail_output': detail_output})

# def make_detail_page(request) :
#     user_input_str = request.POST['search_input']#검색어를 받음
#     user_output_str = search_engine(user_input_str)
#     page_name_list =
#     for href in user_output_str :
#         page_name_list.append(href[3])










# def searched_list(request) :
#     user_input_str = request.POST['todoContent']
#     new_todo = Todo(content = user_input_str)
#     new_todo.save()
#     return HttpResponseRedirect(reverse('index'))
#

# Create your views here.