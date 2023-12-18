from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from api.models import Book, Author, Category, User
from api.serializers import *

@api_view(['GET'])
def get_all_books(request):
    Books = Book.objects.all()
    serializer = BookSerializer(Books, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_all_authors(request):
    Authors = Author.objects.all()
    serializer = AuthorSerializer(Authors, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_all_categories(request):
    Categories = Category.objects.all()
    serializer = CategorySerializer(Categories, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_all_users(request):
    Users = User.objects.all()
    serializer = UserSerializer(Users, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def get_author(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AuthorSerializer(author)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def get_Category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def get_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def add_book(request):
    data = JSONParser().parse(request)
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def add_author(request):
    data = JSONParser().parse(request)
    serializer = AuthorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def add_category(request):
    data = JSONParser().parse(request)
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def add_user(request):
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def edit_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    serializer = BookSerializer(book, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def edit_author(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    serializer = AuthorSerializer(author, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def edit_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    serializer = CategorySerializer(category, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def edit_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_author(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    author.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_books_by_author(request, pk):
    try:
        books = Book.objects.filter(author=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_books_by_category(request, pk):
    try:
        books = Book.objects.filter(category=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_books_read_by_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    books = user.read_books.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_best_authors(request, n):
    authors = Author.objects.all().order_by('-average_rating')[:n]
    serializer = AuthorSerializer(authors, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_best_books(request, n):
    books = Book.objects.all().order_by('-rating')[:n]
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def search_books(request, title):
    books = Book.objects.filter(title__contains=title)
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)


