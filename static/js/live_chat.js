// Source: https://www.geeksforgeeks.org/realtime-chat-app-using-django/
const chatSocket = new WebSocket("wss://" + window.location.host + "/");
const liveChatContainer = document.querySelector("#id-chat-item-container");
const chatAnchor = document.querySelector("#chat-anchor");

chatSocket.onopen = function () {
  let div = document.createElement("div");
  div.innerHTML = "Connected to chat!";
  liveChatContainer.insertBefore(div, chatAnchor.nextSibling);
};
chatSocket.onclose = function () {
  let div = document.createElement("div");
  div.innerHTML =("Connection to chat has closed due to inactivity!"
                + "<br/>Refresh page to reconnect");
  liveChatContainer.insertBefore(div, chatAnchor.nextSibling);
};
document.querySelector("#id_message_send_input").focus();
document.querySelector("#id_message_send_input").onkeyup = function (e) {
  if (e.keyCode == 13) {
    document.querySelector("#id_message_send_button").click();
  }
};
document.querySelector("#id_message_send_button").onclick = function () {
  let messageInput = document.querySelector(
    "#id_message_send_input"
  ).value;
  chatSocket.send(JSON.stringify({
    message: messageInput,
    username: username
  }));
};
chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  let div = document.createElement("div");
  div.innerHTML = data.username + " : " + data.message;
  document.querySelector("#id_message_send_input").value = "";
  liveChatContainer.insertBefore(div, chatAnchor.nextSibling);
};