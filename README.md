petridish
=========

Warning
-------
This project is designed for malware analysts and researchers, to make it easier
to collect malware samples. While none of the downloaded samples are run once on
your system, it is sill *actual, fresh malware*. Practice caution when using the
tool.

I am not liable for any damage you do to your system by using this tool.

Dependencies
------------
`petridish` is written in Python3, and requires `requests` and `beautifulsoup`
to be installed. These libraries are used to crawl the supported databases,
and can be installed by running `pip install -r requirements.txt`.

Usage
-----
You run `petridish` by simply typing `./petridish.py` or `python petridish.py`
into your commandline. By default, it reads `petri.cfg` for configuration such
as API keys and credentials, and it downloads 10 samples *from each supported
site* by default.

The following options are supported on the commandline:

```
usage: petridish.py [-h] [-n NUM] [--cfg CFG]

optional arguments:
  -h, --help  show this help message and exit
  -n NUM      Number of samples to download from each site
  --cfg CFG   Configuration file to use
```

Supported data bases
--------------------
* malshare.com - Requires API key to be provided via the configuration file
* malekal.com

Possible future support
-----------------------
* vxvault.net - Partially implemented, but requires authentication that I don't
  have, so I can't test the last steps
* virusshare.com
* malware.lu
* scumware.org
* malc0de.com
* sucuri.net
* clean-mx.com
* ...
