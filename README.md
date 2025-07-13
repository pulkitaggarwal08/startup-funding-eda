🚀 Indian Startup Funding Analysis

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pulkitaggarwal08/startup-funding-eda/blob/main/funding_analysis.ipynb)

Over 2,000 startup funding deals. Cleaned, analyzed, and visualized — to make sense of how capital actually flows in India's startup ecosystem.

This project isn’t just about charts. It’s about answering key questions:

Who’s getting funded?

Which sectors are booming?

What kind of investors back what kind of ideas?

And how does all of this change with time?

📌 What’s inside
⏱ Time trends – Yearly/monthly patterns in funding across the decade.

🌍 City-wise breakdowns – Where startups raise early vs mature rounds.

🏭 Industry patterns – Who dominates funding, who’s stagnating.

🤝 Investor behavior – Co-investor networks, sector biases, and repeat players.

📈 Custom metrics like:

Funding concentration

Deal outliers

Vertical volatility

Ecosystem momentum

💡 Insights that stood out
Some seed rounds were over $10M — major outliers for that stage.

Just 5 industries captured 70%+ of all funding.

Bengaluru drives early-stage deals; Mumbai leans towards larger late-stage bets.

Co-investing patterns aren’t random — certain VCs show up together, again and again.

🔧 Tools used
Python libraries: pandas, seaborn, matplotlib, scipy, networkx, squarify

Cleaning-heavy work: dates, currencies, cities, inconsistent investor formats

Network graphs + heatmaps to go deeper into investor relationships

🧠 Why I built this
I’ve always been curious about the bigger picture — not just which startup raised funding, but why it happened, who enabled it, and how the ecosystem shifts over time.

This project helped me practice combining:

Data storytelling

Strategic thinking

And real-world startup patterns

All in one place.

💭 What’s next?
Build an investor dashboard (VC radar).

Add funding momentum prediction using historical cycles.

Wrap it all into a simple Streamlit app — useful for founders, VCs, and analysts alike.

📁 Repo structure
vbnet
Copy
Edit
📦 indian-startup-funding-analysis/
├── funding_analysis.ipynb      → Interactive notebook (Colab-friendly)
├── funding_eda.py              → Script version of the full analysis
├── README.md                   → You're reading this
├── requirements.txt            → All required packages
├── visuals/                    → (Optional) Saved charts and graphics
└── data/                       → (Optional) Sample or cleaned CSVs (excluded if private)
