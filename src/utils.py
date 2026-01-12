import math

def convert_timestamp(seconds):
    """Convert seconds to SRT timestamp format"""
    hours = math.floor(seconds / 3600)
    seconds = seconds % 3600
    minutes = math.floor(seconds / 60)
    seconds = seconds % 60
    milliseconds = math.floor((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)

    # Format: HH:MM:SS,mmm
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"