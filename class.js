const { Builder, Browser, By, Key, until } = require("selenium-webdriver");
const CHROME = require("chromedriver");
(async function example() {
  let driver = new Builder().forBrowser(Browser.CHROME).build();
  try {
    driver.get("https://nftcalendar.io/event/metagoblin-nft-presale/");
    driver.findElement(By.name("q")).sendKeys("webdriver", Key.RETURN);
    driver.wait(until.titleIs("webdriver - Google Search"), 1000);
  } finally {
    //await driver.quit();
  }
})();
