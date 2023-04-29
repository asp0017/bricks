const path = require('path');

module.exports = async ({ config }) => {
  // 添加對 Pug 和 Sass 的支持
  config.module.rules.push(
    {
      test: /\.sass$/,
      use:[
        require.resolve('vue-style-loader'),
        require.resolve('css-loader'),
        {
          loader: require.resolve('sass-loader'),
          options: {
            sassOptions: {
              indentedSyntax: true// 使用縮排語法
            }
          }
        }
      ],
    },
    {
      test: /\.pug$/,
      oneOf: [
        {
          exclude: /\.vue$/,
          use:[
              'raw-loader',
              'pug-plain-loader'
          ]
        },
        {
          use: 'vue-pug-loader'
        }
      ]
    },
    {
      test: /\.(png|jpe?g|gif)$/i,
      use: [
        {
          loader: "file-loader",
        },
      ],
    },
  );

  // 解析文件擴展名
  config.resolve.extensions.push('.pug', '.sass');

  // 返回修改後的配置
  return config;
};
