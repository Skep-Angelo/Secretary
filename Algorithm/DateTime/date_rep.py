# datetime_operations_reference.py
# A practical reference file for date/time representations and operations in Python
# Covers:
# - datetime
# - date
# - time
# - timedelta
# - timezone handling
# - interval operations
# - recurrence helpers

from datetime import datetime, date, time, timedelta, timezone
from zoneinfo import ZoneInfo

# --------------------------------------------------
# BASIC REPRESENTATIONS
# --------------------------------------------------

# Current date and time (local machine clock)
now_local = datetime.now()

# Current UTC time
now_utc = datetime.now(timezone.utc)

# Specific datetime
custom_dt = datetime(2026, 2, 7, 10, 30, 0)

# Date only
only_date = date(2026, 2, 7)

# Time only
only_time = time(10, 30, 0)

# Combine date + time → datetime
combined = datetime.combine(only_date, only_time)

# --------------------------------------------------
# STRING FORMATS
# --------------------------------------------------

# To ISO string (best for storage)
iso_str = now_utc.isoformat()

# From ISO string
parsed_iso = datetime.fromisoformat(iso_str)

# Custom formatting
formatted = now_local.strftime("%Y-%m-%d %H:%M:%S")

# Parse from custom string
parsed_custom = datetime.strptime("2026-02-07 10:30:00", "%Y-%m-%d %H:%M:%S")

# --------------------------------------------------
# TIMEZONES
# --------------------------------------------------

# Attach timezone
accra_tz = ZoneInfo("Africa/Accra")
accra_time = datetime.now(accra_tz)

# Convert timezone
ny_tz = ZoneInfo("America/New_York")
ny_time = accra_time.astimezone(ny_tz)

# --------------------------------------------------
# TIMEDELTA (DURATION)
# --------------------------------------------------

# Create duration
delta = timedelta(days=2, hours=3, minutes=15)

# Add / subtract duration
future = now_local + delta
past = now_local - delta

# Difference between two datetimes
elapsed = future - now_local
seconds = elapsed.total_seconds()

# --------------------------------------------------
# COMPARISONS
# --------------------------------------------------

# Comparison operators work directly
is_future = future > now_local
is_same = now_local == parsed_iso

# --------------------------------------------------
# RANGE / INTERVAL OPERATIONS
# --------------------------------------------------

class TimeInterval:
    def __init__(self, start: datetime, end: datetime):
        if end <= start:
            raise ValueError("End must be after start")
        self.start = start
        self.end = end

    def duration(self):
        return self.end - self.start

    def contains(self, moment: datetime):
        return self.start <= moment <= self.end

    def intersects(self, other: "TimeInterval"):
        return self.start < other.end and other.start < self.end

    def intersection(self, other: "TimeInterval"):
        if not self.intersects(other):
            return None
        return TimeInterval(
            max(self.start, other.start),
            min(self.end, other.end)
        )

    def is_subset_of(self, other: "TimeInterval"):
        return self.start >= other.start and self.end <= other.end


# Example intervals
a = TimeInterval(
    datetime(2026, 2, 7, 9, 0),
    datetime(2026, 2, 7, 11, 0)
)

b = TimeInterval(
    datetime(2026, 2, 7, 10, 0),
    datetime(2026, 2, 7, 12, 0)
)

has_overlap = a.intersects(b)
overlap_block = a.intersection(b)

# --------------------------------------------------
# WEEK / MONTH HELPERS
# --------------------------------------------------

# Start of day
start_of_day = now_local.replace(hour=0, minute=0, second=0, microsecond=0)

# End of day
end_of_day = now_local.replace(hour=23, minute=59, second=59, microsecond=999999)

# Weekday (0 = Monday)
weekday = now_local.weekday()

# ISO week number
week_number = now_local.isocalendar().week

# --------------------------------------------------
# SIMPLE RECURRENCE GENERATORS
# --------------------------------------------------

def daily_occurrences(start: datetime, count: int):
    return [start + timedelta(days=i) for i in range(count)]


def weekly_occurrences(start: datetime, count: int):
    return [start + timedelta(weeks=i) for i in range(count)]


def every_n_minutes(start: datetime, n: int, count: int):
    return [start + timedelta(minutes=n * i) for i in range(count)]


# --------------------------------------------------
# ROUNDING
# --------------------------------------------------

def round_to_nearest_minute(dt: datetime):
    return dt.replace(second=0, microsecond=0)


def round_to_next_hour(dt: datetime):
    return (dt.replace(minute=0, second=0, microsecond=0)
            + timedelta(hours=1))

# --------------------------------------------------
# SORTING LISTS OF DATETIME
# --------------------------------------------------

dates = [
    datetime(2026, 2, 7, 12),
    datetime(2026, 2, 7, 9),
    datetime(2026, 2, 7, 18),
]

sorted_dates = sorted(dates)

# --------------------------------------------------
# SAFE STORAGE FORMAT RECOMMENDATION
# --------------------------------------------------

# Always store as:
# ISO 8601 string in UTC
safe_store = datetime.now(timezone.utc).isoformat()

# And parse with:
# datetime.fromisoformat(value)
