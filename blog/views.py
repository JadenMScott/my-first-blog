from django.shortcuts import render

# Create your views here.
def post_request(request):
    return render(request, 'blog/post_list.html',{})