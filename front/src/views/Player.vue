<template>
    <div class="body">

        <h1 style="text-indent: -9999"></h1>
        <div id="titleBar">
            <span class="name">
                <span>
                    <span style="color: RGB(87,96,113); size: 25px; "> 2051857's Video Player </span>
                </span>
            </span>
            <ul>
                <li style="cursor: default" @click="exit">退出登录</li>
            </ul>
        </div>

        <div id="player">
            <video id="video" ref="videoElement" controls="controls" autoplay="autoplay"></video>
            <div id="controls">
                <!--播放/暂停按钮-->
                <button id="play-pause-btn" ref="playPauseBtn" class="play" @click="togglePlayPause"></button>
                <div id="progress-bar-container" ref="progressBarContainer" @click="Progressclick">
                    <!--视频播放的进度条-->
                    <div id="progress-bar" ref="progressBar"></div>
                </div>
                <button id="beisu_show" @click="AddRate"></button>
                <button id="jiansu_show" @click="DownRate"></button>
                <button id="add_volume" @click="Addvolume"></button>
                <button id="down_volume" @click="Downvolume"></button>
                <button id="screen-size" class="all_screen" @click="toggleScreen"></button>
            </div>
        </div>
        <!--播放列表-->
        <div id="selector">
            <div id="Per" v-for="(play_video, index) in playlist" @click="playVideo(index)">
                <div id="title">{{ play_video.videoName }}</div>
                <div id="descript">{{ play_video.videoDescript }}</div>
            </div>
        </div>

    </div>
</template>

<script>
import request from '../../utils/request';

// import Selector_vedio from './Selector_vedio.vue';
export default {
    name: "Player",
    // components:{
    //     Selector_vedio//调用中间
    // },
    data() {
        return {
            playlist: [],
            currentVideoIndex: 0,
            isPlaying: false,
            currentTime: '00:00',
            duration: '00:00',
            progressPercentage: '0%',
            isMuted: false,
            volume: 1,
            isFullscreen: false,
        };
    },
    created() {
        this.fetchData()
    },
    mounted() {
        const videoElement = this.$refs.videoElement;
        // videoElement.pause();
        videoElement.addEventListener('timeupdate', this.updateProgress);
        videoElement.addEventListener('ended', this.Endplay);

    },
    beforeDestroy() {
        const videoElement = this.$refs.videoElement;
        videoElement.removeEventListener('timeupdate', this.updateProgress);
        videoElement.removeEventListener('ended', this.Endplay);
    },
    methods: {
        async fetchData() {
            const res = await request.get(`/all_vedio`)
            this.playlist = res.data.data
            // console.log(this.playlist)
        },
        exit() {
            this.$router.push('/')
        },
        playVideo(index) {//点击视频选择播放
            this.currentVideoIndex = index;
            const videoElement = this.$refs.videoElement;
            videoElement.src = this.playlist[index].videoUrl;
            videoElement.load();
            videoElement.play();
            this.isPlaying = true;
            const playPauseBtn = this.$refs.playPauseBtn;
            playPauseBtn.classList.remove("play");
            playPauseBtn.classList.add("pause");
        },
        togglePlayPause() {//播放/暂停
            const playPauseBtn = this.$refs.playPauseBtn;
            const videoElement = this.$refs.videoElement;
            if (this.isPlaying) {
                videoElement.pause();
                //playPauseBTn应该显示为play而不是pause
                playPauseBtn.classList.remove("pause");
                playPauseBtn.classList.add("play");
            } else {
                videoElement.play();
                //playPauseBTn应该显示为pause而不是play
                playPauseBtn.classList.remove("play");
                playPauseBtn.classList.add("pause");
            }
            this.isPlaying = !this.isPlaying;
        },
        Progressclick(e) {//监听进度条的点击事件
            const progressBarContainer = this.$refs.progressBarContainer;
            // 计算鼠标点击的位置所对应的视频时间
            //getBoundingClientRect获得页面中某个元素的左，上，右和下分别相对浏览器视窗的位置,.left即获取左边相对浏览器视窗的位置
            const containerPosition = progressBarContainer.getBoundingClientRect().left;
            const containerWidth = progressBarContainer.clientWidth; //获取完整进度条元素的像素宽度
            const clickPercentage = (e.clientX - containerPosition) / containerWidth; //clientX是事件发生时的应用客户端区域的水平坐标，获取实际比例
            const videoElement = this.$refs.videoElement;
            videoElement.currentTime = clickPercentage * video.duration; //获取真实时间长
        },
        updateProgress() {// 监听视频的时间更新事件
            const videoElement = this.$refs.videoElement;
            const progressBar = this.$refs.progressBar;
            const progress = (videoElement.currentTime / videoElement.duration) * 100; //进度=当前时间/总时间，*100后范围在【0-100】
            progressBar.style.width = `${progress}%`; //进度条宽度更新
        },
        Endplay() {// 监听视频的播放结束事件
            // 默认重新播放将播放按钮设置为“播放”状态
            const playPauseBtn = this.$refs.playPauseBtn;
            playPauseBtn.classList.remove("pause");
            playPauseBtn.classList.add("play");
        },
        Loadend() {// 监听视频的加载完成事件
            const progressBar = this.$refs.progressBar;
            // 设置已经播放进度条为0
            progressBar.style.width = "0%";
            const videoElement = this.$refs.videoElement;
            videoElement.volume = 0.2; //声音最开始设置为0.2
            videoElement.playbackRate = 1.0; //播放速度初始化为正常
            this.isFullscreen = false;
        },
        Addvolume() {//监听增加声音事件
            const videoElement = this.$refs.videoElement;
            if (videoElement.volume >= 1) { //volume在0-1之间
                alert('音量已经最大啦！');
                return;
            }
            videoElement.volume += 0.2;
            videoElement.volume = video.volume.toFixed(2); //解决小数运算精度问题
        },
        Downvolume() {//监听减少声音事件
            const videoElement = this.$refs.videoElement;
            if (videoElement.volume <= 0) { //volume在0-1之间
                alert('音量已为零！');
                return;
            }
            videoElement.volume -= 0.2;
            videoElement.volume = video.volume.toFixed(2); //解决小数运算精度问题
        },
        AddRate() {//监听加速事件
            const videoElement = this.$refs.videoElement;
            videoElement.playbackRate += 0.5; //一次减少0.5
            videoElement.playbackRate = video.playbackRate.toFixed(2); //解决小数运算精度问题
        },
        DownRate() {
            const videoElement = this.$refs.videoElement;
            if (videoElement.playbackRate <= 0) {
                alert('视频播放速度已经为0!');
                return;
            }
            videoElement.playbackRate -= 0.5; //一次减少0.5
            videoElement.playbackRate = video.playbackRate.toFixed(2); //解决小数运算精度问题
        },
        toggleScreen() {//全屏/取消全屏，暂未实现

        }
    }
}
</script>

<style scoped>
.body {
    /* background-color: rgb(32, 177, 212); */
    /* background-color: #c5d5d0; */
    width: 1530px;
    height: 750px;
    float: left;
    float: top;
}

* {
    margin: 0px;
    padding: 0px;
}

#titleBar {
    background-color: #07cbc9;
    height: 10%;
    position: absolute;
    width: 100%;
}

#titleBar>.name {
    font-size: 40px;
    /* font-family: 华文新魏; */
    margin: 0px 0.8%;
    line-height: 180%;
    /* float: left; */
    background: linear-gradient(135deg, goldenrod 25%, blue 100%);
    /*设置渐变背景，右下角方向，颜色25%开始*/
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
}

#titleBar>ul {
    float: right;
    list-style-type: none;
    width: 15%;
    margin-right: 5%;
}

#titleBar>ul li {
    text-align: center;
    width: 50%;
    float: left;
    font-size: 20px;
    font-family: 行楷;
    paddig: 0 5%;
    line-height: 350%;
    transition: font-weight 0.3s, color 0.3s, background-color 0.3s, transform 0.3s;
    -moz-transition: font-weight 0.3s, color 0.3s, background-color 0.3s, -moz-transform 0.3s;
    -webkit-transition: font-weight 0.3s, color 0.3s, background-color 0.3s, -webkit-transform 0.3s;
    -o-transition: font-weight 0.3s, color 0.3s, background-color 0.3s, -o-transform 0.3s;
}

#titleBar>ul li:hover {
    font-weight: bolder;
    color: white;
    background-color: darkslategray;
    transform: scale(1.1, 1.1);
}

#titleBar>ul a {
    color: #000000;
    text-decoration: none;
}

#player {
    height: 80%;
    width: 55%;
    position: absolute;
    left: 5%;
    top: 15%;
    box-shadow: 5px 5px 10px 2px black;
    -moz-box-shadow: 5px 5px 10px 2px black;
    /* 老的 Firefox */
    background-color: white;
}

#player>#video {
    width: 100%;
    height: 90%;
    float: left;
    /* position: absolute; */
    top: 0;
}

#player>#controls {
    /*控制条的位置*/
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 60px;
    background-color: rgba(0, 0, 0, 0.5);
}

.play {
    /*播放按钮设置*/
    width: 30px;
    height: 30px;
    /* position: relative; */
    margin: 20px;
    float: left;
    background-image: url("/static/img/播放.png");
    background-size: cover;
}

.pause {
    /*暂停按钮设置，后面两者会相互转化*/
    width: 30px;
    height: 30px;
    margin: 20px;
    float: left;
    background-image: url("/static/img/暂停.png");
    background-size: cover;
}

#progress-bar-container {
    /*总进度条*/
    position: absolute;
    top: 4px;
    left: 0px;
    width: 100%;
    height: 8px;
    background-color: rgba(255, 255, 255, 0.5);
}

#progress-bar {
    /*真实的播放进度条*/
    height: 100%;
    background-color: rgb(242, 233, 233);
    width: 0%;
}

#add_volume {
    /*声音增加按钮*/
    position: absolute;
    width: 30px;
    height: 30px;
    margin: 20px;
    left: calc(100% - 140px);
    background-image: url("/static/img/音量加.png");
    background-size: cover;
}

#down_volume {
    /*声音减少按钮*/
    position: absolute;
    width: 30px;
    height: 30px;
    margin: 20px;
    left: calc(100% - 100px);
    background-image: url("/static/img/音量减.png");
    background-size: cover;
}

#jiansu_show {
    /*减速播放*/
    position: absolute;
    width: 30px;
    height: 30px;
    margin: 20px;
    left: calc(100% - 180px);
    background-image: url("/static/img/减速.png");
    background-size: cover;
}

#beisu_show {
    /*倍速播放*/
    position: absolute;
    width: 30px;
    height: 30px;
    margin: 20px;
    left: calc(100% - 220px);
    background-image: url("/static/img/倍速播放.png");
    background-size: cover;
}

.all_screen {
    /*全屏显示按钮设置*/
    width: 30px;
    height: 30px;
    position: absolute;
    margin: 20px;
    left: calc(100% - 60px);
    background-image: url("/static/img/全屏.png");
    background-size: cover;
}

.small_screen {
    /*退出全屏按钮设置，后面两者会相互转化*/
    width: 30px;
    height: 30px;
    margin: 20px;
    left: calc(100% - 60px);
    position: absolute;
    background-image: url("/static/img/取消全屏.png");
    background-size: cover;
}

#selector {
    overflow: auto;
    height: 85%;
    width: 20%;
    position: absolute;
    right: 10%;
    top: 12.5%;
    background-color: #abf1f1;
}

#Per {
    /*这是selector里每个选项框*/
    width: 100%;
    height: 20%;
    position: relative;
    padding: 2px 0px;
    border-bottom: 2px solid black;
}

#Per:hover {
    background-color: #07cbc9;
}

#title {
    /*选项的视频*/
    width: 100%;
    height: 15%;
    float: left;
    font-size: 25px;
    color: rgb(8, 121, 83);
}

#descript {
    /*描述 */
    width: 100%;
    /* padding-top: 20px; */
    margin-top: 15px;
    padding-left: 5px;
    padding-right: 5px;
    height: 80%;
    float: left;
    font-size: 18px;
}
</style>