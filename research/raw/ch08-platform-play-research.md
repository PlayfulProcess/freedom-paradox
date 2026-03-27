# Chapter 8 Research: The Platform Play

## Research Date: March 27, 2026

---

## 1. Chrome / Chromium

### Timeline
- **Sept 2008**: Google launches Chrome browser and simultaneously releases Chromium open-source project
- **2013**: Google forks WebKit into Blink engine (used in Chromium)
- **V8**: JavaScript runtime engine, also open-sourced (later powers Node.js)
- **2015**: Microsoft launches Edge with EdgeHTML engine (Trident successor)
- **2017**: Satya Nadella tells Edge team the product needs to be better; pushes for open-source engine
- **Sept 2018**: Internal Microsoft decision reached to switch Edge to Chromium
- **Dec 6, 2018**: Microsoft publicly announces intent to rebuild Edge on Chromium (codenamed "Anaheim")
- **Jan 15, 2020**: New Chromium-based Edge launches

### Market Share (2025-2026)
- Chrome: ~65-71% global browser market share (varies by source and device type)
  - Desktop: ~65-78% depending on source
  - Mobile: ~65-71%
- Edge: ~5-12.5% (second-most on desktop due to Windows bundling)
- Safari: ~19.5% mobile (WebKit engine)
- Firefox: ~2.2-3% globally (Gecko engine) — down from 10%+ a decade ago
- Chromium-based browsers collectively power 80%+ of desktop browsing

### Chromium-Based Browsers (nearly 30 total)
- Google Chrome, Microsoft Edge, Brave (70M+ active users), Opera, Opera GX, Vivaldi, Arc, DuckDuckGo Browser, Samsung Internet, Perplexity Comet, Genspark, Kosmik, Thorium, Sidekick
- OpenAI reportedly building browser [VERIFY: status of OpenAI browser project]

### Independent Engines Remaining
- **WebKit** (Apple Safari) — required on iOS for all browsers until EU DMA forced change
- **Gecko** (Mozilla Firefox) — only fully independent engine, ~2-3% share, declining
- Browser monoculture concern: if Firefox dies, web standards effectively controlled by Google + Apple

### Key Quotes / Framing
- Joe Belfiore (Microsoft): "Edge had a pretty mixed reputation" [from WindowsLatest interview]
- Nadella pushed engineers to create paper weighing benefits/drawbacks of Chromium switch
- Google "open core" applied to browser: open the engine, monetize the services (Search, Gmail, YouTube, ads)

### Sources
- StatCounter Global Stats: https://gs.statcounter.com/browser-market-share
- DemandSage Browser Market Share 2026: https://www.demandsage.com/browser-market-share/
- WindowsLatest (inside story of Chromium Edge): https://www.windowslatest.com/2019/05/07/the-inside-story-of-microsoft-chromium-edge-browser/
- Backlinko Browser Market Share: https://backlinko.com/browser-market-share

---

## 2. Android / AOSP

### Timeline
- **2003**: Andy Rubin, Rich Miner, Nick Sears, Chris White found Android Inc. (originally for digital cameras)
- **July 11, 2005**: Google acquires Android Inc. for $50 million. Larry Page and Sergey Brin met Rubin; deal closed after two meetings. David Lawee (Google VP Corp Dev) later called it Google's "best deal ever" (2010).
- **2007**: Open Handset Alliance announced (34 members including HTC, Samsung, Motorola, Qualcomm)
- **Sept 2008**: First Android phone (HTC Dream / T-Mobile G1)
- **AOSP**: Android Open Source Project — base OS freely available

### Market Share (2025-2026)
- Global mobile OS: 72-73% Android, ~27-29% iOS
- Active devices: ~3.9 billion (up 8% from 3.6B in 2024)
- All OS market share (including desktop): ~38-39%
- Regional breakdown:
  - India: 95.2% Android
  - Indonesia: 86.8%
  - Brazil: 81.4%
  - US: ~41.7% Android (~58.3% iOS)
  - Japan: iOS dominates (~69%)

### Revenue Paradox
- iOS App Store revenue: ~$85.1 billion (67% of global app spending)
- Google Play revenue: ~$47.9 billion
- Combined 2025 consumer spending: $166.8 billion
- Per-user monthly spending: iOS $10.40-$11.20 vs Android $1.40-$1.70
- iOS users average income: $53,251/year vs Android $37,040/year
- iOS captures ~68-70% of app revenue with ~28% of users

### Top Android Manufacturers
- Samsung: 19.7% global smartphone share (30.8% of Android vendors)
- Xiaomi: 14.4%
- Vivo: 9.2%
- Transsion: 8.5% (major in Africa/South Asia — Tecno, Infinix, itel brands)

### Sources
- DemandSage Android Statistics 2026: https://www.demandsage.com/android-statistics/
- Backlinko iPhone vs Android: https://backlinko.com/iphone-vs-android-statistics
- Android Wikipedia: https://en.wikipedia.org/wiki/Android_(operating_system)
- AndroidAuthority (Google acquisition): https://www.androidauthority.com/google-android-acquisition-884194/

---

## 3. Google Mobile Services (GMS) — The Proprietary Lock-in Layer

### What GMS Includes
- Google Play Store, Google Search, Chrome, YouTube, Gmail, Maps, Google Photos, Google Drive, Google Assistant, Google Pay, Google Calendar — bundle of ~11 core apps
- GMS is NOT part of AOSP — it is proprietary and requires a license from Google

### OEM Requirements
- Manufacturers must sign a license agreement with Google to pre-install GMS
- Must pass thousands of compatibility tests
- Mobile Application Distribution Agreements (MADAs) 2015-2018: required full GMS suite as condition for Play Store access
- OEMs cannot develop derivative works from Google's proprietary apps
- Restrictions on home screen layouts, app icon positioning
- Cannot display ads while launching Google apps

### Antitrust Actions
- **EU (July 2018)**: European Commission fined Google EUR 4.34 billion ($5 billion) — largest antitrust fine in EU history at the time. Three violations: (1) required bundling of Google Search + Chrome with Play Store, (2) payments to OEMs/carriers for exclusive Google Search pre-installation, (3) prevented OEMs from selling devices with modified Android (anti-fragmentation agreements)
- **Appeal (Sept 2022)**: General Court reduced fine by EUR 200 million but upheld core finding
- **India**: Competition Commission ruled mandatory GMS pre-installation is unfair to manufacturers
- **Post-EU ruling**: Google created paid GMS licensing in EU that decoupled GMS from base Android

### The Strategic Logic
- AOSP is the open-source bait — free, functional, attracts manufacturers
- GMS is the proprietary trap — Play Store + Google services are what consumers actually want
- Without GMS, Android phones lose access to most popular apps (many require Google Play Services)
- Huawei lost GMS access (US sanctions, 2019) — phone sales collapsed outside China despite building HarmonyOS/HMS

### Sources
- Android Authority (GMS explained): https://www.androidauthority.com/google-mobile-services-gms-3025963/
- Wikipedia (GMS): https://en.wikipedia.org/wiki/Google_Mobile_Services
- EU Commission press release: https://europa.eu/rapid/press-release_IP-18-4581_en.htm
- emteria (GMS certification guide): https://emteria.com/learn/google-mobile-services

---

## 4. Zuckerberg / Meta — Bridge to Chapter 9

### The Quote (July 2024, open letter on Meta blog)
"One of my formative experiences has been building our services constrained by what Apple will let us build on their platforms... Between Apple's developer taxes, arbitrary rules about what we can and can't build, and the fact that they've blocked a lot of product innovations, it's clear that we and many others in the industry would build much better products for people if not constrained."

He continued: on a philosophical level, this is a major reason he believes in building open ecosystems in AI and AR/VR for the next generation of computing — to ensure "that power isn't concentrated in the hands of a small number of companies."

### Context
- Published alongside Llama 3.1 405B release (July 23, 2024)
- Full essay title: "Open Source AI Is the Path Forward"
- Meta's argument: they were a victim of platform lock-in (Apple's App Store), so they want to prevent the same in AI
- Strategic self-interest: Meta doesn't sell cloud compute, so open-sourcing AI models hurts competitors (Google, OpenAI, Microsoft) who do sell API access

### Sources
- Meta blog: https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/
- Entrepreneur.com: https://www.entrepreneur.com/business-news/mark-zuckerberg-calls-out-apple-outlines-meta-ai-strategy/477517

---

## 5. Open Questions / Gaps

- [RESEARCH NEEDED]: Google's exact advertising revenue attributable to Chrome/Android ecosystem
- [RESEARCH NEEDED]: How many apps on Play Store require Google Play Services to function?
- [VERIFY]: Status of OpenAI browser project (ChatGPT browser)
- [RESEARCH NEEDED]: Huawei's experience after losing GMS — specific sales decline figures
- [RESEARCH NEEDED]: Chrome's role in pushing web standards that benefit Google (AMP, Web Vitals)
- [QUOTE NEEDED]: Developer or Mozilla figure on browser monoculture risk
