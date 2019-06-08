<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/shell-cache.svg?maxAge=3600)](https://pypi.org/project/shell-cache/)
[![](https://img.shields.io/npm/v/shell-cache.svg?maxAge=3600)](https://www.npmjs.com/package/shell-cache)
[![Travis](https://api.travis-ci.org/looking-for-a-job/shell-cache.svg?branch=master)](https://travis-ci.org/looking-for-a-job/shell-cache/)

#### Installation
```bash
$ [sudo] npm i -g shell-cache
```
```bash
$ [sudo] pip install shell-cache
```

#### How it works
```bash
$SHELL_CACHE/<hash> # ~/.cache/shell-cache/<hash> by default
```

#### Config
optional. environment variables:
```bash
$ export SHELL_CACHE=~/.cache/shell-cache # $XDG_CACHE_HOME/shell-cache by default
```

#### Scripts usage
command|`usage`
-|-
`shell-cache` |`usage: shell-cache key [value]`

#### Examples
```bash
$ shell-cache "key" "value ..."
$ shell-cache "key"
"value ..."
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>