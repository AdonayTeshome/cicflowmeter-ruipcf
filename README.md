# Python CICFlowMeter

> This project is an update of the existing CiCFlowMeter ([https://gitlab.com/hieulw/cicflowmeter](https://github.com/datthinh1801/cicflowmeter)) that can run with Python 3.10 with the libraries updated and include some bug fixes.
### Installation

```sh
git clone https://github.com/ruipcf/cicflowmeter.git
cd cicflowmeter
python3 setup.py install
```

### Usage

```sh
usage: cicflowmeter [-h] (-i INPUT_INTERFACE | -f INPUT_FILE) [-c] [-u URL_MODEL] output

positional arguments:
  output                output file name (in flow mode) or directory (in sequence mode)

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_INTERFACE    capture online data from INPUT_INTERFACE
  -f INPUT_FILE         capture offline data from INPUT_FILE
  -c, --csv, --flow     output flows as csv
```

Convert pcap file to flow csv:

```
cicflowmeter -f example.pcap -c flows.csv
```

Sniff packets real-time from interface to flow csv: (**need root permission**)

I advise you to run the "main.py" that is a code ready to run from console and the packets will be dumped into a file "flow.csv".

```
cicflowmeter -i eth0 -c flows.csv
```

### Reference: https://www.unb.ca/cic/research/applications.html#CICFlowMeter
