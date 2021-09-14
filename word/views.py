from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def count(request):
    fulltext = request.GET['fulltext'].lower()
    words = fulltext.split()
    wordlist = {}
    for word in words:
        if word in wordlist:
            wordlist[word] += 1
        else:
            wordlist[word] = 1
    return render(request, 'count.html', {'fulltext':fulltext, 'words':len(words), 'word_list':sorted(wordlist.items())})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
