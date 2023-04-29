<template lang="pug">
div(:class="classes" @click="onClick" :style="style" tabindex="0")
  img(v-if="icon" src="../assets/plus24.svg" alt="")
  span(v-if="label") {{label}}
</template>

<script>
import "./Button.sass";

export default {
  name: 'my-button',
  props: {
    label: { 
      type: String,
      default: '',
    },
    icon: {
      type: String,
      default: '',
      validator: function (value) {
        return ['', 'plus'].indexOf(value) !== -1;
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
  },

  methods: {
    onClick() {
      this.$emit('onClick');
    },
  },
};
</script>

