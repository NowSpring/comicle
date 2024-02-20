module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ["plugin:vue/vue3-essential", "eslint:recommended"],
  parserOptions: {
    parser: "@babel/eslint-parser",
  },
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    "vue/html-self-closing": "off",
    /* tslint:disable:no-empty */
    // "no-empty": "off",
    "no-empty-function": "off",
    "vue/no-multiple-template-root": "off",
    "vue/multi-word-component-names": 0,
  },
};
