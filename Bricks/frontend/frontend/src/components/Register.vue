<template>
  <div>
    <div class="header cov">
      <div class="logo"><img src="../assets/brickslogo.png" alt="" /></div>
      <div class="topright">
        <div><a href="../components/Homepage.vue">回首頁</a></div>
      </div>
    </div>
    <div class="middle cov">
      <p class="title">註冊</p>
      <div class="enter">
        <div class="account box">
          <p>帳號</p>
          <input type="text" placeholder="請輸入(規則)帳號名稱(不可改)" />
        </div>
        <div class="password box">
          <p>密碼</p>
          <input type="password" placeholder="請輸入(規則)密碼" id="password" />
          <button id="eye1"><img src="../assets/eye.png" alt="" /></button>
        </div>
        <div class="repassword box">
          <p>確認密碼</p>
          <input type="password" placeholder="請再次輸入您的密碼" id="repassword" />
          <button id="eye2"><img src="../assets/eye.png" alt="" /></button>
        </div>
        <div class="email box">
          <p>電子信箱</p>
          <input type="email" placeholder="請填寫聯絡用電子信箱(可更改)" />
        </div>
      </div>
      <button class="login">登入</button>
      <div class="already">
        <p>已經有帳戶？</p>
        <a href="./Login.vue">登入</a>
      </div>
      <div class="line">
        <div class="leftline"></div>
        <p>或</p>
        <div class="rightline"></div>
      </div>
      <div class="from_other">
        <a href="https://www.google.com.tw/?hl=zh_TW" class="google">
          <img src="../assets/google.png" alt="" />
          <p>Google登入</p>
        </a>
        <a href="https://www.facebook.com/" class="facebook">
          <img src="../assets/facebook.png" alt="" />
          <p>Facebook登入</p>
        </a>
      </div>
    </div>
  </div>
</template>

<!-- <script>
var passwordinput = document.querySelector("#password");
var repasswordinput = document.querySelector("#repassword");
var eyebtn1 = document.querySelector("#eye1");
var eyebtn2 = document.querySelector("#eye2");
eyebtn1.onclick = function () {
  if (passwordinput.type === "password") {
    passwordinput.type = "text";
  } else {
    passwordinput.type = "password";
  }
};
eyebtn2.onclick = function () {
  if (repasswordinput.type === "password") {
    repasswordinput.type = "text";
  } else {
    repasswordinput.type = "password";
  }
};
</script> -->

<style scoped>
* {
  margin: 0;
  padding: 0;
  font-family: "Noto Sans TC", sans-serif;
}

.cov {
  width: 1920px;
  margin: 0 auto;
}

.header {
  height: 99px;
  overflow: hidden;
  margin-bottom: -14px;
}

.header .logo {
  position: absolute;
  top: 10px;
  left: 80px;
  line-height: 61px;
}

.header img {
  height: 95px;
}

.header .topright {
  height: 49px;
  margin: 24px 61px 27px 0px;
}

.header a {
  position: absolute;
  top: 30px;
  right: 80px;
  width: 111px;
  border: 1px solid #676767;
  line-height: 47px;
  border-radius: 50px;
  text-align: center;
  margin-left: 25px;
  font-size: 20px;
  background-color: white;
  font-weight: 700;
  cursor: pointer;
  text-decoration: none;
  color: #363b3e;
}

.header a:active {
  color: #363b3e;
}

.middle {
  position: relative;
  width: 700px;
  height: 774px;
}

.title {
  width: 110px;
  height: 67px;
  line-height: 67px;
  font-size: 55px;
  position: absolute;
  left: 295px;
}

.enter {
  height: 360px;
  width: 635px;
  position: absolute;
  top: 115px;
  left: 0;
}

.box {
  width: 597px;
  height: 60px;
  margin-bottom: 40px;
}

.enter .email {
  margin-bottom: 0;
}

.enter p {
  position: relative;
  top: 19px;
  font-size: 20px;
  color: #363b3e;
  font-weight: 700;
}

.enter .account p {
  left: 38px;
}

.enter .password p {
  left: 38px;
}

.enter input {
  position: relative;
  top: -26px;
  left: 105px;
  width: 508px;
  height: 58px;
  border: 1px solid #bfbfbf;
  border-radius: 10px;
  font-size: 20px;
  padding-left: 20px;
}

.enter button {
  position: relative;
  top: -18px;
  left: 47px;
  border: none;
  background-color: white;
  cursor: pointer;
}

.login {
  width: 528px;
  height: 48px;
  border: 1px solid #9a2b2e;
  border-radius: 50px;
  background-color: #9a2b2e;
  cursor: pointer;
  font-size: 20px;
  color: white;
  line-height: 48px;
  position: absolute;
  top: 520px;
  left: 105px;
}

.already {
  width: 170px;
  height: 24px;
  position: absolute;
  top: 590px;
  left: 285px;
  margin-bottom: 66px;
}

.already p {
  font-size: 20px;
  line-height: 24px;
  float: left;
  color: #676767;
}

.already a {
  font-size: 20px;
  line-height: 24px;
  color: #1977f3;
  text-decoration: none;
  float: right;
}

.line .leftline {
  position: absolute;
  left: 40px;
  top: 672px;
  border-bottom: 2px solid #bcbcbc;
  width: 315px;
  height: 1px;
}

.line p {
  position: absolute;
  top: 660px;
  left: 360px;
  font-size: 20px;
  color: #676767;
}

.line .rightline {
  position: absolute;
  top: 672px;
  left: 385px;
  border-bottom: 2px solid #bcbcbc;
  width: 315px;
  height: 1px;
}

.from_other {
  width: 530px;
  height: 60px;
  position: absolute;
  top: 714px;
  left: 105px;
}

.from_other a {
  width: 248px;
  height: 58px;
  border: 1px solid #bfbfbf;
  border-radius: 10px;
  font-size: 20px;
  line-height: 58px;
  text-decoration: none;
  color: #676767;
  overflow: hidden;
}

.from_other img {
  height: 35px;
  width: 35px;
  margin: 13px 85px 12px 30px;
}

.from_other p {
  display: inline-block;
  position: relative;
  top: -83px;
  left: 100px;
}

.google {
  float: left;
}

.facebook {
  float: right;
}

.facebook p {
  left: 90px;
}

.from_other a:active {
  color: #676767;
}
</style>
