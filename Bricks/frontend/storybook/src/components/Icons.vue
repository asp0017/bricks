<template>
  <component :is="getIcon" />
</template>

<script>
import { Colors, ColorsArray } from "./Colors.js";

export default {
  name: "my-icon",
  props: {
    size: {
      type: Number,
      default: 16,
      validator: function(value) {
        return [16, 24].indexOf(value) !== -1;
      }
    },
    color: {  
      type: String,
      default: "black",
      validator: function(c) {
        return ColorsArray.indexOf(c) !== -1;
      },
    },
    name: {
      type: String,
      required: true,
    },
  },
  computed: {
    colorhex() {
      return Colors[this.color];
    },
    classes() {
      return {
        'my-icon': true,
        [`my-icon--name-${this.name}`]: true,
        [`my-icon--size-${this.size}`]: true,
      };
    },
    style() {
      return {
        stroke: this.colorhex,
      };
    },
    getIcon() {
      return () => import(`../Icons/${this.name}.vue`);
    },
  }
};

</script>