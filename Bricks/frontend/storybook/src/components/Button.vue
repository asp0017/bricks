<template>
<div :class="classes" @click="onClick" :style="style" tabindex="0" :disabled="disabled">
  <my-icon v-if="icon" :name="icon" :size="iconsize" :color="iconcolor"></my-icon>
  <span v-if="label">{{label}}</span>
</div>
</template>

<script>

import MyIcon from "./Icons.vue";
import { Icons } from "./Icons.js";

export default {
  name: 'my-button',
  components: { MyIcon },
  props: {
    label: { 
      type: String,
      default: '',
    },
    icon: {
      type: String,
      validator: function (value) {
        return Icons.indexOf(value) !== -1;
      },
    },
    theme: {
      type: String,
      default: 'filled',
      validator: function (value) {
        return ['filled', 'outline', 'floating', 'flat'].indexOf(value) !== -1;
      },
    },
    size: {
      type: String,
      default: 'medium',
      validator: function (value) {
        return ['small', 'medium', 'large'].indexOf(value) !== -1;
      },
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },

  computed: {
    classes() {
      return {
        'my-button': true,
        [`my-button--theme-${this.theme}`]: true,
        [`my-button--size-${this.size}`]: true,
        'my-button--icon-only': this.icon && !this.label,
        'my-button--label-only': !this.icon && this.label,
        'my-button--icon-label': this.icon && this.label,
      };
    },
    style() {
      return {
      };
    },
    iconsize() {
      switch (this.size) {
        case 'small':
          return 16;
        case 'medium':
          return 16;
        case 'large':
          return 24;
      }
    },
    iconcolor() {
      switch (this.theme) {
        case 'filled':
          return 'white';
        case 'outline':
          return 'black';
        case 'floating':
          return 'white';
        case 'flat':
          return 'black';
      }
    },
  },

  methods: {
    onClick() {
      this.$emit('onClick');
    },
  },
};
</script>

<style scoped lang="sass">
@import 'colors'
@import 'font'

.my-button
  cursor: pointer
  display: inline-flex
  align-items: center
  vertical-align: middle

  span
    margin: 0

.my-button--size-large
  padding: 8px 20px 
  font-size: 18px
  line-height: 32px
  border-radius: 14px

.my-button--size-medium
  padding: 6px 18px
  font-size: 16px
  line-height: 29px
  border-radius: 12px

.my-button--size-small
  padding: 4px 16px
  font-size: 14px
  line-height: 25px
  border-radius: 10px
  img
    width: 16px
    height: 16px

.my-button--icon-only
  &.my-button--size-large
    padding: 12px 
  &.my-button--size-medium
    padding: 8.5px
  &.my-button--size-small
    padding: 8.5px

.my-button--theme-floating
  &.my-button--size-large
    padding: 8px 24px 
    border-radius: 24px
  &.my-button--size-medium
    padding: 6px 22px
    border-radius: 20px
  &.my-button--size-small
    padding: 4px 20px
    border-radius: 16px

.my-button--theme-floating.my-button--icon-only
  &.my-button--size-large
    padding: 12px 
  &.my-button--size-medium
    padding: 8.5px
  &.my-button--size-small
    padding: 8.5px

.my-button--icon-label
  span
    margin-left: 12px


.my-button--theme-filled
  background-color: $bricks-red
  border: 0
  span
    color: $white
.my-button--theme-filled:hover
  background-color: $red400
.my-button--theme-filled:active
  background-color: $red700
.my-button--theme-filled:focus:not(:active)
  box-shadow: 0px 4px 8px 0px #00000066
.my-button--theme-filled:disabled
  background-color: $normal-grey


.my-button--theme-outline
  background-color: $white
  border: 1px solid $red1000
.my-button--theme-outline:hover
  background-color: $light-grey
.my-button--theme-outline:active
  background-color: $red200
  border: 1.5px solid $red1000
.my-button--theme-outline:focus:not(:active)
  background-color: $white
  border: 1px solid $bricks-red
.my-button--theme-outline:disabled
  border: 1px solid $normal-grey
  color: $normal-grey

.my-button--theme-flat
  @extend .my-button--theme-outline
  border: none
  &:active
    border: none
  &:focus:not(:active)
    border: 1px solid $bricks-red

.my-button--theme-floating
  @extend .my-button--theme-filled
  box-shadow: 0px 4px 8px 0px #00000066
</style>