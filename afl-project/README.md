# AFL porject

> 使用方法见实验报告

1. 把 binutils-2.39.tar.gz 解压两份，分别命名为 binutils-2.39-fuzz 和 binutils-2.39-gcov。前者用于fuzzing，后者用于gcov。（因文件较大不方便提交，在此只留下空文件夹以展示项目结构）
2. out是afl-fuzz得到的结果。
3. cov-result下每一个文件夹对应一个实验对象，每个实验对象目录中有经过gcov计算覆盖率的结果(.gcov .gcda .gcno .info)，还有page文件夹即为lcov可视化处理得到的html页面(index.html)。
