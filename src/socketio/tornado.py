import sys
if sys.version_info >= (3, 5):
    try:
        from engineio_yas.async_drivers.tornado import get_tornado_handler as \
            get_engineio_handler
    except ImportError:  # pragma: no cover
        get_engineio_handler = None


def get_tornado_handler(socketio_server):  # pragma: no cover
    return get_engineio_handler(socketio_server.eio)
