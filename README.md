# Cache Eviction Policy Simulator

## Student Info
- **Name:** Carlos Felipe
- **UFID:** 70583368

## Overview
Implements and compares three cache eviction policies — FIFO, LRU, and OPTFF (Belady's optimal) on a given request sequence.

## Requirements
- Python 3.10+
- No external dependencies

## How to Run
From the root of the repository:
```bash
python3 src/main.py <input_file>
```

**Example:**
```bash
python3 src/main.py data/example.in
```

**Expected output:**
```
FIFO  : 8
LRU   : 8
OPTFF : 6
```

## Input Format
```
k m
r1 r2 r3 ... rm
```
- `k` — cache capacity
- `m` — number of requests
- `r1 ... rm` — space-separated integer request IDs

## Repository Structure
```
cache-eviction/
├── src/
│   └── main.py
├── data/
│   ├── example.in
│   ├── example.out
│   ├── file1.in / file1.out
│   ├── file2.in / file2.out
│   └── file3.in / file3.out
├── tests/
│   └── test_cache.py
└── README.md
```

## Assumptions
- Input is well-formed and follows the format above
- Request IDs are integers
- Cache capacity k >= 1 and m >= 1
