# Time Converter (24h to 12h)
# You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
# - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
# - if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
# Here you can find some useful information about the 12-hour format.
# Input: Time in a 24-hour format (as a string).

# Output: Time in a 12-hour format (as a string).

# Example:

# time_converter('12:30') == '12:30 p.m.'
# time_converter('09:00') == '9:00 a.m.'
# time_converter('23:15') == '11:15 p.m.'
# 1
# 2
# 3
# How it is used: For work with the different time formats.

# Precondition:
# '00:00' <= time <= '23:59'
