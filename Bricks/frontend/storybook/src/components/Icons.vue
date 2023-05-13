<template lang="pug">
embed(:src="svgPath" :style="style" :class="classes")
</template>

<script>
import { Icons } from "./Icons.js";
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
        return ["white", "black"].indexOf(c) !== -1;
      },
    },
    name: {
      type: String,
      validator: function(value) {
        return Icons.indexOf(value) !== -1;
      }
    }
  },
  computed: {
    colorhex: function() {
      return Colors[this.color];
    },
    svgPath: function() {
      return require(`../assets/Icons-${this.size}/${this.name}.svg`);
    },
    classes() {
      return {
        'my-icon': true,
        [`my-icon--name-${this.name}`]: true,
        [`my-icon--size-${this.size}`]: true,
      };
    },
    style() {
      if (this.color == "white") {
        return {
          filter: `invert(100%)`
        };
      }
      return {
        filter: `invert(0%)`
      };
    }
  }

};

</script>