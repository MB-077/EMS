const Dashboard = document.querySelector(".dash");
const impCont = document.querySelector(".Imp");
const set = document.querySelector(".settings");
const Red = document.querySelector(".red");
const Green = document.querySelector(".green");
const right = document.querySelector(".RightSide");
const left = document.querySelector(".leftSide");
const InnerLeft = document.querySelector(".leftSide_inner");
const input = document.querySelector("#inPUt");
const output = document.querySelector("#outPut");
const leaveRequest = document.querySelector(".LeaveReq");
const User = document.querySelector(".userMain");
const pop = document.querySelector(".PopUp");
const D1 = {
  key: Dashboard,
  Func: function () {},
};
const Imp = {
  key: impCont,
  Func: function () {},
};
const Sett = {
  key: set,
  Func: function () {},
};

const selectArr = [D1, Sett, Imp];
selectArr.forEach((el) => {
  const name = el.key;
  console.log(name);

  name.addEventListener("click", function () {
    const arr = selectArr.slice();
    name.classList.add("underline");
    arr.splice(arr.indexOf(el), 1);
    console.log(arr);
    arr.forEach((ele) => {
      const name2 = ele.key;
      name2.classList.remove("underline");
    });
  });
});

const readMe = () => {
  InnerLeft.classList.toggle("hidden");
  left.classList.toggle("w-16");
  left.classList.toggle("w-1/4");
  right.classList.toggle("w-full");
  right.classList.toggle("w-3/4");
};

Red.addEventListener("click", function () {
  readMe();
  Green.classList.remove("hidden");
});

Green.addEventListener("click", function () {
  readMe();
});
input.addEventListener("input", function () {
  output.textContent = this.value + "mins";
});
leaveRequest.addEventListener("click", function () {
  User.style.filter = "blur(10px)";
  pop.classList.remove("hidden");
  pop.classList.add("flex");
});
document.body.addEventListener("keydown", function (e) {
  if (e.key === "Escape") {
    User.style.filter = "blur(0px)";
    pop.classList.add("hidden");
    pop.classList.remove("flex");
  }
});


$(document).ready(function(){
  setInterval(()=>{
      var now = new Date().toLocaleTimeString();
      $('#datetime').text(now);
  }
  , 10);
   
  $('#roomNumber').text('Your Room Number');

  // Current Status Start
  var currentStatus = 'absent'; /* Change current status value here  it will effect all*/
  $('#currentStatus').text(currentStatus);
  $('#currentStatusBox').addClass(currentStatus);
   

  // $('#reliefTime').on('input', function() {
  //     $('#output').text($(this).val() + ' mins');
  // });
});
