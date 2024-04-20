// const eMail = document.querySelector(".inputE");
// const pAss = document.querySelector(".inputP");
// const btn = document.querySelector(".btn");
// const mAin1 = document.querySelector(".main1");
// const mAin2 = document.querySelector(".main2");
// const inputHead = document.querySelector(".input_heading");
// const inputHead2 = document.querySelector(".input_heading2");
// const inputfoot = document.querySelector(".input_footer");
// const Cir1 = document.querySelector(".circle1");
// const Cir2 = document.querySelector(".circle2");
// const About = document.querySelector(".about");
// const Services = document.querySelector(".services");
// const Second = document.querySelector(".second");
// const Imagey = document.querySelector(".imga");
// const Admin = document.querySelector(".admin");
// const UserMain = document.querySelector(".UserMain");
// const Dashboard = document.querySelector(".dash");
// const impCont = document.querySelector(".Imp");
// const Pass = document.querySelector(".Pass");
// const SignOut = document.querySelector(".sign");

// //info
// const account1 = { Id: "krrish_be12@thapar.edu", passW: 12345 };
// const account2 = { Id: "marul_be12@thapar.edu", passW: 23456 };
// const account3 = { Id: "kanav_be12@thapar.edu", passW: 34567 };
// const accounts = [account1, account2, account3];
// const D1 = {
//   key: Dashboard,
//   Func: function () {
//     UserMain.classList.remove("hidden");
//     UserMain.classList.add("flex");
//   },
// };
// const Imp = {
//   key: impCont,
//   Func: function () {},
// };
// const Pa = {
//   key: Pass,
//   Func: function () {},
// };
// const So = {
//   key: SignOut,
//   Func: function () {},
// };
// const selectArr = [D1, Imp, Pa, So];

// //function
// const onFocus = (head) => {
//   head.classList.remove("text-gray-800");
//   head.classList.add("text-white");
// };
// const onBlur = (head) => {
//   head.classList.add("text-gray-800");
//   head.classList.remove("text-white");
// };
// const onFocus2 = (foot) => {
//   foot.classList.remove("text-gray-800");
//   foot.classList.add("text-white");
// };
// const onBlur2 = (foot) => {
//   foot.classList.add("text-gray-800");
//   foot.classList.remove("text-white");
// };
// const HideNSeek = () => {
//   mAin1.classList.add("opacity-0");
//   mAin2.classList.add("opacity-0");

//   setTimeout(HideNSeek2, 1000);
// };
// const HideNSeek2 = () => {
//   mAin1.classList.remove("flex");
//   mAin2.classList.remove("flex");
//   mAin1.classList.add("hidden");
//   mAin2.classList.add("hidden");
//   Admin.classList.remove("hidden");
//   Admin.classList.add("flex");
// };
// const CirclsToggle = () => {
//   Cir1.classList.toggle("bg-white");
//   Cir1.classList.toggle("bg-gray-800");
//   Cir2.classList.toggle("bg-white");
//   Cir2.classList.toggle("bg-gray-800");
// };

// //event handler
// let currentAccount;
// btn.addEventListener("click", function (e) {
//   e.preventDefault();
  
//   currentAccount = accounts.find((acc) => acc.Id === eMail.value);
//   console.log(currentAccount);
//   if (currentAccount?.passW === Number(pAss.value)) {
//     HideNSeek();
//   }
// });
// document.body.addEventListener("keydown", function (e) {
//   currentAccount = accounts.find((acc) => acc.Id === eMail.value);
//   console.log(currentAccount);
//   if (currentAccount?.passW === Number(pAss.value)) {
//     if (e.key === "Enter") {
//       HideNSeek();
//     }
//   }
// });

// eMail.addEventListener("focus", function () {
//   onFocus(inputHead);
// });
// eMail.addEventListener("blur", function () {
//   onBlur(inputHead);
// });
// pAss.addEventListener("focus", function () {
//   onFocus(inputHead2);
//   onFocus2(inputfoot);
// });
// pAss.addEventListener("blur", function () {
//   onBlur(inputHead2);
//   onBlur2(inputfoot);
// });

// Cir1.addEventListener("click", function () {
//   About.style.transform = "translateX(  0px)";
//   About.classList.remove("opacity-0");
//   Services.style.transform = "translateX(0px)";
//   Services.classList.add("opacity-0");
//   CirclsToggle();
// });
// Cir2.addEventListener("click", function () {
//   About.style.transform = "translateX(-20px)";
//   About.classList.add("opacity-0");
//   Services.style.transform = "translateX(-20px)";
//   Services.classList.remove("opacity-0");
//   CirclsToggle();
// });
// selectArr.forEach((el) => {
//   const name = el.key;
//   const display = el.Func;
//   name.addEventListener("click", function (e) {
//     const arr = selectArr.slice();
//     name.classList.add("bg-slate-900");
//     name.classList.add("text-white");
//     name.classList.remove("bg-teal-600");
//     display();
//     arr.splice(arr.indexOf(el), 1);
//     console.log(arr);
//     arr.forEach((ele) => {
//       const name2 = ele.key;
//       console.log(name2);
//       name2.classList.remove("bg-slate-900");
//       name2.classList.add("bg-teal-600");
//       name2.classList.add("text-black");
//       name2.classList.remove("text-white");
//     });
//   });
// });
