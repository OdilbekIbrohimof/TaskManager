// ========================================
// ==================Time==================
// ========================================
const months = [
  "yanvar",
  "fevrel",
  "mart",
  "aprel",
  "may",
  "iyun",
  "iyul",
  "avgust",
  "sentabr",
  "oktabr",
  "noyabr",
  "dekabr",
];
function load() {
  let nowDay = document.querySelector(".now-day-js");
  let nowHour = document.querySelector(".now-hour-js");
  let nowMinute = document.querySelector(".now-minute-js");
  let nowSecond = document.querySelector(".now-second-js");
  let newDate = new Date();

  let day = newDate.getDate();
  let monthNumber = newDate.getMonth();
  let hour = newDate.getHours();
  let minute = newDate.getMinutes();
  let second = newDate.getSeconds();

  nowDay.textContent = `${day}-${months[monthNumber]}`;
  nowHour.textContent = `${(hour = hour < 10 ? "0" + hour : hour)} :`;
  nowMinute.textContent = `${(minute = minute < 10 ? "0" + minute : minute)} :`;
  nowSecond.textContent = `${(second = second < 10 ? "0" + second : second)}`;
}

setInterval(load, 999);

// ========================================
// ===========Calendar js==================
// ========================================
const currentDate = document.querySelector(".current-date");
const daysTag = document.querySelector(".days");
const prevNextIcon = document.querySelectorAll(".prev-next-icon");

let date = new Date();
let currYear = date.getFullYear();
let currMonth = date.getMonth();

const renderCalendar = () => {
  let firstDayOfMonth = new Date(currYear, currMonth, 1).getDay();
  let lastDateOfMonth = new Date(currYear, currMonth + 1, 0).getDate();
  let lastDayOfMonth = new Date(currYear, currMonth, lastDateOfMonth).getDay();
  let lastDateOfLastMonth = new Date(currYear, currMonth, 0).getDate();
  let liTag = "";

  for (let i = firstDayOfMonth; i > 0; i--) {
    liTag += `<li class="inactive">${lastDateOfLastMonth - i + 1}</li>`;
  }

  for (let i = 1; i <= lastDateOfMonth; i++) {
    let isToday =
      i === date.getDate() &&
      currMonth === new Date().getMonth() &&
      currYear === new Date().getFullYear()
        ? "active"
        : "";
    liTag += `<li class="${isToday}">${i}</li>`;
  }

  for (let i = lastDayOfMonth; i < 6; i++) {
    liTag += `<li class="inactive">${i - lastDayOfMonth + 1}</li>`;
  }

  currentDate.innerHTML = `${currYear} ${months[currMonth]} oyi`;
  daysTag.innerHTML = liTag;
};

renderCalendar();

prevNextIcon.forEach((icon) => {
  icon.addEventListener("click", () => {
    currMonth = icon.id === "prev" ? currMonth - 1 : currMonth + 1;

    if (currMonth < 0 || currMonth > 11) {
      date = new Date(currYear, currMonth);
      currYear = date.getFullYear();
      currMonth = date.getMonth();
    } else {
      date = new Date();
    }
    renderCalendar();
  });
});