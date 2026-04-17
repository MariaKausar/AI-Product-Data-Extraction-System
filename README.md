## 📌 Project Title

AI Product Data Extraction System (FastAPI)

## 📖 Overview

This project is a lightweight AI-powered system that extracts structured information from unstructured product descriptions. It uses NLP-based regex parsing and rule-based intelligence to simulate real-world data extraction pipelines.

## ⚙️ Features
Extracts product, material, price, sustainability
Price classification (cheap / expensive)
Sustainability scoring system
Confidence score estimation
Eco-friendly classification
REST API using FastAPI

## 🧠 Tech Stack
Python
FastAPI
Regex (NLP techniques)

## 🚀 How to Run
1. uvicorn main:app --reload
2. Open: http://127.0.0.1:8000/docs
3. Input:
Product: Wooden Table  
Material: Wood  
Price: £150  
Sustainability: Recyclable

5. Output:
{
  "product": "Wooden Table",
  "material": "Wood",
  "price": "£150",
  "sustainability": "Recyclable",
  "eco_friendly": true,
  "price_category": "expensive",
  "sustainability_score": 2,
  "confidence": 1.0
}

## 🎯 Purpose

To simulate real-world AI data extraction systems used in product databases, sustainability tracking, and enterprise AI pipelines.

