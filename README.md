# CNN-kaf
这是基于论文《Convolutional Neural Networks for Sentence Classification》中作者源代码,经过修改和扩展的python项目。作者在论文中实现的是基于英语短句子的文本分类。经过修改，我们实现了在企业给的数据集上训练模型。另外我们实现了TF—IDF，计算所有词向量平均值的对于句子的建模方式，并且对比了SVM，RandomForest在同样数据集上的准确率。其中,RandomForest训练时采用10折交叉验证.使用到作者代码的是文件 BOW/trainGraph.py, 用到的是作者在论文中描述的CNN的model搭建过程,我们修改了部分参数来使模型适合本项目.

环境说明:python 2.7 需要安装有关的python库,如sklearn,keras,numpy,tensorflow等

1.目录说明（按照目录顺序）
目录：average : 计算词向量的平均值(SVM&RandomForest)
内容：在这个文件夹中，实现了在均值情况下对于SVM和RandomForest分类效果的对比。词向量是基于Google的Word2Vec训练的，这部分工作是单独的代码，同项目文件一起提交。

目录：BOW : SVM & RandomForest & CNN
内容：这个目录下是使用了Bag of words来作为分类器的输入，对比了论文中的CNN，SVM和RandomForest。

目录：data
内容：目录下存放着所有企业给出的带标签的数据。五个维度分别以五个csv文件给出：business.csv/others.csv/platform.csv/product.csv/service.csv 分别对应 业务/其他/平台/产品/服务 五个维度.
    vectors.bin:基于35w条评论分词处理获得的词向量二进制文件.
    split.txt:基于35w条评论分词得到的结果,也是google word2vec的输入,其产出就是vectors.bin

目录:docs
内容:论文pdf

目录:TF-IDF
内容:目录下存放基于TF-IDF的输入下,各个分类器准确率对比的代码.

目录:word2vec_models
内容:论文中用到的word2vec模型


2.运行说明:
运行BOW,TF-IDF,计算词向量的平均值 这三个目录下的trainGraph.py即可
注:SVM模型训练耗时较长,需要等待大概30min左右. RandomForest很快,几秒钟可以给出结果.
