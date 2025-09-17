from typing import List, Tuple, Optional
from collections import defaultdict


def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    """Return a new list with duplicate emails removed, preserving first seen.
    Treat emails case-insensitively. Keep the first form you saw.
    Ignore entries that do not contain an '@' character.
    """
    seen = set()
    result = []

    for email in emails:
        if '@' not in email:
            continue
        lower_email = email.lower()
        if lower_email not in seen:
            seen.add(lower_email)
            result.append(email)

    return result


def first_with_domain(emails: List[str], domain: str) -> Optional[int]:
    """Return the index of the first email whose domain matches `domain`.
    Comparison is case-insensitive.
    """
    domain_lower = domain.lower()
    for i, email in enumerate(emails):
        if '@' not in email:
            continue
        _, email_domain = email.rsplit('@', 1)
        if email_domain.lower() == domain_lower:
            return i
    return None


def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    """Return (domain, count) pairs sorted by domain (A..Z), case-insensitive.
    Skip malformed entries without an '@'.
    Keep the first-seen form of the domain (case preserved).
    """
    counts = defaultdict(int)
    original = {}

    for email in emails:
        if '@' not in email:
            continue
        _, domain = email.rsplit('@', 1)
        d_lower = domain.lower()
        counts[d_lower] += 1
        if d_lower not in original:
            original[d_lower] = domain  # preserve first-seen casing

    return sorted(
        ((original[d], counts[d]) for d in counts),
        key=lambda x: x[0].lower()
    )
