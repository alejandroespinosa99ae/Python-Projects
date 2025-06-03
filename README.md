# 📈 Yahoo Finance Stock Scraper Dashboard

This project is a simple web scraping tool built with Python that extracts the **top 5 gainers** and **top 5 losers** from the [Yahoo Finance](https://finance.yahoo.com/) website. The data is processed using **Power Query** and visualized in an **auto-refreshing Excel dashboard**.

---

## 🔧 Features

- Scrapes daily stock market data from Yahoo Finance
- Extracts and formats:
  - Top 5 gainers
  - Top 5 losers
- Cleans and transforms data using Power Query
- Automatically refreshes an Excel dashboard with the latest data

---

## 🧰 Tech Stack

- **Python** – for scraping and basic processing
- **Selectolax / requests** – for HTML parsing and web requests
- **Power Query** – for data cleaning and shaping
- **Excel** – for dashboard visualization and daily updates

---

## 📊 Output

The final output is a clean Excel dashboard showing:
- 📈 Top 5 stock gainers of the day
- 📉 Top 5 stock losers of the day

---

## 📌 Notes

- The script is designed to pull data once per day.
- You can automate it using **Task Scheduler** (Windows) or **cron** (Linux/Mac).
- Make sure Excel’s data connection settings allow for automatic refresh.

---

## 📄 License

This project is licensed under the MIT License.

