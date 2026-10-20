
const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  reporter: 'html',
  use: {
    baseURL: 'http://127.0.0.1:8000',
    browserName: 'chromium',
    headless: true,
  },
  webServer: {
    command: 'python manage.py runserver 127.0.0.1:8000',
    url: 'http://127.0.0.1:8000/accounts/login/',
    reuseExistingServer: !process.env.CI,
    timeout: 30000,
  },
});
