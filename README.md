I googled and found no existing tools. The only useful piece of information I got was a mapping file that contains a Unicode Pinyin table. So I have to do it myself… to write a script to convert the Unicode Chinese file names to Pinyin using the mapping file.
Since I was doing Python Challenge at the time, natually I just scripted something in Python to get the job done.

The reason I did that was this. I have a HDTV that has a feature to play music from an USB drive. When I wanted to play the songs I downloaded from the Voice of China. I had a problem. The file name of the songs had many Unicode Chinese characters. The TV obviously doesn’t support Unicode. It just doesn’t display those Chinese characters at all. For example:
```
01 04张玮 – High歌.mp3
05 09吉克隽逸 – I Fell Good.mp3
```
All I can see is:
```
01 04 – High.mp3
05 09 – I Fell Good.mp3
```
If those above are okay, then the following ones are ridiculous:
```
11 11 – .mp3
11 12 – .mp3
11 13 – .mp3
11 14 – .mp3
```
I have no idea what was what when I tried to choose the songs. Actually their filenames are as the following:
```
11 11大山 – 王妃.mp3
11 12王韵壹 – 你快乐所以我快乐.mp3
11 13金池 – 后知后觉.mp3
11 14吴莫愁 – 痒.mp3
```
Putting the mapping file and the script in one folder, all renaming Unicode files under a sub folder “VoC”, then just run the script. Finally I got all the file names like this, not perfect but I am able to tell what songs they are:
```
11 11 DaShan – WangFei.mp3
11 12 WangYunYi – NiKuaiLeSuoYiWoKuaiLe.mp3
11 13 JinChi – HouZhiHouJue.mp3
11 14 WuMoChou – Yang.mp3
```
I hope you find my solution helpful.

This is the link where I got the mapping file:

ftp://ftp.cuhk.hk/pub/chinese/ifcss/software/data/Uni2Pinyin.gz
