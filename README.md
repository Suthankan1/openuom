# Price Comparison Program for Online Supermarkets

This program compares the prices of similar products from two online supermarkets and recommends which option is cheaper at a given instance of time.

## Objective

The objective of this program is to acquire, extract, and compare the price from two different suppliers for a given product.

## Usage

To use the program, you need to run the `compare_prices.py` script in your Python environment. The `compare_prices` function is pre-loaded in the script, which takes in two similar products from two suppliers and compares the prices to recommend which option is cheaper.

### Example Usage

```python
from compare_prices import compare_prices

laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'

compare_prices(laughs_coconut, glomark_coconut)
