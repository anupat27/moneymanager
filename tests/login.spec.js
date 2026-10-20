

const { test, expect } = require('@playwright/test');

test('1. Login page loads correctly', async ({ page }) => {
  await page.goto('/accounts/login/');

  await expect(
    page.getByRole('heading', { name: /login/i })
  ).toBeVisible();

  await expect(page.getByLabel(/username/i)).toBeVisible();
  await expect(page.getByLabel(/password/i)).toBeVisible();
});

test('2. Invalid login displays an error', async ({ page }) => {
  await page.goto('/accounts/login/');

  await page.getByLabel(/username/i).fill('invalid_user_123');
  await page.getByLabel(/password/i).fill('WrongPassword123!');
  await page.getByRole('button', { name: /log in/i }).click();

  await expect(
    page.getByText(/correct username and password/i)
  ).toBeVisible();
});

test('3. Empty login does not authenticate', async ({ page }) => {
  await page.goto('/accounts/login/');

  await page.getByLabel(/username/i).fill('');
  await page.getByLabel(/password/i).fill('');
  await page.getByRole('button', { name: /log in/i }).click();

  await expect(page).toHaveURL(/accounts\/login/);
});

test('4. Login page remains accessible after refresh', async ({ page }) => {
  await page.goto('/accounts/login/');
  await page.reload();

  await expect(
    page.getByRole('heading', { name: /login/i })
  ).toBeVisible();

  await expect(page.getByLabel(/username/i)).toBeVisible();
});

