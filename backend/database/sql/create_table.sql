drop database if exists video_player;
create database video_player;
use video_player;
drop table if exists user;
create table user(
	userName varchar(200) primary key Not NULL,
    userKey varchar(200) Not NULL
);
drop table if exists video;
create table video(
	videoId int not null primary key auto_increment,
    videoName varchar(100) not null,
    videoUrl varchar(100) not null,
    videoDescript varchar(100) not null
);
insert into video(videoName,videoUrl,videoDescript) values("喜羊羊","/static/video/show-1.mp4","欢迎来到喜羊羊与灰太狼的世界！(对不起，有点中二)");
insert into video(videoName,videoUrl,videoDescript) values('猫猫','/static/video/show-2.mp4', '看，这只小猫叫瓣瓣，十分亲人，她喜欢蹭人~我也好想当猫猫啊');
insert into video(videoName,videoUrl,videoDescript) values('电子蝴蝶', '/static/video/show-3.mp4', 'Cifer!!!这首歌叫电子蝴蝶，我的年度单曲，怎么可以这么好听！！！');
insert into video(videoName,videoUrl,videoDescript) values('破阵','/static/video/show-4.mp4', '这首歌叫破阵！！！是广播剧《营业悖论》里面的歌，真的超级好听！！！');
insert into video(videoName,videoUrl,videoDescript) values('大宋少年志', '/static/video/show-5.mp4','大宋少年志，我一直在期待第二季！！！yyds');
insert into video(videoName,videoUrl,videoDescript) values('深深', '/static/video/show-6.mp4', '周深就是好听之王！！！谁能拒绝戏腔的兰亭集序呢！！！');

