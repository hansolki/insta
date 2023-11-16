from django.shorcuts.import redirect

def main(request):
    return redirect('posts:index')
