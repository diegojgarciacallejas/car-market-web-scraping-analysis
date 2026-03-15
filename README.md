# Car Market Web Scraping Analysis

This project collects, cleans, and analyzes used car listings from multiple automotive marketplaces across several European countries. The goal is to build a comparable dataset of vehicles with similar characteristics and perform exploratory analyses on pricing, mileage, and registration year patterns by country.

## Project Overview

The project is divided into three main stages:

1. **Web scraping** of used car listings from multiple online marketplaces
2. **Data cleaning and transformation** into country-level datasets
3. **Exploratory analysis and visualization** using Jupyter notebooks

This repository was originally developed as an academic project and has been reorganized into a cleaner, portfolio-oriented structure.

---

## Objectives

- Scrape car listing data from multiple sources in different countries
- Standardize and clean heterogeneous datasets
- Build processed datasets grouped by country
- Compare used car market patterns across countries
- Explore relationships between:
  - registration year and car brand
  - mileage and price
  - cross-country availability of similar car models

---

## Data Sources

The data was collected from the following websites:

### Spain
- Autocasion
- Clicar / Clicars
- Flexicar
- OcasionPlus

### France
- AutoScout24 France

### Netherlands
- AutoScout24 Netherlands

### Germany
- Mobile.de

> Different scraping scripts were required because each website has a different HTML structure and extraction logic.

---

## Project Workflow

```text
Web Scraping Scripts
        ↓
Raw CSV files (per source)
        ↓
Data Cleaning Notebook
        ↓
Processed CSV files (per country)
        ↓
Analysis Notebooks and Visualizations
```
