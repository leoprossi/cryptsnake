# cryptsnake

An encryption tool for Linux

## Installation

### Prerequisites
First of all, make sure you have `python3` and `pip3` installed on your machine. These are the only requirements for the installation proccess to work.

See more:
* Python3: https://www.python.org/downloads/ or check the wiki of your Linux distribution.
* Pip3: https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers

### Installation walkthrough

If you have everything set up, then you should be able to proceed. Navigate to the project directory and run:
```
$ chmod +x install.sh && ./install.sh
```

In the middle of the installation, you'll be prompted to type your password. This step is necessary for creating a global `cryptsnake` command that's gonna work from eeverywhere in your system.

## Usage

`cryptsnake` is acually pretty simple and has only three running modes:

### Key generator
For generating keys, just run:
```
$ cryptsnake K key.txt seed
```
where:
* `K` is the flag that tells `cryptsnake` to run in Key Generator mode;
* `key.txt` is the name of the file that's going to store the generated key;
* `seed` is any string that's going to be used as seed for generating the key;

### Encrypt
For encrypting files, you have to run:
```
$ cryptsnake C text.txt encrypted.txt key.txt
```
where:
* `C` is the flag that tells `cryptsnake` to run in Encrypt mode;
* 'text.txt' is the file that's going to be encrypted;
* 'decrypted.txt' is the file that's going to store the encrypted content;
* 'key.txt' is the file that holds the encryption key;

### Decrypt
For decrypting encrypted files, run:
```
$ cryptsnake D encrypted.txt decrypted.txt key.txt
```
where:
* `D` is the flag that tells `cryptsnake` to run in Dencrypt mode;
* 'encrypted.txt' is the encrypted file;
* 'decrypted.txt' is the file that's going to store the decrypted content;
* 'key.txt' is the file that holds the encryption key;

## Getting help
```
$ cryptsnake -h
```
