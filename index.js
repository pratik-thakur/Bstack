const express = require("express");
const app = express();
const router = new express.Router();
const open = require("open");
const fkill = require("fkill");
const { ProcessName, ProcessNameConstants } = require("process-name");

// const browser = require("browser");
// const getCurrentTabUrl = require("get-current-tab-url");
// getCurrentTabUrl().then((url) => console.log(url));

router.get("/start", async (req, res) => {
  await open(req.query.url, { app: { name: req.query.browser } });
  console.log("Browser started");
  res.send("Browser started");
});

router.get("/stop", async (req, res) => {
  if (req.query.browser === "chrome") {
    chrome();
  } else {
    firefox();
  }
  console.log("Browser stopped");
  res.send("Browser Stopped");
});

router.get("/geturl", async (req, res) => {
  // const gettingCurrent = browser.tabs;
  // console.log(gettingCurrent);
  //   getCurrentTabUrl().then((url) => console.log(url));
  //   res.send("Get URL");
});

router.get("/cleanup", async (req, res) => {
  res.send("browser Cleaned");
});

const chrome = async (force) => {
  const {
    BROWSERS: { CHROME },
  } = ProcessNameConstants;
  const procName = ProcessName.BROWSERS[CHROME][process.platform];
  return await fkill(procName, { force: force || true });
};

const firefox = async (force) => {
  const {
    BROWSERS: { FIREFOX },
  } = ProcessNameConstants;
  const procName = ProcessName.BROWSERS[FIREFOX][process.platform];
  return await fkill(procName, { force: force || true });
};

app.use(express.json());
app.use(router);

app.listen(4000, () => {
  console.log("Server is up on port 4000");
});
