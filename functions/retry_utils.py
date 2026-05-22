import time
import functools
import random

# Retry decorator for handling 429/503 errors with exponential backoff
def retry_on_429_503(max_retries=5, base_delay=1.0, max_delay=30.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            delay = base_delay
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Check for HTTP error codes 429 or 503
                    status = getattr(e, 'status_code', None) or getattr(e, 'code', None)
                    if status in (429, 503):
                        if retries >= max_retries:
                            raise
                        sleep_time = delay + random.uniform(0, delay * 0.2)
                        print(f"Retryable error {status} encountered. Sleeping {sleep_time:.2f}s before retry {retries+1}...")
                        time.sleep(sleep_time)
                        delay = min(delay * 2, max_delay)
                        retries += 1
                    else:
                        raise
        return wrapper
    return decorator
