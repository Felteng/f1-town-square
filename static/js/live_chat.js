// Source: https://www.geeksforgeeks.org/realtime-chat-app-using-django/
const chatSocket = new WebSocket("wss://" + window.location.host + "/");
const liveChatContainer = document.querySelector("#id-chat-item-container");
const chatAnchor = document.querySelector("#chat-anchor");


chatSocket.onopen = function () {
  let div = document.createElement("div");
  div.innerHTML = "Connected to chat!";
  $(div).addClass("text-start");
  liveChatContainer.insertBefore(div, chatAnchor);
};


chatSocket.onclose = function () {
  let div = document.createElement("div");
  div.innerHTML =(`Connection to chat has closed due to inactivity!
    <br/>Refresh page to reconnect`
  );
  $(div).addClass("text-start");
  liveChatContainer.insertBefore(div, chatAnchor);
};


document.querySelector("#id_message_send_input").focus();
document.querySelector("#id_message_send_input").onkeyup = function (e) {
  if (e.keyCode === 13) {
    document.querySelector("#id_message_send_button").click();
  }
};


document.querySelector("#id_message_send_button").onclick = function () {
  /**
   * Custom addition of 'if (/[a-z0-9]/i.test(messageInput))'
   * used to check if the input contains any alphanumerical
   * characters to not have the chat spammed with empty
   * strings of text.
   *
   * Username variable is defined in the template using DTL.
   */
  let messageInput = document.querySelector(
    "#id_message_send_input"
  ).value;
  if (/[a-z0-9]/i.test(messageInput)) {
    chatSocket.send(JSON.stringify({
    message: messageInput,
    username: username
  }));
  }
};


chatSocket.onmessage = function (e) {
  /**
   * Adds the message received and the time of day
   * to a div that will dispaly that information
   * to users in the chat when inserted.
   */
  const data = JSON.parse(e.data);
  const date = new Date();
  let div = document.createElement("div");
  div.innerHTML = `<h6 class="mb-0">${data.username}
  <span class="message-date">
  @${date.getHours() + ":" +
  (date.getMinutes() < 10 ? "0" : "") + date.getMinutes() + ":" +
  date.getSeconds()}
  </span></h6>
  <p class="chat-message">${data.message}</p>
  <hr class="message-break">`;
  $(div).addClass("text-start");
  document.querySelector("#id_message_send_input").value = "";
  liveChatContainer.insertBefore(div, chatAnchor);
};