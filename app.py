from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # HTML content from the previous code
    html_content = '''
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Slot Machine Animation</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
      background-color: #222;
      color: #fff;
      overflow: hidden;
    }
    .slot-container {
      display: flex;
      gap: 20px;
      margin-bottom: 20px;
    }
    .slot-box {
      width: 120px;
      height: 120px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 3px solid gold;
      border-radius: 15px;
      background: linear-gradient(145deg, #f0f0f0, #ddd);
      font-size: 24px;
      font-weight: bold;
      color: #111;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
      overflow: hidden;
      position: relative;
    }
    .slot-box .name {
      position: absolute;
      width: 100%;
      text-align: center;
    }
    .spinning {
      animation: spin 0.0125s linear infinite;
    }
    button {
      padding: 15px 30px;
      font-size: 18px;
      border: none;
      border-radius: 5px;
      background-color: gold;
      color: #111;
      cursor: pointer;
      transition: transform 0.2s, background-color 0.2s;
    }
    button:hover {
      background-color: orange;
      transform: scale(1.05);
    }
    @keyframes spin {
      0% {
        transform: translateY(100%);
      }
      25% {
        transform: translateY(0);
      }
      50% {
        transform: translateY(-100%);
      }
      75% {
        transform: translateY(0);
      }
      100% {
        transform: translateY(100%);
      }
    }
  </style>
</head>
<body>
  <div class="slot-container">
    <div class="slot-box" id="box1">
      <div class="name">-</div>
    </div>
    <div class="slot-box" id="box2">
      <div class="name">-</div>
    </div>
  </div>
  <button id="startButton">Start</button>

  <script>
    const names = ["1ο ΓΕΛ", "ΓΕΛ Κρεμαστής", "3ο ΓΕΛ", "4ο ΓΕΛ"];
    let isHeld = false;
    let holdTimer;
    let holdCompleted = false;  // Flag to track if 2 seconds hold has completed

    function getRandomName(exclude) {
      let filteredNames = names.filter(name => name !== exclude);
      return filteredNames[Math.floor(Math.random() * filteredNames.length)];
    }

    function startSlotMachine() {
      const box1 = document.getElementById('box1');
      const box2 = document.getElementById('box2');
      const name1 = box1.querySelector('.name');
      const name2 = box2.querySelector('.name');

      // Add spinning class to trigger animation
      name1.classList.add('spinning');
      name2.classList.add('spinning');

      let interval1, interval2;

      interval1 = setInterval(() => {
        name1.textContent = getRandomName(name2.textContent); // Ensure different from box2
      }, 50);

      interval2 = setInterval(() => {
        name2.textContent = getRandomName(name1.textContent); // Ensure different from box1
      }, 50);

      // Stop after a random duration
      setTimeout(() => {
        clearInterval(interval1);
        name1.textContent = getRandomName(name2.textContent); // Final value for box1
        name1.classList.remove('spinning');
      }, 3000);

      setTimeout(() => {
        clearInterval(interval2);
        name2.textContent = getRandomName(name1.textContent); // Final value for box2
        name2.classList.remove('spinning');
      }, 3500);
    }

    function setSpecificCombination() {
      const box1 = document.getElementById('box1');
      const box2 = document.getElementById('box2');
      const name1 = box1.querySelector('.name');
      const name2 = box2.querySelector('.name');

      // Show rigged results after normal animation
      setTimeout(() => {
        name1.textContent = "1ο ΓΕΛ"; // Specific combination
        name2.textContent = "ΓΕΛ Κρεμαστής";
      }, 3500); // Show rigged result after 3.5 seconds (end of normal spin animation)
    }

    const startButton = document.getElementById('startButton');

    // Handle touchstart and mousedown for both mobile and desktop
    startButton.addEventListener('mousedown', startHold);
    startButton.addEventListener('touchstart', startHold);

    // Handle touchend and mouseup for both mobile and desktop
    startButton.addEventListener('mouseup', endHold);
    startButton.addEventListener('touchend', endHold);

    function startHold(event) {
      event.preventDefault();  // Prevent the default behavior on touch devices
      isHeld = true;

      // Start a timer to check if the button is held for 2 seconds
      holdTimer = setTimeout(() => {
        if (isHeld) {
          holdCompleted = true;
          startSlotMachine(); // Start normal animation after 2 seconds
          setSpecificCombination(); // Show rigged result after animation
        }
      }, 2000); // 2 seconds
    }

    function endHold(event) {
      if (!holdCompleted) {
        // If the button is released before 2 seconds, do nothing
        clearTimeout(holdTimer);  // Clear the timer
        return;
      }
    }

    startButton.addEventListener('click', () => {
      if (!holdCompleted) {
        startSlotMachine(); // Normal slot machine spin if no rigged results
      }
    });
  </script>
</body>
</html>

    '''

    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
