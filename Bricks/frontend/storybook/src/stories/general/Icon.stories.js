import { Controls } from '@storybook/blocks';
import MyIcon from '../../components/Icon.vue';
import IconTemplate from './Icon.storytemplate.pug'
import IconNames from "../../components/Icon.json";

// More on how to set up stories at: https://storybook.js.org/docs/vue/writing-stories/introduction
export default {
  title: 'General 通用/Icon 圖標',
  component: MyIcon,
  tags: ['autodocs'],

  render: (args, { argTypes }) => ({
    props: Object.keys(argTypes),
    components: { MyIcon },
    template: IconTemplate,
  }),

  argTypes: {
    name: {
      control: { type: 'select' },
    },
    size: {
    },
  },
};

export const facebook = {
  args: {
    name: 'facebook',
  },
};