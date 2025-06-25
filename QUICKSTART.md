# 🚀 AI Daily Dose - Quick Start Guide

Get your AI Daily Dose Slack bot running in 5 minutes!

## Prerequisites

- Python 3.7+
- A Slack workspace where you have admin permissions
- GitHub account (for automated scheduling)

## Quick Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Setup Script
```bash
python setup.py
```

### 3. Create Slack App
1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Click "Create New App" → "From scratch"
3. Name: "AI Daily Dose Bot"
4. Select your workspace

### 4. Configure Bot Permissions
1. Go to "OAuth & Permissions"
2. Add scopes: `chat:write`, `chat:write.public`
3. Click "Install to Workspace"
4. Copy the "Bot User OAuth Token" (starts with `xoxb-`)

### 5. Configure Environment
Edit `.env` file:
```env
SLACK_BOT_TOKEN=xoxb-your-token-here
SLACK_CHANNEL_ID=general
```

### 6. Test Your Bot
```bash
python test_slack.py
```

### 7. Run the Bot
```bash
python chatops.py
```

## What You'll Get

- 🤖 Daily AI terms posted to your Slack channel
- 📚 Definitions and Wikipedia links
- 💬 Interactive discussions
- 🔗 Optional LinkedIn cross-posting
- ⏰ Automated scheduling via GitHub Actions

## Troubleshooting

### Bot not posting messages?
- Check if bot is invited to the channel
- Verify bot token is correct
- Ensure bot has proper permissions

### Getting permission errors?
- Make sure you added `chat:write` and `chat:write.public` scopes
- Reinstall the app to your workspace after adding scopes

### Channel not found?
- Use channel name (e.g., `#general`) instead of ID
- Make sure the bot is in the channel

## Next Steps

- Set up GitHub Actions for automated daily posting
- Configure LinkedIn integration
- Customize the AI terms database
- Add your own AI concepts

## Support

- Check the main [README.md](README.md) for detailed instructions
- Run `python test_slack.py` for diagnostics
- Review the [setup.py](setup.py) script for step-by-step guidance

---

🎉 **You're all set!** Your AI Daily Dose bot will now post daily AI terms to your Slack channel. 