# Why this data?
The CDCR (California Department of Corrections and Rehabilitation) releases monthly reports on the number of people in state prisons around California. These reports also include the designed capacities of each prison, and how the current population compares to that capacity. California prisons have had extreme overcrowding issues for a long time - see, e.g. [Brown v Plata](https://en.wikipedia.org/wiki/Brown_v._Plata), which is the US Supreme Court case that finally sparked a concerted effort to reduce overcrowding.

Unfortunately, the reports provided by the CDCR are only available in PDF format, and therefore very difficult to do any structured analysis with. This repository changes that, parsing the monthly PDF reports from 1996 to the present day to provide these data in an easy-to-use CSV format. The data look something like this:
```
head data/monthly_cdcr_population.csv | column -t -s,
year  month  institution_name               population_felons  civil_addict  total_population  designed_capacity  percent_occupied  staffed_capacity
1996  01     VSP (VALLEY SP)                2294               0             2294              1980               115.9             1980
1996  01     SCC (SIERRA CONSERV CTR)       322                0             322               320                100.6             320
1996  01     NCWF (NO CAL WOMEN'S FACIL)    786                4             790               400                197.5             760
1996  01     CCWF (CENT CAL WOMEN'S FACIL)  2846               13            2859              2004               142.7             3224
...
```

## Raw PDFs
Data come from the PDFs of monthly archives at: https://www.cdcr.ca.gov/Reports_Research/Offender_Information_Services_Branch/Monthly/Monthly_Tpop1a_Archive.html

The PDFs themselves are pulled down and checked into this repository under data/raw_monthly_pdfs/. The names of the PDFs has not been changed. They were downloaded by running the following script:
```
python datacleaning/scrape_from_cdcr.py
```

## Parsing the PDFs
The PDFs are parsed using tools in the `datacleaning` directory in the root of this repo. The result of their parsing is in this directory at `data/monthly_cdcr_population.csv`.

To re-parse / re-generate that CSV, run:
```
python datacleaning/bulk_parse_pdfs.py --verbose
```
