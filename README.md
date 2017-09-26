##### duSheCommunity
  - 利用Fiddler抓包分析毒舌影评社区的APP api接口。单机版的scrapy爬虫，基于scrapy-redis的分布式爬虫。
##### 使用方法：
  - 项目依赖模块文件
  ```
  pip install scrapy-redis
  pip install scrapy
  ```
  - 如果遇到scrapy无法加载，可以直接下载Anaconda，避免下载过多的依赖包文件，造成无法搭建运行环境
  - dushe与dusheSingle是两个不同的版本。
  - git clone下来，随便一个项目，然后运行一下命令
  ```
  scrapy crawl duzheMovie
  ```
