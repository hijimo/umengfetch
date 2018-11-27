/* 注入灵魂 */
/*  干掉 webdriver  */
Object.defineProperty(navigator, 'webdriver', {
  get: () => false,
  configurable: true,
  writable: true,
});
Reflect.deleteProperty(navigator, 'webdriver')

/* 干掉 navigator.chrome */

Object.defineProperty(navigator, 'chrome', {
  get: () => undefined,
  configurable: true,
  writable: true,
});

Reflect.deleteProperty(window, 'chrome')
// 添加 window.chrome
window.navigator.chrome = {
  runtime: {},

};
/*  干掉 permissions */
const originalQuery = window.navigator.permissions.query;
return window.navigator.permissions.query = (parameters) => (
  parameters.name === 'notifications' ?
    Promise.resolve({ state: Notification.permission }) :
    originalQuery(parameters)
);

 /* 干提 navigator.plugins */
Object.defineProperty(navigator, 'plugins', {

  get: () => [1, 2, 3, 4, 5],
});

/* 干掉 languages */
Object.defineProperty(navigator, 'languages', {
  get: () => ['zh-CN', 'zh'],
});