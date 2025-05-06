function refreshStatus() {
  fetch("/status")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("free").textContent = data.free;
      document.getElementById("occupied").textContent = data.occupied;
      document.getElementById("suggested").textContent = data.suggested;
    });
}

// Keep your existing status refresh every 9 seconds
setInterval(refreshStatus, 9000);

// Add separate interval ONLY for video refresh every 10 seconds
setInterval(() => {
  const video = document.querySelector(".video-feed");
  if (video) {
    // Reload the video by adding a random query to bypass cache
    video.src = "/video_feed?rand=" + Math.random();
  }
}, 10000);
