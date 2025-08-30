# README

## Objective
Refactor the current codebase into a **modular Python package** called `algorithms` that contains both sorting and searching functionality, and provide a main script that uses them.

---

## Requirements

1. **Package Structure**
   - Create a folder named `algorithms` containing:
     - `sorting.py` — all sorting functions
     - `searching.py` — all search functions
     - `__init__.py` — exposes key functions for simplified imports

2. **Main Script**
   - Create `main.py` outside the package
   - Demonstrates usage of the sorting and searching functions from `algorithms`

3. **Functionality**
   - `insertion_sort` — sorts a list and returns a new sorted list
   - `binary_search` — searches a sorted list and returns the index or `None`
   - The main script should show:
     - Sorting an unsorted list
     - Searching for values in a sorted list

4. **Imports**
   - Use the `__init__.py` file to allow importing functions directly from the package:
     ```python
     from algorithms import insertion_sort, binary_search
     ```
   - If I try to import everything with:
     ```python
     from algorithms import *
     ```
     the `_check_input_types` function should not be imported.

5. **Code Quality**
   - Keep each module focused on a single type of algorithm
   - Ensure the main script can run as a standalone program
