from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# we want to be able to POST to this view from clients that won't have a
# CSRF token we need to mark the view as csrf_exempt
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets (GET) or
    create a  new snippet (POST)
    """
    if request.method == 'GET':
        # Serialize Snippets to JSON
        snippets_queryset = Snippet.objects.all()
        serializer = SnippetSerializer(snippets_queryset, many=True)
        snippets_dict = serializer.data
        return JsonResponse(snippets_dict, safe=False)
    elif request.method == 'POST':
        # De-serialize JSON to snippet(A new Snippet)
        data = JSONParser.parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete individual snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        snippet_dict = serializer.data
        return JsonResponse(snippet_dict)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)
