# Options
This python project uses data from yahoo finance to graph option profit-loss diagrams

## Dependencies
Run this in the terminal:
```bash
pip install -r requirements.txt
```

## Usage
Simple program graphing a long call option:
```python
import options

contractName = 'AMD201218C00040000'
optionObj = options.scrapeCallOptions('AMD')

options.graphLongCall(optionObj, contractName)
```
*Note: the contract name (AMD201218C00040000) has likely expired
