# 🌱 PVZ Fuzion Console Manager – User Guide

Welcome to **PVZ Fuzion Console Manager**, a tool built to make your translation work for *Plants vs Zombies: Fuzion* easier, faster, and more organized. You don’t need to look at the code — everything you need is already packed inside the file you received: `python_console.pyz`.

This short guide explains how to use the console step by step and how to interpret the reports it generates.

---

## 🧩 What this tool does

The Console Manager scans the game’s translation files, compares each language with the English base version, and detects missing or incomplete entries.

It then generates a Markdown report (a text file with simple formatting) summarizing what needs to be translated. Each report is clear, structured, and easy to read.

---

## ⚙️ Before You Start

You only need **Python 3.10 or later** installed on your computer.
To check, open your terminal or PowerShell and type:

```bash
python --version
```

If you see something like `Python 3.10.x`, you’re good to go.

---

## 🚀 How to Run the Program

1. Place `python_console.pyz` in your project folder (next to your translation files).
2. Open a terminal in that folder.
3. Type this command:

```bash
python python_console.pyz
```

You’ll see the following message:

```
=== PVZ Fuzion Console Manager ===
Hi! Welcome to the PVZ Fuzion Console Manager.
```

The program will then show you a series of menus to guide you through the process.

---

## 🧭 Step-by-Step Menu Guide

1. **Select Localization**
   Choose one or more languages you want to check (e.g., French, Spanish, Indonesian).

2. **Choose Translation Type**
   You can select one of the following options:

   * 🌱 Plants
   * 🧟 Zombies
   * 🏆 Achievements
   * 🔁 All (to check everything)

3. **Wait for the Analysis**
   The console will compare the data and display the number of missing entries.

4. **View the Reports**
   Once finished, open the folder `reports/` — new Markdown files will appear there.

---

## 📄 Understanding the Reports

Each report is named after the language and category, for example:

```
/reports/plants/missing_plants_Indonesian.md
```

Inside the file, you’ll find a clean summary of everything that’s missing.

Example:

```markdown
# 🌱 Missing Plant Translations — INDONESIAN

> **Total missing entries:** 108
> Generated automatically by PVZ Fuzion Console Manager 🧩

---

### 🪴 Lucky Blover (ID: 229)
**Description:**
> *❌ Missing translation*

**Info:**
> Changes the winds of fate for you~
> Special: Forces your next Plant Giftbox to generate a guaranteed Advanced fusion.

**Cost:**
> 200 Sun — 50s recharge

---
```

✅ *Tip:* You can open Markdown files directly on GitHub, VS Code, or Notion — they’ll display beautifully formatted.

---

## 💡 Why Markdown?

Markdown files are simple text files but can include titles, bullet points, and highlights. This makes them easy to share and read, even without special software.

---

## 🔧 Common Questions

**Q: Can I run the program without Python?**
➡️ No, Python must be installed. It’s lightweight and free.

**Q: Where are my reports saved?**
➡️ In the `reports/` folder, sorted by category.

---

## 🏁 That’s It!

Once you’ve run the program, all missing translations are neatly listed for you. Just open the generated files, fill in the missing parts, and your localization will be one step closer to completion.

---

## 👤 Credits

**Developed by:** Charles Lindecker
**Project:** PVZ Fuzion Translation Project 🧠🌿
**GitHub:** [https://github.com/LINDECKER-Charles](https://github.com/LINDECKER-Charles)
**LinkedIn:** [https://www.linkedin.com/in/charles-lindecker](https://www.linkedin.com/in/charles-lindecker)
**Email:** [charles.lindecker](mailto:charles.lindecker@outlook.fr)
