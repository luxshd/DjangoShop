import logging
import time

logger = logging.getLogger(__name__)

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)
        duration = (time.perf_counter() - start) * 1000
        user = request.user.username if request.user.is_authenticated else "anonymous"
        logger.info("%s %s -> %s | %.1f ms | user=%s",
                    request.method, request.path, response.status_code, duration, user)
        response["X-Request-Duration-ms"] = f"{duration:.1f}"
        return response