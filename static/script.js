let mediaRecorder;
let audioChunks = [];
let currentAudio = null;

// 🎤 Start Recording
async function startRecording() {
    try {
        document.getElementById("status").innerText = "🎙 Recording...";

        // 🔥 Disable button while recording
        document.querySelector("button[onclick='startRecording()']").disabled = true;

        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);

        audioChunks = [];

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = async () => {
            document.getElementById("status").innerText = "⏳ Processing...";

            const blob = new Blob(audioChunks, { type: 'audio/webm' });
            audioChunks = [];

            const formData = new FormData();
            formData.append("file", blob, "recording.webm");

            try {
                const response = await fetch("/log-voice", {
                    method: "POST",
                    body: formData
                });

                const data = await response.json();

                // ✅ Update UI safely
                document.getElementById("recognizedText").innerText =
                    data.text && data.text.trim() !== "" ? data.text : "Not detected";

                document.getElementById("project").innerText =
                    data.project && data.project.trim() !== "" ? data.project : "Not detected";

                document.getElementById("timeSpent").innerText =
                    data.time_spent && data.time_spent.trim() !== "" ? data.time_spent : "Not detected";

                // 🔊 Stop previous audio
                if (currentAudio) {
                    currentAudio.pause();
                }

                // 🔊 Play new audio
                if (data.audio) {
                    currentAudio = new Audio("data:audio/mp3;base64," + data.audio);
                    currentAudio.play();
                }

                document.getElementById("status").innerText = "✅ Done";

                loadLogs();

            } catch (error) {
                console.error("API Error:", error);
                document.getElementById("status").innerText = "❌ Error processing audio";
            }

            // 🔥 Enable button again
            document.querySelector("button[onclick='startRecording()']").disabled = false;
        };

        mediaRecorder.start();

    } catch (error) {
        console.error("Mic Error:", error);
        document.getElementById("status").innerText = "❌ Microphone access denied";
    }
}


// 🛑 Stop Recording
function stopRecording() {
    if (mediaRecorder && mediaRecorder.state !== "inactive") {
        mediaRecorder.stop();
    }
}


// 📊 Load logs
async function loadLogs() {
    try {
        const res = await fetch("/logs");
        const data = await res.json();

        const table = document.getElementById("logsTable");
        table.innerHTML = "";

        data.forEach(log => {
            table.innerHTML += `
                <tr>
                    <td>${log.id}</td>
                    <td>${log.task}</td>
                    <td>${log.project}</td>
                    <td>${log.time_spent}</td>
                </tr>
            `;
        });

    } catch (error) {
        console.error("Logs Error:", error);
    }
}


// 🔄 Load logs on start
loadLogs();