<template>
    <div>
        <div class="nav">
            <a href="">
                <img src="../assets/brickslogo.svg" alt="">
            </a>
            <div class="tribtn">
                <div class="btn">試用</div>
                <div class="btn" style="background-color: #b82c30; border-color: #b82c30; color: #ffffff;">登入</div>
                <div class="btn" style="margin-right: 0px;">註冊</div>
            </div>
        </div>
        <div class="bg">
            <div class="middle" style="background-color: antiquewhite;">
                <p class="title">註冊</p>
                <div class="enter">
                    <input required autofocus class="account" placeholder="請輸入 (規則) 帳號名稱 (後續無法更改)" style="margin-top: 0px;">
                    <div class="wrong"></div>
                    <input v-if="showpassword_1" required class="password" type="text" placeholder="請輸入 (規則) 密碼">
                    <input v-else required class="password" type="password" placeholder="請輸入 (規則) 密碼">
                    <img class="eye1" v-if="showpassword_1" id="eye_on" src="../assets/eye/eye_on.svg" alt="" @click="eyebtn_1">
                    <img class="eye1" v-else id="eye_off" src="../assets/eye/eye_origin.svg" alt="" @click="eyebtn_1">
                    <div class="wrong"></div>
                    <input v-if="showpassword_2" required class="password" type="text" placeholder="請再次輸入密碼">
                    <input v-else required class="password" type="password" placeholder="請再次輸入密碼">
                    <img class="eye2" v-if="showpassword_2" id="eye_on" src="../assets/eye/eye_on.svg" alt="" @click="eyebtn_2">
                    <img class="eye2" v-else id="eye_off" src="../assets/eye/eye_origin.svg" alt="" @click="eyebtn_2">
                    <div class="wrong"></div>
                    <input required type="text" class="email" placeholder="請填寫聯絡用電子信箱 (可更改)">
                    <div class="wrong"></div>
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
    name: 'Login_2',
    data() {
        return {
            showpassword_1: false,
            showpassword_2: false,
        };
    },
    methods: {
        eyebtn_1() {
            this.showpassword_1 = !this.showpassword_1;
        },
        eyebtn_2() {
            this.showpassword_2 = !this.showpassword_2;
        },
    },
    created() {

    }
}
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
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
}


.bg {
    background-image: url(../assets/bricks_bg.svg);
}

@media screen and (min-width: 1920px) {
    .middle {
        width: 576px;
        height: 846px;
        position: absolute;
        top: 105px;
        left: 50%;
        transform: translate(-50%);
    }

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
    .middle {
        width: 470px;
        height: 846px;
        position: absolute;
        top: 105px;
        left: 50%;
        transform: translate(-50%);
    }

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
    .middle {
        width: 416px;
        height: 846px;
        position: absolute;
        top: 105px;
        left: 50%;
        transform: translate(-50%);
    }

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

.enter {
    width: 100%;
    height: 364px;
    position: absolute;
    top: 202px;
    background-color: #c7c2c2;
}

input {
    width: 99.8%;
    height: 45px;
    border: 1.5px solid #c7c2c2;
    border-radius: 12px;
    font-size: 18px;
    font-family: 'Noto Sans TC';
    font-weight: 500;
    letter-spacing: 1.25px;
    text-indent: 33.5px;
    margin-top: 21px;
}

input::placeholder {
    color: #b6aeae;
}

.wrong {
    margin-top: 6px;
    width: 92%;
    height: 22px;
}

.enter img {
    position: absolute;
    right: 28px;
    height: 24px;
    cursor: pointer;
    z-index: 90;
    user-select: none;
}

.eye1{
    top: 106px;
}

.eye2{
    top: 205px;
}

.title {
    width: 100%;
    height: 182px;
    font-size: 58px;
    text-align: center;
    font-family: 'Noto Sans TC';
    letter-spacing: -0.5px;
    font-weight: 400;
    line-height: 182px;
    user-select: none;
}

.bottom {
    width: 100vw;
    height: 65px;
    position: fixed;
    bottom: 0px;
    box-shadow: 0px -4px 8px rgba(0, 0, 0, 0.1);
}

.privacy {
    width: 116px;
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