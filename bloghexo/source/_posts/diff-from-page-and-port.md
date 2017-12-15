---
title: diff from page and port
date: 2017-12-14 17:30:15
---
## diff from page and port

## debian没有装中文系统，中文输入法也没有。

  如果只有post没有page, 在主页上没有显示。主页上的日志数也没有计数。加上page 的Index就可以。index 有没有东西都无所谓。
  另外，如果在Markdown文章内容开头添加more即可折叠内容。更美观。
<!-- more -->

  NEXT官方提供了三种**全文阅读**的设置方法：

  1. 文章开头添加```<!--more-->```
  2. 文章的front-matter中添加`description`, 就是在上面的title,和date下面添加一行 `description:`;
  3. 修改主题配置文件`theme\next\_config.yml`, 将`auto_excerpt: enable: true`.

我设置了最后一种啦。
