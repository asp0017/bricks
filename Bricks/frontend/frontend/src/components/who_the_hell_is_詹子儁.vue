
<template>
    <div id="app">
        <div class="container">
            <h1 class="title">誰是詹子儁，生日快樂！</h1>
            <div class="confetti-container">
                <div class="confetti">🖕🖕🖕</div>
            </div>
        </div>
    </div>
</template>
  
<style scoped>
#app {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #b82c30;
}

.container {
    text-align: center;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.title {
    font-size: 30px;
    color: #333;
    margin-bottom: 20px;
}

.confetti-container {
    position: relative;
    overflow: hidden;
    height: 100px;
}

.confetti {
    width: 20px;
    height: 20px;
    background-color: #E74C3C;
    border-radius: 50%;
    position: absolute;
    top: -20px;
    left: 50%;
    transform: translateX(-50%);
    animation: confetti-fall 3s infinite;
}

@keyframes confetti-fall {
    0% {
        transform: translateX(-50%) translateY(-20px);
    }

    10% {
        transform: translateX(-50%) translateY(0);
    }

    90% {
        transform: translateX(-50%) translateY(0);
    }

    100% {
        transform: translateX(-50%) translateY(100vh);
    }
}
</style>
  