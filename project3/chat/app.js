function date_format(timestamp) {
    var date = new Date(timestamp * 1000);
    return date.toLocaleDateString("en-US") + " " + date.toLocaleTimeString("en-US");
}
function login() {
    var request = new XMLHttpRequest();
    var form = new FormData();
    form.append("password", password.value);
    form.append("username", username.value);
    sessionStorage.setItem("url", url.value);
    request.open("POST", sessionStorage.getItem("url") + "/login");
    request.onreadystatechange = function() {
        if (this.readyState != 4) return;
        if (this.status === 201) {
            login_modal.style.display = "none";
            password.value = "";
            username.value = "";
            const data = JSON.parse(this.responseText);
            messageToken = data.message_token;
            streamToken = data.stream_token;
            start_stream();
        } else if (this.status === 403) {
            alert("Invalid username or password");
        } else if (this.status === 409) {
            alert(username.value + " is already logged in");

        } else {
            alert(this.status + " failure to /login");
        }
    };
    request.send(form);
}
function handle_connect() {
    message.disabled = false;
    message.value = "";
    title.classList.remove("disconnected");
}
function handle_disconnect(clear_users) {
    message.disabled = true;
    message.value = "Please connect to send messages.";
    title.classList.add("disconnected");
    if (clear_users) {
        users = new Set();
        update_users();
    }
}
function output(node) {
    var element = document.createElement("div");
    element.appendChild(node);
    chat.appendChild(element);
    chat.scrollTop = chat.scrollHeight - chat.clientHeight;
}
function show_login() {
    url.value = sessionStorage.getItem("url") || "https://chat.cs291.com";
    login_modal.style.display = "block";
}
function start_stream() {
    stream = new EventSource(
        sessionStorage.getItem("url") + "/stream/" + streamToken
    );
    stream.addEventListener(
        "open",
        function(_event) {
            handle_connect();
        }
    );
    stream.addEventListener(
        "Disconnect",
        function(_event) {
            stream.close();
            handle_disconnect(true);
            messageToken = null;
            streamToken = null;
            chat.innerHTML = "";
            show_login();
        },
        false
    );
    stream.addEventListener(
        "Join",
        function(event) {
            var data = JSON.parse(event.data);
            users.add(data.user);
            update_users();
            output(document.createTextNode(date_format(data["created"]) + " JOIN: " + data.user));
        },
        false
    );
    stream.addEventListener(
        "Message",
        function(event) {
            var data = JSON.parse(event.data);
            output(
                document.createTextNode(
                    date_format(data["created"]) + " (" + data.user + ") " + data.message
                )
            );
        },
        false
    );
    stream.addEventListener(
        "Part",
        function(event) {
            var data = JSON.parse(event.data);
            users.delete(data.user);
            update_users();
            output(document.createTextNode(date_format(data["created"]) + " PART: " + data.user));
        },
        false
    );
    stream.addEventListener(
        "ServerStatus",
        function(event) {
            var data = JSON.parse(event.data);
            output(document.createTextNode(date_format(data["created"]) + " STATUS: " + data.status));
        },
        false
    );
    stream.addEventListener(
        "Users",
        function(event) {
            users = new Set(JSON.parse(event.data).users);
            update_users();
        },
        false
    );
    stream.addEventListener(
        "error",
        function(event) {
            if (event.target.readyState == 2) {
                messageToken = null;
                streamToken = null;
                handle_disconnect(true);
                show_login();
            } else {
                handle_disconnect(false);
                console.log("Disconnected, retrying");
            }
        },
        false
    );
}
function update_users() {
    user_list.innerHTML = "";
    for (let item of Array.from(users).sort()) {
        var element = document.createElement("li");
        element.appendChild(document.createTextNode(item));
        user_list.appendChild(element);
    }
}
var messageToken = null;
var streamToken = null;
var chat = document.getElementById("chat");
var login_modal = document.getElementById("login-modal");
var message = document.getElementById("message");
var password = document.getElementById("password");
var stream = null;
var title = document.getElementById("title");
var url = document.getElementById("url");
var user_list = document.getElementById("users");
var username = document.getElementById("username");
var users = new Set();
login_modal.addEventListener("keyup", function(event) {
    if (messageToken !== null || event.keyCode !== 13)
        return;
    login();
});
message.addEventListener("keyup", function(event) {
    if (messageToken === null || event.keyCode !== 13)
        return;
    event.preventDefault();
    if (message.value === "") return;

    var form = new FormData();
    form.append("message", message.value);

    var request = new XMLHttpRequest();
    request.open("POST", sessionStorage.getItem("url") + "/message");
    request.setRequestHeader(
        "Authorization",
        "Bearer " + messageToken
    );
    request.onreadystatechange = function(event) {
        if (event.target.readyState == 4 && event.target.status != 403 && messageToken != null) {
            messageToken = event.target.getResponseHeader("token");
        }
    }
    request.send(form);

    message.value = "";
});

if (messageToken === null) {
    handle_disconnect(true);
    show_login();
} else {
    start_stream();
}
