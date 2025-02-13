# Health-Score-System

## Overview

This Python-based Health Score Evaluation System calculates an individual's health score based on their vital signs, using WHO standard ranges. It provides a quantitative assessment (0-100) and a categorical classification (Excellent, Good, Average, Poor).

## Features

> Uses WHO-defined normal ranges for vital signs.

> Computes a health score (0-100) based on deviations from the ideal range.

> Classifies health status as Excellent, Good, Average, or Poor.

> Supports both numerical and binary health indicators.

> Can be easily integrated into health monitoring applications.

## How It Works 🚀

The system defines **WHO standard health ranges** for vital signs like:

- **Blood Pressure** (Systolic & Diastolic)
- **Glucose Levels**
- **Oxygen Saturation (SpO₂)**
- **ECG Heart Rate**
- **Temperature**
- **Malaria, Hepatitis B, and Widal Test** (binary indicators)

### 📝 User Input
- The user **inputs** their test results.
- Each vital is **compared against WHO ranges** and assigned a **score**.
- A **total health score** is computed by averaging all individual scores.

### 📊 Final Health Status
The system categorizes health status into **four levels**:

| Score Range   | Status      | Indicator |
|--------------|------------|-----------|
| **90 - 100** | Excellent  | ✅         |
| **70 - 89**  | Good       | 🟡        |
| **50 - 69**  | Average    | 🟠        |
| **< 50**     | Poor       | 🔴        |

---


Ensure you have Python installed (version 3.7+).

