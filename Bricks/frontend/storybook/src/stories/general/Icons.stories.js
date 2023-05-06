import { Controls } from '@storybook/blocks';
import MyIcon from '../../components/Icons.vue';
import IconsTemplate from './Icons.storytemplate.pug';


// More on how to set up stories at: https://storybook.js.org/docs/vue/writing-stories/introduction
export default {
  title: 'General 通用/Icons 圖標',
  component: MyIcon,
  tags: ['autodocs'],
  
  render: (args, { argTypes }) => ({
    props: Object.keys(argTypes),
    components: { MyIcon },
    template: IconsTemplate,
  }),

  argTypes: {
    size: {
      control: { type: 'inline-radio' },
    },
    color: {
      control: { type: 'select' },
    },
    name: {
      control: { type: 'select' },
    }
  },
};

export const facebook = {
  args: {
    name: 'facebook',
    size: 16
  },
};