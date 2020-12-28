from django.shortcuts import render
from search.documents import NutritionDocument
# Create your views here.

def search(request):
      q = request.GET.get('q')
      if q:
            food = NutritionDocument.search().query('match', food=q)
            print(len(q))

      else:
            food = ''
            
      return render(request, 'search.html', {'food':food})