<h1 align="center">AI Daily Dose</h1>
<p align="center"><h2 align="center">A Slack Channel and Bot</h2></p>
<br>

<h2 align="center">Intro & Purpose</h2>
<h3 align="center">Intro</h3>
Daily, incremental presentation of relevant and challenging information is efficient, fun and provides a foundation for learning, communication and confidence which extends beyond the walls of classroom and corporate office alike.

<br>

<h3 align="center">Purpose</h3>

- <strong>What is it?</strong>

The AI Daily Dose is a Slack channel where a random AI word/concept is sent daily. It includes a definition and a link to learn more. Users can then interact by posting and sharing anecdotes, images, or memes relating to the AI concept.

But interaction is not limited to the topic of the day. Members are encouraged to share any AI/ML related information in the channel.

<br>

- <strong>Why should you join?</strong>

It's a great way to grow, spread, and practice your AI knowledge. Some people in the channel are strictly learners, while others with more experience can impart their knowledge. Furthermore, it allows people who are interested in AI to network and socialize.

<br>
 	   
- <strong>What will you get out of it?</strong>

Often, people are so busy with daily tasks that they don't have time to keep up with their AI learning and networking. By joining this channel, IT professionals can establish a consistent pattern of daily AI learning and interaction. This can take as little as one minute (e.g., reading a word and its definition), while those who want to dive deeper or contribute to the discussion have the opportunity to do so.

<br>

<h2 align="center">Setup Instructions</h2>

<h3 align="center">Slack Bot Setup</h3>

1. **Create a Slack App:**
   - Go to [api.slack.com/apps](https://api.slack.com/apps)
   - Click "Create New App" → "From scratch"
   - Give your app a name (e.g., "AI Daily Dose Bot")
   - Select your workspace

2. **Configure Bot Token Scopes:**
   - Go to "OAuth & Permissions" in the left sidebar
   - Add the following scopes:
     - `chat:write` - Send messages to channels
     - `chat:write.public` - Send messages to public channels
   - Click "Install to Workspace"

3. **Get Your Bot Token:**
   - Copy the "Bot User OAuth Token" (starts with `xoxb-`)
   - This will be your `SLACK_BOT_TOKEN`

4. **Get Channel ID:**
   - Right-click on your target channel in Slack
   - Select "Copy link" and extract the channel ID from the URL
   - Or use the channel name (e.g., "#general")

5. **Set Environment Variables:**
   - `SLACK_BOT_TOKEN`: Your bot's OAuth token
   - `SLACK_CHANNEL_ID`: The channel ID or name where messages will be posted
   - `LI_ACCESS_TOKEN`: LinkedIn API token (optional)
   - `PROFILE_ID`: LinkedIn profile ID (optional)
   - `PAT`: GitHub Personal Access Token (for workflow)

<h3 align="center">Local Development</h3>

```bash
# Clone the repository
git clone https://github.com/xanderstevenson/ai-wotd.git
cd ai-wotd

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export SLACK_BOT_TOKEN="xoxb-your-bot-token"
export SLACK_CHANNEL_ID="your-channel-id"

# Run the bot
python chatops.py
```

<h3 align="center">GitHub Actions Setup</h3>

1. **Add Repository Secrets:**
   - Go to your repository → Settings → Secrets and variables → Actions
   - Add the following secrets:
     - `SLACK_BOT_TOKEN`
     - `SLACK_CHANNEL_ID`
     - `LI_ACCESS_TOKEN` (optional)
     - `PROFILE_ID` (optional)
     - `PAT` (GitHub Personal Access Token)

2. **The workflow will automatically run daily at 9 AM EST**

<br>

<h2 align="center">Features</h2>

- 🤖 **Daily AI Terms**: Posts a random AI/ML concept daily
- 📱 **Slack Integration**: Rich message formatting with buttons and links
- 🔗 **LinkedIn Cross-posting**: Optional LinkedIn integration
- 📊 **Database Tracking**: Prevents duplicate posts
- ⏰ **Automated Scheduling**: Runs via GitHub Actions
- 🎨 **Beautiful UI**: Modern Slack blocks with emojis and formatting
