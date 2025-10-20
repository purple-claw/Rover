Rover - Your Last Chance to Master DSA from Scratch

Because apparently watching 50 YouTube tutorials didn't work. Let's try this instead.

What the Hell is This?

A brutally effective DSA learning platform that actually teaches you how to think instead of just copying code. Built for developers who are tired of "just memorize these 100 LeetCode patterns."

Features That Don't Suck

· Pattern Recognition: The 5 patterns that actually matter (not 50, just 5)
· Complexity Analysis: Learn why your O(n³) solution makes interviewers cry
· Real Code Examples: 40+ copy-paste-ready blocks (we know you're going to copy them anyway)
· Dark Theme: Because light themes are for people who don't debug at 3 AM

Quick Start (For the Impatient)

```bash
# 1. Get the code
git clone https://github.com/purple-claw/Rover.git
cd Rover

# 2. Isolate your mess
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install the magic
pip install -r requirements.txt

# 4. Make it go
python app.py
```

Now open http://localhost:8000 and stop making excuses.

Project Structure (Where Things Live)

```
Rover/
├── app.py                    # The brain
├── content_parser.py         # Makes HTML less painful
├── navigation_builder.py     # So you don't get lost
├── requirements.txt          # Things Python needs
│
├── static/                   # The pretty parts
│   ├── landingPage.html     # "Look how professional we are"
│   ├── dashboard.html       # Where the magic happens
│   ├── main.css            # Colors and sparkles
│   └── index.js            # The interactive bits
│
└── templates/               # All the knowledge
    ├── Complexity/          # Why your code is slow
    ├── Problem Solving/     # How to not be clueless
    └── Sliding Window/      # Fancy array tricks
```

Adding Content (For When You're Feeling Helpful)

1. Create a new HTML file in the right folder:
   ```bash
   touch templates/Your-Topic/your_amazing_content.html
   ```
2. Follow the template (or don't, but then it'll look weird)
3. Restart the server because it's not psychic
4. Test it like you actually care about quality

API Endpoints (For Your Curious Side)

· GET / - The front door
· GET /dashboard - The control center
· GET /view/{path} - Actual content (the useful part)
· GET /api/navigation - JSON for the robots
· GET /health - Is this thing on?

Contributing (Please Don't Break Things)

1. Fork it
2. Make a branch: git checkout -b feature/your-brilliant-idea
3. Commit your changes: git commit -m "Add: something that actually works"
4. Push: git push origin feature/your-brilliant-idea
5. Pull Request: Pray we merge it

Pro tip: Test your code. No, seriously.

Why This Exists

Because DSA interviews are the hazing ritual of our industry, and someone needs to make it less painful. This is that someone.

License

MIT - Do whatever you want, just don't blame us when your code still has bugs.

---

Built with FastAPI, caffeine, and the tears of frustrated developers.