# Patented-search-site-with-[n-gram](https://en.wikipedia.org/wiki/N-gram)-search-engine-using-Kipris-data
[Search engine and search site development motivation]

The issue has been raised that it is cumbersome for companies to search for researchers and corresponding patents in the field of research they want during industry-academic cooperation.

I decided to solve the issue. So I collected data myself and created a search engine using [n-gram](https://en.wikipedia.org/wiki/N-gram). And it has developed a patent search site that applies corresponding search engine.

I used the [Django](https://www.djangoproject.com/) web framework and the [whoosh](https://whoosh.readthedocs.io/en/latest/intro.html) engine library. 

I had a hard time because it was my first time, but I finally did it.
#
[Search Site Main Screen]
![Industrial Intelligence Laboratory Page Button](https://user-images.githubusercontent.com/66030601/124103257-0f37ca80-da9c-11eb-839b-3a7d9e85ee1d.gif)
You can visit the website of the Industrial Intelligence Research Institute where I studied through the link to the main page of the patent search site.
#
[Crawled Patent Data]
![Crawled Patent Data](https://user-images.githubusercontent.com/66030601/124113894-e832c600-daa6-11eb-9090-cf4b80bb8288.gif)
The data used in the search engine was collected in the form of csv by crawling directly.
#
[Crawled Patent Image Data]
![Crawled Patent Image Data](https://user-images.githubusercontent.com/66030601/124110568-54132f80-daa3-11eb-918d-42554af9fc3b.gif)
Image data was crawled in the same way, and name values were saved and collected to match the data in the csv file.
#
[Search for a topic of interest]
![Search for a topic of interest](https://user-images.githubusercontent.com/66030601/124114452-8d4d9e80-daa7-11eb-9a79-2042e541c608.gif)
I searched by typing in the search term "electricity". Patents containing the word "electricity" are presented as search results after a search engine applied with [n-gram](https://en.wikipedia.org/wiki/N-gram).
#
[Verifying Long Information]
![Verifying Long Information](https://user-images.githubusercontent.com/66030601/124116439-ecacae00-daa9-11eb-89ab-392fecc619c1.gif)
Long information can be checked by scrolling.
#
[Retrieving information containing Electricity1]
![Retrieving information containing Electricity1](https://user-images.githubusercontent.com/66030601/124115296-9854fe80-daa8-11eb-8dfa-92f2cbea3e88.gif)
If you click on the results of a patent search that includes a search term, the details of the patent will come out.
#
[Retrieving information containing Electricity2]
![Retrieving information containing Electricity2](https://user-images.githubusercontent.com/66030601/124115372-b15daf80-daa8-11eb-987e-3efdab7cdfe4.gif)
Various information about the patent can be found on the detail page.

And you can also zoom in on the patent drawing.

※List of available information※

▶Patent name

▶ IPC Number

▶Application made

▶Application number

▶Application date

▶Registration number

▶ Registration date

▶ Disclosure number

▶ Date of disclosure date

▶ Agent

▶Inventor

▶Patent description


#
By implementing paging function, you can get up to 10 search results per page.

If the search results exceed 10, they are divided into 10 and placed on the next page of that page.

[Next Page Button]
![Next Page Button](https://user-images.githubusercontent.com/66030601/124118477-5a59d980-daac-11eb-85e6-eb8916fa49ec.gif)

[Last Page Button]
![Last Page Button](https://user-images.githubusercontent.com/66030601/124118595-79f10200-daac-11eb-92b7-83f64377e3ac.gif)

[Previous Button]
![Previous Button](https://user-images.githubusercontent.com/66030601/124118682-8d03d200-daac-11eb-891f-b4d003735a1c.gif)

[First page Button ]
![First page Button ](https://user-images.githubusercontent.com/66030601/124118736-9c831b00-daac-11eb-8cd1-f42fc4f2dc78.gif)

#
[Search for new search terms]
![New Search](https://user-images.githubusercontent.com/66030601/124118918-d6ecb800-daac-11eb-898e-c5415aec1c2d.gif)
If you want to search for a new search term, click the INU logo.






