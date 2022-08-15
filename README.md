## Python documentation Scrapy based parser

A simple Scrapy based parser that collects data from Python documentation. 

### Overview

The parser collects information about all PEPs in 2 csv files:

- the first file contains the numbers of all PEPs, their names and statuses

- the second one shows the number of PEPs with a particular status, as well as the total number of PEPs

### Technologies

- Python 3.9.5

- Scrapy 2.5.1

### Installation and launch

Clone the repository and go to it using the command line:

```bash
git clone 
```

```bash
cd scrapy_parser_pep
```

Create and activate a virtual environment:

Windows:

```bash
py -3 -m venv env
```

```bash
. venv/Scripts/activate 
```

```bash
py -m pip install --upgrade pip
```

macOS/Linux:

```bash
python3 -m venv .venv
```

```bash
source env/bin/activate
```

```bash
python3 -m pip install --upgrade pip
```

Install dependencies from a file requirements.txt:

```bash
pip install -r requirements.txt
```

Launch:

In order to launch you just have to use the following command:

```bash
scrapy crawl pep - it generates both files at once
```

### License

MIT