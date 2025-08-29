# 🌍 Countries Population Scraper

## 📌 Overview
This project is a **web scraping tool** built with [Scrapy](https://scrapy.org/).  
It extracts data about **countries, their population, and continents** from the Wikipedia page:  
[List of countries by population (United Nations)](https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)).

The scraped data is stored in a clean **CSV file** for analysis and reporting.

---

## ⚙️ Technologies Used
- **Python 3.x**
- **Scrapy Framework**
- **XPath Selectors**
- **CSV Output**

---

## 🚀 How it Works
1. The Scrapy spider sends a request to the Wikipedia page.  
2. It parses the main **population table** (`wikitable`).  
3. Extracts:
   - 🏳️ **Country name**
   - 👥 **Population**
   - 🌐 **Continent**
4. Saves the extracted data to a **CSV file**.

---

## 📂 Project Structure
countries-population-scraper/
│
├── countries/ # Scrapy project folder
│ ├── spiders/ # Contains the spider file
│ │ └── countries_spider.py
│ ├── items.py
│ ├── pipelines.py
│ └── settings.py
│
├── output.csv # Final scraped data
├── Countries_Scraper_Report.pdf # Project report
└── README.md # Project documentation


---

## 📊 Example Output
| Country        | Population    | Continent       |
|----------------|--------------|-----------------|
| China          | 1,425,671,352| Asia            |
| India          | 1,417,173,173| Asia            |
| United States  | 339,996,563  | North America   |

---

## 📝 Report
A detailed PDF report is included in this repository:  
👉 [Countries_Scraper_Report.pdf](./Countries_Scraper_Report.pdf)

---

## 📎 How to Run
1. Clone the repository:

   git clone https://github.com/your-username/countries-population-scraper.git


2. Navigate into the project folder:

cd countries-population-scraper


3. Run the spider:

scrapy crawl countries -o countries.csv


⭐ Future Improvements
* Add population growth rate for each country.

* Visualize data using graphs (Matplotlib / Seaborn).

* Store data in a database (SQLite / MongoDB).

👤 Author:
      Tendo

📧 Email: 
      tendooza123@gmail.com

🔗 | GitHub:
      TendoOZA

