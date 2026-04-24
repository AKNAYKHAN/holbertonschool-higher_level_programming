#!/usr/bin/python3
"""Simple templating program for generating invitation files."""


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template."""

    # Type checks
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Empty checks
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            invitation = invitation.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)

        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as error:
            print("Error writing file {}: {}".format(filename, error))
            return
