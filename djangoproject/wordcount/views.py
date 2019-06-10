from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split() # 이거 자체가 list 
    word_dictionary = {}

    for word in words: 
        if word in word_dictionary:
            # increse 
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1
            
    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary':word_dictionary.items()})