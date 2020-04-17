<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <!-- 轮播图 -->
        <div v-show="index === nowIndex" v-for="(item,index) in sliderImgList" :key="index" class="slider-item" v-bind:class="['item'+[index+1]]">
            <a href="">
                <img v-bind:src=item.imgUrl alt="" style="width: 900px;height: 500px;">
            </a>
        </div>
        <!-- 图片标题 -->
        <h2 class="slider-title" v-show="index === nowIndex" v-for="(item,index) in sliderImgList">{{ item.title }}</h2>
        <!-- 左右按钮 -->
        <a v-on:click="preHandler" href="javascript:void(0)" class="btn pre-btn">&lt;</a>
        <a v-on:click="nextHandler" href="javascript:void(0)" class="btn next-btn">&gt;</a>

        <!-- dots -->
        <ul class="slider-dots">
            <li v-on:click="clickdots(index)" v-for="(item,index) in sliderImgList" :key="index">{{ index+1 }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            nowIndex:0,
            sliderImgList:[
                {
                    imgUrl:require('../assets/img1.jpg'),
                    title:'第一张'
                },
                {
                    imgUrl:require('../assets/img2.jpg'),
                    title:'第二张'
                },
                {
                    imgUrl:require('../assets/img3.jpg'),
                    title:'第三张'
                },
                {
                    imgUrl:require('../assets/img4.jpg'),
                    title:'第四张'
                },
                ]
        }
    },
    methods: {
        preHandler(){
            this.nowIndex--;
            if(this.nowIndex <0 ){
                this.nowIndex = 3
            }
        },
        nextHandler(){
            this.autoPlay()
        },
        clickdots(index){
            this.nowIndex = index
        },
        autoPlay(){
            this.nowIndex++;
            if(this.nowIndex > 3){
                this.nowIndex = 0
            }
        },
        runInv(){
            this.invId = setInterval(this.autoPlay,2000)
        },
        clearInv(){
            clearInterval(this.invId)
        }
    },
    created() {
        this.runInv()
    },
}
</script>

<style scoped>
    .slider-wrapper{
        width: 900px;
        height: 500px;
        overflow: hidden;
        position: relative;
    }
    .slider-item{
        width: 900px;
        height: 500px;
        position: absolute;
    }
    .item1{
        z-index: 100;
    }
    .item2{
        z-index: 90;
    }
    .item3{
        z-index: 80;
    }
    .item4{
        z-index: 70;
    }
    .slider-dots{
        position: absolute;
        right: 50px;
        bottom: 20px;
        z-index: 200;
    }
    .slider-dots li{
        width: 20px;
        height: 20px;
        border-radius: 50%;
        text-align: center;
        line-height: 20px;
        background: #000;
        float: left;
        color: #ffffff;
        opacity: 0.6;
        margin: 0 10px;
    }
    .btn{
        width:50px;
        height: 50px;
        background:black;
        color: white;
        position:absolute;
        z-index: 300;
        font-size: 40px;
        text-align: center;
        line-height: 50px;
        top:50%;
        margin-top:-25px;
        opacity: 0.2;
    }
    .pre-btn{
        left:10px;
    }
    .next-btn{
        right:10px;
    }
    .slider-title{
        position: absolute;
        z-index: 400;
        background:black;
        color: white;
        bottom: 10px;
        left:20px;
        opacity: 0.6;
    }

</style>