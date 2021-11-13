1. start test file

```
python3 log_test2.py
```

2. change config level in conf file

```
[handler_consoleHandler]
class=StreamHandler
level=ERROR
formatter=consoleFormatter
args=(sys.stdout,)
```

to

```
[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=consoleFormatter
args=(sys.stdout,)
```


3. send to the server

```
./log_test2_cli.py logging.conf
```
