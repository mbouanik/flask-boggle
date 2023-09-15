const form = $("#form");
const input = $("#word");
const notification = $("#notification");
const score = $("#score");
const button = $("button");
const timer = $("#timer");

notification.hide();
setTimeout(() => {
  input.prop("disabled", true);
  button.prop("disabled", true);
}, 60000);

setInterval(() => {
  if (parseInt(timer.html()) > 0) {
    timer.html(`${parseInt(timer.html()) - 1}`);
  }
}, 1000);

console.log(notification);
form.on("submit", (evt) => {
  evt.preventDefault();
  console.log(input.val());
  checkValidWord(input.val().length);
  input.val("");
  setTimeout(() => {
    notification.slideUp(500);
  }, 2000);
});

async function checkValidWord(len) {
  const res = await axios.post("/check_valid_word/", {
    word: input.val(),
  });

  console.log(res.data);
  notification.removeClass("good bad");
  notification.hide();
  if (res.data["result"] == "ok") {
    notification.html(`Word found`);
    notification.toggleClass("good");
    notification.show(700);
    console.log(score.html());
    score.html(`${parseInt(score.html()) + len}`);
  } else if (res.data["result"] == "not-on-board") {
    notification.html("Not on the Board");
    notification.toggleClass("bad");
    notification.show(700);
  } else {
    notification.html("Not a Word");
    notification.toggleClass("bad");
    notification.show(700);
  }
}

// function notification(){

// }
