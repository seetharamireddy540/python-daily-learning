import decimal


def calc_duration(seconds: decimal, stretch: bool = False) -> str:
    """Format seconds with ns resolution into human-readable time string.

    Args:
        seconds: Number of seconds with nanosecond resolution
        stretch: If True, include ms, us, ns in output

    Returns:
        Formatted time string with non-zero values only
    """
    if seconds == 0:
        return "0 seconds"

    ns_total = round(seconds * 1_000_000_000)

    days, ns_total = divmod(ns_total, 86_400_000_000_000)
    hours, ns_total = divmod(ns_total, 3_600_000_000_000)
    minutes, ns_total = divmod(ns_total, 60_000_000_000)
    secs, ns_total = divmod(ns_total, 1_000_000_000)

    parts = []

    if days:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if secs:
        parts.append(f"{secs} second{'s' if secs != 1 else ''}")

    if stretch and ns_total:
        ms, ns_total = divmod(ns_total, 1_000_000)
        us, ns = divmod(ns_total, 1_000)

        if ms:
            parts.append(f"{ms} ms")
        if us:
            parts.append(f"{us} us")
        if ns:
            parts.append(f"{ns} ns")

    return ", ".join(parts)
