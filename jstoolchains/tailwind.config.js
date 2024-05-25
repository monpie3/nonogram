/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./../**/templates/**/*.{html,js}", "./../static/js/**/*.js"],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
    require('flowbite/plugin')
  ],
};
