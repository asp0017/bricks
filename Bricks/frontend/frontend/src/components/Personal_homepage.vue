<template>
    <div>
        <div class="nav">
            <img src="../assets/brickslogo.svg" alt="">
            <div class="tri_btn">
                <input type="text">
                <img src="../assets/search.svg" alt="" class="search">
                <img src="../assets/Notice/Notice_Default.svg" alt="" class="notice">
                <img src="../assets/Profile/Profile_Default.svg" alt="" class="profile">
            </div>
        </div>
        <div class="left_bar">
            <div class="add_btn" @click="add_btn">新增專案</div>
            <div class="plus" @click="add_btn"></div>
            <div class="three_pointer">
                <input type="radio" id="overview" class="list" name="list" checked value="option1">
                <label for="overview" @click="change(1)">專案總覽</label>
                <img src="../assets/icon/icon_file.svg" style="top: 26px">
                <input type="radio" id="over" class="list" name="list" value="option2">
                <label for="over" @click="change(2)">已結束專案</label>
                <img src="../assets/icon/icon_file.svg" style="top: 102px">
                <input type="radio" id="trash" class="list" name="list" value="option3">
                <label for="trash" @click="change(3)">垃圾桶</label>
                <img src="../assets/icon/icon_trashcan.svg" style="top: 178px">
            </div>
        </div>
        <div class="add_proj_box" v-show="add_proj_show">
            <div class="close_add_proj_box" @click="add_btn"></div>
            <p class="add_proj_title">新增專案</p>
            <div class="add_proj_pic">
                <img src="../assets/add_proj_pic_plus.svg" class="add_proj_pic_plus">
            </div>
            <input type="text" placeholder="輸入專案名稱" class="add_proj_name">
            <select name="" id="" class="add_proj_type" placeholder="選擇專案類型">
                <option value="" disabled selected hidden style="color: #b6aeae;">選擇專案類型</option>
                <option value="">社團 / 活動</option>
                <option value="">社團 / 活動</option>
                <option value="">社團 / 活動</option>
            </select>
            <div class="add_proj_build" @click="new_project_btn">建立專案</div>
        </div>
        <div class="main_body">
            <div class="bg">
                <!-- 背景透明灰色 -->
                <div class="overlay" v-if="showOverlay"></div>
                <div class="middle">
                    <div class="overview_page" v-show="middle_show_overview_page">
                        <div class="uncategorized" ref="uncategorized">
                            <p class="card_title">未分類</p>
                            <div class="title_underline"></div>
                            <div class="box_container" ref="box_container">
                                <div class="box">實驗1</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                                <div class="box">實驗2</div>
                            </div>
                        </div>
                    </div>
                    <div class="over_page" v-show="middle_show_over_page"></div>
                    <div class="trash_page" v-show="middle_show_trash_page"></div>
                </div>
            </div>
        </div>
    </div>
</div></template>

<script>
export default {
    name: 'Personal_homepage',
    data() {
        return {
            middle_show_overview_page: true,
            middle_show_over_page: false,
            middle_show_trash_page: false,
            add_proj_show: false,
            showOverlay: false,
        };
    },
    computed: {
        box_container_height() {
            return this.$refs.box_container.offsetHeight + 103 + 'px';
        },
    },
    methods: {
        add_btn() {
            this.add_proj_show = this.add_proj_show === false ? true : false;
            this.showOverlay = !this.showOverlay;
            console.log(this.add_proj_show)
        },
        // 建立專案的事件
        new_project_btn() {
            this.add_proj_show = this.add_proj_show === false ? true : false;
            this.showOverlay = false;
        },
        change(index) {
            if (index === 1) {
                this.middle_show_overview_page = true
                this.middle_show_over_page = false
                this.middle_show_trash_page = false
            }
            if (index === 2) {
                this.middle_show_over_page = true
                this.middle_show_overview_page = false
                this.middle_show_trash_page = false
            }
            if (index === 3) {
                this.middle_show_trash_page = true
                this.middle_show_overview_page = false
                this.middle_show_over_page = false
            }
        },
    },
    created() {

    },
    mounted() {
        console.log(this.$refs.box_container.offsetHeight);
        console.log(this.$refs.uncategorized.offsetHeight);
        console.log(this.box_container_height)
    }
}
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    font-family: 'Noto Sans TC';
}

/* navigation bar的部分 起點*/
.nav {
    width: 100vw;
    height: 49px;
    background-color: white;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    position: fixed;
    z-index: 9;
}

.nav>img {
    height: 32.06px;
    width: auto;
    position: absolute;
    top: 8px;
    left: 2.6%;
    -webkit-user-drag: none;
}

.tri_btn {
    width: 340px;
    height: 30px;
    position: absolute;
    right: 50px;
    top: 9.03px;
}

.tri_btn input {
    width: 248px;
    height: 28px;
    background-color: #f2eeee;
    border-radius: 24px;
    border: 1px solid transparent;
    outline: none;
    text-indent: 43px;
    font-size: 16px;
    font-weight: 400;
    position: absolute;
}


.tri_btn input:hover {
    background-color: #e1dcdc;
}

.tri_btn input:focus {
    background-color: white;
    border-color: #c7c2c2;
}

.search {
    position: absolute;
    top: 7px;
    left: 15px;
}

.notice {
    position: absolute;
    right: 45px;
    cursor: pointer;
    -webkit-user-drag: none;
}

.notice:hover {
    content: url(../assets/Notice/Notice_Hover.svg);
}

.notice:active {
    content: url(../assets/Notice/Notice_Active.svg);
}

.profile {
    position: absolute;
    right: 0px;
    cursor: pointer;
    -webkit-user-drag: none;
}

.profile:hover {
    content: url(../assets/Profile/Profile_Hover.svg);
}

.profile:active {
    content: url(../assets/Profile/Profile_Active.svg);
}

/* navigation bar的部分 終點 */

/* 左側欄的部分 起點 */
.left_bar {
    width: 272px;
    height: calc(100vh - 48px);
    background-color: #f2eeee;
    border-radius: 0px 14px 14px 0px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.25);
    position: fixed;
    bottom: 0px;
    z-index: 8;
}

.add_btn {
    width: 174px;
    height: 65px;
    position: relative;
    top: 40px;
    left: 48px;
    border-radius: 32px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.4);
    background-color: #B82C30;
    cursor: pointer;
    font-size: 18px;
    font-weight: 500;
    letter-spacing: 1.25px;
    line-height: 65px;
    color: white;
    text-indent: 68px;
    user-select: none;
}

.plus {
    position: relative;
    width: 14px;
    height: 14px;
    background-color: transparent;
    border: 1.5px solid transparent;
}

.plus::before,
.plus::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 1.5px;
    background-color: white;
    top: 50%;
    left: 83px;
}

.plus::before {
    transform: rotate(90deg);
}

.plus::after {
    transform: rotate(0deg);
}

.three_pointer {
    width: 100%;
    height: 228px;
    position: relative;
    top: 61px;
}

.three_pointer input[type='radio'] {
    display: none;
}

.three_pointer input[type='radio']+label {
    display: inline-block;
    width: 100%;
    height: 76px;
    background-color: transparent;
    font-size: 19px;
    font-weight: 400;
    line-height: 76px;
    letter-spacing: 0.15px;
    text-indent: 116px;
    cursor: pointer;
    user-select: none;
}

.three_pointer input[type='radio']:hover+label {
    background-color: #e1dcdc;
}

.three_pointer input[type='radio']:checked+label {
    background-color: #e1dcdc;
}

.three_pointer img {
    position: absolute;
    left: 64px;
    -webkit-user-drag: none;
}

/* 左側欄的部分 終點 */

/* 新增專案的框框 起點 */
.add_proj_box {
    width: 344px;
    height: 524px;
    position: fixed;
    border-radius: 14px;
    background-color: white;
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.4);
    top: 244px;
    left: 924px;
    z-index: 6;
}

.close_add_proj_box {
    position: relative;
    width: 12px;
    height: 12px;
    cursor: pointer;
    top: 25px;
    left: 307px;
}

.close_add_proj_box::before,
.close_add_proj_box::after {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    width: 2px;
    height: 17px;
    background-color: black;
}

.close_add_proj_box::before {
    transform: translate(-50%, -50%) rotate(45deg);
}

.close_add_proj_box::after {
    transform: translate(-50%, -50%) rotate(-45deg);
}

.add_proj_title {
    font-size: 23px;
    font-weight: 700;
    position: relative;
    top: 40px;
    text-align: center;
    user-select: none;
}

.add_proj_pic {
    width: 280px;
    height: 140px;
    border-radius: 14px;
    background-color: #f2eeee;
    position: relative;
    top: 60px;
    left: 50%;
    transform: translate(-50%);
    cursor: pointer;
    -webkit-user-drag: none;
}

.add_proj_pic_plus {
    position: relative;
    top: 40px;
    left: 110px;
    user-select: none;
    -webkit-user-drag: none;
}

.add_proj_name {
    width: 278px;
    height: 38px;
    border: 1px solid #c7c2c2;
    border-radius: 12px;
    font-size: 16px;
    letter-spacing: 1.25px;
    line-height: 38px;
    text-indent: 20px;
    position: relative;
    top: 108px;
    left: 50%;
    transform: translate(-50%);
}

.add_proj_name:hover {
    border-color: #b6aeae;
}

.add_proj_name:focus {
    border-color: #3b3838;
}

.add_proj_name::placeholder {
    user-select: none;
    color: #b6aeae;
}

.add_proj_type {
    width: 278px;
    height: 38px;
    border: 1px solid #b8b8b8;
    border-radius: 12px;
    position: relative;
    top: 124px;
    left: 50%;
    transform: translate(-50%);
    font-size: 16px;
    letter-spacing: 1.25px;
    line-height: 38px;
    text-indent: 20px;
    color: black;
    cursor: pointer;
    user-select: none;
}

.add_proj_type:hover {
    border-color: #7b7b7b;
}

.add_proj_type select option:first-child {
    display: none;
}

.add_proj_build {
    width: 280px;
    height: 48px;
    border-radius: 14px;
    background-color: #b82c30;
    color: white;
    font-size: 18px;
    font-weight: 500;
    line-height: 48px;
    letter-spacing: 1.25px;
    text-align: center;
    position: relative;
    top: 170px;
    left: 50%;
    transform: translate(-50%);
    cursor: pointer;
    user-select: none;
}

/* 新增專案的框框 終點 */



/* 背景灰色 */
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(59, 56, 56, 0.5);
    z-index: 999;
}

/* 中間的部分 起點 */
.bg {
    width: calc(100vw - 272px);
    height: calc(100vh - 48px);
    position: fixed;
    bottom: 0px;
    right: 0px;
    background-image: url(../assets/bricks_bg.svg);
    overflow-x: auto;
    overflow-y: hidden;
}

.middle {
    width: 1448px;
    height: 1000px;
    position: absolute;
    overflow-y: auto;
    overflow-x: hidden;
    top: 40px;
    left: 96px;
}

::-webkit-scrollbar {
    display: none;
}

.uncategorized {
    width: calc(100% - 10px);
    /* height: 300px; */
    height: var(--box_container_height);
    min-height: 218px;
    /* height: calc(100% + 77px); */
    background-color: #f2eeee;
    border-radius: 14px;
    border: 1px solid #e1dcdc;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
}

.card_title {
    font-size: 16px;
    font-weight: 400;
    line-height: 24px;
    letter-spacing: 0.5px;
    position: relative;
    top: 22px;
    left: 96px;
}

.title_underline {
    width: 304px;
    border-bottom: 1px solid #c7c2c2;
    position: absolute;
    top: 55px;
    left: 80px;
}

.box_container {
    width: 1280px;
    height: auto;
    position: relative;
    top: 56px;
    left: 80px;
    overflow: hidden;
}

.box {
    width: 301px;
    height: 44px;
    border: 1.5px solid #e1dcdc;
    border-radius: 13px;
    background-color: white;
    float: left;
    margin: 0 16px 13px 0;
    cursor: pointer;
    font-size: 16px;
    line-height: 44px;
    font-weight: 400;
    letter-spacing: 1.25px;
    text-indent: 69.67px;
    user-select: none;
}
</style>