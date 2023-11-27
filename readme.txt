此文件夹中包含《Python科研论文配图绘制指南：基于Python》的配套练习数据和代码

针对购买书籍读者反馈的问题，先将运行本书中代码最常见的几个问题汇总如下：

✅：书籍配套代码，请按照书籍介绍自行获取(会更新，按照要求进读者交流群获取信息)

✅：书籍中提到的 from colormaps import parula  为自己编写的文件，使用时需导入对应的colormaps.py文件(已提供，在此文件同一文件夹中)，
        需要将该文件复制到运行环境的同一文件夹内即可。

✅🔶：关于Proplot包的安装，使用pip或者conda 安装都是可以的，推荐如下代码安装：
      conda install -c conda-forge proplot

  🔹注意：导入proplot包(import proplot as pplt)后出现如Figure no attribute等问题，是因为目前版本(0.9.7)不支持3.5系列版本的Matplotlib（非常重要）
  🔹如果想使用Proplot包的功能，大家可以安装proplot,不想使用不安装即可，同时对代码中有关proplot包的代码使用“#”注销即可。
  🔹如果想使用proplot包的功能，建议大家将Matplotlib的版本建议和书籍保持一致：conda install matplotlib==3.4.3 
  🔹关于Proplot包的安装方法和其他函数用法，大家可以直接查看对应官网：https://proplot.readthedocs.io/en/stable/index.html#
  🔹代码中出现pplt均为import proplot as pplt ,没有此行代码自行加入即可。

✅🔶：针对SciencePlots包的安装(详细看书籍42页)，大家仔细看书籍里介绍内容，包括安装方法(官网也有方法，以官网为主)，依赖软件MikTex、
        Ghostscript(非常重要必须安装并添加系统环境变量，注意杀毒软件允许,第2章文件夹中已提供)。

  🟢注意：最新版本(2.1.0)引用的方式可能和书籍中(1.0.9)引用的方式不同：
  🟢最新版本引用方式：import scienceplots 然后再使用plt.style.use('science')等方法引用。
  🟢书籍版本引用方式：plt.style.use('science')

  🔹建议大家安装最新版本，书籍内容后续会修正。
  🔹更多关于SciencePlots介绍可查看官网：https://github.com/garrettj403/SciencePlots
  🔹如果不想使用SciencePlots包的功能，直接在对应代码之前添加“#”符号注释掉对应代码即可

🟢以上关于Proplot包和SciencePlots包的安装和版本选择问题，是目前读者遇到的最多问题，笔者当初在别写此内容的时候，本意想法是
🟢让大家多一个绘图工具和省去不必要的绘图主题设置，没想到这反而成了运行出错最多的问题(而且还是开始的安装问题·····)，学习Python绘图和做科研一样，
🟢要耐着性子去慢慢学习不同包的使用，不同版本的兼容等问题，希望大家认真查看不同包的官网对和书籍对应介绍内容，完成各种拓展包得心应手，成为科研大佬！！

✅ 书籍中的seaborn版本为0.11版本，最新版本的0.12.2可能会出现部分官方的数据没有提供。没有的话，直接从以下网址进行下载:
https://github.com/mwaskom/seaborn-data/tree/master
✅ Seaborn的0.12.2版本代码正在整理中，如果大家想使用0.11版本，即书籍版本，可使用如下代码安装指定版本的seabron:
conda install seaborn==0.11.2

✅ ：书籍对应的Anaconda(集成环境，内置了常用工具包)版本下载方式：
  链接：https://pan.baidu.com/s/1o12ZugRU40LlyF5T4ZSoPQ?pwd=81y4 
  提取码：81y4

✅ ：针对Python版本问题，大家不必一定要和书籍里的一样，主要的matplotlib和Proplot的版本兼容，如果大家想用Proplot的话就一定设置Matplotlib不要为3.5版本系列，
        不想用就无所谓Python版本。

✅：书籍第2页中介绍的不同包版本为主要数据处理、可视化包，不表示全部安装包，运行代码在遇到不存在某个包时，大家自行安装即可。

✅：针对出错提示的安装包等基础问题，大家百度搜索比在群里咨询效率高的多哈。

✅：作者最近在赶项目和更新书籍中的勘误和代码，可能不能第一时间给带大家答复，会统一进行回复的哈，还请谅解🧡

  🔷大家可以关注视频号DataCharm,定制直播答疑书籍中出现的问题和介绍一些优秀的可视化技巧及学习资源🔷









