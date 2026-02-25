import re
from datetime import datetime
from dateutil import parser

def extract_date(thread_name):
    date_found = None
    # Try dateutil.parser first
    try:
        parsed_date = parser.parse(thread_name, fuzzy=True, dayfirst=True)
        date_found = parsed_date.date()
    except Exception:
        pass

    # Regex fallback
    if not date_found:
        match = re.search(r'(\d{1,4})[-/](\d{1,2})[-/](\d{1,4})', thread_name)
        if match:
            parts = match.groups()
            try:
                if len(parts[0]) == 4:  # YYYY-MM-DD
                    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
                else:  # DD-MM-YYYY
                    day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
                date_found = datetime(year, month, day).date()
            except Exception:
                date_found = None
    return date_found
  
