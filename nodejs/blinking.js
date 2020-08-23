var gpio = require('onoff').Gpio;
var red = new gpio(18, 'out');
var yellow = new gpio(23, 'out');
var green = new gpio(24, 'out');

var blinkInterval = setInterval(blinkLed, 500);

function blinkLed() {
    red.writeSync(red.readSync() === 0 ? 1: 0);
    yellow.writeSync(yellow.readSync() === 0 ? 1: 0);
    green.writeSync(green.readSync() === 0 ? 1: 0);
}

function endBlink() {
    clearInterval(blinkInterval);
    red.writeSync(0);
    red.unexport();
    
    yellow.writeSync(0);
    yellow.unexport();

    green.writeSync(0);
    green.unexport();
}

setTimeout(endBlink, 60000);