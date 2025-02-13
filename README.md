# Health-Score-System

## Overview

This Python-based Health Score Evaluation System calculates an individual's health score based on their vital signs, using WHO standard ranges. It provides a quantitative assessment (0-100) and a categorical classification (Excellent, Good, Average, Poor).

## Features

> Uses WHO-defined normal ranges for vital signs.

> Computes a health score (0-100) based on deviations from the ideal range.

> Classifies health status as Excellent, Good, Average, or Poor.

> Supports both numerical and binary health indicators.

> Can be easily integrated into health monitoring applications.

## How It Works

1. The system defines WHO standard health ranges for vital signs like:

> Blood Pressure (Systolic & Diastolic)

> Glucose Levels

> Oxygen Saturation (SpO2)

> ECG Heart Rate

> Temperature

> Malaria, Hepatitis B, and Widal Test (binary indicators)

2. The user inputs their test results.

3. Each vital is compared against the WHO range and assigned a score.

4. A total health score is computed by averaging all individual scores.

5. The final health status is categorized as:

> Excellent (90-100) ✅

> Good (70-89) 🟡

> Average (50-69) 🟠

> Poor (<50) 🔴


Ensure you have Python installed (version 3.7+).

