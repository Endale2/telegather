# Telegather

**Version:** 0.1.4 | **License:** MIT

A lightweight CLI tool to scrape messages from a public Telegram channel and save them to CSV. Supports both flag-driven and interactive modes with a colored banner.

---

## 🚀 Installation

```bash
# From PyPI:
pip install --upgrade telegather
```

To install a specific version:

```bash
pip install telegather==0.1.4
```

> **Tip (Windows):** Ensure your Python “Scripts” folder is on `%PATH%` so `telegather` is recognized.

---

## 📋 Usage

### 1. Non-Interactive Mode

If you already have your Telegram API credentials:

```bash
telegather \
  --api-id 1234567 \
  --api-hash abcdef0123456789abcdef0123456789 \
  --channel someChannelUsername \
  --limit 50 \
  --output messages.csv
```

- `--api-id` (integer): your Telegram API ID  
- `--api-hash` (string): your Telegram API hash  
- `--channel` (string): channel username (omit `t.me/`)  
- `--limit` (int): number of messages (0 or omit for ALL)  
- `--output` (string): output CSV filename (default: `msgs.csv`)

### 2. Interactive Mode

Run without flags:

```bash
telegather
```

1. Clears screen & displays a colored banner.  
2. Prompts step-by-step for:
   - **API_ID**  
   - **API_HASH**  
   - **Channel username**  
   - **Limit** (blank or 0 = ALL)  
   - **Output CSV path** (default shown in brackets)  
3. Shows a summary, then scrapes and writes CSV.

---

## 📁 Example CSV

```csv
id,date,text
12345,2025-06-01T14:23:00,"First message text..."
12346,2025-06-01T14:25:10,"Another message—newlines become spaces."
…
```

- **id:** Telegram message ID  
- **date:** ISO 8601 timestamp  
- **text:** Message body (newlines replaced by spaces)

---

## 🛠 Development & Local Testing

1. Clone the repo:
   ```bash
   git clone https://github.com/Endale2/telegather.git
   cd telegather
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\Activate.ps1   # Windows PowerShell
   ```

3. Install in editable mode:
   ```bash
   pip install --upgrade pip setuptools wheel
   pip install -e .
   ```

4. Verify the version and run the CLI:
   ```bash
   pip show telegather   # should show Version: 0.1.4
   telegather --help
   telegather
   ```

---

