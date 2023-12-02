from django.http import HttpRequest


def get_ngrok_url(request: HttpRequest) -> str:
    host_header = request.headers.get('Host', '')
    return f'https://{host_header}' if 'ngrok' in host_header else 'http://localhost:8000'
