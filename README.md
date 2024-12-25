# Automated RSVP Bot

![automated-rsvp-bot Jenderal92](https://github.com/user-attachments/assets/091d78ad-1d75-45f5-9f92-c363af87f0f7)


**Automated RSVP Bot** is a Python-based tool that uses the **Google Calendar API** to automate RSVP responses for your calendar events. It scans your upcoming events and sends RSVP responses (Accept, Tentative, or Decline) based on your preferences or manual input.

## Features
- **Google Calendar Integration**: Connects securely using OAuth2.
- **Automated RSVP**: Automatically respond to calendar event invitations.
- **Manual Confirmation**: Allows users to decide RSVP responses manually if desired.
- **Event Scanning**: Scans up to 10 upcoming events from your Google Calendar.
- **Customizable**: The logic for RSVP responses can be tailored to your needs.

## Requirements
- Python 2.7
- A Google Cloud project with **Google Calendar API** enabled.
- `credentials.json` file for authentication.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Jenderal92/automated-rsvp-bot.git
   cd automated-rsvp-bot
   ```

2. **Install Dependencies**:
   Install required Python packages:
   ```bash
   pip install oauth2client google-api-python-client httplib2
   ```

3. **Setup Google API**:
   - Visit the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project and enable the **Google Calendar API**.
   - Download the `credentials.json` file and place it in the project directory.

## Usage
1. **Run the Script**:
   ```bash
   python rsvp_bot.py
   ```

2. **Authenticate**:
   - The script will open a browser window to authenticate with your Google account.
   - After successful authentication, it will save the token in `token.json` for future use.

3. **Respond to Events**:
   - The script will display upcoming events.
   - You can choose to Accept (`A`), Tentative (`T`), or Decline (`D`) the invitations.

## How It Works
1. **Authenticate Google Account**:
   - The script uses OAuth2 to securely access your Google Calendar.

2. **Scan Events**:
   - It fetches a list of up to 10 upcoming events using the Google Calendar API.

3. **Send RSVP**:
   - Based on your input, it sends RSVP responses (`accepted`, `tentative`, `declined`) for each event.

## Customization
- Modify the RSVP logic in the `auto_rsvp()` function to automate responses based on event properties like title or time.

## Troubleshooting
- **Invalid Token**: Delete `token.json` and re-run the script to re-authenticate.
- **Missing Credentials**: Ensure `credentials.json` is in the project directory.
- **API Errors**: Check that the **Google Calendar API** is enabled in your Google Cloud project.
