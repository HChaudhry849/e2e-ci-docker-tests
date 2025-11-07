import { test, expect } from '@playwright/test';

test('check title on homepage', async ({ page }) => {
  await page.goto('http://web:5000/');
  await expect(page.getByText('Hello, World, from Python!')).toBeVisible();
});
