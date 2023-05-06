<template lang="pug">
div(:class="classes" @click="onClick" :style="style" tabindex="0")
  my-icon(v-if="icon" :name="icon" :size="iconsize" :color="iconcolor")
  span(v-if="label") {{label}}
</template>

<script>
import "./Button.sass";
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

