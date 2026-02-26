from app import build_response


def test_root() -> None:
    status, payload = build_response("/")
    assert status == 200
    assert payload == {"message": "Service is running"}


def test_health() -> None:
    status, payload = build_response("/health")
    assert status == 200
    assert payload == {"status": "ok"}


def test_not_found() -> None:
    status, payload = build_response("/unknown")
    assert status == 404
    assert payload == {"error": "Not found"}
