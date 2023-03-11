from datetime import timedelta


def format_bytes(bytes):
    bytes = bytes if bytes > 0 else 0
    if bytes < 1024:
        return f'{bytes} B'
    prefix = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 1
    while True:
        bytes /= 1024
        if bytes < 1024:
            bytes = round(bytes, 2)
            if str(bytes).endswith('.0'):
                bytes = int(bytes)
            return f'{bytes} {prefix[i]}'
        i += 1


def sum_bytes(*bytes):
    return format_bytes(sum(bytes))


def format_duration(duration):
    return str(timedelta(seconds=duration))


def sum_duration(*duration):
    return format_duration(sum(duration))
