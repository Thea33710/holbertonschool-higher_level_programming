#!/usr/bin/python3
"""
Function that generates personalized invitation files
from a template with placeholders and a list of objects.
"""

import os

def generate_invitations(template, attendees):
    """
    Generates invitation files from a template string and a list of attendees.

    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries containing attendee data.
    """

    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") or "N/A"
        title = attendee.get("event_title") or "N/A"
        date = attendee.get("event_date") or "N/A"
        location = attendee.get("event_location") or "N/A"

        personalized = (template
                        .replace("{name}", name)
                        .replace("{event_title}", title)
                        .replace("{event_date}", date)
                        .replace("{event_location}", location))

        output_filename = f"output_{i}.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(personalized)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
            continue

    print(f"{len(attendees)} invitation file(s) generated successfully.")
