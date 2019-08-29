# continuous-pull

A command-line utility to continuously pull Git repository locally.

## Usage

Go to the Git repository that you want to continuously pull from a branch.
Then run the following command:

```sh
cpull
```

To see the options:

```sh
$ cpull --help
Usage: cpull [OPTIONS]

Options:
  -b, --branch TEXT            Branch to pull. Defaults to 'master'.
  -i, --interval INTEGER       Interval between git pulls.
  -h, --hide / -nh, --no-hide  Whether or not to hide the output from the
                               tool.
  --help                       Show this message and exit.
```

## Installation

To install `continuous-pull`, follow one of the following instructions.

### Install from GitHub

```bash
pip install git+https://github.com/ericmjl/continuous-pull
```
