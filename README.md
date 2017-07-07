Bi-Stream Logging Handler
=========================

Python logging handler which divides output stdout and stderr by log level

* If log level is over the threshold (default WARNING), output to stderr
* log level is under the threshold, output to stdout

cf.
https://stackoverflow.com/questions/2302315/how-can-info-and-debug-logging-message-be-sent-to-stdout-and-higher-level-messag

## install

* `> pip install git+https://github.com/tetutaro/bistream_logging_handler`

## Usage

see [sample](sample)
