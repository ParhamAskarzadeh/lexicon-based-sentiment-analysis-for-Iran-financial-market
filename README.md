# Lexicon-based Sentiment Analysis for Iran Financial Market

This repository contains code for performing lexicon-based sentiment analysis on text data related to the Iran financial market. The code is written in Python and uses regular expressions for pattern matching.

## Dependencies
The code requires the following dependencies:
- Python 3.x
- re (regular expression) module

## Usage
1. Import the `TextAnalyser` class from the code file.
2. Create an instance of the `TextAnalyser` class.
3. Use the instance methods to analyze text and extract sentiment-related information.

### Example Usage
```python
import re
from text_analyser import TextAnalyser

analyser = TextAnalyser()

text = "Sample text containing reports."
reports = analyser.find_reports(text)
for report in reports:
    print(report)

text = "Sample text containing events."
events = analyser.find_events(text)
for event in events:
    print(event)

text = "Sample text containing symbols."
symbols = analyser.find_symbols(text)
for symbol in symbols:
    print(symbol)
```

## Methods
The `TextAnalyser` class provides the following methods:

### `find_reports(text)`
This method takes a text string as input and returns a list of dictionaries representing reports found in the text. Each dictionary contains information about the type of report, the marker (e.g., the name of the report), and the span of the report within the text.

### `find_events(text)`
This method takes a text string as input and returns a list of dictionaries representing events found in the text. Each dictionary contains information about the type of event, the marker (e.g., keywords related to the event), and the span of the event within the text.

### `find_symbols(text)`
This method takes a text string as input and returns a list of dictionaries representing symbols found in the text. Each dictionary contains information about the type of symbol (e.g., company or stock symbol), the marker (e.g., the symbol itself), and the span of the symbol within the text.
