<template>
    <div>
        <div class="nav">
            <a href="./homepage_2">
                <img src="../assets/brickslogo.svg" alt="">
            </a>
            <div class="tribtn">
                <a href="" class="btn">試用</a>
                <a href="./login_2" class="btn nav_login_btn"
                    style="background-color: #b82c30; border-color: #b82c30; color: #ffffff;">登入</a>
                <a href="./register_2" class="btn" style="margin-right: 0px;">註冊</a>
            </div>
        </div>
        <div class="bg">
            <div class="middle">
                <p class="title">註冊</p>
                <div class="select">
                    <div class="card" style="margin-top: 0px;">
                        <p>一、使用 BRICKS 的用途 (多選)</p>
                        <div class="multiple_select">
                            <input type="checkbox" id="one_one" name="one">
                            <label for="one_one" style="margin-left: 0px;">課堂作業</label>
                            <input type="checkbox" id="one_two" name="one">
                            <label for="one_two">營隊</label>
                            <input type="checkbox" id="one_three" name="one">
                            <label for="one_three">社團</label>
                            <input type="checkbox" id="one_four" name="one">
                            <label for="one_four" style="margin-left: 0px;">個人筆記</label>
                            <input type="checkbox" id="one_five" name="one">
                            <label for="one_five">競賽</label>
                            <input type="checkbox" id="one_six" name="one">
                            <label for="one_six">其它</label>
                        </div>
                    </div>
                    <div class="card">
                        <p>二、您的身分 (單選)</p>
                        <div class="multiple_select">
                            <input type="radio" id="two_one" name="two">
                            <label for="two_one" style="margin-left: 0px; width: 276px;">高中職 (含) 以下</label>
                            <input type="radio" id="two_two" name="two">
                            <label for="two_two" style="margin-left: 20.5px; width: 276px;">大專院校</label>
                            <input type="radio" id="two_three" name="two">
                            <label for="two_three" style="margin-left: 0px;">碩士</label>
                            <input type="radio" id="two_four" name="two">
                            <label for="two_four">博士</label>
                            <input type="radio" id="two_five" name="two">
                            <label for="two_five">社會人士</label>
                        </div>
                    </div>
                    <div class="card">
                        <p>三、是否用過其餘專案軟體工具 (多選)</p>
                        <div class="multiple_select">
                            <input type="checkbox" id="three_one" name="three">
                            <label for="three_one" style="margin-left: 0px;">Google 雲端</label>
                            <input type="checkbox" id="three_two" name="three">
                            <label for="three_two">Notion</label>
                            <input type="checkbox" id="three_three" name="three">
                            <label for="three_three">Trello</label>
                            <input type="checkbox" id="three_four" name="three">
                            <label for="three_four" style="margin-left: 0px;">Evernote</label>
                            <input type="checkbox" id="three_five" name="three">
                            <label for="three_five">Asana</label>
                            <input type="checkbox" id="three_six" name="three">
                            <label for="three_six">其它</label>
                        </div>
                    </div>
                </div>
                <div class="next">
                    <a href="" class="skip">
                        <div>略過問卷</div>
                    </a>
                    <a href="" class="complete">
                        <div style="background-color: #b82c30; color: white;" @click="complete_btn">完成</div>
                    </a>
                </div>
            </div>
        </div>
        <div class="bottom">
            <a href="" class="privacy"># <span style="text-decoration: underline;">隱私權政策</span></a>
            <a href="" class="contact"># 聯絡我們 <span style="color: #b6aeae;">bricks@gmail.com</span></a>
            <div class="photo"># Photo by <a href="https://unsplash.com/@charlesdeluvio">charlesdeluvio</a> on Unsplash
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Register_second',
    // props: {
    //     email,
    //     password
    // },
    data() {
        return {

        };
    },
    methods: {
        complete_btn() {
            console.log(userId());
            // console.log(this.password);
        }
    },
    computed: {
        userId() {
            return this.$route.params.id
        }
    },
    created() {

    },
}
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    font-family: 'Noto Sans TC';
}

.nav {
    width: 100vw;
    height: 65px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.nav img {
    height: 32.06px;
    width: auto;
    position: absolute;
    top: 16.47px;
    left: 5.21%;
}

.tribtn {
    width: 284px;
    height: 41px;
    position: absolute;
    top: 12px;
    right: 5.21%;
}

.btn {
    width: 76px;
    height: 39px;
    border: 1px solid #120405;
    background-color: white;
    border-radius: 10px;
    float: left;
    margin-right: 25px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    line-height: 39px;
    font-family: 'Noto Sans TC';
    text-align: center;
    letter-spacing: 1.25px;
    user-select: none;
    text-decoration: none;
    color: black;
}

.btn:hover {
    background-color: rgba(242, 238, 238, 1);
}

.nav_login_btn:hover {
    background-color: rgba(212, 128, 131, 1) !important;
}

.bg {
    background-image: url(../assets/bricks_bg.svg);
}

.middle {
    width: 576px;
    height: 739px;
    position: absolute;
    top: 105px;
    left: 50%;
    transform: translate(-50%);
}

@media screen and (min-width: 1920px) {
    .bg {
        height: 950px;
    }

    .privacy {
        left: 540px;
    }

    .contact {
        left: 688px;
    }

    .photo {
        right: 540px;
    }
}


@media screen and (min-width: 1600px) and (max-width: 1920px) {
    .bg {
        height: 950px;
    }

    .privacy {
        left: 380px;
    }

    .contact {
        left: 528px;
    }

    .photo {
        right: 380px;
    }
}

@media screen and (max-width: 1600px) {
    .bg {
        height: 770px;
    }

    .privacy {
        left: 300px;
    }

    .contact {
        left: 448px;
    }

    .photo {
        right: 300px;
    }
}

.title {
    width: 100%;
    height: 112px;
    font-size: 33px;
    text-align: center;
    font-family: 'Noto Sans TC';
    letter-spacing: 0.25px;
    font-weight: 700;
    line-height: 112px;
    user-select: none;
}

.select {
    width: 100%;
    height: 523px;
    margin-top: 32px;
}

.card {
    width: 100%;
    height: 153px;
    margin-top: 32px;
}

.card>p {
    height: 23px;
    font-size: 19px;
    letter-spacing: 0.15px;
    font-weight: 700;
    line-height: 23px;
    position: relative;
    top: 8px;
}

.multiple_select {
    width: 130%;
    height: 90px;
    position: relative;
    top: 32px;
}

.card input[type="checkbox"] {
    display: none;
}

.card input[type="radio"] {
    display: none;
}

.card input[type="checkbox"]+label {
    display: inline-block;
    background-color: white;
    cursor: pointer;
    width: 174px;
    height: 39px;
    border: 1px solid #b6aeae;
    border-radius: 12px;
    color: #3b3838;
    font-size: 16px;
    font-weight: 500;
    letter-spacing: 1.25px;
    line-height: 39px;
    text-align: center;
    user-select: none;
    margin-left: 24.5px;
    margin-bottom: 10px;
}

.card input[type="radio"]+label {
    display: inline-block;
    background-color: white;
    cursor: pointer;
    width: 174px;
    height: 39px;
    border: 1px solid #b6aeae;
    border-radius: 12px;
    color: #3b3838;
    font-size: 16px;
    font-weight: 500;
    letter-spacing: 1.25px;
    line-height: 39px;
    text-align: center;
    user-select: none;
    margin-left: 24.5px;
    margin-bottom: 10px;
}

.card input[type="checkbox"]:hover+label {
    background-color: #f2eeee;
}

.card input[type="radio"]:hover+label {
    background-color: #f2eeee;
}

.card input[type="checkbox"]:active+label {
    background-color: #f1d5d6;
}

.card input[type="radio"]:active+label {
    background-color: #f1d5d6;
}

.card input[type="checkbox"]:checked+label {
    background-color: #f1d5d6;
}

.card input[type="radio"]:checked+label {
    background-color: #f1d5d6;
}


.next {
    width: 100%;
    height: 48px;
    position: relative;
    top: 24px;
}

.next a div {
    width: 262px;
    height: 46px;
    border: 1px solid #b6aeae;
    border-radius: 14px;
    background-color: white;
    font-size: 18px;
    line-height: 46px;
    text-align: center;
    letter-spacing: 1.25px;
    font-weight: 500;
}

.skip {
    float: left;
    color: #b6aeae;
    text-decoration: none;
}

.skip div:hover {
    background-color: #f2eeee;
}

.skip div:active {
    background-color: #f1d5d6;
}

.complete {
    float: right;
    border-color: #b82c30;
    text-decoration: none;
}

.complete div:hover {
    background-color: #d48083 !important;
}

.complete div:active {
    background-color: #932326 !important;
}

.bottom {
    width: 100vw;
    height: 65px;
    position: fixed;
    bottom: 0px;
    box-shadow: 0px -4px 8px rgba(0, 0, 0, 0.1);
    background-color: white;
}

.privacy {
    width: 116px;
    height: 112px;
    font-size: 19px;
    font-family: 'Noto Sans TC';
    line-height: 112px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    letter-spacing: 0.15px;
    cursor: pointer;
    color: #120406;
    text-decoration: none;
}

.contact {
    width: 271px;
    height: 23px;
    font-size: 19px;
    font-family: 'Noto Sans TC';
    line-height: 23px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    letter-spacing: 0.15px;
    cursor: pointer;
    color: #120406;
    text-decoration: none;
}

.photo {
    width: 357px;
    height: 23px;
    font-size: 19px;
    font-family: 'Noto Sans TC';
    line-height: 23px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    letter-spacing: 0.15px;
    color: #c7c2c2;
}

.photo a {
    color: #c7c2c2;
}
</style>