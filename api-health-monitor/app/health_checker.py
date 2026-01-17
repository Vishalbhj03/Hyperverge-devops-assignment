import requests
import time


def check_health(url, expected_status, timeout_ms):
    try:
        start = time.time()
        response = requests.get(url, timeout=timeout_ms / 1000)
        end = time.time()

        response_time_ms = (end - start) * 1000

        if response.status_code == expected_status and response_time_ms <= timeout_ms:
            return "HEALTHY"

        return "UNHEALTHY"

    except requests.RequestException:
        return "UNHEALTHY"

