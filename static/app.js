const form = $("#form");
const input = $("#word");
const notification = $("#notification");
const score = $("#score");
const button = $("button");
const timer = $("#timer");
const gamesPlayed = $("#game-played");
const highestScore = $("#highest-score");
const wordFound = {};
notification.hide();

setTimeout(async () => {
  const res = await endOfGame();
  input.prop("disabled", true);
  button.prop("disabled", true);
  gamesPlayed.html(`${parseInt(gamesPlayed.html()) + 1}`);
  highestScore.html(`${res["highest-score"]}`);
}, 60000);

setInterval(() => {
  if (parseInt(timer.html()) > 0) {
    timer.html(`${parseInt(timer.html()) - 1}`);
  }
}, 1000);

async function endOfGame() {
  const res = await axios.post("/end-of-game", {
    score: parseInt(score.html()),
  });

  return res.data;
}

form.on("submit", (evt) => {
  evt.preventDefault();
  checkValidWord();
  input.val("");
  setTimeout(() => {
    notification.slideUp(500);
  }, 2000);
});

async function checkValidWord() {
  word = input.val().toLowerCase();
  const res = await axios.post("/check-word", {
    word: input.val(),
  });

  notification.removeClass("good bad");
  notification.hide();
  if (word in wordFound) {
    notification.html("Word Already found");
    notification.toggleClass("bad");
    notification.show(700);
  } else {
    if (res.data["result"] == "ok") {
      notification.html(`Word found`);
      notification.toggleClass("good");
      notification.show(700);
      wordFound[word] = wordFound.length;
      $("#word-found").append(`<li>${word} </li>`);
      score.html(`${parseInt(score.html()) + word.length}`);
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
}
// $("input:text:visible:first").focus();
