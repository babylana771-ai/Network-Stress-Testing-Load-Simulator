# Asynchronous Network Connection & Stress Tester

An asynchronous, high-concurrency network simulation tool developed in Python utilizing the `asyncio` framework. This project is designed for system administrators and cybersecurity researchers to conduct capacity testing, evaluate network infrastructure resilience, and analyze firewall/IDS behavior under concurrent TCP connection loads.

## 📌 Key Features
* **Asynchronous Architecture:** Leverages Python's `asyncio` loop to handle high-concurrency socket connections efficiently without multi-threading overhead.
* **Capacity Simulation:** Models transport-layer resource limits by initiating and holding up to 500+ concurrent TCP connections.
* **Controlled Flow:** Features rate-limiting adjustments (`CONCURRENCY_RATE`) to safely test network capacity.
* **Graceful Teardown:** Implements structured exception handling for clean socket closure and resource release upon interruption.

## 🛠️ Technical Background
This script demonstrates proficiency in:
* Advanced network programming in Python.
* Asynchronous socket programming and coroutines.
* Modeling resource starvation scenarios to design robust network defense mitigation strategies.

## 🚀 Disclaimer & Usage
This tool is developed strictly for **educational purposes, defensive research, and authorized local laboratory testing**. Do not use this tool against infrastructure without explicit, written authorization. The developer assumes no liability for misuse or damage caused by this software.
