# 自动化测试大作业

**题目：** 基于覆盖率的模糊器评估

## 1 分工

组长：

+ 杜威：实验报告框架，AFL及对应部分报告

组员：

+ 朱甲豪：AFL++及对应部分报告
+ 金冯阳：Angora及对应部分报告
+ 马子睿：绘图及结果分析

## 2 作业仓库

github：https://github.com/cyrus-iwnl/fuzz-cov

gitlink：https://www.gitlink.org.cn/Cyrus/fuzz-cov

## 3 项目结构

+ AFL，AFL++，Angora三个目录分别是三个fuzzer的项目，项目的详细结构可以看对应fuzzer目录下的README。

+ result-analysis是结果分析部分，cov-chart目录下是根据fuzz+gcov的结果绘制的图形，statistics文件是所有fuzzer覆盖率的结果统计。
+ tools是实验过程中用到的一些脚本

+ 实验报告