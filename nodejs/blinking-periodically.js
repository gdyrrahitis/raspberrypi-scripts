var gpio = require('onoff').Gpio;
var red = new gpio(18, 'out');
var yellow = new gpio(23, 'out');
var green = new gpio(24, 'out');

var blinkRedInterval = setInterval(blinkRed, 500);
var blinkYellowInterval = setInterval(blinkYellow, 600);
var blinkGreenInterval = setInterval(blinkGreen, 700);

function blinkRed() {
    red.writeSync(red.readSync() === 0 ? 1: 0);
}

function blinkYellow() {
    yellow.writeSync(yellow.readSync() === 0 ? 1: 0);
}

function blinkGreen() {
    green.writeSync(green.readSync() === 0 ? 1: 0);
}
function endBlink() {
    clearInterval(blinkRedInterval);
    clearInterval(blinkYellowInterval);
    clearInterval(blinkGreenInterval);

    red.writeSync(0);
    red.unexport();
    
    yellow.writeSync(0);
    yellow.unexport();

    green.writeSync(0);
    green.unexport();
}

setTimeout(endBlink, 60000);