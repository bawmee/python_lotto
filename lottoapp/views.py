from django.shortcuts import render
import random

def index(request):
    return render(request, 'index.html')


def result(request):

    randset = set()

    while len(randset) < 7:
        randset.add(random.randint(1, 45))
    
    lotto = sorted(randset)

    c = ['one', 'two', 'three', 'four', 'five']

    colorball = dict()
    for i in lotto:
        colorball[i] = c[i // 10]

    print(colorball)
    

    return render(request, 'result.html', {'lotto' : lotto, 'colorball':colorball})
