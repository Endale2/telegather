<!-- # Telegather **Version:** 0.1.4 **License:** MIT **Home Page:** https://github.com/Endale2/telegather -->
Telegather
A simple, yet powerful command-line tool that scrapes messages from a public Telegram channel and saves them into a CSV file. Telegather supports both non-interactive (all flags provided) and interactive (step-by-step prompts) modes, and comes with a colorful, banner-style interface.

Features
Scrape any public Telegram channel by username.

Save messages to CSV (with BOM for Excel compatibility).

Interactive prompts if you don’t supply all flags.

Colorful CLI banner and step-by-step inputs for a polished experience.

Flexible limit option: fetch the N most recent messages or “ALL.”

Cross-platform (Windows, macOS, Linux).

Table of Contents
Installation

Quick Start

Usage

Non-Interactive Mode

Interactive Mode

Running as a Python Module

Arguments & Flags

Example CSV Output

Development & Local Testing

Contributing

License

Installation
Telegather is published on PyPI. Simply run:

bash
Copy
Edit
pip install --upgrade telegather
This will install the latest stable version (e.g. 0.1.4). If you want to install a specific version, you can pin it:

bash
Copy
Edit
pip install telegather==0.1.4
Note for Windows users: Make sure your Python Scripts folder (e.g. C:\Users\<you>\AppData\Roaming\Python\Python3X\Scripts) is on your %PATH% so that the telegather command is recognized in your terminal.

Quick Start
Obtain Telegram API credentials
Visit my.telegram.org, log in with your phone number, go to “API Development Tools,” and copy your api_id and api_hash.

Install Telegather

bash
Copy
Edit
pip install --upgrade telegather
Scrape a channel non-interactively

bash
Copy
Edit
telegather \
  --api-id 1234567 \
  --api-hash abcdef0123456789abcdef0123456789 \
  --channel nytimesworld \
  --limit 100 \
  --output msgs.csv
This fetches the 100 most recent messages from t.me/nytimesworld and writes them into msgs.csv.

Or run interactively

bash
Copy
Edit
telegather
You’ll see a colorful banner and step-by-step prompts for API_ID, API_HASH, channel, limit, and output.

Open the resulting CSV

bash
Copy
Edit
# macOS
open msgs.csv

# Linux
xdg-open msgs.csv

# Windows (PowerShell)
start msgs.csv
Usage
Non-Interactive Mode
If you already know all the required values, provide them as flags:

bash
Copy
Edit
telegather \
  --api-id 1234567 \
  --api-hash abcdef0123456789abcdef0123456789 \
  --channel someChannelUsername \
  --limit 50 \
  --output latest_posts.csv
--api-id: Your numeric Telegram API ID.

--api-hash: Your Telegram API hash string.

--channel: The target channel username (omit t.me/).

--limit: Number of messages to fetch (omit or 0 for ALL).

--output: CSV file path (defaults to msgs.csv).

Once executed, you will see:

pgsql
Copy
Edit
→ Starting scrape: channel='someChannelUsername', limit=50, output='latest_posts.csv'
✅ Successfully saved 50 messages to 'latest_posts.csv'.
Interactive Mode
If any required flags are missing, Telegather will prompt you:

bash
Copy
Edit
$ telegather
Banner (clears the terminal, prints the colored header).

Step 1/4: API_ID

scss
Copy
Edit
→ [Step 1/4] Enter your Telegram API_ID
   API_ID (integer):
Step 2/4: API_HASH

scss
Copy
Edit
→ [Step 2/4] Enter your Telegram API_HASH
   API_HASH (string):
Step 3/4: Channel

scss
Copy
Edit
→ [Step 3/4] Enter the target channel username
   Channel username (without t.me/):
Step 4/4: Limit

less
Copy
Edit
→ [Step 4/4] How many messages to scrape?
   Enter a number (blank or 0 = ALL):
Output Filename

css
Copy
Edit
Output CSV file path [msgs.csv]:
(Press ENTER to accept msgs.csv, or type a custom name.)

Summary

yaml
Copy
Edit
───────────────────────────────────────────────────
→ About to scrape from channel: my_channel
   API_ID:        1234567
   API_HASH:      abcdef0123456789abcdef
   Limit:         100
   Output CSV:    msgs.csv
───────────────────────────────────────────────────
Scraping Starts

pgsql
Copy
Edit
→ Starting scrape: channel='my_channel', limit=100, output='msgs.csv'
✅ Successfully saved 100 messages to 'msgs.csv'.
Running as a Python Module
If for some reason your telegather command isn’t on $PATH, you can always run:

bash
Copy
Edit
python -m telegather.cli \
  --api-id 1234567 \
  --api-hash abcdef0123456789abcdef \
  --channel nytimesworld \
  --limit 50
Or interactively:

bash
Copy
Edit
python -m telegather.cli
All the same banner, prompts, and functionality will work exactly as described above.

Arguments & Flags
Flag	Type	Description	Default
--api-id	integer	Your Telegram API ID (from my.telegram.org).	None (prompts if missing)
--api-hash	string	Your Telegram API hash (from my.telegram.org).	None (prompts if missing)
--channel	string	Target channel username (omit t.me/).	None (prompts if missing)
--limit	integer	Number of messages to fetch. Use 0 or leave blank for ALL messages.	None (prompts if missing)
--output	string	Output CSV file path. Written with UTF-8 BOM for Excel compatibility.	msgs.csv
-h, --help	—	Show help text and exit.	—

Note: If you supply any of the first three flags (api-id, api-hash, channel), the script will not prompt for that value. Likewise, if you supply --limit, it won’t ask you about message count.

Example CSV Output
After a successful run, you’ll see a CSV file like this:

bash
Copy
Edit
id,date,text
12345,2025-06-01T14:23:00,"First message text…"
12346,2025-06-01T14:25:10,"Another message (newlines → spaces)…"
12347,2025-06-01T14:27:05,"Yet another message…"
…
id: Telegram’s internal message ID.

date: ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SS).

text: The message body, with any newline characters replaced by spaces.

You can open this file in Excel, Google Sheets, or any CSV-capable tool.

Development & Local Testing
If you want to test changes locally (prior to publishing on PyPI):

Clone the repository (if you haven’t already):

bash
Copy
Edit
git clone https://github.com/Endale2/telegather.git
cd telegather
Create a virtual environment and activate it:

bash
Copy
Edit
python3 -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
.venv\Scripts\Activate.ps1
Install in editable mode:

bash
Copy
Edit
pip install --upgrade pip setuptools wheel
pip install -e .
Now telegather on your path points to your local source code.

Verify the version:

bash
Copy
Edit
pip show telegather
It should show Version: 0.1.4 and Location: /path/to/your/telegather/project.

Run the CLI:

Check help:

bash
Copy
Edit
telegather --help
Try interactive mode:

bash
Copy
Edit
telegather
Try a dry-run (invalid credentials will error but you’ll see the banner/prompts):

bash
Copy
Edit
telegather --api-id 1234 --api-hash invalid --channel test_channel
Make changes & repeat
Whenever you update cli.py or other code, just re-run:

bash
Copy
Edit
pip install -e .
to pick up the latest edits.

Contributing
Contributions, bug reports, and pull requests are welcome! Here’s how you can help:

Fork the repo
https://github.com/Endale2/telegather/fork

Create a new branch

bash
Copy
Edit
git checkout -b feature/my-new-feature
Make your changes, then run tests (if any) and ensure flake8/black (or your style guide) is satisfied.

Commit & push

bash
Copy
Edit
git add .
git commit -m "Add some feature or fix a bug"
git push origin feature/my-new-feature
Open a Pull Request on GitHub. Describe the change in detail and reference any related issues.

License
This project is licensed under the MIT License. See LICENSE for the full text.








