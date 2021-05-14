from rest_framework.response import Response


def success_response(data, message, status=200):
    return Response(
        {
            'success': True,
            'data': data,
            "message": message
        }, status=status
    )


def error_response(message, status):
    return Response(
        {
            'success': False,
            'data': None,
            "message": message
        }, status=status
    )
