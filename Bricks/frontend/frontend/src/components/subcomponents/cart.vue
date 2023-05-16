<template>
    <div class="cart">
        <p class="cart_title">{{ title_word }}</p>
        <img src="../../assets/cart_drag_icon.svg" alt="" class="cart_drag_icon">
        <div class="title_underline"></div>
        <div class="box_container">
            <div class="box" v-for="(proj_name,index) in projects" :key="index">{{ proj_name }}</div>
        </div>
    </div>
</template>
  
<script>
export default {
    data(){
        return{
            projects: [],
        }
    },
    props:{
        title_word: String,
        proj_name: String,
    },
    methods:{
        
    },
};
</script>
  
<style scoped>
*{
    margin: 0;
    padding: 0;
    font-family: 'Noto Sans TC';
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
.cart_title {
    font-size: 16px;
    font-weight: 400;
    line-height: 24px;
    letter-spacing: 0.5px;
    position: relative;
    top: 22px;
    left: 96px;
}
.cart_drag_icon{
    position: relative;
    -webkit-user-drag: none;
    top: -3px;
    left: 32px;
}

.title_underline {
    width: 304px;
    border-bottom: 1px solid #c7c2c2;
    position: relative;
    top: 5px;
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
</style>
  