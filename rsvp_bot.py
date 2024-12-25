import os
import datetime
import json
import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow

SCOPES = ['https://www.googleapis.com/auth/calendar.events']
CLIENT_SECRET_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

def print_banner():
    print("=" * 50)
    print("          AUTOMATED RSVP BOT".center(50))
    print("=" * 50)
    print("   Manage RSVPs Easily and Quickly".center(50))
    print("=" * 50)

def authenticate_google():
    storage = Storage(TOKEN_FILE)
    credentials = storage.get()

    if not credentials or credentials.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        credentials = run_flow(flow, storage)
    
    http = credentials.authorize(httplib2.Http())
    service = build('calendar', 'v3', http=http)
    return service

def get_upcoming_events(service):
    now = datetime.datetime.utcnow().isoformat() + 'Z' 
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    return events

def auto_rsvp(service, events):
    for event in events:
        event_id = event['id']
        summary = event.get('summary', 'No Title')
        start = event['start'].get('dateTime', event['start'].get('date'))
        print("[INFO] Event: {} at {}".format(summary, start))

        decision = raw_input("RSVP (Accept/Tentative/Decline)? [A/T/D]: ").strip().lower()
        if decision == 'a':
            response = 'accepted'
        elif decision == 't':
            response = 'tentative'
        else:
            response = 'declined'

        service.events().update(
            calendarId='primary',
            eventId=event_id,
            body={"status": response}
        ).execute()
        print("[SUCCESS] RSVP '{}' untuk {}".format(response, summary))

def main():
    print_banner()
    print("[INFO] Autentikasi Google Calendar...")
    service = authenticate_google()

    print("[INFO] Mendapatkan acara mendatang...")
    events = get_upcoming_events(service)

    if not events:
        print("[ERROR] Tidak ada acara yang ditemukan.")
        return

    print("[INFO] Mulai RSVP otomatis...")
    auto_rsvp(service, events)

if __name__ == '__main__':
    main()
