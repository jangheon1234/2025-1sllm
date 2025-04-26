async function sendmsge() {
    const input = document.getElementById("userInput");
    const usermsge = input.value.trim();

    if (!usermsge) return;  // 입력이 없으면 그냥 리턴

    addmsge(usermsge, "user");

    const response = await fetch(`http://127.0.0.1:8000/chat?q=${encodeURIComponent(usermsge)}`);

    const data = await response.json();

    addmsge(data.response, "bot");

    input.value = "";
}

// 메시지를 화면에 추가하는 함수
function addmsge(msge, sender) {
    const msgeBox = document.getElementById("msge");

    const msgeDiv = document.createElement("div");
    msgeDiv.classList.add("msge", sender === "user" ? "user-msge" : "bot-msge");
    msgeDiv.innerText = msge;

    msgeBox.appendChild(msgeDiv);
    msgeBox.scrollTop = msgeBox.scrollHeight;
}
