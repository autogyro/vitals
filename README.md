# Vitals
A program to log your vitals (blood pressure, pulse) for further analysis.

## Getting started

### Dependencies
- cargo
- rustc

### Install
To install, ensure you have the required dependencies above, then run the following command:
```shell
make install
```

### Usage
Once the CLI is installed, you can run the following command from the terminal.

```shell
USAGE:
    vitals <systolic> <diastolic> <pulse> <file>

OPTIONS:
    -h, --help       Prints help information
    -V, --version    Prints version information

ARGS:
    <systolic>     Your systolic blood pressure reading in mmHg
    <diastolic>    Your diastolic blood pressure reading in mmHg
    <pulse>        Your pulse in bpm
    <file>         The file to log your vitals to (csv format).
```

## Contributing
Please fork this repo and submit a pull request to contribute. I will review all changes and respond if they are accepted or rejected (as well as reasons, so it will be accepted).

### Issues
If you are submitting a bug, please describe the bug in detail and how to replicate if possible. Logs are also very useful.

If you are submitting a feature idea, please describe it in detail and document the potential use cases of that feature if it isn't clear.

## Credits
- @kylecorry31 - Initial work

## License
You are free to copy, modify, and distribute vitals with attribution under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
