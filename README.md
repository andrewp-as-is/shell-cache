<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/shell-cache.svg?maxAge=3600)](https://pypi.org/project/shell-cache/)
[![](https://img.shields.io/npm/v/shell-cache.svg?maxAge=3600)](https://www.npmjs.com/package/shell-cache)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/shell-cache/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/shell-cache/actions)

### Installation
```bash
$ [sudo] pip install shell-cache
```

```bash
$ [sudo] npm i -g shell-cache
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

#### Examples
```bash
$ shell-cache "key" "value ..."
$ shell-cache "key"
"value ..."
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>