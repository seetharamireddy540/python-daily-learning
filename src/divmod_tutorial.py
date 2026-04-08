"""Complete guide to divmod and related division operations in Python."""


# ============================================================================
# 1. DIVMOD BASICS
# ============================================================================

def divmod_basics():
    """divmod(a, b) returns (quotient, remainder) as a tuple."""
    
    # divmod(17, 5) means: 17 ÷ 5 = 3 remainder 2
    quotient, remainder = divmod(17, 5)
    print(f"17 ÷ 5 = {quotient} remainder {remainder}")  # 3 remainder 2
    
    # Equivalent to:
    q = 17 // 5  # Floor division (quotient)
    r = 17 % 5   # Modulo (remainder)
    print(f"Using // and %: {q} remainder {r}")
    
    # Why use divmod? It's more efficient (one operation vs two)
    result = divmod(100, 7)
    print(f"divmod(100, 7) = {result}")  # (14, 2)


# ============================================================================
# 2. PRACTICAL USE CASES
# ============================================================================

def convert_seconds_to_time(total_seconds):
    """Convert seconds to hours, minutes, seconds."""
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"


def convert_cents_to_dollars(cents):
    """Convert cents to dollars and cents."""
    dollars, remaining_cents = divmod(cents, 100)
    return f"${dollars}.{remaining_cents:02d}"


def split_into_groups(total_items, group_size):
    """Calculate full groups and leftover items."""
    full_groups, leftover = divmod(total_items, group_size)
    return f"{full_groups} groups of {group_size}, {leftover} left over"


# ============================================================================
# 3. DIVISION OPERATORS COMPARISON
# ============================================================================

def division_operators():
    """Compare all division operators in Python."""
    a, b = 17, 5
    
    print(f"a = {a}, b = {b}\n")
    
    # Regular division (float result)
    print(f"a / b  = {a / b}")           # 3.4 (true division)
    
    # Floor division (rounds down to nearest integer)
    print(f"a // b = {a // b}")          # 3 (quotient)
    
    # Modulo (remainder)
    print(f"a % b  = {a % b}")           # 2 (remainder)
    
    # divmod (both at once)
    print(f"divmod(a, b) = {divmod(a, b)}")  # (3, 2)
    
    # Verify: quotient * divisor + remainder = dividend
    q, r = divmod(a, b)
    print(f"\nVerify: {q} * {b} + {r} = {q * b + r}")  # 3 * 5 + 2 = 17


# ============================================================================
# 4. NEGATIVE NUMBERS
# ============================================================================

def negative_numbers():
    """divmod with negative numbers (floors toward negative infinity)."""
    
    print("Positive numbers:")
    print(f"divmod(17, 5) = {divmod(17, 5)}")    # (3, 2)
    
    print("\nNegative dividend:")
    print(f"divmod(-17, 5) = {divmod(-17, 5)}")  # (-4, 3)
    # -17 = -4 * 5 + 3 = -20 + 3 = -17 ✓
    
    print("\nNegative divisor:")
    print(f"divmod(17, -5) = {divmod(17, -5)}")  # (-4, -3)
    # 17 = -4 * -5 + -3 = 20 - 3 = 17 ✓
    
    print("\nBoth negative:")
    print(f"divmod(-17, -5) = {divmod(-17, -5)}")  # (3, -2)
    # -17 = 3 * -5 + -2 = -15 - 2 = -17 ✓


# ============================================================================
# 5. REAL-WORLD EXAMPLES
# ============================================================================

def format_bytes(bytes_count):
    """Convert bytes to KB, MB, GB."""
    gb, remainder = divmod(bytes_count, 1024**3)
    mb, remainder = divmod(remainder, 1024**2)
    kb, b = divmod(remainder, 1024)
    
    parts = []
    if gb: parts.append(f"{gb}GB")
    if mb: parts.append(f"{mb}MB")
    if kb: parts.append(f"{kb}KB")
    if b: parts.append(f"{b}B")
    
    return " ".join(parts) or "0B"


def paginate(total_items, items_per_page):
    """Calculate pagination info."""
    total_pages, extra = divmod(total_items, items_per_page)
    if extra > 0:
        total_pages += 1  # Need one more page for remaining items
    return total_pages


def decimal_to_base(number, base):
    """Convert decimal number to any base (2-36)."""
    if number == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    
    while number > 0:
        number, remainder = divmod(number, base)
        result.append(digits[remainder])
    
    return "".join(reversed(result))


# ============================================================================
# 6. PERFORMANCE COMPARISON
# ============================================================================

def performance_test():
    """divmod is faster than separate // and % operations."""
    import timeit
    
    # Using divmod
    time_divmod = timeit.timeit(
        "divmod(123456789, 7)",
        number=1_000_000
    )
    
    # Using separate operations
    time_separate = timeit.timeit(
        "123456789 // 7; 123456789 % 7",
        number=1_000_000
    )
    
    print(f"divmod: {time_divmod:.4f}s")
    print(f"// and %: {time_separate:.4f}s")
    print(f"divmod is {time_separate/time_divmod:.2f}x faster")


# ============================================================================
# DEMO
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("1. DIVMOD BASICS")
    print("=" * 60)
    divmod_basics()
    
    print("\n" + "=" * 60)
    print("2. PRACTICAL EXAMPLES")
    print("=" * 60)
    print(convert_seconds_to_time(3665))
    print(convert_cents_to_dollars(1234))
    print(split_into_groups(47, 5))
    
    print("\n" + "=" * 60)
    print("3. DIVISION OPERATORS")
    print("=" * 60)
    division_operators()
    
    print("\n" + "=" * 60)
    print("4. NEGATIVE NUMBERS")
    print("=" * 60)
    negative_numbers()
    
    print("\n" + "=" * 60)
    print("5. REAL-WORLD EXAMPLES")
    print("=" * 60)
    print(f"Bytes: {format_bytes(5_368_709_120)}")
    print(f"Pages needed for 100 items (10/page): {paginate(100, 10)}")
    print(f"255 in binary: {decimal_to_base(255, 2)}")
    print(f"255 in hex: {decimal_to_base(255, 16)}")
    
    print("\n" + "=" * 60)
    print("6. PERFORMANCE")
    print("=" * 60)
    performance_test()
