<template lang="pug">
div
  svg(:class="['icon', 'icon-' + name]")
    use(:xlink:href="iconUrl")
  p {{ name }}
</template>

<script>
import IconNames from "./Icon.json";
export default {
  name: "my-icon",
  props: {
    name: {
      type: String,
      validator: function(value) {
        return IconNames.indexOf(value) !== -1;
      }
    },
    size: {
      type: Number,
      default: 16,
      validator: function(value) {
        return [16, 24].indexOf(value) !== -1;
      }
    }
  },
  computed: {
    iconUrl() {
      return "../assets/Icons-" + this.size + "/" + this.name + ".svg";
    }
  }
};

</script>