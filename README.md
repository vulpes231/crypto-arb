# Crypto Scanner Bot

A **real-time crypto scanner bot** that monitors multiple exchanges, identifies arbitrage opportunities, and alerts on price spreads. Perfect for traders looking to spot profitable opportunities quickly.

## Features

- Tracks multiple cryptocurrency exchanges in real-time
- Detects price differences and potential arbitrage opportunities
- Sends alerts when spreads cross configurable thresholds
- Lightweight, fast, and easy to configure
- Supports popular coins like BTC, ETH, SOL, and more

## Installation

1. Clone this repository:

git clone https://github.com/yourusername/crypto-scanner-bot.git
cd crypto-scanner-bot

2. Install dependencies:

<pre class="overflow-visible! px-0!" data-start="894" data-end="937"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>pip install </span><span class="ͼu">-r</span><span> requirements.txt</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

or for Node.js version:

<pre class="overflow-visible! px-0!" data-start="964" data-end="987"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼs">npm</span><span> install</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

3. Configure your API keys in `config.json` (or `.env`):

` <pre class="overflow-visible! px-0!" data-start="1048" data-end="1196"><div class="relative w-full mt-4 mb-1">``<div class=""><div class="relative">``<div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0">``<div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback">``<div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!">``<div class="sticky bg-token-border-light"></div>``</div></div>``<div class=""><div class="relative z-0 flex max-w-full">``<div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller">``<div class="cm-content q9tKkq_readonly"><span> `{`<br/><span>` "binance_api_key": `<span class="ͼr">`"YOUR_KEY"`<span>`,`<br/><span>` "binance_secret": `<span class="ͼr">`"YOUR_SECRET"`<span>`,`<br/><span>` "kucoin_api_key": `<span class="ͼr">`"YOUR_KEY"`<span>`,`<br/><span>` "kucoin_secret": `<span class="ͼr">`"YOUR_SECRET"`<br/><span>`}` </div></div>``</div></div>``</div></div>``</div></div>``</div></div>``</div></div>``</pre> `

## Usage

<pre class="overflow-visible! px-0!" data-start="1208" data-end="1233"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python bot.py</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

or for Node.js:

<pre class="overflow-visible! px-0!" data-start="1252" data-end="1275"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼs">node</span><span> bot.js</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

- The bot will start monitoring prices across exchanges.
- Alerts are printed to the console or sent via your preferred notification method (email, Telegram, etc.).

## Configuration

- **Coins to monitor:** `BTC, ETH, SOL` (customizable in `config.json`)
- **Spread threshold:** Set the minimum price difference to trigger alerts
- **Polling interval:** Set how often the bot checks exchange prices

## Contributing

Contributions are welcome! Feel free to:

- Add support for more exchanges
- Improve alerting features
- Optimize performance

Please fork the repo and submit a pull request.
