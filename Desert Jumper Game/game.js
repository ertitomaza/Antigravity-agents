const canvas = document.getElementById('game-canvas');
const ctx = canvas.getContext('2d');
const timeDisplay = document.getElementById('time-display');
const livesDisplay = document.getElementById('lives-display');
const modal = document.getElementById('modal');
const modalTitle = document.getElementById('modal-title');
const modalMessage = document.getElementById('modal-message');
const restartBtn = document.getElementById('restart-btn');

// Game constants
const GRAVITY = 0.8;
const JUMP_FORCE = -15;
const INITIAL_SPEED = 5;
const SPEED_INCREMENT = 0.5;
const GROUND_Y = 320;
const SKY_COLORS = ['#87CEEB', '#70c5eb', '#58bceb', '#41b3eb', '#29aaeb'];

// Game state
let isPlaying = false;
let score = 0;
let lives = 3;
let speed = INITIAL_SPEED;
let startTime = 0;
let lastSpeedIncrease = 0;
let animationId;

class Blob {
    constructor() {
        this.reset();
    }

    reset() {
        this.x = 100;
        this.y = GROUND_Y;
        this.radius = 25;
        this.dy = 0;
        this.isJumping = false;
        this.color = '#A78BFA';
        this.pulse = 0;
    }

    draw() {
        // Squash and stretch effect
        const squash = this.isJumping ? Math.min(1.2, 1 + Math.abs(this.dy) / 30) : 1;
        const stretch = this.isJumping ? Math.max(0.8, 1 - Math.abs(this.dy) / 30) : (1 + Math.sin(this.pulse) * 0.05);

        ctx.save();
        ctx.translate(this.x, this.y);

        // Draw shadow
        ctx.beginPath();
        ctx.ellipse(0, GROUND_Y - this.y + 25, 20 * stretch, 5, 0, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(0,0,0,0.1)';
        ctx.fill();

        // Draw Blob body
        ctx.beginPath();
        ctx.ellipse(0, 0, this.radius * stretch, this.radius * squash, 0, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();

        // Add a nice highlight
        ctx.beginPath();
        ctx.ellipse(-8, -8, 8, 5, -Math.PI / 4, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255,255,255,0.3)';
        ctx.fill();

        // Eyes
        ctx.fillStyle = '#1a1a1a';
        ctx.beginPath();
        ctx.arc(8, -5, 3, 0, Math.PI * 2);
        ctx.arc(20, -5, 3, 0, Math.PI * 2);
        ctx.fill();

        ctx.restore();

        if (!this.isJumping) this.pulse += 0.1;
    }

    update() {
        this.y += this.dy;

        if (this.y + this.radius < GROUND_Y) {
            this.dy += GRAVITY;
            this.isJumping = true;
        } else {
            this.y = GROUND_Y - this.radius;
            this.dy = 0;
            this.isJumping = false;
        }
    }

    jump() {
        if (!this.isJumping) {
            this.dy = JUMP_FORCE;
            this.isJumping = true;
        }
    }
}

class Obstacle {
    constructor(type) {
        this.x = canvas.width + 100;
        this.type = type; // 'rock' or 'cactus'
        this.width = type === 'rock' ? 40 : 30;
        this.height = type === 'rock' ? 30 : 50;
        this.y = GROUND_Y - this.height;
    }

    draw() {
        ctx.fillStyle = this.type === 'rock' ? '#71717a' : '#166534';
        if (this.type === 'rock') {
            // Draw a rounded rock
            ctx.beginPath();
            ctx.moveTo(this.x, GROUND_Y);
            ctx.quadraticCurveTo(this.x + this.width / 2, GROUND_Y - this.height * 2, this.x + this.width, GROUND_Y);
            ctx.fill();
        } else {
            // Draw a cactus
            ctx.fillRect(this.x + 10, this.y, 10, this.height);
            ctx.fillRect(this.x, this.y + 15, 10, 5);
            ctx.fillRect(this.x + 20, this.y + 10, 10, 5);
        }
    }

    update() {
        this.x -= speed;
    }
}

const blob = new Blob();
let obstacles = [];
let obstacleTimer = 0;

function spawnObstacle() {
    if (obstacleTimer <= 0) {
        const type = Math.random() > 0.5 ? 'rock' : 'cactus';
        obstacles.push(new Obstacle(type));
        obstacleTimer = 50 + Math.random() * 100; // Intervals depend on speed eventually
    }
    obstacleTimer--;
}

function updateHUD() {
    const elapsed = Math.floor((Date.now() - startTime) / 1000);
    const mins = Math.floor(elapsed / 60).toString().padStart(2, '0');
    const secs = (elapsed % 60).toString().padStart(2, '0');
    timeDisplay.textContent = `${mins}:${secs}`;

    // Lives
    livesDisplay.innerHTML = '❤️'.repeat(lives);

    // Difficulty scaling every 30s
    if (elapsed > 0 && elapsed % 30 === 0 && elapsed !== lastSpeedIncrease) {
        speed += SPEED_INCREMENT;
        lastSpeedIncrease = elapsed;

        // Update sky color based on difficulty level
        const level = Math.min(SKY_COLORS.length - 1, Math.floor(elapsed / 30));
        document.documentElement.style.setProperty('--bg-sky', SKY_COLORS[level]);
        console.log('Speed increased:', speed);
    }
}

function checkCollisions() {
    obstacles.forEach((obs, index) => {
        // Simple bounding box collision
        if (
            blob.x + blob.radius > obs.x &&
            blob.x - blob.radius < obs.x + obs.width &&
            blob.y + blob.radius > obs.y &&
            blob.y - blob.radius < obs.y + obs.height
        ) {
            obstacles.splice(index, 1);
            handleHit();
        }
    });
}

function handleHit() {
    lives--;

    // Smooth pulse for HUD
    livesDisplay.style.transform = 'scale(1.2)';
    setTimeout(() => livesDisplay.style.transform = 'scale(1)', 200);

    // Screen shake
    canvas.style.transform = 'translateX(5px)';
    setTimeout(() => canvas.style.transform = 'translateX(-5px)', 50);
    setTimeout(() => canvas.style.transform = 'translateX(3px)', 100);
    setTimeout(() => canvas.style.transform = 'translateX(-3px)', 150);
    setTimeout(() => canvas.style.transform = 'translateX(0)', 200);

    if (lives <= 0) {
        gameOver();
    }
}

function gameOver() {
    isPlaying = false;
    cancelAnimationFrame(animationId);
    modalTitle.textContent = 'GAME OVER';
    modalMessage.textContent = `Has sobrevivido ${timeDisplay.textContent}`;
    restartBtn.textContent = 'REINTENTAR';
    modal.classList.add('active');
}

function resetGame() {
    lives = 3;
    speed = INITIAL_SPEED;
    startTime = Date.now();
    lastSpeedIncrease = 0;
    obstacles = [];
    blob.reset();
    modal.classList.remove('active');
    isPlaying = true;
    gameLoop();
}

function drawBackground() {
    // Clear
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Track/Ground
    ctx.fillStyle = '#F4A460';
    ctx.fillRect(0, GROUND_Y, canvas.width, canvas.height - GROUND_Y);

    // Grid or texture for movement feel
    ctx.strokeStyle = '#e69550';
    ctx.lineWidth = 2;
    for (let i = 0; i < canvas.width + speed; i += 50) {
        const offset = (Date.now() / 10 * speed) % 50;
        ctx.beginPath();
        ctx.moveTo(i - offset, GROUND_Y);
        ctx.lineTo(i - offset - 20, canvas.height);
        ctx.stroke();
    }
}

function gameLoop() {
    if (!isPlaying) return;

    drawBackground();

    blob.update();
    blob.draw();

    spawnObstacle();
    obstacles.forEach((obs, index) => {
        obs.update();
        obs.draw();

        if (obs.x + obs.width < 0) {
            obstacles.splice(index, 1);
        }
    });

    checkCollisions();
    updateHUD();

    animationId = requestAnimationFrame(gameLoop);
}

// Initial state
modal.classList.add('active');

// Input handling
window.addEventListener('keydown', (e) => {
    if (e.code === 'Space') {
        if (!isPlaying && modal.classList.contains('active')) {
            resetGame();
        } else if (isPlaying) {
            blob.jump();
        }
    }
});

restartBtn.addEventListener('click', resetGame);
