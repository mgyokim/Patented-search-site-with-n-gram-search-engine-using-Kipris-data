# -*- coding:utf-8 -*-
import os
from whoosh.index import create_in
from whoosh.fields import *
import csv
from whoosh.qparser import QueryParser,MultifieldParser




def indexing():  # 단어 인덱싱 함수
    global ix
    indexdir = r'C:\Users\kimmi\PycharmProjects\Whoosh_django\django1\searchengine_whoosh'
    if not os.path.exists(indexdir): os.makedirs(indexdir)

    schema = Schema(Patent_Name=NGRAMWORDS(stored=True), IPC_Number=ID(stored=True), Applicant=NGRAMWORDS(stored=True),
                    # lable 별 스키마 지정
                    Application_Number=NGRAMWORDS(stored=True), Application_date=NGRAMWORDS(stored=True),
                    Registration_Number=NGRAMWORDS(stored=True), Registration_date=NGRAMWORDS(stored=True),
                    Public_Number=NGRAMWORDS(stored=True), Public_date=NGRAMWORDS(stored=True),
                    Agent=TEXT(stored=True), Inventor=KEYWORD(stored=True), Description=KEYWORD(stored=True)
                    )

    ix = create_in(indexdir, schema)  # Directory 생성

    writer = ix.writer()
    f = open(r'C:\Users\kimmi\PycharmProjects\Whoosh_django\django1\searchengine_whoosh\인천대학교(인천).csv', encoding="UTF-8")
    title_list = csv.reader(f)  # DB대체로 CSV로 되어있는 인천대학교(인천)csv 파일 읽어오기

    for a in title_list:
        writer.add_document(Patent_Name=f"{a[0]}", IPC_Number=f"{a[1]}", Applicant=f"{a[2]}",
                            Application_Number=f"{a[3]}", Application_date=f"{a[4]}"  # 위치별 정해진 스키마로 analyzing
                            , Registration_Number=f"{a[5]}", Registration_date=f"{a[6]}",
                            Public_Number=f"{a[7]}", Public_date=f"{a[8]}",
                            Agent=f"{a[9]}", Inventor=f"{a[10]}", Description=f"{a[11]}")

    writer.commit()


def search_engine(search):  # 분석된 Schenma 에서 검색어를 찾아주는 함수

    # search = input('검색어를 입력하세요 : ')  # 단어 input
    with ix.searcher() as searcher:


            query1 = MultifieldParser(['Patent_Name','Application_Number',"Description","Inventor"], ix.schema).parse(search)  # input 값을 QueryParser.parse로 찾기
            results = searcher.search(query1,limit = None)  # 결과값 저장

            # if len(results) == 0  :
            #     query2 = QueryParser("Description", ix.schema).parse(search)
            #     results = searcher.search(query2, limit=20)  # 결과값 저장
            #
            # if len(results) == 0  :
            #     query3 = QueryParser("Inventor", ix.schema).parse(search)
            #     results = searcher.search(query3, limit=None)  # 결과값 저장

            print(results)  # 딕셔너리라 하나씩 뽑아서 보여줘야함
            print(len(results))  # 결과값이 원래 갯수
            print(type(results))
            print(query1)

            results_dic=[]
            output_results = list()
            if len(results) == 0:
                output_results = []

            else :
                for r in results:
                    temp_result = []
                    temp_result.append(r['Patent_Name'])
                    temp_result.append(r['IPC_Number'])
                    temp_result.append(r['Applicant'])
                    temp_result.append(r['Application_Number'])
                    temp_result.append(r['Application_date'])
                    temp_result.append(r['Registration_Number'])
                    temp_result.append(r['Registration_date'])
                    temp_result.append(r['Public_Number'])
                    temp_result.append(r['Public_date'])
                    temp_result.append(r['Agent'])
                    temp_result.append(r['Inventor'])
                    temp_result.append(r['Description'])

                    output_results.append(temp_result)
                pk = []
                for k in output_results:
                    pk.append(k[3])
                results_dic = dict(zip(pk, output_results))



            return output_results


        #     output.append(r.values())
        # return output
        #     temp = [r.values(['Patent_Name'])]
        #     output.append(temp)
        # ret   urn output
    #         output = []
    #         temp = []
    #         for i in r :
    #             temp.append(r.values())
    #             break
    #         #     output.append(temp)
    #         # print(output)
    #         # print(r['Patent_Name'], r['IPC_Number'], r['Applicant'], r['Application_Number'], r['Application_date'],
    #         #       r['Registration_Number'], r['Registration_date'], r['Public_Number'], r['Public_date'], r['Agent'],r['Inventor'], r['Description'])
    #         # break
    #         # print(r['Patent_Name'], r['IPC_Number'], r['Applicant'], r['Application_Number'], r['Application_date'],
    #         #       r['Registration_Number'], r['Registration_date'], r['Public_Number'], r['Public_date'], r['Agent'],r['Inventor'], r['Description'])
    #         # break
    # #         output.append(r['Patent_Name'], r['IPC_Number'], r['Applicant'], r['Application_Number'], r['Application_date'],
    # #               r['Registration_Number'], r['Registration_date'], r['Public_Number'], r['Public_date'], r['Agent'],r['Inventor'], r['Description'])
    # #         output_list.append(output)
    # # return output_list

if __name__ == '__main__':  # 웹서버때문에 해놓은 __name__=='__main__' 문
    indexing()
    search_engine('무선')
