# Computer-Infrastructure
## 1. Overall Description
This repository contains problems and coursework from 25-26: 8645 -- COMPUTER INFRASTRUCTURE. This consists of a Python project that automates the downloading and plotting of hourly yfinance stock data for the past five days using GitHub Actions.

The program downloads data for META, Apple, Google, Netflix, and Amazon and saves it to CSV files in ./data using the current day and time as a naming convention. The program then accesses this data to plot the closing prices for each of the five stocks and saves the plot as a png in ./plots. 

GitHub Actions has been used to create a YAML file that automatically runs this programme every Saturday morning and pushes the output to the repository. 

## 2. Repository Structure 📂

```plaintext
├── .github/workflows/faang.yml # GitHub Actions workflow which runs faang.py automatically at 08:37 UTC on a Saturday.
├── data/                # Directory for downloaded CSV files
├── plots/               # Directory generated PNG plots
├── faang.py             # Main executable Python script containing two core functions: get_data() for downloading stock data and plot_data() for creating visualizations.
├── problems.ipynb       # Jupyter notebook with explanations of code and problem solutions
├── requirements.txt     # Lists all Python dependencies (e.g., yfinance, pandas, seaborn, matplotlib) required to run the script and notebook
```

## 3. Installation ⚙️

### Clone the repository:
```bash
git clone https://github.com/EmmaChubbCode/computer-infrastructure.git
cd computer-infrastructure
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
## 4. Use and Automation ▶️
The GitHub Actions workflow (faang.yml) runs the script every Saturday at 08:37 UTC and commits new data and plots to the repository.

To run the faang.py script manually from the command line:
```bash
./faang.py
``` 
## Technologies Used 💻
- **Python 3**
- **IPython/Jupyter Notebook** for development and write up
- **yfinance** for stock data
- **pandas** for data manipulation
- **seaborn & matplotlib** for visualization
- **GitHub Actions** for automation