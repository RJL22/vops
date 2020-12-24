# Vops
This python project uses data from yahoo finance to graph option profit-loss diagrams

## Installing
Installing with pip:
```bash
pip install vops
```

## Usage
Simple program graphing a long call option:
```python
from vops import scraping
from vops import graphing

contractName = 'AMD201218C00040000'
optionObj = scraping.scrapeCallOptions('AMD')

graphing.graphLongCall(optionObj, contractName)
```
