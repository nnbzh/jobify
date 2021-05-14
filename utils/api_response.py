import logging

from rest_framework.response import Response

logger = logging.getLogger('main')


def success_response(data, message, status=200):
    return Response(
        {
            'success': True,
            'data': data,
            "message": message
        }, status=status
    )


def error_response(message, status):
    logger.error(f'Error occurred: {message}. CODE: {status}')
    return Response(
        {
            'success': False,
            'data': None,
            "message": message
        }, status=status
    )
