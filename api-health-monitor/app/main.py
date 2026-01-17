from app.health_checker import check_health
from app.db import get_all_apis, get_previous_state, update_state
from app.notifier import send_notification


def main():
    apis = get_all_apis()

    for api in apis:
        api_id = api["api_id"]
        url = api["url"]
        expected_status = int(api["expected_status"])
        timeout_ms = int(api["timeout_ms"])

        current_state = check_health(url, expected_status, timeout_ms)
        previous = get_previous_state(api_id)

        if previous and previous["last_state"] != current_state:
            message = (
                f"API {url} changed from "
                f"{previous['last_state']} to {current_state}"
            )
            send_notification(message)

        update_state(api_id, current_state)


if __name__ == "__main__":
    main()


