// Needs to be JS and in CJS format; will be run during webpack config
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
  console.log('process.env.REACT_APP_PROXY', process.env.REACT_APP_PROXY);
  if (process.env.REACT_APP_PROXY) {
    app.use(
      '/api',
      createProxyMiddleware({
        target: process.env.REACT_APP_PROXY,
        changeOrigin: true,
      })
    );
  }
};