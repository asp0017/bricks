<template>
    <div>
        <div class="nav">
            <img src="../assets/brickslogo.svg" @click="test_btn">
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
                <input type="radio" id="overview" class="list" name="list" value="option1" v-model="selectOption">
                <label for="overview" @click="change(1)">專案總覽</label>
                <img src="../assets/icon/icon_file.svg" style="top: 26px">
                <input type="radio" id="over" class="list" name="list" value="option2" v-model="selectOption">
                <label for="over" @click="change(2)">已結束專案</label>
                <img src="../assets/icon/icon_over.svg" style="top: 102px">
                <input type="radio" id="trash" class="list" name="list" value="option3" v-model="selectOption">
                <label for="trash" @click="change(3)">垃圾桶</label>
                <img src="../assets/icon/icon_trashcan.svg" style="top: 178px">
            </div>
        </div>
        <div class="add_proj_box" v-show="add_proj_show">
            <div class="close_add_proj_box" @click="add_btn(); close_add_proj()"></div>
            <p class="add_proj_title">新增專案</p>
            <div class="add_proj_pic">
                <img src="../assets/add_proj_pic_plus.svg" class="add_proj_pic_plus">
            </div>
            <input type="text" placeholder="輸入專案名稱" class="add_proj_name" v-model="add_proj_name">
            <div class="add_proj_type" @click="add_proj_type_btn" :style="{background: add_proj_type_arrow, color:proj_type_color}" ref="test">{{proj_type}}</div>
            <div class="add_proj_type_list" v-show="show_add_proj_type_list">
                <div class="add_proj_type_option" @click="type_not_choose">未分類</div>
                <div v-for="(option,index) in add_proj_type_options" :key="index" class="add_proj_type_option" @click="type_choosen(option)">
                    {{ option }}
                </div>
                <div class="add_proj_type_list_line"></div>
                <input type="text" class="add_proj_type_text" placeholder="新增類別" v-model="add_proj_type_text" @keyup.enter="list_add_a_cart">
                <div class="add_proj_type_text_plus" @click="list_add_a_cart"></div>
            </div>
            <div class="add_proj_build" @click="new_project_btn">建立專案</div>
        </div>
        <div class="main_body">
            <div class="bg">
                <!-- 背景透明灰色 -->
                <div class="overlay" v-if="showOverlay"></div>
                <div class="middle">
                    <div class="overview_page" v-show="middle_show_overview_page">
                        <div class="uncategorized cart" ref="uncategorized">
                            <p class="cart_title">未分類</p>
                            <div class="title_underline"></div>
                            <div class="box_container">
                                <div class="box" v-for="(proj_name,index) in uncategorized_projs" :key="index">{{ proj_name }}</div>
                            </div>
                        </div>
                        <div v-for="(cart,index) in carts" :key="index">
                            <cart :title_word="cart.title_word"/>
                        </div>
                        <div class="new_type cart" :class="{'new_type_highlight': isFocused }">
                            <input class="cart_title_input" placeholder="新增類型" @focus="new_type_focus" @blur="new_type_blur" @keyup.enter="add_a_cart" v-model="cart_title_input">
                            <div class="title_underline"></div>
                            <div class="box_container"></div>
                        </div>
                    </div>
                    <div class="over_page" v-show="middle_show_over_page">
                        <div class="uncategorized cart" ref="uncategorized">
                            <p class="cart_title">未分類</p>
                            <div class="title_underline"></div>
                            <div class="box_container">
                                <div class="box" v-for="(proj_name,index) in uncategorized_projs" :key="index">{{ proj_name }}</div>
                            </div>
                        </div>
                        <div v-for="(cart,index) in carts" :key="index">
                            <cart :title_word="cart.title_word"/>
                        </div>
                        <div class="new_type cart" :class="{'new_type_highlight': isFocused }">
                            <input class="cart_title_input" placeholder="新增類型" @focus="new_type_focus" @blur="new_type_blur" @keyup.enter="add_a_cart" v-model="cart_title_input">
                            <div class="title_underline"></div>
                            <div class="box_container"></div>
                        </div>
                    </div>
                    <div class="trash_page" v-show="middle_show_trash_page">
                        <div class="trash_page_middle">
                            <div class="last_30_days">
                                <p class="last_time">近 30 天</p>
                                <div class="time_subline"></div>
                                <img v-if="recover" src="../assets/trash_page/recover_default.svg" alt="" class="recover trash_pic">
                                <img v-else src="../assets/trash_page/recover_active.svg" alt="" class="recover trash_pic" style="cursor: pointer;" @click="recover_project">
                                <img v-if="trashcan" src="../assets/trash_page/trashcan_default.svg" alt="" class="forever_delete trash_pic">
                                <img v-else src="../assets/trash_page/trashcan_active.svg" alt="" class="forever_delete trash_pic" style="cursor: pointer;" @click="forever_delete_project">
                                <div class="trash_box_container">
                                    <div class="trash_box" v-for="(trash_box,index) in trash_boxes" :key="index">
                                        <input type="checkbox" :id="'trash_box-' + index" v-model="checked_trash_box[index]" @change="selected_trash_box(index)">
                                        <label :for="'trash_box-' + index">{{trash_box.text}}</label>
                                    </div>
                                </div>
                            </div>
                            <div class="last_one_year">
                                <p class="last_time">近一年</p>
                                <div class="time_subline"></div>
                                <div class="trash_box_container"></div>
                            </div>
                            <div class="recovered" v-show="recovered">
                                <img src="../assets/recovered_icon.svg" alt="">
                                <p>檔案已還原</p>
                            </div>
                            <div class="forever_delete_confirm" v-show="forever_delete_confirm">
                                <div class="close_forever_delete_confirm" @click="close_forever_delete_confirm"></div>
                                <p class="forever_delete_confirm_first_text">永久刪除專案</p>
                                <img src="../assets/forever_delete_icon.svg" alt="">
                                <p class="forever_delete_confirm_second_text">確定永久刪除專案？刪除後將無法復原</p>
                                <div class="forever_delete_confirm_btn_container">
                                    <button class="forever_delete_confirm_btn forever_delete_confirm_btn_cancel" @click="close_forever_delete_confirm()">取消</button>
                                    <button class="forever_delete_confirm_btn forever_delete_confirm_btn_delete" @click="close_forever_delete_confirm()">刪除</button>
                                </div>
                            </div>
                            <div class="overlay" v-if="showOverlay_trash"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import cart from './subcomponents/cart.vue';
export default {
    name: 'Personal_homepage',
    data() {
        return {
            middle_show_overview_page: false,
            middle_show_over_page: false,
            middle_show_trash_page: true,
            add_proj_show: false,
            showOverlay: false,
            add_proj_type: '',
            isFocused: false,
            carts:[],
            cart_titles: '',
            cart_title_input: '',
            selectOption: 'option1',
            show_add_proj_type_list: false,
            add_proj_type_arrow: '',
            add_proj_type_options: [],
            proj_type: '選擇專案類型',
            proj_type_color: '#b6aeae',
            add_proj_type_text: '',
            add_proj_name: '',
            uncategorized_projs: [],
            porjects: [],
            cart_box_name_list: [],
            trash_boxes: [],
            checked_trash_box: [],
            recover: true,
            trashcan: true,
            recovered: false,
            forever_delete_confirm: false,
            showOverlay_trash: false,
        };
    },
    methods: {
        add_btn() {
            this.add_proj_show = this.add_proj_show === false ? true : false;
            this.showOverlay = !this.showOverlay;
            this.proj_type = '選擇專案類型';
            this.proj_type_color = '#b6aeae';
            this.add_proj_name = '';
            this.forever_delete_confirm = false;
            this.showOverlay_trash = false;
        },
        close_add_proj(){
            this.show_add_proj_type_list = false;
            this.proj_type_color = '#b6aeae';
        },
        // 建立專案的事件
        new_project_btn() {
            this.add_proj_show = this.add_proj_show === false ? true : false;
            this.showOverlay = false;
            this.middle_show_overview_page = true
            this.middle_show_over_page = false
            this.middle_show_trash_page = false
            this.selectOption = 'option1';
            this.show_add_proj_type_list = false;
            this.proj_type_color = '#b6aeae';
            if(this.add_proj_name !== ''){
                if(this.proj_type === '選擇專案類型'|| this.proj_type === '未分類'){
                    this.uncategorized_projs.push(this.add_proj_name);
                    this.add_proj_name = '';
                }
                else if(this.add_proj_type_options.includes(this.proj_type) === true){
                    this.porjects.push(this.add_proj_name);
                    this.add_proj_name = '';
                }
            }
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
        blurSelect() {
            this.$refs.select.blur();
        },
        new_type_focus(){
            this.isFocused = true;
        },
        new_type_blur(){
            this.isFocused = false;
            this.cart_title_input = '';
        },
        add_a_cart(){
            if(this.cart_title_input !==''){
                const cart={
                    title_word: this.cart_title_input,
                };
                this.carts.push(cart);
                this.add_proj_type_options.push(this.cart_title_input)
                this.cart_title_input = '';
            }
        },
        add_proj_type_btn(){
            this.show_add_proj_type_list = this.show_add_proj_type_list === false ? true : false;
            this.add_proj_type_arrow = 'url(../assets/dropdown_arrow/dropdown_arrow_down.svg) no-repeat center right;';
            const div = this.$refs.test;
            const computedStyle = window.getComputedStyle(div);
            const backgroundImage = computedStyle.getPropertyValue('background-image');
            console.log(backgroundImage);
            console.log(this.add_proj_type_arrow)
        },
        type_choosen(option){
            this.show_add_proj_type_list = false;
            this.proj_type = option;
            this.proj_type_color = 'black';
            this.add_proj_type_text = '';
        },
        type_not_choose(){
            this.show_add_proj_type_list = false;
            this.proj_type = '未分類';
            this.proj_type_color = 'black';
            this.add_proj_type_text = '';
        },
        list_add_a_cart(){
            if(this.add_proj_type_text !== ''){
                this.show_add_proj_type_list = false;
                this.proj_type = this.add_proj_type_text;
                this.proj_type_color = 'black';
                this.add_proj_type_text = '';
            }
        },
        test_btn(){
            const trash_box={
                text : '實驗',
            };
            this.trash_boxes.push(trash_box);
        },
        selected_trash_box(index){
            const allFalse = this.checked_trash_box.every(function(element){
                return element === false
            })
            if (allFalse){
                this.recover = true;
                this.trashcan = true;
            }
            else{
                this.recover = false;
                this.trashcan = false;
            }
        },
        recover_project(){
            this.recovered = true;
            setTimeout(() => {
                this.recovered = false;
            }, 1000);
            this.recover = true;
            this.trashcan = true;
        },
        forever_delete_project(){
            this.forever_delete_confirm = true;
            this.showOverlay_trash = true;
        },
        close_forever_delete_confirm(){
            this.forever_delete_confirm =false;
            this.showOverlay_trash = false;
        },
    },
    components: {
        cart
    },
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
    user-select: none;
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
    -webkit-user-drag: none;
    user-select: none;
}

.notice {
    position: absolute;
    right: 45px;
    cursor: pointer;
    -webkit-user-drag: none;
    user-select: none;
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
    user-select: none;
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
    user-select: none;
    cursor: pointer;
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
    outline: #7b7b7b;
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
    line-height: 36px;
    text-indent: 20px;
    color: #b6aeae;
    cursor: pointer;
    user-select: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    background: url(../assets/dropdown_arrow/dropdown_arrow_right.svg) no-repeat center right;
}
.add_proj_type:hover{
    border-color: #7b7b7b;
    background: url(../assets/dropdown_arrow/dropdown_arrow_right_hover.svg) no-repeat center right;
}

.add_proj_type_list{
    width: 214px;
    height: auto;
    padding-top: 8px;
    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.3), 0px 2px 15px rgba(0, 0, 0, 0.15);
    border-radius: 14px;
    position: absolute;
    top: 396px;
    left: 86px;
    z-index: 3;
    background-color: white;
}
.add_proj_type_option{
    width: 100%;
    height: 45px;
    line-height: 45px;
    font-size: 16px;
    font-weight: 500;
    letter-spacing: 1.25;
    text-indent: 16px;
    cursor: pointer;
    color: #3B3838;
    user-select: none;
}
.add_proj_type_option:hover{
    background-color: #F2EEEE;
}
.add_proj_type_list_line{
    height: 7px;
    border-bottom: 2px solid #E1DCDC;
    margin-bottom: 7px;
    user-select: none;
}
.add_proj_type_text{
    height: 45px;
    width: 100%;
    font-size: 16px;
    font-weight: 500;
    letter-spacing: 1.25;
    text-indent: 16px;
    border: none;
    outline: none;
    color: #3B3838;
    user-select: none;
}   
.add_proj_type_text::placeholder{
    color: #3B3838;
}
.add_proj_type_text:hover{
    background-color: #F2EEEE;
}
.add_proj_type_text_plus {
    position: relative;
    width: 9.33px;
    height: 9.33px;
    background-color: transparent;
    border: 1px solid transparent;
    top: -23px;
}

.add_proj_type_text_plus::before,
.add_proj_type_text_plus::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 1px;
    background-color: #120405;
    top: 0px;
    left: 176.83px;
    -webkit-user-drag: none;
    cursor: pointer;
}

.add_proj_type_text_plus::before {
    transform: rotate(90deg);
}

.add_proj_type_text_plus::after {
    transform: rotate(0deg);
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
    z-index: 5;
}

/* 中間的部分 起點 */
.bg {
    width: calc(100vw - 272px);
    height: calc(100vh - 48px);
    position: fixed;
    bottom: 0px;
    right: 0px;
    background-image: url(../assets/bricks_bg_small.svg);
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
.cart{
    width: calc(100% - 10px);
    min-height: 218px;
    background-color: white;
    border-radius: 14px;
    border: 1px solid #e1dcdc;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
}
.uncategorized {
    background-color: #f2eeee;
}

.cart_title {
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
    position: relative;
    top: 34px;
    left: 80px;
}

.box_container {
    width: 1280px;
    height: auto;
    position: relative;
    top: 56px;
    left: 80px;
    overflow: hidden;   
    margin-bottom: 80px;
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
.cart_title_input{
    font-size: 16px;
    font-weight: 400;
    line-height: 24px;
    letter-spacing: 0.5px;
    position: relative;
    top: 22px;
    left: 96px;
    border: none;
    outline: none;
}
.new_type_highlight{
    border: 2px solid #C7C2C2;
}
/* 中間的部分 終點 */

/* 垃圾桶的部分 起點 */
.trash_page_middle{
    width: 100%;
    height: 85vh;
    border: 1px solid #E1DCDC;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    border-radius: 14px;
    background-color: white;
}
.last_30_days{
    width: 1264px;
    min-height:222px;
    margin-top: 40px;
    position: relative;
    left: 80px;
    padding-bottom: 25px;
}
.last_time{
    position: relative;
    height: 44px;
    left: 16px;
    color: #3B3838;
    font-size: 16px;
    letter-spacing: 0.5px;
    line-height: 44px;
    user-select: none;
}
.time_subline{
    width: 304px;
    height: 1px;
    border-bottom: 1px solid #C7C2C2;
    position: relative;
}
.trash_pic{
    -webkit-user-drag: none;
    user-select: none;
}
.recover{
    position: absolute;
    top: 0px;
    right: 68px;
}
.forever_delete{
    position: absolute;
    top: 0px;
    right: 0px;
}
.trash_box_container{
    width: 1280px;
    height: auto;
    position: relative;
    top: 52px;
    overflow: hidden;
    margin-bottom: 0px;
}
.trash_box input[type="checkbox"]{
    display: none;
}
.trash_box input[type="checkbox"] + label{
    width: 301px;
    height: 44px;
    border: 1.5px solid #e1dcdc;
    border-radius: 13px;
    background-color: white;
    float: left;
    margin: 0 16px 25px 0;
    cursor: pointer;
    font-size: 16px;
    line-height: 44px;
    font-weight: 400;
    letter-spacing: 1.25px;
    text-indent: 69.67px;
    user-select: none;
}
.trash_box input[type="checkbox"]:hover + label{
    background-color: #f2eeee;
}
.trash_box input[type="checkbox"]:active + label{
    background-color: #f2eeee;
}
.trash_box input[type="checkbox"]:checked + label{
    background-color: #f2eeee;
}
.last_one_year{
    width: 1264px;
    min-height:242px;
    position: relative;
    top: 50px;
    left: 80px;
}
.recovered{
    width: 399px;
    height: 141px;
    background-color: white;
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.4);
    border-radius: 14px;
    position: absolute;
    top: 30vh;
    left: 529px;
    z-index: 9;
}
.recovered img{
    position: relative;
    top: 32px;
    left: 183.5px;
    -webkit-user-drag: none;
    user-select: none;
}
.recovered p{
    position: relative;
    top: 40px;
    left: 164px;
    font-size: 14px;
    font-weight: 400;
    letter-spacing: 0.25px;
    color: #3B3838;
    user-select: none;
    -webkit-user-drag: none;
}
.forever_delete_confirm{
    width: 412px;
    height: 372px;
    position: absolute;
    top: 20%;
    left: 520px;
    background-color: white;
    border: 1.5px solid #C7C2C2;
    box-shadow: 0px 0px 5px 1px rgba(65, 65, 65, 0.25);
    border-radius: 14px;
    z-index: 8;
}
.forever_delete_confirm_first_text{
    width: 156px;
    height: 28px;
    position: relative;
    top: 28px;
    left: 50%;
    transform: translate(-50%);
    font-size: 26px;
    font-weight: 700;
    line-height: 28px;
    user-select: none;
}
.close_forever_delete_confirm {
    position: relative;
    width: 12px;
    height: 12px;
    cursor: pointer;
    top: 25px;
    left: 375px;
}

.close_forever_delete_confirm::before,
.close_forever_delete_confirm::after {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    width: 1.5px;
    height: 17px;
    background-color: black;
}

.close_forever_delete_confirm::before {
    transform: translate(-50%, -50%) rotate(45deg);
}

.close_forever_delete_confirm::after {
    transform: translate(-50%, -50%) rotate(-45deg);
}
.forever_delete_confirm img{
    -webkit-user-drag: none;
    user-select: none;
    position: relative;
    top: 56px;
    left: 50%;
    transform: translate(-50%);
}
.forever_delete_confirm_second_text{
    position: relative;
    color: #3B3838;
    font-weight: 400;
    font-size: 14px;
    height: 21px;
    line-height: 21px;
    letter-spacing: 0.25px;
    user-select: none;
    top: 83px;
    left: 50%;
    transform: translate(-50%);
    width: 243px;
}
.forever_delete_confirm_btn_container{
    width: 332px;
    height: 48px;
    position: relative;
    top: 108px;
    left: 50%;
    transform: translate(-50%);
}
.forever_delete_confirm_btn{
    width: 150px;
    height: 48px;
    border-radius: 14px;
    cursor: pointer;
    background-color: #B82C30;
    color: white;
    font-size: 18px;
    letter-spacing: 1.25px;
    font-weight: 500;
    line-height: 48px;
    border: none;
    float: right;
    user-select: none;
}
.forever_delete_confirm_btn_cancel{
    background-color: white;
    color: #120405;
    float: left !important;
}
/* 垃圾桶的部分 終點 */
</style>