---
title: first chapter
date: 2017-12-08 17:06:28
tags: test
---

# My first chapter

HEXO + gitpage + Aliyun ECS == blog

1. node.js install

```bash
apt-get install -y nodejs
```

2. hexo install

```bash
npm install -g hexo

npm install
```

<!-- more -->

3. git install

```bash
apt-get install git
```

4. create a directory and init hexo

```bash
mkdir /home/jenney/hexoblog
cd /home/jenney/hexoblog

hexo init
```

5. git configuration
  a. create a repository from github.com, name:<Your github account name>.github.io
  b. create ssh key and copy id_rsa.pub to your github setting.

```bash
//create ssh key
ssh-keygen -t rsa -C "youremail@example.com"
```
 
```bash
git config --global user.name "your name"
git config --global user.email "your email"

cd /home/jenney/hexoblog
git init

vim _config.yml

//add follow config to file _config.yml
deploy: //after ":" has a space
type: git
repository: git@github.com:<your name>/<yourname>.github.io.git
branch: master
```

