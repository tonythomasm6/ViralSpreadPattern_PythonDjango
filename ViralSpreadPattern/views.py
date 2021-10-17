from django.shortcuts import render
from .Actions import task3
from .Actions import base
from django.http import HttpResponse
from .forms import PatternForm
# Create your views here.
def homepage(request):
    return render(request, "homepage.html",{})


def load_people(request):
    all_people = base.loadPeople()
    return render(request, 'people.html', {"all_people":all_people})

def findPattern(request):

    if request.method == "POST":
        myPatternForm = PatternForm(request.POST)
        if myPatternForm.is_valid():
            days = myPatternForm.cleaned_data["days"]
            probability = myPatternForm.cleaned_data["probability"]
            inithealth = myPatternForm.cleaned_data["inithealth"]
            if days ==" " or probability == "" or inithealth == "" or days == None or probability == None or inithealth == None:
                return render(request, "error.html",{"errmsg":"None of the field can be empty"})
            elif probability < 0 or probability > 1:
                return render(request, "error.html", {"errmsg": "Probability of meet should be between 0 and 1"})
            elif inithealth > 100 or inithealth < 0:
                return render(request, "error.html", {"errmsg": "Patient zero health should be between 0 and 100"})
            else:
                base.loadgraph(days, probability, inithealth)

            return render(request, "graph.html", {"form":myPatternForm})
