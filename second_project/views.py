from django.http import JsonResponse

def home_view(request):
    data = {
        'name': 'name',
        'success': True,
    }
    return JsonResponse(data, status=200)